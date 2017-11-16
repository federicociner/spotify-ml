# Machine Learning with Spotify

Testing different machine learning models in Python to classify "good" vs "bad" songs based on features provided by the Spotify web API.

Credits to Nick Behrens for putting together the original tutorial at https://towardsdatascience.com/making-your-own-discover-weekly-f1ac7546fedb.

See below for a breakdown of the project directory:
* _data_ - contains the base feature datasets generated through the generate_features module in src/features
* _models_ - contains cached/pre-trained models
* _notebooks_ - contains data exploration and visualistion Jupyter Notebooks
* _src_
    1. features - source code for extracting JSON data via Spotify API and generate feature datasets
    1. models - contains
