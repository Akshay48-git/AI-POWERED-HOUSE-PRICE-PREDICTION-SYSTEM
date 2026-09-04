# House Price Prediction System

## Project Overview

This project is a **House Price Prediction System built using Machine Learning**.

The application analyzes various house features such as location, area, number of bedrooms, bathrooms, and other property-related attributes to predict the estimated price of a house.

## Technologies Used

Python 3.x
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Jupyter Notebook
Machine Learning

## Dependency Installation

Install all the required Python packages using the following command:

pip install pandas numpy scikit-learn matplotlib seaborn jupyter

## Dataset

The project uses a house price dataset containing property features and their corresponding prices.

The dataset is cleaned and preprocessed before training the machine learning model.

## Data Preprocessing

The following preprocessing steps are performed:

* Handling missing values
* Removing unnecessary columns
* Encoding categorical variables
* Feature selection
* Splitting data into training and testing sets
* Feature scaling when required

## Machine Learning Model

The project uses regression algorithms to predict house prices.


Linear Regression
Decision Tree Regression
Random Forest Regression
XG Boost
Gradient Boost

The models are evaluated using metrics such as **MAE, MSE, RMSE, and R² Score** to identify the best-performing model.

## How It Works

Load the house price dataset.
The data is cleaned and preprocessed.
Important features are selected for prediction.
The dataset is divided into training and testing data.
Machine learning regression models are trained using the training data.
The models are evaluated using standard regression metrics.
The best-performing model is used to predict the price of a new house.

## Prediction

The system takes property details such as:
Location
Area
Bedrooms
Bathrooms
Property Features
and predicts the **estimated house price** based on the trained machine learning model.

## Future Enhancements

* Develop a web-based prediction interface.
* Deploy the model using Flask or FastAPI.
* Improve prediction accuracy with advanced ML algorithms.
* Add real-time property price prediction.

## Disclaimer

This project is developed for **educational and demonstration purposes**. The predicted prices are estimates and may differ from actual market prices.
