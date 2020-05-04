import sys

import numpy
import pandas
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

from Linker import linker

question = ""
while question != "Leave":
    print("What would you like to do?")
    question = input("A, B or Leave: ")

    df = pandas.read_csv("../Input/winequality-red.csv")
    X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity", "citric acid",
                                                            "residual sugar", "chlorides", "free sulfur dioxide",
                                                            "total sulfur dioxide", "density", "pH", "sulphates",
                                                            "alcohol"]], df.quality, test_size=0.25)

    if question == "A":
        print("This is A")
        clf = SVC(gamma='auto')
        clf.fit(X_train, y_train)
        final = clf.predict(X_test)
        # print(final)

        print("f1 Score:\t\t\t", float(f1_score(y_test, final, average='micro')))
        print("Precision Score:\t", float(precision_score(y_test, final, average='micro')))
        print("Recall Score:\t\t", float(recall_score(y_test, final, average='micro')), "\n\n")
        # print(sklearn.metrics.classification_report(y_test, final))

    elif question == "B":
        print("This is B")
        X_train['quality'] = y_train
        df2 = X_train
        # print(df2)
        X_train, X_test, y_train, y_test = train_test_split(df2[["fixed acidity", "volatile acidity", "citric acid",
                                                                 "residual sugar", "chlorides", "free sulfur dioxide",
                                                                 "total sulfur dioxide", "density", "sulphates",
                                                                 "alcohol", "quality"]], df2.pH, test_size=0.33)
        # print(X_train, y_train)
        choice = ""
        while choice != "Leave":
            choice = input("Choose one between Average, Logistic Regression, K-means or Leave: ")
            if choice == "Average":
                print("Average")
                X_train_Average = X_train
                X_test_Average = X_test
                y_train_Average = y_train
                y_test_Average = y_test
                # print(y_train)
                average = sum(y_train_Average) / len(y_train_Average)
                y_test_new = [round(average, 2) for x in y_test_Average]
                # print(len(y_test_new))
                # X_test_Average.insert(8, "pH", y_test_new, True)
                # print(X_test)
                print(y_test_new)
            elif choice == "Logistic Regression":
                print("Logistic Regression")
                X_train_Logistic_Regression = X_train
                X_test_Logistic_Regression = X_test
                y_train_Logistic_Regression = y_train
                y_test_Logistic_Regression = y_test
                y_train_encoded = [x * 100 for x in y_train_Logistic_Regression]
                model = LogisticRegression(max_iter=10000)
                print("I am learning...")
                # X_test.drop(["pH"], axis=1, inplace=True)
                model.fit(X_train_Logistic_Regression, y_train_encoded)
                print(X_test_Logistic_Regression)
                y_test_decoded = [x / 100 for x in model.predict(X_test_Logistic_Regression)]
                # X_test_Logistic_Regression.insert(8, "pH", y_test_decoded, True)
                print(y_test_decoded)
            elif choice == "K-means":
                print("K-means")
                X_train_K_means = X_train
                X_test_K_means = X_test
                y_train_K_means = y_train
                y_test_K_means = y_test
                clusters = input("Now choose number of clusters: ")
                numpy.set_printoptions(threshold=sys.maxsize, suppress=True)
                model = KMeans(n_clusters=int(clusters))
                # X_test.drop(["pH"], axis=1, inplace=True)
                # print(X_train, y_train)
                # print(X_test, y_test)
                X_train_K_means.insert(8, "pH", y_train_K_means, True)
                X_test_K_means.insert(8, "pH", y_test_K_means, True)
                # print(X_train, X_test)
                given = model.fit_predict(X_train_K_means, y_train_K_means)
                for k in (range(int(clusters))):
                    print("pH for cluster no.", int(k), "is:", round(model.cluster_centers_[k][8], 2))
                # print(numpy.array(given))
                what_I_want = model.predict(X_test_K_means)
                # print(numpy.array(wanted))
                what_I_really_want = []
                # print(X_test)
                # X_test.insert(8, "pH", y_test_decoded, True)
                for k in (range(len(what_I_want))):
                    # print(wanted[k], round(model.cluster_centers_[what_I_want][k][8], 2))
                    what_I_really_want.append(round(model.cluster_centers_[what_I_want][k][8], 2))
                print(what_I_really_want)

