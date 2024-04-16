from pandas import read_csv


def delete_rows_that_contain_duplicate_data(df):
    # delete duplicate rows
    df.drop_duplicates(inplace=True)
    print(df.shape)


if __name__ == "__main__":
    # load the dataset
    df = read_csv('dataset/iris.csv', header=None)
    print(df.shape)
    delete_rows_that_contain_duplicate_data(df)
