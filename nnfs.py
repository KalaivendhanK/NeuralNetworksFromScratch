
"""######### Exercise 1 ############
The neural networks has 3 input neurons , 2 hidden layers of 3 neurons each and one output layer of 2 neuron
"
Below is the implementation for one hidden layer neuron, which gets input from its 3 sources.
So, each source has its weight associated with this neuron, and each hidden layer neuron has a bias associated to it.
So, there are 3 weights(one from each source). 3 inputs and a bias.
"""#####################

'''
inputs = [2.3, 4.3, 1.2]
weights = [1.3, 0.3, 3.4]
bias = 3.0

output = inputs[0] * weights[0] + inputs[1]* weights[1] +inputs[2]* weights[2] + bias
print(output)
'''

"""########## Exercise 2 ###########
Below is the complete hidden layer, 
It has 3 neurons in this layer.So each neuron has 1 input, 3 weights, and 1 bias associated with it.
Since there are total of 3 neurons in this first layer, there will be 3 inputs , 9 weights and 3 biases in total
"""
'''
inputs = [1.0, 2.0, 3.0, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2.0
bias2 = 3.0
bias3 = 0.5

output = [ inputs[0]*weights1[0] + inputs[1]* weights1[1]+ inputs[2]* weights1[2] + inputs[3]* weights1[3] + bias1,
           inputs[0]* weights2[0] + inputs[1]*weights2[1] + inputs[2]* weights2[2] + inputs[3]* weights2[3] + bias2,
           inputs[0]* weights3[0] + inputs[1]* weights3[1] + inputs[2]*weights3[2] + inputs[3]* weights3[3] + bias3
           ]

print(output)
'''


"""########## Exercise 3 ###########
Here, we are using numpy module to perform dot product.
"""#####################

'''
import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]
output = np.dot( weights , inputs) + biases
print(output)
'''