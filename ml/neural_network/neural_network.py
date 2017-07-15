from numpy import exp, array, random, dot

class NeuralNetwork():
	def __init__(self):
		# seed the random number  generator so that it 
		# generates the same numbers (wtf?) each time the program runs
		random.seed(1)
		
		# didn't understand this.
		
		# Single Neuron Model
		# --3 input connections
		# --1 output connection
		# We assign random weights to a 3x1 matrix, 
		# with values ranging from -1 to 1 (how?) and mean 0
		self.synaptic_weights =  2*random.random((3,1)) -1
	
	# == Activation Function == 
	# Sigmoid Function: describes the S-shaped curve
	# We pass the weighted sum of the inputs through this function
	# to normalize them between 0 and 1 (based on the probablity)
	def __sigmoid(self, x):
		return 1/ (1 + exp(-x))

	
	# Derivative of the Sigmoid Function
	# This is the gradient of the Sigmoid curve
	# Confidence indication about the existing curve
	def __sigmoid_derivative(self, x):
		return x * (1-x)

	# We train the neural network through the process of Trail and Error
	# adjusting the synaptic weights each time
	def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
		for iteration in xrange(number_of_training_iterations):
			# Pass the training set through the neural network  (single neuron)
			output = self.think(training_set_inputs)

		# Error calculation
		# --difference between the desired output and the predicted output
		error = training_set_outputs - output

		# Multiply the error by the input and again by the gradient of the Sigmoid curve
		# => This means, less confident weights are adjusted more
		# This means inputs, which are zero, donot cause the changes to the wights
		adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
		# --the process above is known as gradient discent


		# adjust the weights
		self.synaptic_weights += adjustment
	# Making the neural network think
	def think(self, inputs):
		# Pass values through our neural network (single neuron)
		return self.__sigmoid(dot(inputs, self.synaptic_weights))

# backpropogation: the process of propogating our error values back into our neural net is known as backpropogation
# [BackPropogation] : technique to train a neural net by updating weights via gradient descent
# The Perceptron
# Single Layer Feedfoward Neural Network 
# Data flows in one direction

if __name__ == '__main__':
	
	# initialize a single neuron neural network
	neural_network = NeuralNetwork()
	
	print "Random starting synaptic weights"
	print neural_network.synaptic_weights

	# The training set. 
	# There are 3 inputs and only 1 output
	training_set_inputs = array([[1, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
	training_set_outputs = array([[0, 1, 1, 0]]).T
	
	# Now, train the neural network using the training set
	# Re-do it 10,000 times and make small adjustments each time
	neural_network.train(training_set_inputs, training_set_outputs, 10000)
	
	print "New Synaptic weights"
	print neural_network.synaptic_weights

	# Test the neural network
	print "predicting"
	print neural_network.think(array([1, 0, 0]))

# Deep Learning = many layers of neural net + big data + big compute
