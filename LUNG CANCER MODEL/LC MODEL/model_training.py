import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split  # Corrected import statement
from imblearn.over_sampling import SMOTE  # Import SMOTE
from sklearn.linear_model import LogisticRegression
import pickle




pp_data = pd.read_csv('Preprocessed_data.csv')
pp_data.drop('Unnamed: 0',axis=1,inplace=True)

X = pp_data.drop('Cancer', axis=1)          #Input
y = pp_data['Cancer']                       #Output

cor = pp_data.corr()
print(cor)



smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X, y)


X_train, X_test, y_train, y_test = train_test_split(X_train_smote, y_train_smote, test_size=0.2, random_state=42)



lreg = LogisticRegression()

lreg.fit(X_train,y_train)

ypred = lreg.predict(X_test)


from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(ypred,y_test))

filename='Model.pkl'

with open(filename, 'wb') as f:
    pickle.dump(lreg, f)

