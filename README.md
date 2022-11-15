# Chocolate Hackathon (Dataiku)

This is a repository for our team (Team Crunch 'The Numbers' Bar)'s submission for the [2022 Lubin School and Dataiku Hackathon](https://www.pace.edu/lubin/life-lubin/events-students/case-competitions/dataiku-hackathon). It contains scripts for the data cleaning, EDA, and machine learning model predictions that we performed on the dataset. We have produced a [short video presentation](https://www.youtube.com/watch?v=Mu1sPQxeojc) to summarize our findings.

![image](https://user-images.githubusercontent.com/56360465/201800749-5f5ad3cc-6bb3-4517-99ec-9b891371d62a.png)

## Research Problem
We are provided a dataset of over 2000 chocolates’ defining characteristics such as cacao bean source, company, cocoa percentage, ingredient composition, most memorable characteristics, and ratings. We are interested in learning about the specific characteristics of chocolate that make it likable (or delicious) and in constructing models to predict ratings of chocolates.

## Data Cleaning Methods
There are two [data files](https://github.com/woodskd24/ChocolateHackathon/tree/main/Chocolate%20Data%20Files) provided, “data.csv”, and “scoringData.csv”. The first file is for training the data, and the latter for testing the data. For the training dataset, cleaning was performed using Python and packages like pandas and numpy. We removed missing variables, dropped “NA” or null values, encoded character strings to numeric variables, and converted objects to float or integer data types, coerced variables when necessary, and summed all possible null rows by variable. All these data cleaning steps resulted in us being able to use it for further analysis with no complications.

## Exploratory Data Analysis (EDA)
The Python pandas package provided the tools to [download, visualize, and transform the data](https://github.com/woodskd24/ChocolateHackathon/tree/main/Code). Visualization of the target variable (rating) accomplished by calculating the mean and other descriptive statistics by column. A box plot was used to visualize the descriptive statistics and determine outliers. All variables vs target variables (rating) were visualized and calculated for an overall view of the correlations. To further understand which features contributed the least and most to ratings. We found that features such as  cocoa, creamy, vanilla, ingredient_beans, ingredient_sugar were highly correlated with rating, and had a high probability of affecting the target variable column the most.

## Prediction and Findings
We used Weka to test various models on the data, in order to quickly ascertain which models might provide a good fit for the data. We found that the Random Forest Regression method provided the best results. We used Python’s scikit-learn package to use a random forest regression model on the training data to train the model, and used the test data (scoringData.csv) to generate the [predictions](https://github.com/woodskd24/ChocolateHackathon/blob/main/prediction.ipynb). We obtained a mean absolute error of 0.41 degrees, and a model accuracy of 86.67%. Fig. 1 shows the distribution of the predicted ratings we generated, and Fig. 2 shows a box plot distribution of the predicted ratings. We used the scikit-learn function features_importance to extract the weights of the features in the model. The key features that influenced rating in the model are Cocoa_percent, Country_of_bean_origin, Company_location, Number_of_ingredients. 

## Conclusions
We analyzed the dataset of chocolate characteristics to determine the features of chocolate that affect ratings. The data was prepared using methods in Python, primarily the pandas package. Using the cleaned data, we performed exploratory data analysis in order to examine the variables and their relationships with each other. We determined correlations of features which could be affecting the ratings. We then converted this clean dataset to an ARFF format and used WEKA to identify machine learning models, including the best fit; random forest regression. A set of predictions for chocolate ratings were created. A model was trained using the training data in Python with the help of scikit-learn. A high accuracy of 86.67% was obtained using the adjusted random forest regression, indicating that the predictions were highly reliable. Key features were identified. The features which affected the ratings of chocolate were Cocoa_percent, Country_of_bean_origin, Company_location, Number_of_ingredients. It can be concluded that the listed variables affected the ratings the most. Further analysis of this dataset should include a more in-depth comparison of machine learning models to identify all best models and features.
