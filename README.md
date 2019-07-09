# StreamOutlierDetector
Detect outliers of sequence in stream.  
In this project we have some assumption:
-   This project works online that means has no idea about the future data
-   This project forget older data (more than size of sample array)
-   If more than half of sample array be in outlier then this project assume the majority is not outlier and calculate outlier detection for the sample again


### Usage
```bash
pip install outlierDetectorOnline
pip install --upgrade outlierDetectorOnline
```

```python
from src.OutlierDetector import OutlierDetector

outlier_detector = OutlierDetector(bound_factor_standard_deviation=3, window_size=20, size_initial_ignore=10)

is_outlier = outlier_detector.push(your_value)
```

if you want, you can use it with callback function
```python
from src.OutlierDetector import OutlierDetector

def result(is_outlier):
    print(is_outlier)

outlier_detector = OutlierDetector(bound_factor_standard_deviation=3, window_size=20, size_initial_ignore=10)

is_outlier = outlier_detector.push(value=your_value, callback=result)
```
### Help
``bound_factor_standard_deviation`` is the factor that multiple with standard deviation. ``|value - mean| > bound_factor_standard_deviation * satandard deviation`` is the outlier.  
``window_size`` is the size of array is effective for finding outlier.  
``first_learning_number`` is the number of first value we ignore and learn from them.  

Warning ⚠                               |
----------------------------------------| 
if the outlier be in the first ``first_learning_number`` we return it is not outlier and more dangerous we learn it and ruined the mean and variance for a while| 


## Result
I test this class and show the functionality of it on a chart.  
❌ are the outliers we detect.  
🔵 are the normal values.  
<span> - </span> are the bound of outlier detection.  

Without bound                           | With bounds
----------------------------------------| ------------------------------ 
![]( ./images/test_result_normal.png)   | ![]( ./images/test_result.png) 
 

