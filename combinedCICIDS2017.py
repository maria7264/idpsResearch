import pandas as pd
import os
#This is code is simply to combine all the data found on dataset CICIDS 2017

folderPath = 'C:\\Users\\homep\\Desktop\\PRISM URP\\Datasets\\Focus\\CICIDS 2017\\MachineLearningCSV'
dataframes = []

for file in os.listdir(folderPath):
    if file.endswith('.csv'):
        filePath = os.path.join(folderPath, file)
        print(f"Processing file: {file}")
        dataF = pd.read_csv(filePath)
        dataF['SourceFile'] = file
        dataframes.append(dataF)

combinedData = pd.concat(dataframes, ignore_index=True)
combinedData.to_csv('combined_CICIDS2017.csv', index=False)
print(f"Combined data shape: {combinedData.shape}")

# Keep in mind the output was a larger CSV File in which in contain data extracted from multiple smaller CSV files
