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
    return num_of_columns - 1

#############################################################################################
# "mean_imputation_table.loc[X, :].values[Y]" gets a cell at a certain location, where "X" is row and "Y" is the column
# and "mean_imputation_table" is the data frame that was imported from the .csv file


def get_mean(column_to_find_mean, data_frame):
    num_of_rows = find_num_of_rows(data_frame)
    sum_values = 0
    number_to_divide_by = 0
    for i in range(0, num_of_rows):
        temp = data_frame.loc[i].values[column_to_find_mean]
        if temp != "?":
            number_to_divide_by += 1
            sum_values += float(temp)

    return sum_values / number_to_divide_by


def impute_mean(data_frame):
    num_of_rows = find_num_of_rows(data_frame)
    num_of_columns = find_num_of_columns(data_frame)

    for x in range(0, find_num_of_columns(data_frame)):
        mean = get_mean(x, data_frame)
        for i in range(0, num_of_rows):
            temp = data_frame.loc[i].values[x]
            if temp == "?":
                data_frame.loc[i].values[x] = mean
    return data_frame






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

#                                               MAE STUFF


def get_mae(incomplete, imputed, complete):
    n = check_for_missing_data(incomplete)
    print("n = ", n)
    if n == 0:
        print("No missing value in data set")
        return 0

    num_of_columns = find_num_of_columns(complete)
    num_of_rows = find_num_of_rows(complete)
    sum_of_all = 0

    for x in range(1, num_of_columns):
        for i in range(0, num_of_rows):
            if float(imputed.loc[i].values[x]) != float(complete.loc[i].values[x]):
                temp = abs(float(imputed.loc[i].values[x]) - float(complete.loc[i].values[x]))
                sum_of_all = sum_of_all + temp
                print(sum_of_all)
    return sum_of_all / n


# def get_mae_05_mean(incomplete, imputed, complete):
#     print("MAE_05_mean =",get_mae(incomplete, imputed, complete))


def print_mae_values():
    print("print_mae_value")

# MAE_05_mean = 0.1234
# MAE_05_mean_conditional = 0.5678
# MAE_05_hd = 0.1234
# MAE_05_hd_conditional = 0.5678
# MAE_20_mean = 0.1234
# MAE_20_mean_conditional = 0.5678
# MAE_20_hd = 0.1234
# MAE_20_hd_conditional = 0.5678



#                                               END OF MAE STUFF


def mae_test():

    MAE_incomplete = pd.read_csv("MAE_test_INcomplete.csv")
    MAE_COMPLETE = pd.read_csv("MAE_test_complete.csv")
    MAE_imputed = pd.read_csv("MAE_test_imputed.csv")
    print(check_for_missing_data(MAE_incomplete))

    print(MAE_incomplete.head())
    print()
    print(MAE_imputed.head())
    print()
    print(MAE_COMPLETE.head())
    print()

    x = get_mae(MAE_incomplete, MAE_imputed, MAE_COMPLETE)
    print(x)


def main():
    print("START")
    print()

    dataset_missing05 = pd.read_csv("dataset_missing05.csv")
    dataset_missing20 = pd.read_csv("dataset_missing20.csv")
    dataset_complete = pd.read_csv("dataset_complete.csv")

    # Uncomment this to do impute mean for 05 and 20
    # impute_mean(dataset_missing05).to_csv("V00880079_missing05_imputed_mean.csv", index=False)
    impute_mean(dataset_missing20).to_csv("V00880079_missing20_imputed_mean.csv", index=False)




    #########################################################
    # dataset_missing20 = pd.read_csv("dataset_missing20.csv")
    #
    #
    # imputed_mean = pd.read_csv("V00880079_missing05_imputed_mean.csv")
    #
    # dataset_complete = pd.read_csv("dataset_complete.csv")
    #
    # print(get_mae(dataset_missing05, imputed_mean, dataset_complete))

    ############################################################


    print()
    print("END")


main()

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

# MAE_05_mean = 0.1234
# MAE_05_mean_conditional = 0.5678
# MAE_05_hd = 0.1234
# MAE_05_hd_conditional = 0.5678
# MAE_20_mean = 0.1234
# MAE_20_mean_conditional = 0.5678
# MAE_20_hd = 0.1234
# MAE_20_hd_conditional = 0.5678