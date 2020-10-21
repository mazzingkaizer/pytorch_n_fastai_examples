PyTorch Recipes
---------------------------------------------
Recipes are bite-sized, actionable examples of how to use specific PyTorch features, different from our full-length tutorials.

.. raw:: html

        </div>
    </div>

    <div id="tutorial-cards-container">

    <nav class="navbar navbar-expand-lg navbar-light tutorials-nav col-12">
        <div class="tutorial-tags-container">
            <div id="dropdown-filter-tags">
                <div class="tutorial-filter-menu">
                    <div class="tutorial-filter filter-btn all-tag-selected" data-tag="all">All</div>
                </div>
            </div>
        </div>
    </nav>

    <hr class="tutorials-hr">

    <div class="row">

    <div id="tutorial-cards">
    <div class="list">

.. Add recipe cards below this line

.. Basics

.. customcarditem::
   :header: Loading data in PyTorch
   :card_description: Learn how to use PyTorch packages to prepare and load common datasets for your model.
   :image: ../_static/img/thumbnails/cropped/loading-data.PNG
   :link: ../recipes/recipes/loading_data_recipe.html
   :tags: Basics


.. customcarditem::
   :header: Defining a Neural Network
   :card_description: Learn how to use PyTorch's torch.nn package to create and define a neural network for the MNIST dataset.
   :image: ../_static/img/thumbnails/cropped/defining-a-network.PNG
   :link: ../recipes/recipes/defining_a_neural_network.html
   :tags: Basics

.. customcarditem::
   :header: What is a state_dict in PyTorch
   :card_description: Learn how state_dict objects and Python dictionaries are used in saving or loading models from PyTorch.
   :image: ../_static/img/thumbnails/cropped/what-is-a-state-dict.PNG
   :link: ../recipes/recipes/what_is_state_dict.html
   :tags: Basics

.. customcarditem::
   :header: Saving and loading models for inference in PyTorch
   :card_description: Learn about the two approaches for saving and loading models for inference in PyTorch - via the state_dict and via the entire model.
   :image: ../_static/img/thumbnails/cropped/saving-and-loading-models-for-inference.PNG
   :link: ../recipes/recipes/saving_and_loading_models_for_inference.html
   :tags: Basics


.. customcarditem::
   :header: Saving and loading a general checkpoint in PyTorch
   :card_description: Saving and loading a general checkpoint model for inference or resuming training can be helpful for picking up where you last left off. In this recipe, explore how to save and load multiple checkpoints.
   :image: ../_static/img/thumbnails/cropped/saving-and-loading-general-checkpoint.PNG
   :link: ../recipes/recipes/saving_and_loading_a_general_checkpoint.html
   :tags: Basics

.. customcarditem::
   :header: Saving and loading multiple models in one file using PyTorch
   :card_description: In this recipe, learn how saving and loading multiple models can be helpful for reusing models that you have previously trained.
   :image: ../_static/img/thumbnails/cropped/saving-multiple-models.PNG
   :link: ../recipes/recipes/saving_multiple_models_in_one_file.html
   :tags: Basics

.. customcarditem::
   :header: Warmstarting model using parameters from a different model in PyTorch
   :card_description: Learn how warmstarting the training process by partially loading a model or loading a partial model can help your model converge much faster than training from scratch.
   :image: ../_static/img/thumbnails/cropped/warmstarting-models.PNG
   :link: ../recipes/recipes/warmstarting_model_using_parameters_from_a_different_model.html
   :tags: Basics

.. customcarditem::
   :header: Saving and loading models across devices in PyTorch
   :card_description: Learn how saving and loading models across devices (CPUs and GPUs) is relatively straightforward using PyTorch.
   :image: ../_static/img/thumbnails/cropped/saving-and-loading-models-across-devices.PNG
   :link: ../recipes/recipes/save_load_across_devices.html
   :tags: Basics

.. customcarditem::
   :header: Zeroing out gradients in PyTorch
   :card_description: Learn when you should zero out gradients and how doing so can help increase the accuracy of your model.
   :image: ../_static/img/thumbnails/cropped/zeroing-out-gradients.PNG
   :link: ../recipes/recipes/zeroing_out_gradients.html
   :tags: Basics

.. customcarditem::
   :header: PyTorch Profiler
   :card_description: Learn how to use PyTorch's profiler to measure operators time and memory consumption
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/recipes/profiler.html
   :tags: Basics

.. Customization

.. customcarditem::
   :header: Custom Datasets, Transforms & Dataloaders
   :card_description: Learn how to leverage the PyTorch dataset API to easily create a custom dataset and custom dataloader.
   :image: ../_static/img/thumbnails/cropped/custom-datasets-transforms-and-dataloaders.png
   :link: ../recipes/recipes/custom_dataset_transforms_loader.html
   :tags: Data-Customization

.. Interpretability

.. customcarditem::
   :header: Model Interpretability using Captum
   :card_description: Learn how to use Captum attribute the predictions of an image classifier to their corresponding image features and visualize the attribution results.
   :image: ../_static/img/thumbnails/cropped/model-interpretability-using-captum.png
   :link: ../recipes/recipes/Captum_Recipe.html
   :tags: Interpretability,Captum

.. customcarditem::
   :header: How to use TensorBoard with PyTorch
   :card_description: Learn basic usage of TensorBoard with PyTorch, and how to visualize data in TensorBoard UI
   :image: ../_static/img/thumbnails/tensorboard_scalars.png
   :link: ../recipes/recipes/tensorboard_with_pytorch.html
   :tags: Visualization,TensorBoard

.. Quantization

.. customcarditem::
   :header: Dynamic Quantization
   :card_description:  Apply dynamic quantization to a simple LSTM model.
   :image: ../_static/img/thumbnails/cropped/using-dynamic-post-training-quantization.png
   :link: ../recipes/recipes/dynamic_quantization.html
   :tags: Quantization,Text,Model-Optimization


.. Production Development

.. customcarditem::
   :header: TorchScript for Deployment
   :card_description: Learn how to export your trained model in TorchScript format and how to load your TorchScript model in C++ and do inference.
   :image: ../_static/img/thumbnails/cropped/torchscript_overview.png
   :link: ../recipes/torchscript_inference.html
   :tags: TorchScript

.. customcarditem::
   :header: Deploying with Flask
   :card_description: Learn how to use Flask, a lightweight web server, to quickly setup a web API from your trained PyTorch model.
   :image: ../_static/img/thumbnails/cropped/using-flask-create-restful-api.png
   :link: ../recipes/deployment_with_flask.html
   :tags: Production,TorchScript

.. customcarditem::
   :header: PyTorch Mobile Performance Recipes
   :card_description: List of recipes for performance optimizations for using PyTorch on Mobile (Android and iOS).
   :image: ../_static/img/thumbnails/cropped/mobile.png
   :link: ../recipes/mobile_perf.html
   :tags: Mobile,Model-Optimization

.. customcarditem::
   :header: Making Android Native Application That Uses PyTorch Android Prebuilt Libraries
   :card_description: Learn how to make Android application from the scratch that uses LibTorch C++ API and uses TorchScript model with custom C++ operator.
   :image: ../_static/img/thumbnails/cropped/android.png
   :link: ../recipes/android_native_app_with_custom_op.html
   :tags: Mobile
   
.. customcarditem::
   :header: Profiling PyTorch RPC-Based Workloads
   :card_description: How to use the PyTorch profiler to profile RPC-based workloads.
   :image: ../_static/img/thumbnails/cropped/profile.png
   :link: ../recipes/distributed_rpc_profiling.html
   :tags: Production

.. Automatic Mixed Precision

.. customcarditem::
   :header: Automatic Mixed Precision
   :card_description: Use torch.cuda.amp to reduce runtime and save memory on NVIDIA GPUs.
   :image: ../_static/img/thumbnails/cropped/amp.png
   :link: ../recipes/recipes/amp_recipe.html
   :tags: Model-Optimization

.. Performance

.. customcarditem::
   :header: Performance Tuning Guide
   :card_description: Tips for achieving optimal performance.
   :image: ../_static/img/thumbnails/cropped/profiler.png
   :link: ../recipes/recipes/tuning_guide.html
   :tags: Model-Optimization

.. End of tutorial card section

.. raw:: html

    </div>

    <div class="pagination d-flex justify-content-center"></div>

    </div>

    </div>

.. -----------------------------------------
.. Page TOC
.. -----------------------------------------
.. toctree::
   :hidden:

   /recipes/recipes/loading_data_recipe
   /recipes/recipes/defining_a_neural_network
   /recipes/recipes/what_is_state_dict
   /recipes/recipes/saving_and_loading_models_for_inference
   /recipes/recipes/saving_and_loading_a_general_checkpoint
   /recipes/recipes/saving_multiple_models_in_one_file
   /recipes/recipes/warmstarting_model_using_parameters_from_a_different_model
   /recipes/recipes/save_load_across_devices
   /recipes/recipes/zeroing_out_gradients
   /recipes/recipes/profiler
   /recipes/recipes/custom_dataset_transforms_loader
   /recipes/recipes/Captum_Recipe
   /recipes/recipes/tensorboard_with_pytorch
   /recipes/recipes/dynamic_quantization
   /recipes/recipes/amp_recipe
   /recipes/recipes/tuning_guide
   /recipes/torchscript_inference
   /recipes/deployment_with_flask
   /recipes/distributed_rpc_profiling
