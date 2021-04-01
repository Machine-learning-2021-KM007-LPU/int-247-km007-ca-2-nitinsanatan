<h4> Contributor: Nitin Sanatan(11807742) </h4>

# Credit Approval Prediction
A website that predicts whether a loan will be accepted or rejected, based on User Input

## Objectives
In finance, a loan is the lending of money by one or more individuals, organizations, or other entities to other individuals, organizations etc. The recipient (i.e., the borrower) incurs a debt and is usually liable to pay interest on that debt until it is repaid as well as to repay the principal amount borrowed. In order to check the eligibility of the borrower, banks check few informations like Income, Age, Family Income etc. to confirm/reject the loan request. 
**Credit Approval Website** is prepared to assist any lending organization in properly checking all the data of the recipient and predict whether an individual is eligible for loan or not, based on past data.

## Technology Used
- Python3
- Django Framework
- Pandas
- Numpy
- Sklearn
- Seaborn
- HTML
- CSS
- Javascript

## Model Description
This is a Classification Probelm where system will predict if a loan will be approved or not. I have employed a Machine Learning Model to process the user input at backend.
Model is preprocessed and missing values are removed. Hyperparameter tuning is done to get best parameters for data training. Data is trained using 3 techniques; SVM, KNeighbors &
Random Forest Model. Confusion Matrices are utilised for evaluation of accuracy score of models.

- ## Feature Engineering
> Our dataset is contains 690 rows and 16 columns, where first 15 columns are data and last column is showing the Class(+,-) of whether loan is accepted or rejected. There are 9 attributes which contains **Categorical Data** and rest are **Continuous**. Missing values are also there in data denoted by **'?'** 

### Feature Identification
> ![](img/feature1.JPG)

### Handling Missing Data
> ![](img/missing.JPG)

### Label Encoding for Categorical Data
> ![](img/le.JPG)

### Plotting of dataset
> ![](img/plot.JPG)
