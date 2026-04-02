from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import GridSearchCV

def train_linear_regression(x_train, y_train):
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model


def train_ridge_regression(x_train, y_train):

    """ Funzione che implementa la Ridge Regression con la GridSearch"""

    parameters = [{"alpha": [0.001, 0.01, 0.1, 1 ,10, 100]}]
    RR=Ridge()
    Grid = GridSearchCV(RR, parameters, cv=4)
    Grid.fit(x_train, y_train)

    print("Il miglior iperparametro alpha è:", Grid.best_params_)

    model = Grid.best_estimator_
    model.fit(x_train, y_train)
    return model