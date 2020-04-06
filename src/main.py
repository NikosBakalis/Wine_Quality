# Basic library for all my methods
import sys

import numpy
import pandas

from Linker import linker

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn import preprocessing, utils
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
# from mpl_toolkits import Axes3D
from sklearn.preprocessing import scale

import csv

question = ""
while question != "Leave":
    print("What would you like to do?")
    question = input("A, B or Leave: ")

    if question == "A":
        print("This is A")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")

        data = linker.csv_column_to_list(
            "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 11)
        data.pop(0)
        data = [int(i) for i in data]

        data_length = data.__len__()
        data_starting_length_to_test = data_length * 75 / 100
        data_to_test = []
        for i in range(int(data_starting_length_to_test), data.__len__()):
            data_to_test.append(data[i])

        linker.csv_spliter("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 75,
                           "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv",
                           "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")

        file = open("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")
        reader = csv.reader(file, delimiter=',')

        from Linker import SVM_Analyzer

        final = []
        wanted = []
        for row in reader:
            item = SVM_Analyzer.determine(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],
                                          row[9], row[10])
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
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-add.csv")

        linker.csv_spliter("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 67,
                           "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv",
                           "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")
        linker.csv_delete_column(
            "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv", 8,
            "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv")
        choice = ""
        while choice != "Leave":
            choice = input("Choose one between Average, Logistic Regression, K-means or Leave: ")
            if choice == "Average":
                print("Average")
                average_list = linker.csv_column_to_list(
                    "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv", 8)
                average_list.pop(0)
                linker.list_string_to_float(average_list)
                average_number = linker.list_average(average_list)
                linker.csv_add_column(
                    "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv", 8,
                    average_number, "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-add.csv")
            elif choice == "Logistic Regression":
                print("Logistic Regression")
                # X_test = linker.csv_column_to_list(
                #     "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv", 8)
                # X_test.pop(0)
                # linker.list_string_to_float(X_test)
                # linker.csv_delete_column(
                #     "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv", 8,
                #     "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
                # X_train = linker.csv_to_list(
                #     "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
                # X_train.pop(0)
                # for row in X_train:
                #     linker.list_string_to_float(row)
                # y_train = linker.csv_to_list(
                #     "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv")
                # for row in y_train:
                #     linker.list_string_to_float(row)
                # numpy.set_printoptions(threshold=sys.maxsize, suppress=True)

                df = pandas.read_csv("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv")
                X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity",
                                                                        "citric acid", "residual sugar", "chlorides",
                                                                        "free sulfur dioxide", "total sulfur dioxide",
                                                                        "density", "sulphates", "alcohol", "quality"]],
                                                                    df.pH, test_size=0.33)
                print(X_train)
                print(X_test)
                print(y_train)
                print(y_test)
                # lab_enc = preprocessing.LabelEncoder()
                # y_train_encoded = lab_enc.fit_transform(y_train)
                y_train_encoded = [x * 100 for x in y_train]
                # print(len(y_train_encoded))
                # print(len(y_test))
                model = LogisticRegression(max_iter=10000)
                model.fit(X_train, y_train_encoded)
                # print(model.predict(X_test))
                X_test_decoded = [x / 100 for x in model.predict(X_test)]
                print(X_test_decoded)
                # print(f1_score(model.predict(X_test), y_test, average='macro'))
                # training_scores_decoded = lab_enc.fit_transform(model.predict(y_train))
                # print(training_scores_decoded)

            elif choice == "K-means":
                print("K-means")
                print(linker.csv_column_to_list("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 8))


        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-add.csv")

    elif question == "C":
        df = pandas.read_csv("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv")
        X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity", "citric acid",
                                                                "residual sugar", "chlorides", "free sulfur dioxide",
                                                                "total sulfur dioxide", "density", "pH", "sulphates",
                                                                "alcohol"]], df.quality, test_size=0.25)
        print(X_train)
        print(X_test)
        print(y_train)
        print(y_test)
