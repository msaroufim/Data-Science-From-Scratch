def entropy(class_probabilities):
	return sum(-p * math.log(p,2)
			   for p in class_probabilities
			   if p) #ignore zero probability

def class_probabilities(labels):
	total_count = len(labels)
	return [count / total_count
			for count in Counter(labels).values()]

def data_entropy(labeled_data):
	labels = [label for _, label in labeled_data]
	probabilities = class_probabilities(labels)
	return entropy(probabilities)]

def partition_entropy(subsets):

	total_count = sum(len(subset) for subset in subsets)
	return sum(data_entropy(subset) * len(subset) / total_count
			   for subset in subsets)


#ID3 algorithm
#if all same label make leaf node
#
#choose partition with the lowest entropy
#add decision node based on chosen atribute
#recur on subset 

def partition_by(inputs, attribute):
	groups = defaultdict(list)
	for input in inputs:
		key = input[0][attribute]
		groups[key].append(input)
	return groups

def partition_entropy_by(inputs, attribute):
	partitions = partition_by(inputs, attribute)
	return partition_entropy(partition.values())

#