from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
from matplotlib import pyplot


# load the dataset
def load_dataset(filename):
    # load the dataset as a pandas DataFrame
    data = read_csv(filename, header=None)
    # retrieve numpy array
    dataset = data.values
    # split into input (X) and output (y) variables
    _X = dataset[:, :-1]
    _y = dataset[:, -1]
    # format all fields as string
    _X = _X.astype(str)
    return _X, _y


# prepare input data
def prepare_inputs(_X_train, _X_test):
    oe = OrdinalEncoder()
    oe.fit(_X_train)
    _X_train_enc = oe.transform(_X_train)
    _X_test_enc = oe.transform(_X_test)
    return _X_train_enc, _X_test_enc


# prepare target
def prepare_targets(_y_train, _y_test):
    le = LabelEncoder()
    le.fit(_y_train)
    _y_train_enc = le.transform(_y_train)
    _y_test_enc = le.transform(_y_test)
    return _y_train_enc, _y_test_enc


# feature selection
def select_features(_X_train, _y_train, _X_test):
    _fs = SelectKBest(score_func=mutual_info_classif, k='all')
    _fs.fit(_X_train, _y_train)
    _X_train_fs = _fs.transform(_X_train)
    _X_test_fs = _fs.transform(_X_test)
    return _X_train_fs, _X_test_fs, _fs


if __name__ == "__main__":
    # load the dataset
    X, y = load_dataset('dataset/breast-cancer.csv')
    # split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
    # prepare input data
    X_train_enc, X_test_enc = prepare_inputs(X_train, X_test)
    # prepare output data
    y_train_enc, y_test_enc = prepare_targets(y_train, y_test)
    # feature selection
    X_train_fs, X_test_fs, fs = select_features(X_train_enc, y_train_enc, X_test_enc)
    # what are scores for the features
    for i in range(len(fs.scores_)):
        print('Feature %d: %f' % (i, fs.scores_[i]))
    # plot the scores
    pyplot.bar([i for i in range(len(fs.scores_))], fs.scores_)
    pyplot.show()
