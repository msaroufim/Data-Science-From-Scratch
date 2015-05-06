def de_mean_matrix(A):
	nr,nc = shape(A)
	columns_means,_ = scale(A)
	return make_matrix(nc,nr,lambda i,j : A[i][j] - columns_means[j])


def direction(w):
	mag = magnitude(w)
	return [w_i / mag for w_i in w]

def directional_variance_i(x_i,w):
	"""
	Variance of row x_i in direction w
	"""
	return dot(x_i,direction(w))**2

def directional_variance(X,w):
	return sum(directional_variance_i(x_i,w) for x_i in X)


def directional_variance_gradient_i(x_i,w):
	projection_length = dot(x_i,direction(w))
	return [2 * projection_length * x_ij for x_ij in x_i]

def directional_variance_gradient(X,w):
	return vector_sum(directional_variance_gradient_i(x_i,w) for x_i in X)

def first_principal_component_sgd(X):
	guess = [1 for _ in X[0]]
	unscaled_maximizer = maximize_stochastic(
		lambda x, _ , w : directional_variance_i(x,w),
		lambda x, _ , w : directional_variance_gradient_i(x,w)
		X,
		[None for _ in X],
		guess)
		return direction(unscaled_maximizer)	