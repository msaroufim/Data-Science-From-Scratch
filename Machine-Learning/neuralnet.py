def step_function(x):
	return 1 if x >= 0 else 0

def perceptron_output(weights,bias,x):
	calculation = dot(weights,x) + bias
	return step_function(calculation)


weights = [2,2]
bias    = -3


and_gate = min
or_gate  = max
xor_gate = lambda x,y: if x == y else 1


def sigmoid(t):
	return 1 / (1 + math.exp(-t))

def neuron_output(weights,inputs):
	return sigmoid(dot(weights,inputs))

def feed_forward(neural_network,input_vector):
	outputs = []

	for layer in neural_network:
		input_with_bias = input_vector + [1]
		output = [neuron_output(neuron,input_with_bias)
				  for neuron in layer]
		outputs.append(output)
		input_vector = output

	return outputs

	xor_network = [
	[[20,20,-30],
	[20,20,100]],

	[[60,60,-30]]]

	for x in [0,1]:
		for y in [0,1]:
			print x,y,feed_forward(xor_network,[x,y])[-1]


def backpropagate(network,input_vector,targets):
	hidden_outputs, outputs = feed_forward(network,input_vector)

	output_deltas = [output * (1 - output) * (output - target)
					 for output, target in zip(outputs,targets)]

	#adjust weights for output layer one neuron at a time
	for i, output_neuron in enumerate(network[-1]):
		#focus on ith output layer neuron
		for j, hidden_output in enumerate(hidden_outputs) + [1]):
			output_neuron[j] -= output_deltas[i] * hidden_output

	#back propagate errors to hidden layer
	hidden_deltas = [hidden_output * (1 - hidden_output) *
					 dot(output_deltas,[n[i] for n in output_layer])
					 for i, hidden_output in enumerate(hidden_outputs)]

	#adjust weights for hidden layer, one neuron at a time
	for i, hidden_neuron in enumerate(network[0]):
		for j, input in enumerate(input_vector + [1]):
			hidden_neuron[j] -= hidden_deltas[i] * input