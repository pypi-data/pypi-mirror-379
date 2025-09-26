import numpy as np

class LinearRegression:
    def __init__(self, use_intercept=True):
        self.use_intercept = use_intercept
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        X = np.array(X, dtype=float)
        y = np.array(y, dtype=float)

        if self.use_intercept:
            ones = np.ones((X.shape[0], 1))
            X = np.hstack((ones, X))

        # Formule des moindres carrés : β = (X^T X)^(-1) X^T y
        beta = np.linalg.pinv(X.T @ X) @ X.T @ y


        if self.use_intercept:
            self.intercept_ = beta[0]
            self.coef_ = beta[1:]
        else:
            self.intercept_ = 0.0
            self.coef_ = beta

    def predict(self, X):
        X = np.array(X, dtype=float)

        y_pred = X @ self.coef_
        if self.use_intercept:
            y_pred += self.intercept_
        return y_pred
