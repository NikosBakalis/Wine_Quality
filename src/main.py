# Libraries for analysis
import pandas
import numpy
from sklearn import svm
from sklearn.metrics import f1_score, precision_recall_fscore_support

# Basic library for all my methods
from Linker import linker

# Libraries for visuals
import matplotlib.pyplot as plt
import seaborn
seaborn.set(font_scale=1.2)

# Allow charts to appear in the notebook
# %matplotlib inline


test = pandas.read_csv("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red.csv")
# test = pandas.read_excel("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\test.xlsx")
test.head()

seaborn.lmplot("fixed acidity", "volatile acidity", data=test, hue="quality", palette="Set1", fit_reg=False, scatter_kws={"s": 70})
plt.show()

# Specify inputs for the model.
acidities = test[["fixed acidity", "volatile acidity"]].to_numpy()
acidities = test[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]].to_numpy()
type_label = numpy.where(test["quality"] == 7, 0, 1)

# Fit the SVM model.
model = svm.SVC(kernel="linear", decision_function_shape="ovr")
model.fit(acidities, type_label)

# Get the separating hyperplane
w = model.coef_[0]
a = -w[0] / w[1]
xx = numpy.linspace(-100, 100)
yy = a * xx - (model.intercept_[0]) / w[1]

# Plot the parallels to the separating hyperplane that pass through the support vectors
b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = model.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

# Look the margins and support vectors
seaborn.lmplot("fixed acidity", "volatile acidity", data=test, hue="quality", palette="Set1", fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color="black")
plt.plot(xx, yy_down, "k--")
plt.plot(xx, yy_up, "k--")
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=80, facecolors="none")
# plt.show()

# Plot the hyperplane
seaborn.lmplot("fixed acidity", "volatile acidity", data=test, hue="quality", palette="Set1", fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color="black")
plt.show()





# print(linker.csv_column_to_list("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red.csv", 11))

# y_true = [0, 1, 2, 0, 1, 2]
# y_predict = [0, 0, 1, 1, 3, 2]
# print(f1_score(y_true, y_predict, average='macro'))

