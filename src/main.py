import sys
import numpy
import pandas
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

question = ""
while question != "Leave":
    print("What would you like to do?")
    question = input("A, B or Leave: ")

    if question == "A":
        print("This is A")

        df = pandas.read_csv("../Input/winequality-red.csv")
        X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity", "citric acid",
                                                                "residual sugar", "chlorides", "free sulfur dioxide",
                                                                "total sulfur dioxide", "density", "pH", "sulphates",
                                                                "alcohol"]], df.quality, test_size=0.25)

        clf = SVC(gamma='auto')
        clf.fit(X_train, y_train)
        final = clf.predict(X_test)
        # print(final)

        print("f1 Score:\t\t\t", float(f1_score(y_test, final, average='micro')))
        print("Precision Score:\t", float(precision_score(y_test, final, average='micro')))
        print("Recall Score:\t\t", float(recall_score(y_test, final, average='micro')), "\n\n")

    elif question == "B":
        print("This is B")
        df = pandas.read_csv("../Input/winequality-red.csv")
        X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity",
                                                                "citric acid", "residual sugar", "chlorides",
                                                                "free sulfur dioxide", "total sulfur dioxide",
                                                                "density", "pH", "sulphates", "alcohol",
                                                                "quality"]], df.pH, test_size=0.33)
        choice = ""
        while choice != "Leave":
            choice = input("Choose one between Average, Logistic Regression, K-means or Leave: ")
            if choice == "Average":
                print("Average")
                # print(y_train)
                average = sum(y_train) / len(y_train)
                y_test_new = [round(average, 2) for x in y_test]
                print(y_test_new)
            elif choice == "Logistic Regression":
                print("Logistic Regression")
                y_train_encoded = [x * 100 for x in y_train]
                model = LogisticRegression(max_iter=10000)
                print("I am learning...")
                model.fit(X_train, y_train_encoded)
                X_test_decoded = [x / 100 for x in model.predict(X_test)]
                print(X_test_decoded)
            elif choice == "K-means":
                print("K-means")
                clusters = input("Now choose number of clusters: ")
                numpy.set_printoptions(threshold=sys.maxsize, suppress=True)
                model = KMeans(n_clusters=int(clusters))
                given = model.fit_predict(X_train, y_train)
                for k in (range(int(clusters))):
                    print("pH for cluster no.", int(k), "is:", round(model.cluster_centers_[k][8], 2))
                # print(numpy.array(given))
                wanted = model.predict(X_test)
                # print(numpy.array(wanted))
                wanted_new = []
                for k in (range(len(wanted))):
                    # print(wanted[k], round(model.cluster_centers_[wanted][k][8], 2))
                    wanted_new.append(round(model.cluster_centers_[wanted][k][8], 2))
                print(wanted_new)
