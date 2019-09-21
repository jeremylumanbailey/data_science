# Load the Pandas libraries with alias 'pd'
import math

import pandas as pd


# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)

# Preview the first 5 lines of the loaded data
# data_frame = pd.read_csv("dataset_missing05.csv")

# class_column = 0
#
# for col in data_frame:
#     if col == 'Class':
#         break
#     class_column = class_column + 1


#                                           START MEAN IMPUTATION STUFF


def find_class_column(data_frame):
    for col in data_frame:
        if col == 'Class':
            break
        class_column = class_column + 1
    return class_column


def find_num_of_rows(data_frame):
    num_of_rows = len(data_frame.index)
    return num_of_rows


def find_num_of_columns(data_frame):
    num_of_columns = len(data_frame.columns)
    return num_of_columns

#############################################################################################
# "mean_imputation_table.loc[X, :].values[Y]" gets a cell at a certain location, where "X" is row and "Y" is the column
# and "mean_imputation_table" is the data frame that was imported from the .csv file


def get_mean(column_to_find_mean, data_frame):
    num_of_rows = find_num_of_rows(data_frame)
    sum_values = 0
    number_to_divide_by = 0
    for i in range(0, num_of_rows):
        temp = mean_imputation_table.loc[i, :].values[column_to_find_mean]
        if temp != "?":
            number_to_divide_by += 1
            sum_values += float(temp)

    return sum_values / number_to_divide_by


def impute_mean(column_to_impute, data_frame):
    mean_to_impute = get_mean(column_to_impute)
    num_of_rows = find_num_of_rows(data_frame)
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
            mean_imputation_table.loc[i].values[column_to_impute] = mean_to_impute


def run_both_classes_mean_imputation(x):
    impute_mean_conditional(x, "No")
    impute_mean_conditional(x, "Yes")


def run_conditional_mean_imputation(data_frame):
    num_of_columns = find_num_of_columns(data_frame)
    for x in range(0, num_of_columns - 1):
        run_both_classes_mean_imputation(x)


def run_mean_imputation(data_frame):
    num_of_columns = find_num_of_columns(data_frame)
    for x in range(0, num_of_columns - 1):
        impute_mean(x)


def check_for_missing_data(data_frame):
    num_of_columns = find_num_of_columns(data_frame)
    num_of_rows = find_num_of_rows(data_frame)
    num_of_missing_values = 0
    for x in range(0, num_of_columns):
        for i in range(0, num_of_rows):
            if data_frame.loc[i].values[x] == "?":
                num_of_missing_values = num_of_missing_values + 1

    return num_of_missing_values





#                                           END OF MEAN IMPUTATION STUFF


#                                           START OF HOT DECK IMPUTATION

# "mean_imputation_table.loc[X, :].values[Y]" gets a cell at a certain location,
# where "X" is row and "Y" is the column
# and "mean_imputation_table" is the data frame that was imported from the .csv file
#
# hot_deck_table = pd.read_csv("test.csv")
#
# num_of_rows2 = len(hot_deck_table.index)
# num_of_columns2 = len(hot_deck_table.columns)
#
# print(hot_deck_table.head())
# print()
#
# # for x in range(0, num_of_rows2 - 1):
# #     run_both_classes_mean_imputation(x)
#
# # for x in range(0, num_of_columns2 - 1):
# #     run_both_classes_mean_imputation(x)
#
# current_row = 0
# col1 = 0
# col2 = 1
# col3 = 2
# col4 = 3
#
# # for x in range(0, num_of_columns - 1):
# #     run_both_classes_mean_imputation(x)
#
#
# if "?" in hot_deck_table.loc[current_row].values[col1] :
#     val1 = 0
# else:
#     val1 = float(hot_deck_table.loc[current_row].values[col1])
#
# if "?" in hot_deck_table.loc[2].values[0]:
#     val2 = 0
# else:
#     val2 = float(hot_deck_table.loc[2].values[0])
#
# if "?" in hot_deck_table.loc[current_row].values[col2]:
#     val3 = 0
# else:
#     val3 = float(hot_deck_table.loc[current_row].values[col2])
#
# if "?" in hot_deck_table.loc[2].values[1]:
#     val4 = 0
# else:
#     val4 = float(hot_deck_table.loc[2].values[1])
#
# num_to_divide_by = 2
#
#
#
# bruh = math.sqrt(math.pow((val1 - val2), 2) + math.pow((val3 - val4), 2)) / num_to_divide_by
#
# print(hot_deck_table.loc[0].values[2] == "?")
#
# print(round(bruh, 4))
# hot_deck_table.loc[0].values[2] = "????" + hot_deck_table.loc[2].values[2]
#
# print()
# print(hot_deck_table.head())
# print()
#
# hot_deck_table.loc[0].values[2] = hot_deck_table.loc[0].values[2][4:]
#
# print(hot_deck_table.loc[0].values[2] == "?")
#
#     # hot_deck_table.loc[2].values[2]
# print()
#
# print()
# print(hot_deck_table.head())
# print()

#
# print("Number of columns :", num_of_columns2)
# print("Number of rows :", num_of_rows2)



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


def main():
    print("START")
    print()
    complete_data = pd.read_csv("dataset_complete.csv")

    CURRENT_TABLE = pd.read_csv("test.csv")

    print(CURRENT_TABLE.head())
    print()

    print(check_for_missing_data(CURRENT_TABLE))

    print(CURRENT_TABLE.head())
    print()

    # CURRENT_TABLE.to_csv("V00880079_missing20_imputed_mean.csv")

    print()
    print("END")


main()



