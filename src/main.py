import sys
import numpy
import pandas
from sklearn.svm import SVC
from Linker import linker
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

import csv

question = ""
while question != "Leave":
    print("What would you like to do?")
    question = input("A, B or Leave: ")

    if question == "A":
        print("This is A")
        df = pandas.read_csv("../Input/winequality-red.csv")
        X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity", "citric acid",
                                                                "residual sugar", "chlorides", "free sulfur dioxide",
                                                                "total sulfur dioxide", "density", "sulphates",
                                                                "alcohol", "quality"]], df.pH, test_size=0.25)

        # print(X_train, X_test, y_train, y_test)
        y_train_encoded = [round(x * 100) for x in y_train]
        # print(y_train, "\n", y_train_encoded)
        given = [round(x * 100) for x in y_test]
        # print(y_test, "\n", given)

        clf = SVC(gamma='auto')
        clf.fit(X_train, y_train_encoded)
        final = clf.predict(X_test)
        # print(final)

        print("\nf1 Score", float(f1_score(given, final, average='micro')))
        print("Precision Score", float(precision_score(given, final, average='micro')))
        print("Recall Score", float(recall_score(given, final, average='micro')), "\n\n")

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
                numpy.set_printoptions(threshold=sys.maxsize, suppress=True)
                df = pandas.read_csv("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv")
                X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity",
                                                                        "citric acid", "residual sugar", "chlorides",
                                                                        "free sulfur dioxide", "total sulfur dioxide",
                                                                        "density", "pH", "sulphates", "alcohol",
                                                                        "quality"]], df.pH, test_size=0.33)
                df.head()
                model = KMeans(n_clusters=3)
                given = model.fit_predict(X_train, y_train)
                for k in (range(3)):
                    print(model.cluster_centers_[k][8])
                # print(numpy.array(given))
                wanted = model.predict(X_test)
                print(numpy.array(wanted))
                print(numpy.array(y_test))
                print(float(f1_score(numpy.array(wanted), numpy.array(y_test), average='micro')))

        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-delete.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-to-be-tested.csv")
        linker.csv_clear("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-add.csv")

