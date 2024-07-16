# Lung Cancer Prediction Model

## Overview
This project aims to develop a predictive model for lung cancer. The objective is to accurately identify individuals at risk of lung cancer based on several key factors.

## Business Understanding
Early detection of lung cancer can significantly improve treatment outcomes and patient survival rates. By leveraging machine learning, we aim to create a reliable tool for medical professionals to identify high-risk individuals, thereby facilitating early intervention and reducing the burden on healthcare systems.

## Data Understanding
- Gender: Indicates the gender of the individual (Male/Female)
- Age: Age of the individual
- Smoking: Indicates if the individual is a smoker (Yes/No)
- YELLOW_FINGERS: Indicates if the individual has yellow fingers (Yes/No)
- Anxiety: Indicates if the individual suffers from anxiety (Yes/No)
- Peer_Pressure: Indicates if the individual is influenced by peer pressure (Yes/No)
- Chronic Disease: Indicates if the individual has a chronic disease (Yes/No)
- Fatigue: Indicates if the individual experiences fatigue (Yes/No)
- ALLERGY: Indicates if the individual has allergies (Yes/No)
- Wheezing: Indicates if the individual experiences wheezing (Yes/No)
- Alcohol Consuming: Indicates if the individual consumes alcohol (Yes/No)
- Coughing: Indicates if the individual has a persistent cough (Yes/No)
- Shortness of Breath: Indicates if the individual experiences shortness of breath (Yes/No)
- Swallowing Difficulty: Indicates if the individual has difficulty swallowing (Yes/No)
- Chest Pain: Indicates if the individual has chest pain (Yes/No)
- Cancer: Target variable indicating if the individual has lung cancer (Yes/No)

## Modeling and Evaluation
Logistic Regression model was used for predicting lung cancer.The chosen model demonstrated high performance in terms of accuracy, precision, recall, and F1 score.

Key metrics for the Logistic Regression model are as follows:
- Accuracy: 96%
- Precision: 96%
- Recall: 96%
- F1 Score: 96%

## Feature Importance
The analysis identified that factors such as smoking status, age, coughing, shortness of breath, chest pain, and other medical conditions are critical in predicting lung cancer. These variables are most helpful in determining the likelihood of lung cancer.

## Conclusion
The project provides valuable insights into the factors influencing lung cancer prediction. By leveraging these insights, healthcare providers can enhance their screening processes and take proactive measures for early detection and treatment of lung cancer. This model can be a powerful tool in reducing the mortality rate associated with lung cancer through timely diagnosis and intervention.
