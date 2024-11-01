"""
Pseudo Code: 
Load and Merge Multiple CSV Files:
   csvFiles = {CSV_1, ..., CSV_n}
   joinedFiles = []

   for each file in csvFiles:
      load csv_i
      inspect columns of csv_i
      joinedFiles.append(csv_i)

Standard Column Naming:
   standardColumns = {
       "attack type": "Attack_Type",
       "label": "Attack_label",
       "protocol": "Protocol",
       "source ip": "Source_IP",
       "destination ip": "Destination_IP"
   }

Normalize Column Names Across Datasets:
   for each csv_i in joinedFiles:
      for each columnName in csv_i:
         if columnName in standardColumns.keys():
            rename csv_i[columnName] to standardColumns[columnName]
         else:
            # If the column is missing in standardColumns display a message on which columns were excluded but do not add them to the file, and ask user which ones to load.

Align Features:
   - Ensure that all CSVs have consistent column names.
   - If any critical feature is missing in one CSV, handle it by:
      - Notify the user, display which feature and provide user with adding (Y/N) option

Add Attack Labels and Attack Types (if not already present):
   for each row in Joined_files:
      if row corresponds to attack:
         row["Attack_label"] = 1
         row["Attack_type"] = "Attack"
      else:
         row["Attack_label"] = 0
         row["Attack_type"] = "Normal"

Concatenate CSVs into a Single Dataset:
   mergedCSV = concatenate(joinedFiles)

Save the merged dataset for further processing:
   save(mergedCSV, "combinedDatasets.csv")
"""
