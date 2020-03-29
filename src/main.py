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


data = pandas.read_csv("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red-test.csv")
# data = pandas.read_excel("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\test.xlsx")
data.head()

seaborn.lmplot("fixed acidity", "volatile acidity", data=data, hue="quality", palette="Set1", fit_reg=False, scatter_kws={"s": 70})
plt.show()

# Specify inputs for the model.
acidities = data[["fixed acidity", "volatile acidity"]].to_numpy()
# acidities = data[["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]].to_numpy()
type_label1 = numpy.where(data["quality"] == 5, 0, 1)
type_label2 = numpy.where(data["quality"] == 7, 1, 2)

# Fit the SVM model.
model = svm.SVC(kernel="linear", decision_function_shape="ovr")
model.fit(acidities, type_label1)
model.fit(acidities, type_label2)

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
seaborn.lmplot("fixed acidity", "volatile acidity", data=data, hue="quality", palette="Set1", fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color="black")
plt.plot(xx, yy_down, "k--")
plt.plot(xx, yy_up, "k--")
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=80, facecolors="none")
plt.show()

# Plot the hyperplane
seaborn.lmplot("fixed acidity", "volatile acidity", data=data, hue="quality", palette="Set1", fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color="black")
plt.plot(-2, -100, "yo", markersize="9")
# plt.plot(-100, -100, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4, "yo", markersize="9")
plt.show()


def determine(fixed_acidity, volatile_acidity):
    if model.predict([[fixed_acidity, volatile_acidity]]) == 0:
        print(5)
    elif model.predict([[fixed_acidity, volatile_acidity]]) == 1:
        print(7)
    elif model.predict([[fixed_acidity, volatile_acidity]]) == 2:
        print(10)


# def determine(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):
#     if model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]]) == 0:
#         print(5)
#     else:
#         print(7)


print(model.predict([[-2, -100]]))
print(model.predict([[244, -100]]))
print(model.predict([[4234, -500]]))
print(model.predict([[24.4324, 400]]))
print(model.predict([[44.44, 0]]))
print(model.predict([[12323, -134]]))
print(model.predict([[-100, -4]]))

determine(1, 1)
determine(7.4, 0.7)
determine(7.3, 0.65)
determine(-100, -4)


# print(model.predict([[-2, -100, 0.40, 1.2, 0.065, -5.0, -21.0, 4.2143, 33.39, -0.47, 510.0]]))
# print(model.predict([[244, -100, 0.0324, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0]]))
# print(model.predict([[4234, -500, 0.044, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0]]))
# print(model.predict([[24.4324, 400, 0.023423, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0]]))
# print(model.predict([[44.44, 0, 0.024, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0]]))
# print(model.predict([[12323, -134, 0.04344, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0]]))
# print(model.predict([[-100, -4, 224.0, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0]]))
#
# determine(7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4)
# determine(7.3, 0.65, 0.0, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0)
# determine(-2, -100, 0.40, 1.2, 0.065, -5.0, -21.0, 4.2143, 33.39, -0.47, 510.0)


# print(linker.csv_column_to_list("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red.csv", 11))

# y_true = [0, 1, 2, 0, 1, 2]
# y_predict = [0, 0, 1, 1, 3, 2]
# print(f1_score(y_true, y_predict, average='macro'))

