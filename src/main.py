# Basic library for all my methods
from Linker import linker

from sklearn.metrics import f1_score, precision_score, recall_score
import csv


question = ""
while question != "Leave":
    print("What would you like to do?")
    question = input("A, B or Leave: ")

    if question == "A":
        print("This is A")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")

        data = linker.csv_column_to_list("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 11)
        data.pop(0)
        data = [int(i) for i in data]

        data_length = data.__len__()
        data_starting_length_to_test = data_length * 75/100
        data_to_test = []
        for i in range(int(data_starting_length_to_test), data.__len__()):
            data_to_test.append(data[i])

        linker.csv_spliter("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 75, "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv", "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")

        file = open("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")
        reader = csv.reader(file, delimiter=',')

        from Linker import SVM_Analyzer

        final = []
        wanted = []
        for row in reader:
            item = SVM_Analyzer.determine(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            wanted.append(int(row[11]))
            final.append(item[0])

        # svm_data = SVM_Analyzer.type_label.tolist()
        # print(svm_data)
        # print(wanted.__len__())
        # print(final.__len__())
        print(float(f1_score(wanted, final, average='micro')))
        print(float(precision_score(wanted, final, average='micro')))
        print(float(recall_score(wanted, final, average='micro')))

        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")

    elif question == "B":
        print("This is B")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")

        linker.csv_spliter("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 67, "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv", "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")
        linker.csv_delete_column("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 8, "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv")

        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")
