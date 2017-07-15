import pandas as pd
from sklearn import linear_model

import matplotlib.pyplot as plt

# read the data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]


# training the model on the data
# body-reg = body regression
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

# visualize results
plt.scatter(x_values, y_values)
# is this used to plot a line; based on the predictions based 
# on linear regression

# what the below command does is:
#	predict the body_reg based on the current x_values
plt.plot(x_values, body_reg.predict(x_values))
plt.show()

