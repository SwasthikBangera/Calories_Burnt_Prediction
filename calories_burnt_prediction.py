# -*- coding: utf-8 -*-
"""Calories_Burnt_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YwEqb8C1RdppP8tIKchXYrQo71ddNHGk

Importing depedencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
from sklearn import metrics

"""Data Preprocessing"""

# Importing calorie dataset
Calories_dataset = pd.read_csv('/content/calories.csv')
# Importing the exercise dataset
Exercise_dataset = pd.read_csv('/content/exercise.csv')

# Reading the data
Calories_dataset.head()

Exercise_dataset.head()

# Comparing the User_ID columns of two datasets
Calories_dataset['User_ID'].equals(Exercise_dataset['User_ID'])

# Adding Calories dataset column to exercise dataset
Exercise_dataset['Calories'] = Calories_dataset['Calories']

# alternatively use the below:
# Exercise_dataset = pd.concat([Exercise_dataset, Calories_dataset['Calories]], axis=1)

# Verifying the inclusion of Calorie column
Exercise_dataset.head()

# Replacing categorical data in Gender to Numerical data
Exercise_dataset.replace({'Gender':{'male':0,'female':1}},inplace=True)

# Verifying numerical data conversion
Exercise_dataset.head()

# Size of dataset
Exercise_dataset.shape

# Additional information of the dataset
Exercise_dataset.info()

# Empty values
Exercise_dataset.isnull().sum()

"""Data Analysis"""

# Statistical view of the dataset
Exercise_dataset.describe()

"""Data Visualization"""

# Plot dataset bby gender
sns.set()
sns.countplot(Exercise_dataset['Gender'])

# Use distribution plot to determine spread of age
sns.distplot(Exercise_dataset['Age'])

# Distribution plot of Height
sns.distplot(Exercise_dataset['Height'])

# Distribution plot of Weight
sns.distplot(Exercise_dataset['Weight'])

"""Correlation in dataset"""

# Finding correlation in dataset
correlation = Exercise_dataset.corr()

# Heatmap to understand correlation between features
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':10}, cmap='Blues')

"""Splitting features and Target"""

# Splitting data into features and label (Calories)
X = Exercise_dataset.drop(columns=['User_ID','Calories'], axis=1)
Y = Exercise_dataset['Calories']

print(X.head())
print(X.shape)

print(Y.head())
print(Y.shape)

"""Splitting data into Training and target data"""

# Splitting data in to test and training data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print(X_train.shape, X.shape, X_test.shape)

"""Training the model"""

# Call the Regression model
model = XGBRegressor()

model.fit(X_train, Y_train)

"""Evalutaion"""

# Finding the Mean Abs Error for training data
training_data_prediction = model.predict(X_train)
print(training_data_prediction)
print('\n')
mae_train = metrics.mean_absolute_error(Y_train, training_data_prediction)
print("Mean abs error for train data :", mae_train)

# Finding the Mean Abs Error for test data
test_data_prediction = model.predict(X_test)
print(test_data_prediction)
print('\n')
mae_test = metrics.mean_absolute_error(Y_test, test_data_prediction)
print("Mean abs error for test data :", mae_test)

