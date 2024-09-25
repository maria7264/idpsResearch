import pandas as pd

combinedData = pd.read_csv('combined_CICIDS2017.csv')
labelCounts = combinedData[' Label'].value_counts()
print("Counts of each traffic label (Benign vs different attacks):")
print(labelCounts)

combinedData['TrafficType'] = combinedData[' Label'].apply(lambda x: 'benign' if x == 'BENIGN' else 'malicious')
trafficTypeCounts = combinedData['TrafficType'].value_counts()
print("\nCounts of benign and malicious traffic:")
print(trafficTypeCounts)

"""
Output:
C:\Users\homep\PycharmProjects\ids\.venv\Scripts\python.exe C:\Users\homep\PycharmProjects\ids\countTypeCICIDS2017.py 
Counts of each traffic label (Benign vs different attacks):
 Label
BENIGN                        2273097
DoS Hulk                       231073
PortScan                       158930
DDoS                           128027
DoS GoldenEye                   10293
FTP-Patator                      7938
SSH-Patator                      5897
DoS slowloris                    5796
DoS Slowhttptest                 5499
Bot                              1966
Web Attack � Brute Force         1507
Web Attack � XSS                  652
Infiltration                       36
Web Attack � Sql Injection         21
Heartbleed                         11
Name: count, dtype: int64

Counts of benign and malicious traffic:
TrafficType
benign       2273097
malicious     557646
Name: count, dtype: int64

Process finished with exit code 0
"""
