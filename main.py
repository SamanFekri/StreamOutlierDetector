from src.OutlierDetector import OutlierDetector

tmp = [1,2,2,2,4,3,5,6,6,6,6,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,2,6,5,7,6,5,7,8,6,5,7,5,6,7,8,3,4,5,6,7,34,4,5,6,6,5,4,3]
# tmp = [1]

x = OutlierDetector(3)
for t in tmp:
    print(t, x.push(t))
