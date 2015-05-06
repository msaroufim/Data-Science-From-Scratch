import math

#in production you want to use numpy since lists are slow as fuck
#matrix operations

def shape(A):
	num_rows = len(A)
	num_cols = len(A[0])
	return num_rows,num_cols

def make_matrix(num_rows,num_cols,entry_fn):
	return [[entry_fn(i,j)
			for j in range(num_cols]
			for i in range(num_rows)]

def is_diagonal(i,j):
	return 1 if i == j else 0

def all_zero:
	return 0

def get_column(A):

#vectors

def vector_add(v,w):
	return [v_i + w_i for v_i,w_i in zip(v,w)]

def vector_sum(vectors):
	result = vectors[0]
	for vector in vectors[1:]:
		result = vector_add(result,vector)
	return result

def vector_sum(vectors):
	return reduce(vector_add,vectors)

def scalar_multiply(c,v):
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	n = len(vectors)
	return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w):
	return sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
	return dot(v,v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
	return sum_of_squares(vector_substract(v,w))

def distance(v,w):
	return math.sqrt(squared_distance(v,w))

