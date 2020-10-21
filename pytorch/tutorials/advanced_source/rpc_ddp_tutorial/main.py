import os
from functools import wraps

import random
import torch
import torch.distributed as dist
import torch.distributed.autograd as dist_autograd
import torch.distributed.rpc as rpc
from torch.distributed.rpc import TensorPipeRpcBackendOptions
import torch.multiprocessing as mp
import torch.optim as optim
from torch.distributed.optim import DistributedOptimizer
from torch.distributed.rpc import RRef
from torch.nn.parallel import DistributedDataParallel as DDP

NUM_EMBEDDINGS = 100
EMBEDDING_DIM = 16

# BEGIN hybrid_model
class HybridModel(torch.nn.Module):
    r"""
    The model consists of a sparse part and a dense part. The dense part is an
    nn.Linear module that is replicated across all trainers using
    DistributedDataParallel. The sparse part is an nn.EmbeddingBag that is
    stored on the parameter server.

    The model holds a Remote Reference to the embedding table on the parameter
    server.
    """

    def __init__(self, emb_rref, device):
        super(HybridModel, self).__init__()
        self.emb_rref = emb_rref
        self.fc = DDP(torch.nn.Linear(16, 8).cuda(device), device_ids=[device])
        self.device = device

    def forward(self, indices, offsets):
        emb_lookup = self.emb_rref.rpc_sync().forward(indices, offsets)
        return self.fc(emb_lookup.cuda(self.device))
# END hybrid_model

# BEGIN setup_trainer
def _retrieve_embedding_parameters(emb_rref):
    param_rrefs = []
    for param in emb_rref.local_value().parameters():
        param_rrefs.append(RRef(param))
    return param_rrefs


def _run_trainer(emb_rref, rank):
    r"""
    Each trainer runs a forward pass which involves an embedding lookup on the
    parameter server and running nn.Linear locally. During the backward pass,
    DDP is responsible for aggregating the gradients for the dense part
    (nn.Linear) and distributed autograd ensures gradients updates are
    propagated to the parameter server.
    """

    # Setup the model.
    model = HybridModel(emb_rref, rank)

    # Retrieve all model parameters as rrefs for DistributedOptimizer.

    # Retrieve parameters for embedding table.
    model_parameter_rrefs = rpc.rpc_sync(
            "ps", _retrieve_embedding_parameters, args=(emb_rref,))

    # model.parameters() only includes local parameters.
    for param in model.parameters():
        model_parameter_rrefs.append(RRef(param))

    # Setup distributed optimizer
    opt = DistributedOptimizer(
        optim.SGD,
        model_parameter_rrefs,
        lr=0.05,
    )

    criterion = torch.nn.CrossEntropyLoss()
    # END setup_trainer

    # BEGIN run_trainer
    def get_next_batch(rank):
        for _ in range(10):
            num_indices = random.randint(20, 50)
            indices = torch.LongTensor(num_indices).random_(0, NUM_EMBEDDINGS)

            # Generate offsets.
            offsets = []
            start = 0
            batch_size = 0
            while start < num_indices:
                offsets.append(start)
                start += random.randint(1, 10)
                batch_size += 1

            offsets_tensor = torch.LongTensor(offsets)
            target = torch.LongTensor(batch_size).random_(8).cuda(rank)
            yield indices, offsets_tensor, target

    # Train for 100 epochs
    for epoch in range(100):
        # create distributed autograd context
        for indices, offsets, target in get_next_batch(rank):
            with dist_autograd.context() as context_id:
                output = model(indices, offsets)
                loss = criterion(output, target)

                # Run distributed backward pass
                dist_autograd.backward(context_id, [loss])

                # Tun distributed optimizer
                opt.step(context_id)

                # Not necessary to zero grads as each iteration creates a different
                # distributed autograd context which hosts different grads
        print("Training done for epoch {}".format(epoch))
    # END run_trainer


# BEGIN run_worker
def run_worker(rank, world_size):
    r"""
    A wrapper function that initializes RPC, calls the function, and shuts down
    RPC.
    """
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '29500'


    rpc_backend_options = TensorPipeRpcBackendOptions()
    rpc_backend_options.init_method='tcp://localhost:29501'

    # Rank 2 is master, 3 is ps and 0 and 1 are trainers.
    if rank == 2:
        rpc.init_rpc(
                "master",
                rank=rank,
                world_size=world_size,
                rpc_backend_options=rpc_backend_options)

        # Build the embedding table on the ps.
        emb_rref = rpc.remote(
                "ps",
                torch.nn.EmbeddingBag,
                args=(NUM_EMBEDDINGS, EMBEDDING_DIM),
                kwargs={"mode": "sum"})

        # Run the training loop on trainers.
        futs = []
        for trainer_rank in [0, 1]:
            trainer_name = "trainer{}".format(trainer_rank)
            fut = rpc.rpc_async(
                    trainer_name, _run_trainer, args=(emb_rref, rank))
            futs.append(fut)

        # Wait for all training to finish.
        for fut in futs:
            fut.wait()
    elif rank <= 1:
        # Initialize process group for Distributed DataParallel on trainers.
        dist.init_process_group(
                backend="gloo", rank=rank, world_size=2)

        # Initialize RPC.
        trainer_name = "trainer{}".format(rank)
        rpc.init_rpc(
                trainer_name,
                rank=rank,
                world_size=world_size,
                rpc_backend_options=rpc_backend_options)

        # Trainer just waits for RPCs from master.
    else:
        rpc.init_rpc(
                "ps",
                rank=rank,
                world_size=world_size,
                rpc_backend_options=rpc_backend_options)
        # parameter server do nothing
        pass

    # block until all rpcs finish
    rpc.shutdown()


if __name__=="__main__":
    # 2 trainers, 1 parameter server, 1 master.
    world_size = 4
    mp.spawn(run_worker, args=(world_size, ), nprocs=world_size, join=True)
# END run_worker
