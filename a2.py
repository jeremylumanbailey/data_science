print("START")

# Load the Pandas libraries with alias 'pd'
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
mean_imputation_table = pd.read_csv("test.csv")
# Preview the first 5 lines of the loaded data
mean_imputation_table.head()
print(mean_imputation_table.head())
print()
num_of_rows = len(mean_imputation_table.index)


def get_mean(column_to_find_mean):
    sum_values_in_f3 = 0
    valid_values_in_f3 = 0
    i = 0
    while i < num_of_rows:
        x = mean_imputation_table.loc[i, :].values[column_to_find_mean]
        if x != "?":
            valid_values_in_f3 += 1
            sum_values_in_f3 += float(x)
        i += 1

    return(sum_values_in_f3 / valid_values_in_f3)  # print(valid_values_in_f3)


def impute_mean(column_to_impute):
    mean_to_impute = get_mean(column_to_impute)
    i = 0
    while i < num_of_rows:
        x = mean_imputation_table.loc[i, :].values[column_to_impute]
        if x == "?":
            mean_imputation_table.loc[i, :].values[column_to_impute] = mean_to_impute
        i += 1



impute_mean(2)

print(mean_imputation_table.head())
print()

print("Number of rows not including header:", num_of_rows)

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
