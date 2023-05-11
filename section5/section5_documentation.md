# Documentation

## Task Overview

This section requires a a machine learning model to be built to predict the buying price given specific parameters. The dataset contains various parameters related to cars, including buying price, maintenance, number of doors, luggage boot size, safety, and class value. 

## Dataset

The dataset contains 1728 instances and 7 attributes. Each instance represents a car with the following attributes:

1. buying: buying price of the car (vhigh, high, med, low)
2. maint: maintenance price of the car (vhigh, high, med, low)
3. doors: number of doors (2, 3, 4, 5more)
4. persons: capacity in terms of persons to carry (2, 4, more)
5. lug_boot: the size of the luggage boot (small, med, big)
6. safety: estimated safety of the car (low, med, high)
7. class: class value of the car (unacc, acc, vgood, good)

## Approach

The task is to predict the buying price of a car, which means it should be the target variable. However, the original dataset provides information about the overall acceptability of a car based on several features, instead of the buying price. 

Since the class attribute represents the overall acceptability of a car, we will use it as a proxy for the buying price prediction. We also use a combination of the predicted class using the model, as well as the given class from the parameters. This will help us to predict the buying price of a car.

To build a machine learning model to predict the buying price given the specified parameters, we will follow these steps:

1. Load the dataset
2. Data cleaning
3. Feature engineering
4. Split the data into training and testing sets
5. Build and train the model
6. Evaluate the model
7. Make a prediction

### Data Cleaning

The dataset may contain missing or incorrect values, which can affect the performance of the model. Therefore, we need to clean the data by removing any rows with missing values, duplicates, or incorrect values.

### Feature Engineering

We need to convert categorical variables to numerical values before we can use them in our model. We can use one-hot encoding to convert the categorical variables.

### Build and train model

We will use a Random Forest Classifier to build our model. The Random Forest Classifier is an ensemble learning method that combines multiple decision trees to improve the accuracy and robustness of the model.

### Evaluate the model

We will use the accuracy_score function from the sklearn library to evaluate the accuracy of the model.

### Make a prediction

To make a prediction for the specified parameters, we need to create a new dataframe with the same columns as the original dataframe and assign the specified parameter values to the corresponding columns. We then use the ‘predict’ method of the classifier to make a prediction for the given data.

A function is defined to **compute** the most likely buying value given a predicted class. This function uses the group counts of buying for each class to compute the most likely buying value for the predicted and given classes. It then computes the weighted average of the predicted and given buying values.