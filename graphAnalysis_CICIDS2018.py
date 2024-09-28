import matplotlib.pyplot as plt
import pandas as pd

with open('CompleteCount_CICIDS2018.txt', 'r') as f:
    data = f.readlines()

labelCountsData = []

for line in data[1:]:
    if "Counts of benign and malicious traffic:" in line:
        break
    if any(char.isdigit()
           for char in line):
        labelCountsData.append(line.strip())

labelCountsDictionary = {}
for line in labelCountsData:
    try:
        label, count = line.rsplit(' ', 1)
        labelCountsDictionary[label.strip()] = int(count.strip())
    except ValueError:
        print(f"Skipping malformed line: {line}")

labelCountsSeries = pd.Series(labelCountsDictionary)
benignMaliciousData = []
for line in data:
    if "malicious" in line.lower() or "benign" in line.lower():
        benignMaliciousData.append(line.strip())

benignMaliciousDictionary = {}
for line in benignMaliciousData:
    if any(char.isdigit() for char in line):
        try:
            traffic_type, count = line.rsplit(' ', 1)
            benignMaliciousDictionary[traffic_type.strip()] = int(count.strip())
        except ValueError:
            print(f"Skipping malformed line: {line}")

benignMaliciousSeries = pd.Series(benignMaliciousDictionary)

#Graph 1: Benign vs Malicious (Overall)
if not benignMaliciousSeries.empty:
    print(f"Benign vs Malicious Data: \n{benignMaliciousSeries}")

    # Assign colors: benign = green, malicious = red
    colors = ['lightgreen' if label.lower() == 'benign' else 'tomato'
              for label in benignMaliciousSeries.index]

    benignMaliciousSeries.plot(kind='bar', figsize=(6, 4), title='Benign vs Malicious Traffic', color=colors)
    plt.xlabel('Traffic Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()



"""
#Graph #2 --- Have all the malicious attack and overall count

combinedCountsDictionary = labelCountsDictionary.copy()
combinedCountsDictionary.update(benignMaliciousDictionary)
combinedCountsSeries = pd.Series(combinedCountsDictionary)

# Plot the combined counts
if not combinedCountsSeries.empty:
    colors2 = ['lightgreen' if label.lower() == 'benign' else 'cornflowerblue' if 'malicious' in label.lower() else 'cornflowerblue' for label in
              combinedCountsSeries.index]

    combinedCountsSeries.plot(kind='bar', figsize=(12, 6), title='Benign, Malicious, and Attack Types Comparison',
                                color=colors2)
    plt.xlabel('Traffic Label and Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

"""
