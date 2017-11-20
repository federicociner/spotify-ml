from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import hamming_loss
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

import pickle


def model_report(y_pred, y_true):
    clf_report = classification_report(y_true, y_pred)

    report = ''
    report += 'Accuracy: {} \n'.format(accuracy_score(y_true, y_pred))
    report += 'ROC: {} \n'.format(roc_auc_score(y_true, y_pred))
    report += 'Average precision score: {} \n'.format(
        average_precision_score(y_true, y_pred))
    report += 'F1: {} \n'.format(f1_score(y_true, y_pred))
    report += 'Hamming loss: {} \n'.format(hamming_loss(y_true, y_pred))
    report += '\n'
    report += clf_report

    return report


def generate_param_grid():
    param_grid = {
        'n_estimators': [300, 500, 900, 1200, 1500],
        'max_depth': [4, 8, 10, 12, 24],
        'learning_rate': [0.01, 0.05, 0.1, 0.2],
        'subsample': [0.6, 0.7, 0.8, 0.9]
    }

    return param_grid


def train_model(X_train, y_train, scoring='roc_auc', n_jobs=2, cv=4):
    clf_initial = XGBClassifier(n_jobs=n_jobs)  # instantiate classifier
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
