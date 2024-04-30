from pandas import read_csv


def identify_rows_that_contain_duplicate_data(data):
    # calculate duplicates
    duplicates = data.duplicated()
    # report if there are any duplicates
    print(duplicates.any())
    # list all duplicate rows
    print(data[duplicates])


if __name__ == "__main__":
    # load the dataset
    df = read_csv('dataset/iris.csv', header=None)

    identify_rows_that_contain_duplicate_data(df)
