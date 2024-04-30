from numpy import isnan, mean, std
from pandas import read_csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from matplotlib import pyplot


def summarize_missing_values_for_each_column(dataframe):
    # summarize the first few rows
    print(dataframe.head())
    # summarize the number of rows with missing values for each column
    for i in range(dataframe.shape[1]):
        # count number of rows with missing values
        n_miss = dataframe[[i]].isnull().sum()
        perc = n_miss / dataframe.shape[0] * 100
        print(f'> {i}, Missing: {n_miss} {perc}')


def simple_imputer_data_transform(dataframe):
    # split into input and output elements
    data = dataframe.values
    ix = [i for i in range(data.shape[1]) if i != 23]
    X, y = data[:, ix], data[:, 23]
    # summarize total missing
    print('Missing: %d' % sum(isnan(X).flatten()))
    # define imputer
    imputer = SimpleImputer(strategy='mean')
    # fit on the dataset
    imputer.fit(X)
    # transform the dataset
    Xtrans = imputer.transform(X)
    # summarize total missing
    print('Missing: %d' % sum(isnan(Xtrans).flatten()))


def comparison_different_simpleimputer_strategy_data_transform(dataframe):
    # split into input and output elements
    data = dataframe.values
    ix = [i for i in range(data.shape[1]) if i != 23]
    X, y = data[:, ix], data[:, 23]
    # evaluate each strategy on the dataset
    results = list()
    strategies = ['mean', 'median', 'most_frequent', 'constant']
    for s in strategies:
        # create the modeling pipeline
        pipeline = Pipeline(steps=[('i', SimpleImputer(strategy=s)), ('m',
                                                                      RandomForestClassifier())])
        # evaluate the model
        cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
        scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
        # store results
        results.append(scores)
        print('>%s %.3f (%.3f)' % (s, mean(scores), std(scores)))
    # plot model performance for comparison
    pyplot.boxplot(results, labels=strategies, showmeans=True)
    pyplot.show()


if __name__ == "__main__":
    # load dataset
    df = read_csv('dataset/horse-colic.csv', header=None, na_values='?')
    summarize_missing_values_for_each_column(df)
    simple_imputer_data_transform(df)
    comparison_different_simpleimputer_strategy_data_transform(df)
