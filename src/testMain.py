import sys

import numpy
import pandas
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

clusters = input("Now choose number of clusters: ")
numpy.set_printoptions(threshold=sys.maxsize, suppress=True)
df = pandas.read_csv("../Input/winequality-red.csv")
X_train, X_test, y_train, y_test = train_test_split(df[["fixed acidity", "volatile acidity",
                                                        "citric acid", "residual sugar", "chlorides",
                                                        "free sulfur dioxide", "total sulfur dioxide",
                                                        "density", "pH", "sulphates", "alcohol",
                                                        "quality"]], df.pH, test_size=0.33)
# df.head()
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
# print(numpy.array(y_test))

