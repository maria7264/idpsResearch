#The following code is to combine the data found within all the files for a single datasets.
                  #STEP 1
import pandas as pd
import os

folderPath = 'SET PATH HERE' #inside the quotation set the directory or the path where the information will be found 
dataframes = []

for file in os.listdir(folderPath):
    if file.endswith('.csv'):
        filePath = os.path.join(folderPath, file)
        print(f"Processing file: {file}")
        dataF = pd.read_csv(filePath)
        dataF['SourceFile'] = file
        dataframes.append(dataF)

combinedData = pd.concat(dataframes, ignore_index=True)
combinedData.to_csv('SET NAME OF FILE HERE', index=False)
print(f"Combined data shape: {combinedData.shape}")


#The following code is to count the attack types of the combined datasets and create a file to store the results
          #STEP 2
import pandas as pd

combinedData = pd.read_csv('SET THE NAME OF THE FILE YOU CREATE ON STEP 1.csv')
labelCounts = combinedData['Label'].value_counts()
print("Counts of each traffic label (Benign vs different attacks):")
print(labelCounts)

combinedData['TrafficType'] = combinedData['Label'].apply(lambda x: 'benign' if x == 'BENIGN' else 'malicious')
trafficTypeCounts = combinedData['TrafficType'].value_counts()
print("\nCounts of benign and malicious traffic:")
print(trafficTypeCounts)



  #This part is so the results can be saved on a text file that will be utilized after for graph comparison
with open('SET NEW FILE NAME HERE.txt', 'w') as f:
    f.write("Counts of each traffic label (Benign vs different attacks):\n")
    f.write(labelCounts.to_string())
    f.write("\n\n")
    f.write("Counts of benign and malicious traffic:\n")
    f.write(trafficTypeCounts.to_string())

print("Results can now be found on: 'SET NEW FILE NAME HERE.txt'")

#The following code is utilized to do the graph representation


#[[[[[THIS MUST BE EDITED ONCE THE PROGRAM IS DEVELOPED AND TESTED]]]]]



