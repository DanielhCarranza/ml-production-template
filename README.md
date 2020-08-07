# ML Production Template
This is codebase template is as a starting point for every Machine Learning project that you intended to deploy into Production.

This codebase is base on [Full Stack Deep Learning Course](https://course.fullstackdeeplearning.com/).

## Codebase

**`notebooks`:** **Explore and visualize your data** 

**`tasks`** : **Convenience scripts for running frequent tests and training commands**

**`training`**: **Logic for the training itself**

- **`model_core`: the core code of were the model lives (p.e. `cat_recognizer`, `text_classifier`, `tumor detector`, etc)**
    - **`datasets`**: **Logic for downloading, preprocessing, augmenting, and loading data**
    - **`models`: Models wrap networks and add functionality like loss functions. saving, loading, and training**
    - **`networks` : Code for constructing neural networks (dumb input | output mappings)**
    - **`tests`: Regression tests for the models code. Make sure a trained model performs well on important examples.**
    - **`weights` : Weights of the production model**
    - `predictor.py`: **wrapper for model that allows you to do inference**
    - `utils.py`

**`api`**: **Web server serving predictions. DockerFiles, Unit Tests, Flask,  etc.** 

**`evaluation`**: **Run the validation tests** 

**`experiment_manager`**: **Settings of your experiment manager (**p.e. wandb, tensorboard**)**

**`data`**: **use it for data versioning, storing data examples and metadata of your datasets. During traing use it to store your raw and processed data but don't push or save the datasets into the repo.** 

## Note

This [ML Project Template](https://bit.ly/33zMFqw) can help you managing your project
