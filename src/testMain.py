import sys

import numpy
import pandas
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score

df = pandas.read_csv("../Input/winequality-red.csv")
X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity", "citric acid",
                                                        "residual sugar", "chlorides", "free sulfur dioxide",
                                                        "total sulfur dioxide", "density", "pH", "sulphates",
                                                        "alcohol"]], df.quality, test_size=0.25)

# print("This is A")
# clf = SVC(gamma='auto')
# clf.fit(X_train, y_train)
# final = clf.predict(X_test)
# # print(final)
#
# print("f1 Score:\t\t\t", float(f1_score(y_test, final, average='micro')))
# print("Precision Score:\t", float(precision_score(y_test, final, average='micro')))
# print("Recall Score:\t\t", float(recall_score(y_test, final, average='micro')), "\n\n")
#
# print("This is B")
X_train['quality'] = y_train
df2 = X_train
# print(df2)
X_train, X_test, y_train, y_test = train_test_split(df2[["fixed acidity", "volatile acidity", "citric acid",
                                                         "residual sugar", "chlorides", "free sulfur dioxide",
                                                         "total sulfur dioxide", "density", "sulphates",
                                                         "alcohol", "quality"]], df2.pH, test_size=0.33)
#
# print(X_train, y_train)
# print("Average")
# # print(y_train)
# average = sum(y_train) / len(y_train)
# y_test_new = [round(average, 2) for x in y_test]
# print(len(y_test_new))
# X_test.insert(8, "pH", y_test_new, True)
# print(X_test)
#
#
# print("Logistic Regression")
# y_train_encoded = [x * 100 for x in y_train]
# print(len(y_train_encoded))
# print(len(X_train))
# model = LogisticRegression(max_iter=10000)
# print("I am learning...")
# X_test.drop(["pH"], axis=1, inplace=True)
# model.fit(X_train, y_train_encoded)
# y_test_decoded = [x / 100 for x in model.predict(X_test)]
# X_test.insert(8, "pH", y_test_decoded, True)
# print(X_test)


# print("K-means")
# clusters = input("Now choose number of clusters: ")
# numpy.set_printoptions(threshold=sys.maxsize, suppress=True)
# model = KMeans(n_clusters=int(clusters))
# # X_test.drop(["pH"], axis=1, inplace=True)
# given = model.fit_predict(X_train, y_train)
# print(X_train, y_train)
# for k in (range(int(clusters))):
#     print("pH for cluster no.", int(k), "is:", round(model.cluster_centers_[k][8], 2))
# # print(numpy.array(given))
# wanted = model.predict(X_test)
# print(wanted)
# # print(numpy.array(wanted))
# wanted_new = []
# for k in (range(len(wanted))):
#     # print(wanted[k], round(model.cluster_centers_[wanted][k][8], 2))
#     wanted_new.append(round(model.cluster_centers_[wanted][k][8], 2))
# print(wanted_new)


X = numpy.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
kmeans.predict([[0, 0], [12, 3]])
print(kmeans.cluster_centers_)
