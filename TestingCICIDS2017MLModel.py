import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

combinedData = pd.read_csv('combined_CICIDS2017.csv')

combinedData.fillna(combinedData.mean(), inplace=True)

label_encoder = LabelEncoder()
combinedData['Label'] = label_encoder.fit_transform(combinedData['Label'])

features = combinedData.drop(columns=['Label', 'SourceFile'])
target = combinedData['Label']

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(scaled_features, target, test_size=0.3, random_state=42)
rfModel = RandomForestClassifier(n_estimators=100, random_state=42)
rfModel.fit(X_train, y_train)


y_pred = rfModel.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Accuracy: {accuracy}")
print("Classification Report:\n", classification_report(y_test, y_pred))


"""
After running the code for about 20 minutes there was no output, the console did not report any errors
"""
