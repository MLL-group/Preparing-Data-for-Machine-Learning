# Tutorial 




## Presentation
https://docs.google.com/presentation/d/1RyU7X3QJiSzWs3UFx46aB7O4TrQas_y5zb3EGAhgT3g/edit?usp=sharing

## Exercises

### Drop useless columns (with one single value)
```bash
make exercise-1
```
### Drop useless columns (less than 1% unique values)
```bash
make exercise-2
```
### Drop useless columns (with low variance)
```bash
make exercise-3
```
### Identify rows with duplicates
```bash
make exercise-4
```
### Drop rows with duplicates
```bash
make exercise-5
```
### Drop rows with outliers
```bash
make exercise-6
```
### Drop rows with missing values
```bash
make exercise-7
```
### Statistical imputation (mean/median/mode)
```bash
make exercise-8
```
### Statistical imputation (on prediction)
```bash
make exercise-9
```
### KNN imputation
```bash
make exercise-10
```
### KNN imputation (on prediction)
```bash
make exercise-11
```
### Feature selection: mutual information (categorical data)
Mutual information is calculated between two variables and measures the reduction in uncertainty for one variable
given a known value of the other variable
```bash
make exercise-12
```
### Feature selection: model with all features
```bash
make exercise-13
```
### Feature selection: chi squared
Pearson’s chi-squared statistical hypothesis test is an example of a test for independence between categorical variables
```bash
make exercise-14
```
### Feature selection: mutual information
```bash
make exercise-15
```
### Feature selection: no correlation
```bash
make exercise-16
```
### Feature selection: with correlation
```bash
make exercise-17
```
### Feature selection: recursive feature elimination (RFE)
RFE works by searching for a subset of features by starting with all features in the training
dataset and successfully removing features until the desired number remains

RFE is a wrapper-type feature selection algorithm. This means that a different machine
learning algorithm is given and used in the core of the method, is wrapped by RFE, and used
to help select features

```bash
make exercise-18
```
### Scaler: MinMax
```bash
make exercise-19
```
### Scaler: KNN
```bash
make exercise-20
```
### Normalization: Yeo Johnson
A power transform will make the probability distribution of a variable more Gaussian
```bash
make exercise-21
```
### Normalization: KNN
```bash
make exercise-22
```
### Dimensionality Reduction: PCA
```bash
make exercise-23
```

## Based on book
Data Preparation for Machine Learning Data Cleaning, Feature Selection, and Data Transforms in Python 

by Jason Brownlee
## Datasets

https://raw.githubusercontent.com/jbrownlee/Datasets/master/oil-spill.csv
https://raw.githubusercontent.com/jbrownlee/Datasets/master/oil-spill.names

https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv
https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.names

https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv
https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.names

https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csvv
https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.names

https://raw.githubusercontent.com/jbrownlee/Datasets/master/horse-colic.csv
https://raw.githubusercontent.com/jbrownlee/Datasets/master/horse-colic.names

https://raw.githubusercontent.com/jbrownlee/Datasets/master/breast-cancer.csv
https://raw.githubusercontent.com/jbrownlee/Datasets/master/breast-cancer.names


https://raw.githubusercontent.com/jbrownlee/Datasets/master/sonar.csv
https://raw.githubusercontent.com/jbrownlee/Datasets/master/sonar.names