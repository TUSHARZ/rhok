import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

import random

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

	mydict = [{
		'variable': variable ,
		'death': svr_rbf.predict(variable)
		}]
	
	fields = ['variable', 'death']

	# filename = "output.csv"
	# with open(filename, 'w') as csvfile:
	# 	writer = csv.DictWriter(csvfile, fieldnames = fields)
	# 	writer.writeheader()
	# 	writer.writerows(mydict)
	#plt.plot(death,svr_lin.predict(death), color= 'green', label= 'Linear model') # plotting the line made by linear kernel
	#plt.plot(death,svr_poly.predict(death), color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
	plt.xlabel('variable')
	plt.ylabel('Death')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()

	#return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]
	#return svr_lin.predict(x)[0]
	return svr_rbf.predict(x)[0]


print """
	Select one of the following options:
	1. Religion Based vs Literacy [5, 13]
	2. Digestive Diseases vs Water Pollution [7, 11]
	3. Accidents vs No. of Vehicles [4, 14]
	4. Forest Coverage vs Radiation [12, 17] 
	5. Abnormal Findings vs Police Vehicles [1, 15]
	6. others vs Hospitals [9, 16]
"""

choice = raw_input("Enter the choice::")
print choice

while True:
	if int(choice) == 1:
		print "we reached here"
		get_data('ourHawk.csv', 5, 13)
		predicted_death = predict_death(variable, death, 90)  
		mydict
		print predicted_death
		break
	
	elif int(choice) == 2:
		get_data('ourHawk.csv', 7, 11)
		predicted_death = predict_death(variable, death, 90)  
		mydict = mydict
		print predicted_death
		break

	elif int(choice) == 3:
		get_data('ourHawk.csv', 4, 14)
		predicted_death = predict_death(variable, death, 90)  
		mydict = mydict
		print predicted_death
		break

	elif int (choice)==4:
		get_data('ourHawk.csv', 12, 17)
		predicted_death = predict_death(variable, death, 90)  
		mydict = mydict
		print predicted_death
		break

	elif int(choice) == 5:
		get_data('ourHawk.csv', 1, 15)
		predicted_death = predict_death(variable, death, 90)  
		mydict = mydict
		print predicted_death
		break

	elif int(choice) == 6:
		get_data('ourHawk.csv', 9, 16)
		predicted_death = predict_death(variable, death, 90) 
		mydict = mydict 
		print predicted_death
		break

	else: 
		break

