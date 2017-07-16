import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


plt.switch_backend('TkAgg') 

air = []
death = []

def get_data(filename):
	# read the file
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		#skipping the column names
		next(csvFileReader)
		for row in csvFileReader:
			death.append(int(row[7][0]))
			death.append(float(row[4]))
	return

def predict_death(death, air, x):
	# converting to matrix of nx1
	# why?
	death = np.reshape(death, (len(death), 1))
	# why?!
	svr_lin = SVR(kernel='linear', C=1e3)
	#svr_poly = SVR(kernel='poly', C=1e3, degree=2)
	svr_rbf = SVR(kernel= 'rbf', C=1e3, gamma=0.1)
	# defining the support vector regression model
	svr_rbf.fit(death, death)
	svr_lin.fit(death, death)
	#svr_poly.fit(death, death)
	
	# plotting the initial datapoints
	plt.scatter(death, death, color='black', label='Data')
	plt.plot(death, death, color='grey')
	plt.plot(death, svr_rbf.predict(death), color='red', label='RBF model')
	plt.plot(death, svr_lin.predict(death), color='green', label='Linear Model')
	#plt.plot(death, svr_poly.predict(death), color='blue', label='Polynomal Model')
	
	plt.xlabel('death')
	plt.ylabel('death')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()
	
	return svr_rbf.predict(x)[10], svr_lin.predict(x)[10] #svr_poly.predict(x)[10]


# calling get_data fn with the csv file
get_data('ourHawk.csv')

predicted_price = predict_death(death, air, 16)
print predicted_price