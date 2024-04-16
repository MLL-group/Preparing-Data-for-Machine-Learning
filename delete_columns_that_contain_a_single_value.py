from pandas import read_csv


def delete_columns_that_contain_a_single_value(df):
    # record columns to delete
    to_del = [i for i, v in enumerate(counts) if v == 1]
    print(to_del)
    # drop useless columns
    df.drop(to_del, axis=1, inplace=True)
    print(df.shape)


if __name__ == "__main__":
    # load the dataset
    df = read_csv('dataset/oil-spill.csv', header=None)
    print(df.shape)
    # get number of unique values for each column
    counts = df.nunique()
    print(counts)
    delete_columns_that_contain_a_single_value(df)
