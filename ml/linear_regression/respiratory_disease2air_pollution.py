import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


dataframe = pd.read_fwf('ourHawk.csv', 'r')
x_values = dataframe[['respiratory_disease']]
y_values = dataframe[['air_pollution']]

reg = linear_model.LinearRegression()
reg.fit(x_values, y_values)

plt.scatter(x_values, y_values)
plt.plot(x_values, reg.predict(x_values))
plt.show()
