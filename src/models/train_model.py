from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier
import pickle


def generate_param_grid():
    param_grid = {
        'n_estimators': [10, 50, 100, 200, 400, 600, 800],
        'max_depth': [4, 5, 6, 7, 8, 9, 10, 12, 14],
        'learning_rate': [0.075, 0.1, 0.125, 0.15, 0.175],
        'subsample': [0.6, 0.7, 0.8, 0.9, 1.0],
        'gamma': [0.05, 0.075, 0.1, 0.125, 0.15],
        'reg_lambda': [0.005, 0.01, 0.015, 0.2, 0.25]
    }

    return param_grid


def train_model(X_train, y_train, scoring='roc_auc', n_jobs=2, cv=3):
    clf_initial = XGBClassifier()  # instantiate classifier
    param_grid = generate_param_grid()  # get parameters to tune
    grid = GridSearchCV(clf_initial, cv=cv, n_jobs=n_jobs,
                        param_grid=param_grid, scoring=scoring)
    grid.fit(X_train, y_train)

    # get best estimator
    best_clf = grid.best_estimator_

    # get the best parameters
    best_params = grid.best_params_

    return {"best_params": best_params, "best_estimator": best_clf}


def save_model(model_object, filepath):
    with open(filepath, 'wb+') as model_file:
        pickler = pickle.Pickler(model_file)
        pickler.dump(model_object)


def load_model(filepath):
    with open(filepath, 'rb+') as model_file:
        model_object = pickle.load(model_file)

    return model_object
