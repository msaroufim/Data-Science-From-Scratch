def random_point(dim):
	return [random.random() for _ in range(dim)]

def random_distances(dim, num_pairs):
	return [distance(random_point(dim),random_point(dim)) 
					 for _ in range(num_pairs)]

def mean(X):
	length = len(X)
	return sum(1/length * x_i for x_i in X)

dimensions = range(1,101)

avg_distances = []
min_distances = []

random.seed(0)
for dim in dimensions:
	distances = random_distances(dim,10000)
	avg_distances.append(mean(distances))
	min_distances.append(min(distances))

min_avg_ratio = [min_dist / avg_dist
				 for min_dist, avg_dist in zip(min_distances, avg_distances)]