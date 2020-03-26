import csv


def print_csv(csv_path):
    """
    This function takes as argument the path of a csv file and then it prints the csv file
    """
    with open(csv_path) as csv_path:
        reader = csv.reader(csv_path)
        for row in reader:
            print("\t | ".join(row))


print_csv("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red.csv")

