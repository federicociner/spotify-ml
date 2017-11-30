# Machine Learning with Spotify

Testing different classifiers in Python to predict "good" vs "bad" songs based on features provided by the Spotify web API - refer to the [Jupyter Notebook] for a detailed walkthrough of my analysis and model benchmarking.

Project structure:
* _data_ - Contains the base feature datasets generated through the generate_features module in src/features.
* _docker_ - Makefile and Dockerfile for building and running a Docker container with all the required dependencies for this project (builds on a tree of Docker containers that I maintain for Python development purposes).
* _models_ - Contains pickled model files (pre-trained).
* _notebooks_ - Contains the main data exploration, visualisation and classifier benchmarking notebook
* _src_
    1. features - Source code for extracting JSON data via Spotify API and generating feature datasets.
    1. models - Contains files for training classification models and producing predictions given a new set of song features, as well as functions for pickling and loading pickled model files.
    1. visualisation - User modules used to create key visualisations, including histograms, correlation matrices and confusion matrices. Also includes a library for formatting Jupyter Notebooks with some custom JavaScript.

Credit goes to Nick Behrens for putting together the original [tutorial].

[tutorial]: https://towardsdatascience.com/making-your-own-discover-weekly-f1ac7546fedb
[Jupyter Notebook]: http://nbviewer.jupyter.org/github/FedericoCiner/spotify-ml/blob/master/notebooks/1.0-fac-spotifyml-presentation.ipynb