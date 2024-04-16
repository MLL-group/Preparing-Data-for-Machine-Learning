from pandas import read_csv


def identify_rows_that_contain_duplicate_data(df):
    # calculate duplicates
    dups = df.duplicated()
    # report if there are any duplicates
    print(dups.any())
    # list all duplicate rows
    print(df[dups])


if __name__ == "__main__":
    # load the dataset
    df = read_csv('dataset/iris.csv', header=None)

    identify_rows_that_contain_duplicate_data(df)
