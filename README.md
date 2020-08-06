# ml-production-template
This is codebase template to deploy Machine Learning into Production. 

**`Notebooks`:** **Explore and visualize your data** 

**`Tasks`** : **Convenience scripts for running frequent tests and training commands**

**`Training`**: **Logic for the training itself**

- **`Recognizer`: the core code of the model lives**
    - **`Datasets`**: **Logic for downloading, preprocessing, augmenting, and loading data**
    - **`Models`: Models wrap networks and add functionality like loss functions. saving, loading, and training**
    - **`Networks` : Code for constructing neural networks (dumb input | output mappings)**
    - **`Tests`: Regression tests for the models code. Make sure a trained model performs well on important examples.**
    - **`Weights` : Weights of the production model**
    - `predictor.py`: **wrapper for model that allows it to recognize a single character**
    - `utils.py`

**`api`**: **Web server serving predictions. DockerFiles, Unit Tests,  etc.** 

**`evaluation`**: **Run the validation tests** 

**`experiment_manager`**: **Settings of your experiment manager (**p.e. wandb, tensorboard**)**
