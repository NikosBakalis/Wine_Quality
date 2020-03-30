# Libraries for analysis
# import sys
import pandas
import numpy
from sklearn import svm
from Linker import linker
from sklearn.metrics import f1_score, precision_recall_fscore_support

# Libraries for visuals
import matplotlib.pyplot as plt
import seaborn

seaborn.set(font_scale=1.2)


# Allow charts to appear in the notebook
# %matplotlib inline

data = pandas.read_csv("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red-test.csv")
data.head()

seaborn.lmplot("fixed acidity", "volatile acidity", data=data, hue="quality", palette="Set1", fit_reg=False,
               scatter_kws={"s": 70})
plt.show()

# Specify inputs for the model.
# acidities = data[["fixed acidity", "volatile acidity"]].to_numpy()
acidities = data[
    ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide",
     "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]].to_numpy()
type_label = numpy.where(data["quality"] == 1, data["quality"] - 1, data["quality"])
# numpy.set_printoptions(threshold=sys.maxsize)
print(type_label)

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
seaborn.lmplot("fixed acidity", "volatile acidity", data=data, hue="quality", palette="Set1", fit_reg=False,
               scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color="black")
plt.plot(xx, yy_down, "k--")
plt.plot(xx, yy_up, "k--")
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=80, facecolors="none")
plt.show()

# Plot the hyperplane
seaborn.lmplot("fixed acidity", "volatile acidity", data=data, hue="quality", palette="Set1", fit_reg=False,
               scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color="black")
# plt.plot(-2, -100, "yo", markersize="9")
plt.plot(-100, -100, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4, "yo", markersize="9")
plt.show()


def determine(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,
              total_sulfur_dioxide, density, pH, sulphates, alcohol):
    return model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                          free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
