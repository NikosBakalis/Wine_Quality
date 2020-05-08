# This file contains the tree functions we will use to populate our dataframe.
import sys

import numpy
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression

from Linker import linker


def average(y_train, y_test):
    """
    This function will return the average number of y_train dataframe as dataframe.
    :param y_train: Dataframe of all the numbers I want to find the average.
    :param y_test: Dataframe before returning.
    :return: Dataframe populated with one number. The average of y_train list.
    """
    # X_train_Average = X_train
    # X_test_Average = X_test
    y_train_Average = y_train
    y_test_Average = y_test
    print("I am learning...")
    average = linker.list_average(y_train_Average)
    y_test_new = [round(average, 2) for x in y_test_Average]
    return y_test_new


def logistic_regression(X_train, X_test, y_train):
    """
    This function performs the logistic regression model to X_train and y_train dataframes and returns it as a dataframe.
    :param X_train: Dataframe to be trained.
    :param X_test: Dataframe to get the length of return dataframe.
    :param y_train: Dataframe to be trained.
    :return: Dataframe populated with results of X_train and y_train.
    """
    X_train_Logistic_Regression = X_train
    X_test_Logistic_Regression = X_test
    y_train_Logistic_Regression = y_train
    # y_test_Logistic_Regression = y_test
    y_train_encoded = [x * 100 for x in y_train_Logistic_Regression]
    model = LogisticRegression(max_iter=10000)
    print("I am learning...")
    # X_test.drop(["pH"], axis=1, inplace=True)
    model.fit(X_train_Logistic_Regression, y_train_encoded)
    y_test_decoded = [x / 100 for x in model.predict(X_test_Logistic_Regression)]
    return y_test_decoded


def k_means(X_train, X_test, y_train, y_test):
    """
    This function performs the k-means model to X_train and y_train dataframes and returns it as a dataframe.
    :param X_train: Dataframe to be trained.
    :param X_test: Dataframe to be tested.
    :param y_train: Dataframe to be added to X_train.
    :param y_test: Dataframe to be added y_train.
    :return: Dataframe populated with results of X_train and y_train.
    """
    X_train_K_means = X_train
    X_test_K_means = X_test
    y_train_K_means = y_train
    y_test_K_means = y_test
    clusters = input("Now choose number of clusters: ")
    numpy.set_printoptions(threshold=sys.maxsize, suppress=True)
    model = KMeans(n_clusters=int(clusters))
    # X_test.drop(["pH"], axis=1, inplace=True)
    X_train_K_means.insert(8, "pH", y_train_K_means, True)
    X_test_K_means.insert(8, "pH", y_test_K_means, True)
    # print(X_train_K_means)
    print("I am learning...")
    model.fit_predict(X_train_K_means, y_train_K_means)
    for k in (range(int(clusters))):
        print("pH for cluster no.", int(k), "is:", round(model.cluster_centers_[k][8], 2))
    what_I_want = model.predict(X_test_K_means)
    what_I_really_want = []
    # X_test.insert(8, "pH", y_test_decoded, True)
    for k in (range(len(what_I_want))):
        what_I_really_want.append(round(model.cluster_centers_[what_I_want][k][8], 2))
    X_train_K_means.drop(["pH"], axis=1, inplace=True)
    X_test_K_means.drop(["pH"], axis=1, inplace=True)
    return what_I_really_want
