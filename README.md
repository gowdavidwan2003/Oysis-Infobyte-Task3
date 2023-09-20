# Oysis-Infobyte-Task3
CAR PRICE PREDICTION WITH MACHINE LEARNING

The price of a car depends on a lot of factors like the goodwill of the brand of the car, features of the car, horsepower and the mileage it gives and many more. Car price prediction is one of the major research areas in machine learning. So if you want to learn how to train a car price prediction model then this project is for you.

# Car Price Prediction Model

This project uses a Decision Tree Regressor model to predict car prices based on various features such as symboling, company name, fuel type, aspiration, door number, car body, drive wheel, engine location, wheelbase, car length, car width, car height, curb weight, engine type, cylinder number, engine size, fuel system, bore ratio, stroke, compression ratio, horsepower, peak RPM, city MPG and highway MPG.

## Dependencies

The project requires the following Python libraries:
- pandas
- numpy
- sklearn

## Dataset

The dataset used in this project is 'CarPrice_Assignment.csv'. It contains various features related to cars and their corresponding prices.

## Usage

1. Import the necessary libraries.
2. Load the dataset using pandas.
3. Preprocess the data (splitting the 'CarName' column to get the company name and encoding categorical variables).
4. Split the data into training and testing sets.
5. Fit a Decision Tree Regressor model using sklearn.
6. Predict car prices for new data.

## Results

The Decision Tree Regressor model provides a prediction of car prices based on the features provided. The model's performance is evaluated using Mean Absolute Error (MAE).

## Future Work

This is a simple Decision Tree Regressor model which assumes certain relationships between the dependent and independent variables. For future work, more complex models could be explored to capture any non-linear relationships in the data.
