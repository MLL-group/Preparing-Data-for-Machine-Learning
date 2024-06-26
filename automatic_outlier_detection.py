from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.neighbors import LocalOutlierFactor


def evaluate_linear_regression(_X, _y):
    # split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(_X, _y, test_size=0.33, random_state=1)
    print(X_train.shape, y_train.shape)
    # fit the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    # evaluate the model
    yhat = model.predict(X_test)
    # evaluate predictions
    mae = mean_absolute_error(y_test, yhat)
    print('MAE: %.3f' % mae)


def automatic_outlier_detection(_X, _y):
    # split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(_X, _y, test_size=0.33, random_state=1)
    print(X_train.shape, y_train.shape)
    # identify outliers in the training dataset
    lof = LocalOutlierFactor()
    yhat = lof.fit_predict(X_train)
    # select all rows that are not outliers
    mask = yhat != -1
    X_train, y_train = X_train[mask, :], y_train[mask]
    # summarize the shape of the updated training dataset
    print(X_train.shape, y_train.shape)
    # fit the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    # evaluate the model
    yhat = model.predict(X_test)
    # evaluate predictions
    mae = mean_absolute_error(y_test, yhat)
    print('MAE: %.3f' % mae)


if __name__ == "__main__":
    # load the dataset
    df = read_csv('dataset/housing.csv', header=None)
    # retrieve the array
    data = df.values
    # split into input and output elements
    X, y = data[:, :-1], data[:, -1]

    evaluate_linear_regression(X, y)
    automatic_outlier_detection(X, y)
