from src.OutlierDetector import OutlierDetector
import random
import matplotlib.pyplot as plt

# tmp = [1,2,2,2,4,3,5,6,6,6,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,2,6,5,7,6,5,7,8,6,5,7,5,6,7,8,3,4,5,6,7,34,4,5,6,6,5,4,3]
# tmp = [1]
tmp = []
for i in range(100):
    val = random.uniform(1.0, 10.0)
    tmp.append(val)

tmp[32] = 45
tmp[76] = 100

bound = 3

outlier_detector = OutlierDetector(3)
result = []
for i in range(len(tmp)):
    is_outlier, mean, var = outlier_detector.push(tmp[i])
    result.append([i, is_outlier, tmp[i], mean, var])

index_bound = [i for [i, r, x, m, v] in result]
upper_bound = [(m + bound * v) for [i, r, x, m, v] in result]
lower_bound = [(m - bound * v) for [i, r, x, m, v] in result]

x_normal = [i for [i, r, x, m, v] in result if r is False]
y_normal = [x for [i, r, x, m, v] in result if r is False]

x_out = [i for [i, r, x, m, v] in result if r is True]
y_out = [x for [i, r, x, m, v] in result if r is True]

plt.plot(x_normal, y_normal, 'bo', x_out, y_out, 'rx', index_bound, upper_bound, 'r--', index_bound, lower_bound, 'r--')
plt.show()