from collections import Counter

def raw_majority_vote(labels):
	votes = Counter(labels)
	winner, _ = votes.most_common(1)[0]
	return winner

def majority_vote(labels):
	vote_counts = Counter(labels)
	winner,winner_count = vote_counts.most_common(1)[0]
	num_winners = len([count 
					   for count in vote_counts.values()
					   if count == winner_count])
	if num_winners == 1:
		return winner
	else:
		return majority_vote(labels[:-1]) #try again without the furthest point


def distance(v,w):
	return math.sqrt(sum((v_i - w_i)**2 for v_i, w_i in zip(v,w)))


def knn_classify(k, labeled_points, new_point):
	"""
	Labeled points are a pair (point,label)
	"""
	by_distance = sorted(labeled_points,
						 key=lambda (point,_): distance(point,new_point))
	k_nearest_labels = [label for _,label in by_distance[:k]]

	return majority_vote(k_nearest_labels)

