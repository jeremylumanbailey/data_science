import math
import pandas as pd


def find_class_column(data_frame):
    class_col = 0
    for col in data_frame:
        if col == 'Class':
            break
        class_col = class_col + 1
    return class_col


def find_num_of_rows(data_frame):
    num_of_rows = len(data_frame.index)
    return num_of_rows


def find_num_of_columns(data_frame):
    num_of_columns = len(data_frame.columns)
    return num_of_columns - 1


def check_for_missing_data(data_frame):
    num_of_columns = find_num_of_columns(data_frame)
    num_of_rows = find_num_of_rows(data_frame)
    num_of_missing_values = 0
    for x in range(0, num_of_columns):
        for i in range(0, num_of_rows):
            if data_frame.loc[i].values[x] == "?":
                num_of_missing_values = num_of_missing_values + 1

    return num_of_missing_values

#                                           START MEAN IMPUTATION STUFF


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


def run_mean_imputation(data_frame):
    num_of_columns = find_num_of_columns(data_frame)
    for x in range(0, num_of_columns - 1):
        impute_mean(x)


#############################################################################################


def run_conditional_mean_imputation(data_frame):
    num_of_columns = find_num_of_columns(data_frame)
    num_of_rows = find_num_of_rows(data_frame)
    class_column = find_class_column(data_frame)

    def get_mean_conditional(column_to_find_mean, class_type):
        sum_of_values = 0
        number_to_divide_by = 0

        for i in range(0, num_of_rows):

            temp = data_frame.loc[i].values[column_to_find_mean]
            temp2 = data_frame.loc[i].values[class_column]
            if temp != "?" and temp2 == class_type:
                number_to_divide_by += 1
                sum_of_values += float(temp)

        return sum_of_values / number_to_divide_by

    def impute_mean_conditional(column_to_impute, class_type):
        mean_to_impute = get_mean_conditional(column_to_impute, class_type)
        for i in range(0, num_of_rows):
            temp = data_frame.loc[i].values[column_to_impute]
            temp2 = data_frame.loc[i].values[class_column]
            if temp == "?" and temp2 == class_type:
                data_frame.loc[i].values[column_to_impute] = mean_to_impute

    def run_both_classes_mean_imputation(x):
        impute_mean_conditional(x, "No")
        impute_mean_conditional(x, "Yes")

    for x in range(0, num_of_columns):
        run_both_classes_mean_imputation(x)

    return data_frame
#                                           END OF MEAN IMPUTATION STUFF

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



                                          # START OF HOT DECK IMPUTATION

# "mean_imputation_table.loc[X, :].values[Y]" gets a cell at a certain location,
# where "X" is row and "Y" is the column
# and "mean_imputation_table" is the data frame that was imported from the .csv file



def hot_deck_imputation(data_frame):
    # print(data_frame)
    num_of_columns = find_num_of_columns(data_frame)
    num_of_rows = find_num_of_rows(data_frame)


    def sqringfunction(column):
        print()

    def get_distances(row, column):
        distances = {}

        return distances

    def find_row(row, column):
        distances = get_distances(row, column)
        return distances.get(min(distances))

    def find_most_similar_object(row, column):
        in_row = find_row(row, column)
        most_similar = data_frame.loc[in_row].values[column]
        return most_similar

    def impute_hd(row, column):
        data_frame.loc[row].values[column] = find_most_similar_object(row, column)

    def find_missing_values():
        for x in range(0, num_of_columns):
            for i in range(0, num_of_rows):
                if data_frame.loc[i].values[x] == "?":
                    impute_hd(i, x)

    def minusfunciton(obj, obj_n, col):
        if "?" in data_frame.loc[obj].values[col] or "?" in data_frame.loc[obj_n].values[col]:
            return 0
        else:
            return math.pow(
                float(data_frame.loc[obj].values[col])
                - float(data_frame.loc[obj_n].values[col]), 2)

    def function21(base_row, compared_row):
        dis_sum = 0
        m = 0
        for x in range(base_row, num_of_columns):
            if minusfunciton(base_row, compared_row, x) != 0:
                m = m + 1
                dis_sum = minusfunciton(0, compared_row, x) + dis_sum
        # print(minusfunciton(0, 1, x))
        # print(dis_sum)
        # print(m)
        if m != 0:
            print(math.sqrt(dis_sum) / m)
        #print("should be:",math.sqrt(math.pow(0.40256 - 0.41139, 2) + math.pow(0.1497 - 0.3014, 2)) / 2)

    for x in range(0, num_of_rows):
        function21(0, x)
    # return data_frame


def main():
    print("START")
    print()

    dataset_missing05 = pd.read_csv("dataset_missing05.csv")
    dataset_missing20 = pd.read_csv("dataset_missing20.csv")
    dataset_complete = pd.read_csv("dataset_complete.csv")

########################################################################################################################
#
#   MEAN (NOT CONDITIONAL)
#
########################################################################################################################
    # Uncomment this block to do impute mean for 05 and 20 using mean
    # impute_mean(dataset_missing05).to_csv("V00880079_missing05_imputed_mean.csv", index=False)
    # impute_mean(dataset_missing20).to_csv("V00880079_missing20_imputed_mean.csv", index=False)

    # # Uncomment this block to get MAE for missing05 via imputed mean ANSWER: 0.05557397018967987
    # imputed_mean05 = pd.read_csv("V00880079_missing05_imputed_mean.csv")
    # print("MAE_05_mean =", '%.4f' % get_mae(dataset_missing05, imputed_mean05, dataset_complete))

    # Uncomment this block to get MAE for missing20 via imputed mean ANSWER: 0.054991356823082996
    # imputed_mean20 = pd.read_csv("V00880079_missing20_imputed_mean.csv")
    # print("MAE_20_mean =", '%.4f' % get_mae(dataset_missing20, imputed_mean20, dataset_complete))

########################################################################################################################
#
#   MEAN CONDITIONAL
#
########################################################################################################################
    # # Uncomment this block to do impute conditional mean for 05 and 20 using conditional mean
    # run_conditional_mean_imputation(dataset_missing05).to_csv("V00880079_missing05_imputed_mean_conditional.csv", index=False)
    # run_conditional_mean_imputation(dataset_missing20).to_csv("V00880079_missing20_imputed_mean_conditional.csv", index=False)

    # Uncomment this block to get MAE for missing05 via imputed mean conditional ANSWER: 0.0545
    # imputed_mean_conditional05 = pd.read_csv("V00880079_missing05_imputed_mean_conditional.csv")
    # print("MAE_05_mean_conditional =", '%.4f' % get_mae(dataset_missing05, imputed_mean_conditional05, dataset_complete))

    # Uncomment this block to get MAE for missing20 via imputed mean conditional ANSWER: 0.0136
    # imputed_mean_conditional20 = pd.read_csv("V00880079_missing05_imputed_mean_conditional.csv")
    # print("MAE_20_mean_conditional =", '%.4f' % get_mae(dataset_missing20, imputed_mean_conditional20, dataset_complete))
########################################################################################################################

    testdata = pd.read_csv("test.csv")

    print()
    hot_deck_imputation(testdata)

    print()

    # distances_row = {}
    # distances= distances_row
    # # distances_row[DISTANCE] = X_VALUE
    #
    # distances_row[0.1157] = 2
    # distances_row[0.4334] = 1
    # print(distances_row)
    # print()
    # print(max(distances_row))
    # print(distances_row.get(min(distances_row)))
    # print(distances)
    print()
    print("END")
main()





# def mae_test():
#
#     MAE_incomplete = pd.read_csv("MAE_test_INcomplete.csv")
#     MAE_COMPLETE = pd.read_csv("MAE_test_complete.csv")
#     MAE_imputed = pd.read_csv("MAE_test_imputed.csv")
#     print(check_for_missing_data(MAE_incomplete))
#
#     print(MAE_incomplete.head())
#     print()
#     print(MAE_imputed.head())
#     print()
#     print(MAE_COMPLETE.head())
#     print()
#
#     x = get_mae(MAE_incomplete, MAE_imputed, MAE_COMPLETE)
#     print(x)


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

#
# def get_euclidean_for_current_column(base_row, compare_row):
#     for i in compare_row:
#         if i == compare_row:
#             continue
#
#
# # def get_euclidean_for_current_column(row, column):
# #         for i in num_of_columns:
# #
# #             if i == column:
# #                 continue
# #             if get_distance(row, num_of_rows, column) != 0:
# #                 numerator = numerator + get_distance(row, num_of_rows, column)
# #                 denominator = denominator + 1
# #         return math.sqrt(numerator)
#
# # hot_deck_table.loc[row].values[column] = "????" # + hot_deck_table.loc[row].values[column]
#
# def get_distance(obj1, objn, column):
#     if "?" in hot_deck_table.loc[obj1].values[column] or "?" in hot_deck_table.loc[objn].values[column]:
#         return 0
#     else:
#         return math.pow(
#             (float(hot_deck_table.loc[obj1].values[column]) - float(hot_deck_table.loc[objn].values[column])), 2)
#
#
# def impute_hot_deck(row, column):
#     dictionary = {}
#     for x in num_of_rows:
#         print()
#
#
# def find_missing_data():
#     for x in range(0, num_of_columns):
#         for i in range(0, num_of_rows):
#             if hot_deck_table.loc[i].values[x] == "?":
#                 impute_hot_deck(i, x)


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


# distance = math.sqrt(math.pow((val1 - val2), 2) + math.pow((val3 - val4), 2)) / num_to_divide_by

# print(hot_deck_table.loc[0].values[2] == "?")
#
# print(round(distance, 4))
# hot_deck_table.loc[0].values[2] = "????" + hot_deck_table.loc[2].values[2]
#
# hot_deck_table.loc[0].values[2] = hot_deck_table.loc[0].values[2][4:]
#
# print(hot_deck_table.loc[0].values[2] == "?")
#
#     # hot_deck_table.loc[2].values[2]
# print(hot_deck_table.head())
# print()


# def hot_deck_imputation(hot_deck_table):
#
#     num_of_rows = find_num_of_rows(hot_deck_table)
#     num_of_columns = find_num_of_columns(hot_deck_table)
#
#     def return_ED_from_current_row(column_to_avoid, current_row):
#
#         # # CAREFUL THIS MIGHT INCLUDE HEADER ROW
#         # current_row = 0
#         col1 = 0
#         col2 = 1
#         col3 = 2
#         # col4 = 3
#         # col5 = 4
#         # col6 = 5
#         # col6 = 6
#         # col8 = 7
#         num_to_divide_by = 0
#
#         for i in range(0, num_of_rows):
#             if "?" in hot_deck_table.loc[current_row].values[col1] or hot_deck_table.loc[i].values[col1] or col1 == column_to_avoid:
#                 val1 = 0
#             else:
#                 val1 = math.sqrt(
#                     math.pow(float(hot_deck_table.loc[current_row].values[col1]) - float(hot_deck_table.loc[i].values[col1]))
#                 )
#                 num_to_divide_by = num_to_divide_by + 1
#
#             if "?" in hot_deck_table.loc[current_row].values[col2] or hot_deck_table.loc[i].values[col1] or col2 == column_to_avoid:
#                 val2 = 0
#             else:
#                 val2 = math.sqrt(
#                     math.pow(float(hot_deck_table.loc[current_row].values[col2]) - float(hot_deck_table.loc[i].values[col2]))
#                 )
#                 num_to_divide_by = num_to_divide_by + 1
#
#             if "?" in hot_deck_table.loc[current_row].values[col3] or hot_deck_table.loc[i].values[col1] or col3 == column_to_avoid:
#                 val3 = 0
#             else:
#                 val3 = math.sqrt(
#                     math.pow(float(hot_deck_table.loc[current_row].values[col3]) - float(hot_deck_table.loc[i].values[col3]))
#                 )
#                 num_to_divide_by = num_to_divide_by + 1
#
#         return math.sqrt(val1 + val2 + val3) / num_to_divide_by
#
#
#     def stupiddumb():
#         column_to_avoid = 2
#         distances_column = {}
#         distances_row = {}
#         for x in range(0, num_of_rows):
#             if return_ED_from_current_row(column_to_avoid, x) == 0:
#                 print("distance was zero uh oh")
#             distance = return_ED_from_current_row(column_to_avoid, x)
#             distances_row[distance] = x
#         print(distances_row)
#
#     stupiddumb()
#
#     return hot_deck_table
