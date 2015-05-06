def accuracy(tp,fp,fn,tn):
	correct = tp + tn
	total   = tp + tn + fn + tn
	return correct / total


def precision(tp,fp,fn,tn):
	return tp / (tp + fp)

def recall(tp,fp,fn,tn):
	return tp / (tp + fn)


def f1_score(tp,fp,fn,tn):
	p = precision(tp,fp,fn,tn)
	r = recall(tp,fp,fn,tn)
	return 2 * p * r / (p + r)


def split_data(data,prob):
	results = [], []
	for row in data:
		results[0 if random.random() < prob else 1].append(row)
	return results

def train_test_split(x,y,test_pct):
	data = zip(x,y)
	train,test = split_data(data,1 - test_pct)
	x_train, y_train = zip(*train)
	x_test,  y_test  = zip(*test)
	return x_train, x_test, y_train, y_test


# Usage:
# model = SomeKindOfModel()
# x_train, x_test, y_train, y_test = train_test_split(xs,ys,0.33)
# model.train(x_train, y_train)
# performance = model.test(x_test, y_test)