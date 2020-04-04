# Basic library for all my methods
import numpy
import pandas

from Linker import linker

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn import preprocessing, utils
from sklearn.linear_model import LogisticRegression
from sklearn import linear_model
from sklearn import svm
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
                X_test = linker.csv_column_to_list(
                    "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv", 8)
                X_test.pop(0)
                linker.list_string_to_float(X_test)
                linker.csv_delete_column(
                    "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv", 8,
                    "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
                X_train = linker.csv_to_list(
                    "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
                X_train.pop(0)
                for row in X_train:
                    linker.list_string_to_float(row)
                y_train = linker.csv_to_list(
                    "C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv")
                for row in y_train:
                    linker.list_string_to_float(row)
                X_train = numpy.array(X_train)
                print(X_train)
                print(X_train.__len__())
                X_test = numpy.array(X_test)
                print(X_test)
                print(X_test.__len__())
                y_train = numpy.array(y_train)
                print(y_train)
                print(y_train.__len__())
                lab_enc = preprocessing.LabelEncoder()
                training_scores_encoded = lab_enc.fit_transform(y_train)
                print(training_scores_encoded)
                model = LogisticRegression()
                model.fit(X_train, training_scores_encoded)
                # model.predict(X_test)

            elif choice == "K-means":
                print("K-means")
                training_data_X = numpy.array([[1.2, 6.7, 2.7], [2.3, 4.6, 2.2], [0.3, 3.9, 0.8], [2.1, 1.3, 4.3]])
                print(training_data_X)
                print(training_data_X.__len__())
                training_scores_Y = numpy.array([1.4, 9.2, 2.5, 2.2])
                print(training_scores_Y)
                print(training_scores_Y.__len__())
                prediction_data_test = numpy.array([[1.5, 3.4, 2.2], [7.6, 7.2, 0.2]])
                print(prediction_data_test)
                print(prediction_data_test.__len__())
                # clf = LogisticRegression()
                # clf.fit(training_data_X, training_scores_Y)
                lab_enc = preprocessing.LabelEncoder()
                training_scores_encoded = lab_enc.fit_transform(training_scores_Y)
                print(training_scores_encoded)
                clf = LogisticRegression()
                clf.fit(training_data_X, training_scores_encoded)
                # print(clf.predict(prediction_data_test))
                # re = clf.predict(prediction_data_test)
                # re = lab_enc.fit(re)
                # print(re)

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
