from pandas import read_csv
from sklearn.feature_selection import VarianceThreshold
from matplotlib import pyplot
from numpy import arange


def remove_columns_with_low_variance(df):
    data = df.values
    X = data[:, :-1]
    y = data[:, -1]
    print(X.shape, y.shape)
    # define thresholds to check
    thresholds = arange(0.0, 0.55, 0.05)
    # apply transform with each threshold
    results = list()
    for t in thresholds:
        # define the transform
        transform = VarianceThreshold(threshold=t)
        # transform the input data
        X_sel = transform.fit_transform(X)
        # determine the number of input features
        n_features = X_sel.shape[1]
        print('>Threshold=%.2f, Features=%d' % (t, n_features))
        # store the result
        results.append(n_features)
    # plot the threshold vs the number of selected features
    pyplot.plot(thresholds, results)
    pyplot.show()


if __name__ == "__main__":
    # load the dataset
    df = read_csv('dataset/oil-spill.csv', header=None)
    print(df.shape)
    # get number of unique values for each column
    counts = df.nunique()
    print(counts)
    remove_columns_with_low_variance(df)
