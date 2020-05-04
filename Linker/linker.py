from _csv import writer
from itertools import chain
import csv

import pandas


def print_csv(csv_path):
    """
    This function takes as argument the path of a csv file and then it prints the csv file.
    """
    with open(csv_path) as csv_path:
        reader = csv.reader(csv_path)
        for row in reader:
            print("\t | ".join(row))


def print_csv_column(csv_path, column_number):
    """
    This function takes as arguments the path of a csv file and the number of a specific column and then it prints the column.
    """
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(f'\t{row[column_number]}')


def csv_to_list(csv_path):
    """
    This function takes as argument the path of a csv file and then it transforms it to a list.
    """
    with open(csv_path, newline='') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
        return data


def list_to_csv(list_name, csv_path):
    """
    This function takes as argument the name of a list and the path of a csv file and then it transforms it to a csv.
    """
    df = pandas.DataFrame(list_name)
    df.to_csv(csv_path, header=False, index=False)


def csv_to_1d_list(csv_path):
    """
    This function takes as argument the path of a csv file and then it transforms it to an 1-D list.
    """
    with open(csv_path, newline='') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
        data = list(chain.from_iterable(data))
        return data


def csv_column_to_list(csv_path, column_number):
    """
    This function takes as argument the path of a csv file and the number of a specific column and then it transforms it to a list.
    """
    my_list = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            my_list.append(row[column_number])
            # print(f'\t{row[column_number]}')
    return my_list


def csv_splitter(csv_path, percentage, csv_first_path, csv_second_path):
    """
    This function takes as argument the path of a csv file, the percentage we want to split, the target file number 1 and the target file number 2 and then it splits the csv int two different csv's.
    """
    all_data = csv_to_list(csv_path)
    all_data_length = all_data.__len__()
    all_data_starting_length_to_test = all_data_length * percentage / 100
    all_data_to_test = []
    for i in range(0, int(all_data_starting_length_to_test)):
        all_data_to_test.append(all_data[i])

    pandas.DataFrame(all_data_to_test).to_csv(csv_first_path, header=None, index=None)

    all_data_to_be_tested = []
    for i in range(int(all_data_starting_length_to_test), all_data.__len__()):
        all_data_to_be_tested.append(all_data[i])
    pandas.DataFrame(all_data_to_be_tested).to_csv(csv_second_path, header=None, index=None)


def csv_delete_column(csv_path, csv_column, csv_target_path):
    """
    This function takes as argument the path of a csv file and the number of a specific column and then it deletes this column.
    """
    my_list = csv_to_list(csv_path)
    for i in my_list:
        del i[csv_column]
    list_to_csv(my_list, csv_target_path)


def csv_add_column(csv_path, csv_column, to_add, csv_target_path):
    """
    This function takes as argument the path of a csv file and the number of a specific column and then it adds this column.
    """
    my_list = csv_to_list(csv_path)
    for i in my_list:
        i.insert(csv_column, to_add)
    list_to_csv(my_list, csv_target_path)


def add_row_to_csv(csv_path, list_of_elements):
    """
    This function takes as argument  and then it adds rows to this csv file.
    """
    with open(csv_path, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elements)


def csv_clear(csv_path):
    """
    This function takes as argument the path of a csv file and then it clears the entire csv.
    """
    f = open(csv_path, "w+")
    f.close()


def list_average(list_name):
    """
    This function takes as argument the name of a list and then it returns the average of the list.
    """
    return sum(list_name) / len(list_name)


def list_string_to_float(list_name):
    """
    This function takes as argument the name of a string list and then it returns the same list as float list.
    """
    for i in range(0, len(list_name)):
        list_name[i] = float(list_name[i])
    return list_name
