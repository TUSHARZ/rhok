import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


plt.switch_backend('TkAgg')  



death = []
air = []

def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)	# skipping column names
		for row in csvFileReader:
			air.append(float(row[10]))
			death.append(float(row[3]))
	return

def predict_death(air, death, x):
	air = np.reshape(air,(len(air), 1)) # converting to matrix of n X 1

	#svr_lin = SVR(kernel= 'linear', C= 1e3)
	#svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
	svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
	svr_rbf.fit(air, death) # fitting the data points in the models
	#svr_lin.fit(death, air)
	#svr_poly.fit(death, air)

	plt.scatter(air, death, color= 'black', label= 'Data') # plotting the initial datapoints 
	plt.plot(air, death, color='grey')
	plt.plot(air, svr_rbf.predict(air), color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
	#plt.plot(death,svr_lin.predict(death), color= 'green', label= 'Linear model') # plotting the line made by linear kernel
	#plt.plot(death,svr_poly.predict(death), color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
	plt.xlabel('Air Pollution')
	plt.ylabel('Death')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()

	#return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]
	return svr_lin.predict(x)[0]
	return svr_rbf.predict(x)[0]
get_data('ourHawk.csv') # calling get_data method by passing the csv file to it
# print "death- ", death
# print "air- ", air

predicted_death = predict_death(air, death, 90)  

print predicted_death