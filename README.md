# Machine Learning with Spotify

Testing different machine learning models in Python to classify "good" vs "bad" songs based on features provided by the Spotify web API.


Project structure:
* _data_ - Contains the base feature datasets generated through the generate_features module in src/features.
* _docker_ - Makefile and Dockerfile for building and running a Docker container with all the required dependencies for this project (builds on a tree of Docker containers that I maintain for Python development purposes).
* _models_ - Contains pickled model files (pre-trained).
* _notebooks_ - Contains data exploration and visualistion Jupyter Notebooks.
* _src_
    1. features - Source code for extracting JSON data via Spotify API and generating feature datasets.
    1. models - Contains files for training classification models and producing predictions given a new set of song features, as well as functions for pickling and loading pickled model files.

Credit goes to Nick Behrens for putting together the [original tutorial].

[original tutorial](https://towardsdatascience.com/making-your-own-discover-weekly-f1ac7546fedb)