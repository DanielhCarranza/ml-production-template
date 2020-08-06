# Machine Learning Production Template
This is codebase template to deploy Machine Learning into Production. Use it as a startting point for every ML project that you intended to deploy to the real world.
This codebase is strongly base on [Full Stack Deep Learning Course](https://course.fullstackdeeplearning.com/) 

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
