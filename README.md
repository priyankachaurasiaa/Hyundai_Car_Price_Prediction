# Hyundai_Car_Price_Prediction
![image](https://github.com/priyankachaurasiaa/Hyundai_Car_Price_Prediction/assets/134799886/c69a19ea-afe7-4f45-91a1-6e04b49c6220)



## Car-price-regression-Used Hyundai Car Price Prediction

With the help of Machine Learning model we have Predicted the used Hyundai car prices in UK including various Influential Factors such as Model, Year, Mileage, Fuel type, Engine Size which significantly impact the prices of used cars

## Objectives

Our project serves two main objectives:

1. **Accurate Price Predictions for Buyers**: We aim to provide accurate price predictions to empower buyers to make well-informed decisions by evaluating the fairness of asking prices.

2. **Optimized Pricing for Sellers**: For sellers, our predictions enable them to set appropriate prices based on market trends, increasing their chances of a successful sale.


## Dataset

![dataset](https://github.com/priyankachaurasiaa/Hyundai_Car_Price_Prediction/assets/134799886/bb0fe2ed-9a27-41c9-8328-46235f085097)

## Description

- **Objective**: Our primary objective is to build a Linear Regression Machine Learning model to predict used car prices based on various features.

- **Data Collection**: We collected data from spinny.com, a reputable service provider in the field, to obtain a reasonable and large dataset.

- **Data Cleaning & Feature Engineering**: The dataset underwent thorough cleaning to handle null values, duplicates, and noise. We also generated 14 meaningful features through exploratory data analysis (EDA) and feature generation techniques.

- **Final Data Preparation**: The dataset was prepared for training the model through feature selection, encoding, and scaling.

- **Independent Features**: The independent features used for prediction include model, body type, fuel type, transmission, model year, km driven, mileage, seating capacity, ground clearance, boot space, fuel tank capacity, and max power.

- **Data Analysis and Visualization**: We conducted data analysis using group-by, pivot tables, and aggregation techniques. The data was visualized to gain insights.

- **Training**: The dataset was split into training and testing sets, and a Linear Regression model was trained.

- **Testing**: Predicted values for prices were generated and model accuracy was evaluated using R2 score and Adjusted R2 score (85% and 84%, respectively).

- **Predicting**: The model can be used by buyers and sellers to predict the prices of pre-owned cars using hypothetical features.

## Insights
 
![insights](https://github.com/priyankachaurasiaa/Hyundai_Car_Price_Prediction/assets/134799886/ce5f8237-3608-41f3-bff5-5fdea2e2a675)

![insights_2](https://github.com/priyankachaurasiaa/Hyundai_Car_Price_Prediction/assets/134799886/73fcdfa5-6a50-4113-9114-4e2d6e30b2a8)

<img width="591" alt="image" src="https://github.com/priyankachaurasiaa/Hyundai_Car_Price_Prediction/assets/134799886/ff29a56e-132c-41cb-8fa4-19e84d139745">

## Conclusion

- **Error Distribution**: After training our model, we analyzed the difference between the test and predicted values using a distribution plot. The errors followed a normal distribution with a mean close to zero, indicating the accuracy of our predictions.

- **Scatter Plot Analysis**: Scatter plots of test points against predicted points showed a strong correlation, indicating that our model effectively captures data patterns and trends.

- **Performance Metrics**: We evaluated the model's performance using metrics such as Root Mean Square Error (RMSE), R2 Score, and Mean Square Error (MSE). Our model achieved an RMSE of 1.36 and an MSE of 1.97 for the test and predicted test values, indicating high accuracy.

- **Accuracy Score**: We adapted the accuracy score, typically used for classification tasks, to assess our regression model's accuracy. Our model achieved an accuracy score of 93.4%, highlighting its effectiveness in predicting used car prices.

## Challenges

- Transforming categorical values and removing unnecessary features for regression compatibility.

- Finding the best regression algorithm and dealing with challenges in gridsearchCV for hyper parameter tuning.

- Identifying influential features using techniques like Pearson coefficient correlation and extra tree regressor.

- Learning HTML from scratch to develop a webpage showcasing the model's workings.

## Future Scope of the Model

The model holds great potential for future applications:

- **Empowering Buyers:** This model empowers buyers by enabling them to assess the fair market value of used cars based on input characteristics. This valuable information equips buyers to make well-informed decisions and negotiate more effectively for better deals.

- **Transparent Pricing:** The model establishes transparency in pricing, offering standardized and objective valuation. By doing so, it mitigates information asymmetry between sellers and buyers, thus safeguarding against potential exploitation arising from a lack of market knowledge.

- **Efficiency in Decision-Making:** By leveraging this model, buyers can expedite the process of estimating fair price ranges without the need for extensive manual research. This not only saves time but also minimizes the effort involved in the car purchasing process.

- **Effective Selling Assistance:** Sellers can benefit from the model as well, utilizing it to establish competitive prices based on their car's unique characteristics. This approach enhances their ability to attract potential buyers more effectively and efficiently.

## Contact Information

- For inquiries or further information, please contact Priyanka_Chaurasia at priyankachaurasia7050@gmail.com
