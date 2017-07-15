import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


plt.switch_backend('TkAgg') 

dates = []
prices = []

def get_data(filename):
	# read the file
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		#skipping the column names
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))
	return

def predict_price(dates, prices, x):
	# converting to matrix of nx1
	# why?
	dates = np.reshape(dates, (len(dates), 1))
	# why?!
	svr_lin = SVR(kernel='linear', C=1e3)
	svr_poly = SVR(kernel='poly', C=1e3, degree=2)
	svr_rbf = SVR(kernel= 'rbf', C=1e3, gamma=0.1)
	# defining the support vector regression model
	svr_rbf.fit(dates, prices)
	svr_lin.fit(dates, prices)
	svr_poly.fit(dates, prices)
	
	# plotting the initial datapoints
	plt.scatter(dates, prices, color='black', label='Data')
	plt.plot(dates, prices, color='grey')
#	plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
#	plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear Model')
	plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomal Model')
	
	plt.xlabel('Date')
	plt.ylabel('Prices')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()
	
	return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]


# calling get_data fn with the csv file
get_data('appl.csv')

predicted_price = predict_price(dates, prices, 29)
