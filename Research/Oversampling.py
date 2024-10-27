"""
Pseudocode
  Input: 
   - typeT represents the minority class samples from the combined dataset
   - N% is the rate of oversampling
   - k is the number of nearest neighbors
   - RandomForestModel for ranking features

  Output:
   - Generate a new file containing the oversampling

  Initialize:
   - Load the combined dataset (mergedCSV)
   - typeT ← extract minority class samples from mergedCSV
   - typeT* ← T Initialize oversampled dataset with current minority samples
   - w ← Feature Ranking method (RandomForestModel)

  Calculate feature importance using RandomForest:
   - Train RandomForestModel on the combined dataset (mergedCSV)
   - featureRankings ← RandomForestModel.feature_importances_

  Select the top (r) most important features:
   - r ← top R selected features from featureRankings

  For each minority sample i in typeT: # This iterates the minority class determined by the rank previously
   - For each neighbor i' of i, find k-nearest neighbors using the selected r features
      - Compute the Minkowski distance between i and i' using selected features r #Determine how similar it will be
      - Perform IMOWAD on i and i' to interpolate new synthetic points based on feature importance (weighted by w)

  For k = 1 to N:
   - x_k ← randomly select samples from typeT
   - x'_k ← generate synthetic samples via interpolation
   - typeT* ← add synthetic sample x'_k to typeT*

  Combine the oversampled minority class T* with the **singular combined dataset**:
   - mergedCSV ← concatenate(mergedCSV, typeT*)

  New dataset with oversampling to a new file:
   - save mergedCSV to oversampledDataset.csv
   
  Return the oversampledDataset with the oversampled dataset.
"""
