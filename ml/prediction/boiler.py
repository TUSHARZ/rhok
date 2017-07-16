import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


plt.switch_backend('TkAgg')  


death = []
variable = []

def get_data(filename, var, death_no):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)	# skipping column names
		for row in csvFileReader:
			variable.append(float(row[var]))
			death.append(float(row[death_no]))
	return

def predict_death(variable, death, x):
	variable = np.reshape(variable,(len(variable), 1)) # converting to matrix of n X 1

	#svr_lin = SVR(kernel= 'linear', C= 1e3)
	#svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
	svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
	svr_rbf.fit(variable, death) # fitting the data points in the models
	#svr_lin.fit(death, variable)
	#svr_poly.fit(death, variable)

	plt.scatter(variable, death, color= 'black', label= 'Data') # plotting the initial datapoints 
	plt.plot(variable, death, color='grey')
	plt.plot(variable, svr_rbf.predict(variable), color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
	#plt.plot(death,svr_lin.predict(death), color= 'green', label= 'Linear model') # plotting the line made by linear kernel
	#plt.plot(death,svr_poly.predict(death), color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
	plt.xlabel('variable Pollution')
	plt.ylabel('Death')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()

	#return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]
	#return svr_lin.predict(x)[0]
	return svr_rbf.predict(x)[0]

get_data('ourHawk.csv', 12, 17) # calling get_data method by passing the csv file to it
# print "death- ", death
# print "variable- ", variable

predicted_death = predict_death(variable, death, 90)  

print predicted_death

