"""
Created by:
- Jesús Omar Cuenca Espino  (JOmarCuenca)

Date: 03/09/2021
"""

import numpy as np
from progressbar import progressbar, streams

# Setup Progressbar wrapper function
streams.wrap_stderr()

class LinearRegressor():
    def __init__(self, alpha=0.1, epochs=1):
        self.alpha = alpha
        self.epochs = epochs
        self.costs = []
        self.theta = None



    def _cost_function(self, y_pred, y, m):
        """
        Gets the cost for the predicted values when contrasted with the correct ones.
        y_pred: An (1 x m) vector that corresponds to the values predicted by the Linear Regressor
        y: An (1 x m) vector that corresponds to the y (right) values in the dataset
        m: the number of samples (it could be also inferred from the shape of y or y_pred)
        """
        temp = y_pred - y 
        cost : np.ndarray = np.dot(temp, temp.T)
        return (cost.flatten()[0])/(2*m)

    def _hypothesis(self, X):
        """
        Calculates the hypothesis for the given examples using the current self.theta values.
        X: an m x n array of m samples/examples with n features each.
        """
        # * is element wise multiplication
        # numpy.dot(), or @ operator will work

        return np.dot(self.theta.T, X)

    def _cost_function_derivative(self, y_pred, y, X, m):
        """
        Calculates the derivatives (gradient) of the cost function through the obtained/predicted values.
        y_pred: an (1 x m) array with the predicted values for X dataset
        y: an (1 x m) array with the right values for X dataset
        X: the input dataset
        m: the number of samples in the dataset
        """

        temp = y_pred - y # (1 x m)

        temp = np.dot(temp,X.T) # (1 x m) * (m x n) = (1 x n)

        return (self.alpha/m) * temp.T # scalar * (n x 1)

    def fit(self, X, y):
        """
        Fits the linear regressor to the values in the dataset.
        X: is an (n x m) vector, where n is the number of features and m is the number of samples/examples
        y: is an (1 x m) vector, where m is the number of samples/examples
        """

        n, m = X.shape[0], X.shape[1]

        # theta is (nx1) (one theta per dimension)
        self.theta = np.random.uniform(-10, 10, (n, 1))

        for _ in progressbar(range(self.epochs)):
            # Get predictions
            y_pred = self.predict(X)

            # calculate cost
            cost = self._cost_function(y_pred, y, m)
            

            # gradient is an (n) x 1 array, it refers to the derivate per theta
            gradient : np.ndarray = self._cost_function_derivative(y_pred, y, X, m)

            if(gradient.shape != (2,1)):
                print("What the Fuck?")

            # delta/update rule
            self.theta = self.theta - gradient

            self.costs.append(cost)
            pass

        print("Final theta is {} (cost: {})".format(self.theta.T, cost))

    def predict(self, X):
        """
        Predicts the values for the given X samples using the current configuration of the Linear Regressor.

        X: an (n x m') array with m' samples of n dimensions whose value must be predicted.
        """

        # ! You could simply call the hypothesis here
        return self._hypothesis(X)
