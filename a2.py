# Load the Pandas libraries with alias 'pd'
import pandas as pd

print("START")


# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
mean_imputation_table = pd.read_csv("test.csv")
# Preview the first 5 lines of the loaded data
mean_imputation_table.head()
print(mean_imputation_table.head())
print()
num_of_rows = len(mean_imputation_table.index)
num_of_columns = len(mean_imputation_table.columns)

#############################################################################################
# "mean_imputation_table.loc[X, :].values[Y]" gets a cell at a certain location, where "X" is row and "Y" is the column
class_column = 0

for col in mean_imputation_table:
    if col == 'Class':
        break
    class_column = class_column + 1

def get_mean(column_to_find_mean):
    sum_values = 0
    number_to_divide_by = 0
    for i in range(0, num_of_rows):
        temp = mean_imputation_table.loc[i, :].values[column_to_find_mean]
        if temp != "?":
            number_to_divide_by += 1
            sum_values += float(temp)

    return sum_values / number_to_divide_by


def impute_mean(column_to_impute):
    mean_to_impute = get_mean(column_to_impute)
    for i in range(0, num_of_rows):
        temp = mean_imputation_table.loc[i, :].values[column_to_impute]
        if temp == "?":
            mean_imputation_table.loc[i, :].values[column_to_impute] = mean_to_impute


# for x in range(0, num_of_columns - 1):
#     impute_mean(x)

#############################################################################################

def get_mean_conditional(column_to_find_mean, class_type):
    sum_of_values = 0
    number_to_divide_by = 0

    for i in range(0, num_of_rows):

        temp = mean_imputation_table.loc[i, :].values[column_to_find_mean]
        temp2 = mean_imputation_table.loc[i, :].values[class_column]
        if temp != "?" and temp2 == class_type:
            number_to_divide_by += 1
            sum_of_values += float(temp)

    return sum_of_values / number_to_divide_by


def impute_mean_conditional(column_to_impute, class_type):
    mean_to_impute = get_mean_conditional(column_to_impute, class_type)
    for i in range(0, num_of_rows):
        temp = mean_imputation_table.loc[i, :].values[column_to_impute]
        temp2 = mean_imputation_table.loc[i, :].values[class_column]
        if temp == "?" and temp2 == class_type:
            mean_imputation_table.loc[i, :].values[column_to_impute] = mean_to_impute


def run_both_classes_mean_imputation(x):
    impute_mean_conditional(x, "No")
    impute_mean_conditional(x, "Yes")


for x in range(0, num_of_columns - 1):
    run_both_classes_mean_imputation(x)

# impute_mean_conditional(2, "No")
# print(get_mean_conditional(2, "No"))

print(mean_imputation_table.head())
print()


print("Number of columns :", num_of_columns)
print("Number of rows :", num_of_rows)

# Use DATATABLE.to_csv("V00880079....csv") to create tables
# data.to_csv("test.csv")
#
# V00880079_missing05_imputed_mean.csv
# V00880079_missing05_imputed_mean_conditional.csv
# V00880079_missing05_imputed_hd.csv
# V00880079_missing05_imputed_hd_conditional.csv
# V00880079_ missing20_imputed_mean.csv
# V00880079_missing20_imputed_mean_conditional.csv
# V00880079_missing20_imputed_hd.csv
# V00880079_missing20_imputed_hd_conditional.csv

print("END")
