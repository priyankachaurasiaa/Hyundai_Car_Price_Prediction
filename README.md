# Hyundai_Car_Price_Prediction
Car-price-regression-Used Hyundai Car Price Prediction
With the help of Machine Learning model we have Predicted the used Hyundai car prices in UK including various Influential Factors such as Model, Year, Mileage, Fuel type, Engine Size which significantly impact the prices of used cars

Objectives
Accurate price predictions for the buyers to make informed decisions by evaluating the fairness of asking prices and for Sellers they can set appropriate prices based on market trends, which increasing their chances of a successful sale.

This project aims to contribute to the understanding of used car pricing dynamics by analyzing data and uncovering the relationships between factors and prices. And make Valuable insights gained from this research can benefit market participants and improve transparency in the used car market.

Dataset
Screenshot (1615)

Insights
Screenshot (1626)

Screenshot (1628)

Description
Objective: Build a Linear Regression ML model to predict used car prices based on various features.

Data Collection: Scraped data from spinny.com, a service provider in the field, to obtain a reasonable and large dataset.

Data Cleaning & Feature Engineering: Handled null values, duplicates, and noise. Generated 14 meaningful features through EDA and feature generation techniques.

Final Data Preparation: Applied feature selection, encoding, and scaling to prepare the dataset for training the model.

Independent Features: Model, body type, fuel type, transmission, model year, km driven, mileage, seating capacity, ground clearance, boot space, fuel tank capacity, max power.

Data Analysis and Visualization: Conducted data analysis using group by, pivot tables, and aggregation, and visualized the data for insights.

Training: Split the dataset into training and testing sets, and trained the model using Linear Regression.

Testing: Generated predicted values for prices and evaluated model accuracy using R2 score and Adjusted R2 score (85% and 84%, respectively).

Predicting: The model can be used by buyers/sellers to predict the prices of pre-owned cars using hypothetical features.

Conclusion
Error Distribution: After training our model, we analyzed the difference between the test and predicted values using a distribution plot. The errors followed a normal distribution with a mean close to zero. This indicates that our model's predictions are generally accurate, as the errors are minimal.
Scatter Plot Analysis: We plotted the test points against the predicted points using a scatter plot. The points aligned closely along the diagonal line, indicating a strong correlation between the predicted and actual values. This suggests that our model is effectively capturing the patterns and trends in the data.
Performance Metrics: We evaluated the performance of our model using metrics such as Root Mean Square Error (RMSE), R2 Score, and Mean Square Error (MSE). Our model achieved an RMSE of 1.36 and an MSE of 1.97 for the test and predicted test values. These metrics provide insights into the accuracy and precision of our model's predictions.
Accuracy Score: While accuracy score is typically used for classification tasks, we adapted it to assess the accuracy of our regression model. By setting a cutoff based on MSE, we classified predictions as either correct or incorrect. Our model achieved an accuracy score of 93.4%, indicating its effectiveness in predicting used car prices.
Challenges
Transforming categorical values and removing unnecessary features for regression compatibility.

Finding the best regression algorithm and dealing with challenges in gridsearchCV for hyper parameter tuning.

Identifying influential features using techniques like Pearson coefficient correlation and extra tree regressor.

Learning HTML from scratch to develop a webpage showcasing the model's workings.

Future Scope of the Model for the Masses:
Empowering Buyers: The model estimates the fair market value for used cars based on input characteristics (make, model, year, mileage, condition, and features), helping buyers make informed decisions and negotiate better deals.

Transparent Pricing: The model provides standardized and objective pricing, reducing information asymmetry between sellers and buyers, and preventing exploitation due to a lack of market knowledge.

Saving Time and Effort: Buyers can quickly estimate fair price ranges without manual research, saving time and effort during the purchasing process.

Selling Assistance: Sellers can use the model to set reasonable prices based on their car's characteristics, attracting potential buyers more effectively.

Financial Planning: Accurate price predictions aid in financial planning, allowing individuals to make informed decisions about selling their car and its impact on their overall financial situation.
