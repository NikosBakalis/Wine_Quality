import os.path

import pandas
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from Linker import linker, functions

# Clears the csv when program executes.
linker.csv_clear("../Input-Output/winequality-red-Average.csv")
linker.csv_clear("../Input-Output/winequality-red-Logistic-Regression.csv")
linker.csv_clear("../Input-Output/winequality-red-K-means.csv")

# Ask user which sub-question he wants to perform.
question = ""
while question != "Leave":
    print("What would you like to do?")
    question = input("A, B or Leave: ")
    df = pandas.read_csv("../Input-Output/winequality-red.csv")
    # Splitting the dataframe.
    X_train_A, X_test_A, y_train_A, y_test_A = train_test_split(
        df[["fixed acidity", "volatile acidity", "citric acid",
            "residual sugar", "chlorides",
            "free sulfur dioxide", "total sulfur dioxide", "density", "pH",
            "sulphates", "alcohol"]], df.quality, test_size=0.25)
    if question == "A":
        print("This is A")
        file = ""
        print("Now choose the file to SVM.")
        print("Possible files.")
        file = input("winequality-red, winequality-red-Average, "
                     "winequality-red-Logistic-Regression and winequality-red-K-means: ")
        if os.path.exists("../Input-Output/" + file + ".csv"): # If path exists.
            if os.stat("../Input-Output/" + file + ".csv").st_size != 0:   # If file in not empty.
                f1_score_list = []
                precision_score_list = []
                recall_score_list = []
                df = pandas.read_csv("../Input-Output/" + file + ".csv")
                print("This might take a while...")
                for k in range(50): # For usage for better results.
                    X_train_A, X_test_A, y_train_A, y_test_A = train_test_split(
                        df[["fixed acidity", "volatile acidity", "citric acid",
                            "residual sugar", "chlorides",
                            "free sulfur dioxide", "total sulfur dioxide", "density", "pH",
                            "sulphates", "alcohol"]], df.quality, test_size=0.25)
                    clf = SVC(gamma='auto')
                    clf.fit(X_train_A, y_train_A)
                    final = clf.predict(X_test_A)
                    # print(y_test, final)
                    f1_score_list.append(f1_score(y_test_A, final, average='micro'))
                    precision_score_list.append(precision_score(y_test_A, final, average='micro'))
                    recall_score_list.append(recall_score(y_test_A, final, average='micro'))
                print("f1 Score for", k + 1, "times is:\t\t\t", round(float(linker.list_average(f1_score_list)), 3))
                print("Precision Score for", k + 1, "times is:\t", round(float(linker.list_average(precision_score_list)), 3))
                print("Recall Score for", k + 1, "times is:\t\t", round(float(linker.list_average(recall_score_list)), 3), "\n\n")
            else:
                print("This file is empty.")
                print("Try again with another file or populate this file using B.")
        else:
            print("There is no file with that name.")
            print("Please try again with one of the given names.")
    elif question == "B":
        print("This is B")
        choice = ""
        X_train_A['quality'] = y_train_A
        df2 = X_train_A
        X_train, X_test, y_train, y_test = train_test_split(df2[["fixed acidity", "volatile acidity", "citric acid",
                                                                 "residual sugar", "chlorides",
                                                                 "free sulfur dioxide",
                                                                 "total sulfur dioxide", "density", "sulphates",
                                                                 "alcohol", "quality"]], df2.pH, test_size=0.33)
        while choice != "Leave":
            choice = input("Choose one between Average, Logistic Regression, K-means or Leave: ")
            # print(X_train, X_test, y_train, y_test)
            if choice == "Average":
                print("Average")
                result = functions.average(y_train, y_test)
                X_train.insert(8, "pH", y_train, True)
                X_test.insert(8, "pH", result, True)
                X_test_B = X_test_A
                y_test_B = y_test_A
                print(X_test_B, y_test_B)
                X_test_B.insert(11, "quality", y_test_B, True)
                # print(X_train, X_test)
                results = X_train.append(X_test, sort=False)
                results = results.append(X_test_B, sort=False)
                print(results)
                results.to_csv("../Input-Output/winequality-red-Average.csv", index=False)
                # Dataframe management.
                X_train.drop(["pH"], axis=1, inplace=True)
                X_test.drop(["pH"], axis=1, inplace=True)
                X_test_B.drop(["quality"], axis=1, inplace=True)
            elif choice == "Logistic Regression":
                print("Logistic Regression")
                result = functions.logistic_regression(X_train, X_test, y_train)
                X_train.insert(8, "pH", y_train, True)
                X_test.insert(8, "pH", result, True)
                # print(X_train, X_test)
                X_test_B = X_test_A
                y_test_B = y_test_A
                print(X_test_B, y_test_B)
                X_test_B.insert(11, "quality", y_test_B, True)
                # print(X_train, X_test)
                results = X_train.append(X_test, sort=False)
                results = results.append(X_test_B, sort=False)
                print(results)
                results.to_csv("../Input-Output/winequality-red-Logistic-Regression.csv", index=False)
                # Dataframe management.
                X_train.drop(["pH"], axis=1, inplace=True)
                X_test.drop(["pH"], axis=1, inplace=True)
                X_test_B.drop(["quality"], axis=1, inplace=True)
            elif choice == "K-means":
                print("K-means")
                result = functions.k_means(X_train, X_test, y_train, y_test)
                X_train.insert(8, "pH", y_train, True)
                X_test.insert(8, "pH", result, True)
                # print(X_train, X_test)
                X_test_B = X_test_A
                y_test_B = y_test_A
                print(X_test_B, y_test_B)
                X_test_B.insert(11, "quality", y_test_B, True)
                # print(X_train, X_test)
                results = X_train.append(X_test, sort=False)
                results = results.append(X_test_B, sort=False)
                print(results)
                results.to_csv("../Input-Output/winequality-red-K-means.csv", index=False)
                # Dataframe management.
                X_train.drop(["pH"], axis=1, inplace=True)
                X_test.drop(["pH"], axis=1, inplace=True)
                X_test_B.drop(["quality"], axis=1, inplace=True)
