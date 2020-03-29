# Basic library for all my methods
import pandas

from Linker import linker
from Linker import SVM_Analyzer

import csv
import numpy


data = linker.csv_column_to_list("C:\\Users\\Nikolas\\PycharmProjects\\Wine_Quality\\Input\\winequality-red.csv", 11)
data.pop(0)
data = [int(i) for i in data]
print(data)

print("RRRRRRRRRRR")

# print(data.__len__())
data_length = data.__len__()
data_starting_length_to_test = data_length * 75/100
print(int(data_starting_length_to_test))
data_to_test = []
for i in range(int(data_starting_length_to_test), data.__len__()):
    data_to_test.append(data[i])
print(data_to_test)
print(data_to_test.__len__())


print("DDD")


svm_data = SVM_Analyzer.type_label.tolist()
print(svm_data)


if data == svm_data:
    print("equal")
else:
    print("not equal")


# SVM_Analyzer.determine(7.4, 0.59, 0.08, 4.4, 0.086, 6.0, 29.0, 0.9974, 3.38, 0.5, 9.0)
# SVM_Analyzer.determine(8.1, 0.56, 0.28, 1.7, 0.368, 16.0, 56.0, 0.9968, 3.11, 1.28, 9.3)
# SVM_Analyzer.determine(-2, -100, 0.40, 1.2, 0.065, -5.0, -21.0, 4.2143, 33.39, -0.47, 510.0)
# SVM_Analyzer.determine(244, -100, 0.0324, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0)
# SVM_Analyzer.determine(4234, -500, 0.044, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0)
# SVM_Analyzer.determine(24.4324, 400, 0.023423, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0)
# SVM_Analyzer.determine(44.44, 0, 0.024, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0)
# SVM_Analyzer.determine(12323, -134, 0.04344, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0)
# SVM_Analyzer.determine(-100, -4, 224.0, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0)
# SVM_Analyzer.determine(7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4)
# SVM_Analyzer.determine(7.3, 0.65, 0.0, 1.2, 0.065, 15.0, 21.0, 0.9946, 3.39, 0.47, 10.0)
# SVM_Analyzer.determine(-2, -100, 0.40, 1.2, 0.065, -5.0, -21.0, 4.2143, 33.39, -0.47, 510.0)
# SVM_Analyzer.determine(2222, 2222, 2222, 2222, 2222, 2222, 2222, 2222, 2222, 2222, 2222)
# SVM_Analyzer.determine(-2222, -2222, -2222, -2222, -2222, -2222, -2222, -2222, -2222, -2222, -2222)



# print(linker.csv_column_to_list("C:\\Users\\Nikolas\\PycharmProjects\\Support_Vector_Machines\\Input\\winequality-red.csv", 11))

# y_true = [0, 1, 2, 0, 1, 2]
# y_predict = [0, 0, 1, 1, 3, 2]
# print(f1_score(y_true, y_predict, average='macro'))

