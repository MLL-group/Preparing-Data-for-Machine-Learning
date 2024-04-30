from numpy import nan
from pandas import read_csv
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


def evaluate_model(ds):
    # split dataset into inputs and outputs
    values = ds.values
    X = values[:, 0:8]
    y = values[:, 8]
    # define the model
    model = LinearDiscriminantAnalysis()
    # define the model evaluation procedure
    cv = KFold(n_splits=3, shuffle=True, random_state=1)
    # evaluate the model
    result = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
    # report the mean performance
    print('Accuracy: %.3f' % result.mean())


if __name__ == "__main__":
    # load the dataset
    dataset = read_csv('dataset/pima-indians-diabetes.csv', header=None)
    # summarize the dataset
    print(dataset.describe())
    print(print(dataset.head(20)))
    # count the number of missing values for each column
    num_missing = (dataset[[1, 2, 3, 4, 5]] == 0).sum()
    # report the results
    print(num_missing)
    # replace '0' values with 'nan'
    dataset[[1, 2, 3, 4, 5]] = dataset[[1, 2, 3, 4, 5]].replace(0, nan)

    # count the number of nan values in each column
    print(dataset.isnull().sum())
    print(dataset.head(20))

    try:
        evaluate_model(dataset)
    except ValueError:
        print("Error: cant evaluate model with NaN values")

    # drop rows with missing values
    dataset.dropna(inplace=True)
    evaluate_model(dataset)
