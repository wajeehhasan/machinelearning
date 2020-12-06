import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
#reading data and converting it into dataframes
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
#spliting data into train and test using sklearn
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

#implementing simple linear regression model
from sklearn.linear_model import LinearRegression
#create a regression object for LinearREG class
regressor = LinearRegression()
#applying model of LR on object
regressor.fit(x_train, y_train)
#predicting values using x_test


y_predict= regressor.predict(x_test)