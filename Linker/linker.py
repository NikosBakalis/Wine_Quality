from itertools import chain
import csv


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
