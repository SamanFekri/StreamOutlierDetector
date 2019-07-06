from src.OutlierDetector import OutlierDetector

tmp = [1,2,2,2,4,3,5,6,6,6,6,3245,2,6,7,8,3]
# tmp = [1]

x = OutlierDetector(3)
for t in tmp:
    print(t, x.push(t))
