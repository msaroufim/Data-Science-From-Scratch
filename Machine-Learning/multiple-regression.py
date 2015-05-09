def predict(x_i,beta):
	return dot(x_i,beta)

#least squares assumes that columns of x are linearly independent
#there is no true model if this assumption is violated
#none of the colums are correlated with the noise

def error(x_i,y_i,beta):
	return y_i - predict(x_i,beta)

def squared_error(x_i,y_i,beta):
	return error(x_i,y_i,beta) ** 2

def squared_error_gradient(x_i,y_i,beta):
	return [-2 * x_ij * error(x_i,y_i,beta)
			for x_ij in x_i]

def estimate_beta(x,y):
	beta_initial = [random.random() for x_i in x[0]]
	return minimize_stochastic(squared_error,
								squared_error_gradient,
								x,y_i
								beta_initial,
								0.0001)

random.seed(0)
beta = estimate_beta(x,daily_minutes_good)

#With this approach it is very simple to add new features

#tells you 
def multiple_r_squared(x,y,beta):
	sum_of_squared_errors = sum(error(x_i,y_i,beta) ** 2
								for x_i,y_i in zip(x,y))
	return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)

#errors are independent normal random variables with mean 0 and some shared 
#standard deviation sigma



#Regularization

def ridge_penalty(x_i,y_i,beta,alpha):
	return alpha * dot(beta[1:], beta[1:])

def squared_error_ridge(x_i,y_i,beta,alpha):
	return error(x_i,y_i,beta) ** 2 + ridge_penalty(beta,alpha)

def ridge_penalty_gradient(beta,alpha):
	return [0] + [2*alpha * beta_j for beta_j in beta[1:]]

def squared_error_ridge_gradient(x_i,y_i,beta,alpha):
	return vector_add(squared_error_gradient(x_i,y_i,beta),
					  ridge_penalty_gradient(beta,alpha))

def estimate_beta_ridge(x,y,alpha):
	beta_initial = [random.random() for x_i in x[0]]
	return minimize_stochastic(partial(squared_error_ridge,alpha=alpha),
							   partial(squared_error_ridge_gradient,
							   alpha=alpha),
							   x,y
							   beta_initial,
							   0.001)

def lasso_penalty(beta,alpha):
	return alpha * sum(abs(beta_i) for beta_i in beta[1:])


	