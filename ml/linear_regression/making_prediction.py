import pandas as pd
from sklearn import linear_model

import matplotlib.pyplot as plt

# read the data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]


# training the model on the data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

# visualize results
plt.scatter(x_values, y_values)
# is this used to make the predictions?
plt.plot(x_values, body_reg.predict(x_values))
plt.show()

