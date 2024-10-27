"""
Pseudocode
#Existing CSV File Merging
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

  Attack Labels and Attack):
     for each row in joinedFiles:
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

                       
#Feature Collection
  featureSelectionNaiveBayes(CSVFeature, Threshold_TF):
     Initialize Naive Bayes Model
           Model ← NaiveBayesModel()
   
    Iterate until number of features meets the threshold
          while Features(CSVFeature) > Threshold_TF do:
      
   Split the dataset into training and test sets
          csvTrain, csvTest ← splitDataset(CSVFeature)
      
    Train Naive Bayes model
         Model.fit(csvTrain)
      
    Calculate feature importance based on model performance
          featureScores ← evaluateFeatureImportanceNaiveBayes(Model, csvTrain)
      
    Rank features by their importance
          rankedFeatures ← Rank_Features(featureScores)
      
    Remove the least important feature
         leastFeature ← rankedFeatures[-1]
         drop(CSVFeature, leastFeature)
      
    Output the reduced feature set from CSVFeatureand return the important features
        return CSVFeature

#Oversampling 
   Load the combined dataset (mergedCSV)
     typeT ← extract minority class samples from mergedCSV
     typeT* ← T Initialize oversampled dataset with current minority samples
     w ← Feature Ranking method (RandomForestModel)

  Calculate feature importance using RandomForest:
     Train RandomForestModel on the combined dataset (mergedCSV)
     featureRankings ← RandomForestModel.feature_importances_

  Select the top (r) most important features:
     r ← top R selected features from featureRankings

  For each minority sample i in typeT: # This iterates the minority class determined by the rank previously 
     For each neighbor i' of i, find k-nearest neighbors using the selected r features
     Compute the Minkowski distance between i and i' using selected features r #Determine how similar it will be
     Perform IMOWAD on i and i' to interpolate new synthetic points based on feature importance (weighted by w)

  For k = 1 to N:
     x_k ← randomly select samples from typeT
     x'_k ← generate synthetic samples via interpolation
     typeT* ← add synthetic sample x'_k to typeT*

  Combine the oversampled minority class T* with the combined dataset
     mergedCSV ← concatenate(mergedCSV, typeT*)

  New dataset with oversampling to a new file:
     save mergedCSV to oversampledDataset.csv   

  Return the oversampledDataset with the oversampled dataset.

#Train/Test Proposed Model
  Load the oversampled dataset:
    oversampledDataset ← load("oversampledDataset.csv")

  Split the oversampled dataset into training and testing sets:
     x, y ← features and labels from oversampledCSV
     xTrain, xTest, yTrain, yTest ← trainTestSplit(x, y, testSize=TBD, random_state=42)

  Initialize models:
     RandomForestModel ← RandomForestClassifier()
     AdaBoostModel ← AdaBoostClassifier(base_estimator=DecisionTreeClassifier())
     KMeansModel ← KMeans(n_clusters=K)

  Train K-Means for Unsupervised Anomaly Detection:
     KMeansModel.fit(xTrain)
     clusterLabelsTrain ← KMeansModel.predict(xTrain)

  Identify anomalies based on cluster size (for training set):
     smallest_clusters_test ← identifySmallSlusters(clusterLabelsTrain)
     Mark samples in those clusters as anomalies in the training set

  Train Random Forest Classifier on Training Set:
     RandomForestModel.fit(xTrain, yTrain)
     yPredRFtrain ← RandomForestModel.predict(xTrain)

  Train AdaBoost Classifier on Training Set:
      AdaBoostModel.fit(xTrain, yTrain)
      yPredABtrain ← AdaBoostModel.predict(xTrain)

  Test K-Means for Anomaly Detection on Test Set:
     clusterLabelsTest ← KMeansModel.predict(xTest)

  Identify anomalies based on cluster size (for test set):
     smallest_clusters_test ← identifySmallSlusters(clusterLabelsTest)
     Mark samples in those clusters as anomalies in the test set

  Test Random Forest Classifier on Test Set:
     yPredRFtest ← RandomForestModel.predict(xTest)

  Test AdaBoost Classifier on Test Set:
     yPredABtest ← AdaBoostModel.predict(xTest)

    
#Final Anomaly Detection
Combine predictions from K-Means, Random Forest, and AdaBoost:
  finalPredictionsTrain ← majorityVote(clusterLabelsTrain, yPredRFtest, yPredABtrain)
  finalPredictionsTest ← majorityVote(clusterTabelsTest, yPredRFtest, yPredABtest)

Define majority vote:
  If K-Means detects anomaly AND (RandomForestModel or AdaBoostModel predicts attack):
     finalLabel ← "Attack"
  If both RandomForestModel and AdaBoostModel predict "Normal":
     finaLabel ← "Normal"

"""
