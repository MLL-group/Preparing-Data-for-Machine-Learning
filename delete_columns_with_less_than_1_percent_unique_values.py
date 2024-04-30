from pandas import read_csv


def delete_columns_with_less_than_1_percent_unique_values(dataframe):
    # record columns to delete
    to_del = [i for i, v in enumerate(counts) if (float(v) / dataframe.shape[0] * 100) < 1]
    print(to_del)
    # drop useless columns
    dataframe.drop(to_del, axis=1, inplace=True)
    print(df.shape)


if __name__ == "__main__":
    # load the dataset
    df = read_csv('dataset/oil-spill.csv', header=None)
    print(df.shape)
    # get number of unique values for each column
    counts = df.nunique()
    print(counts)
    delete_columns_with_less_than_1_percent_unique_values(df)
