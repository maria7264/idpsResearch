import pandas as pd

combinedData = pd.read_csv('combined_CICIDS2018.csv')
labelCounts = combinedData[' Label'].value_counts()
print("Counts of each traffic label (Benign vs different attacks):")
print(labelCounts)

combinedData['TrafficType'] = combinedData['Label'].apply(lambda x: 'benign' if x == 'BENIGN' else 'malicious')
trafficTypeCounts = combinedData['TrafficType'].value_counts()
print("\nCounts of benign and malicious traffic:")
print(trafficTypeCounts)

"""
Output:
C:\Users\homep\PycharmProjects\ids\.venv\Scripts\python.exe C:\Users\homep\PycharmProjects\ids\Datasets\CSE-CIC-IDS2018-Research\countTypeCICIDS2018.py 
C:\Users\homep\PycharmProjects\ids\Datasets\CSE-CIC-IDS2018-Research\countTypeCICIDS2018.py:3: DtypeWarning: Columns (0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,82,84) have mixed types. Specify dtype option on import or set low_memory=False.
  combinedData = pd.read_csv('combined_CICIDS2018.csv')
Traceback (most recent call last):
  File "C:\Users\homep\PycharmProjects\ids\.venv\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ' Label'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\homep\PycharmProjects\ids\Datasets\CSE-CIC-IDS2018-Research\countTypeCICIDS2018.py", line 4, in <module>
    labelCounts = combinedData[' Label'].value_counts()
                  ~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Users\homep\PycharmProjects\ids\.venv\Lib\site-packages\pandas\core\frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\homep\PycharmProjects\ids\.venv\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: ' Label'

Process finished with exit code 1
"""
