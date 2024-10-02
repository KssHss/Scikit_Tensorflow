# Linear Regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables.  
# It assumes a linear relationship between the variables, meaning the relationship can be represented by a straight line. 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv("/Downloads/house_price_data.csv")

# Separate features (X) and target variable (y)
X = data[['square_footage']]
y = data['price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
