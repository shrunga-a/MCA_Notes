Step 1: Importing the dataset
Step 2: Data pre-processing
Step 3: Splitting the test and train sets
Step 4: Fitting the linear regression model to the training set
Step 5: Predicting test results
Step 6: Visualizing the test results


1. Importing the Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
dataset.head()

X = dataset.iloc[:,:-1].values  #independent variable array
y = dataset.iloc[:,1].values  #dependent variable vector

The X is independent variable array and y is the dependent variable
vector.
Note the difference between the array and vector.
The dependent variable must be in vector and independent
variable must be an array itself.

3. Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)

We don’t need to apply feature scaling for linear regression as libraries take care of it.

4. Fitting linear regression model into the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train) #actually produces the linear eqn for the data

5. Predicting the test set results
We create a vector containing all the predictions of the test set salaries.
The predicted salaries are then put into the vector called
y_pred.(contains prediction for all observations in the test set)

predict method makes the predictions for the test set. Hence, the input is the test set.
The parameter for predict must be an array or sparse matrix, hence input is X_test.

y_pred = regressor.predict(X_test)
y_pred

y_test

y_test is the real salary of the test set.
y_pred are the predicted salaries.

Visualizing the results
1. Plotting the points (observations)

X – coordinate (X_train: number of years)
Y – coordinate (y_train: real salaries of the employees)
Color ( Regression line in red and observation line in blue)




2. Plotting the regression line
plt.plot have the following parameters :

X coordinates (X_train) – number of years
Y coordinates (predict on X_train) – prediction of X-train (based on a number of years).
Note : The y-coordinate is not y_pred because y_pred is predicted salaries
of the test set observations.

#plot for the TRAIN

plt.scatter(X_train, y_train, color='red') # plotting the observation line

plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line

plt.title("Salary vs Experience (Training set)") # stating the title of the graph

plt.xlabel("Years of experience") # adding the name of x-axis
plt.ylabel("Salaries") # adding the name of y-axis
plt.show() # specifies end of graph


The above code generates a plot for the train set shown below:

#plot for the TEST

plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line

plt.title("Salary vs Experience (Testing set)")

plt.xlabel("Years of experience")
plt.ylabel("Salaries")
plt.show()





Step 1: Importing the dataset
Step 2: Data pre-processing
Step 3: Splitting the test and train sets
Step 4: Fitting the linear regression model to the training set
Step 5: Predicting test results
Step 6: Visualizing the test results

Program to Implement Linear regression.
# importing the dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
dataset.head()

# data preprocessing
X = dataset.iloc[:, :-1].values  #independent variable array
y = dataset.iloc[:,1].values  #dependent variable vector

# splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)

# fitting the regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train) #actually produces the linear eqn for the data

# predicting the test set results
y_pred = regressor.predict(X_test)
y_pred
y_test
# visualizing the results
#plot for the TRAIN
plt.scatter(X_train, y_train, color='red') # plotting the observation line
plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
plt.title("Salary vs Experience (Training set)") # stating the title of the graph

plt.xlabel("Years of experience") # adding the name of x-axis
plt.ylabel("Salaries") # adding the name of y-axis
plt.show() # specifies end of graph

#plot for the TEST

plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
plt.xlabel("Years of experience")
plt.ylabel("Salaries")
plt.show()
