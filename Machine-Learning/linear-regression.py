def predict(alpha,beta,x_i):
	return beta * x_i + alpha

def error(alpha,beta,x_i,y_i):
	return y_i - predict(alpha,beta,x_i)

#sum of squared error makes sure that we penalize largely larger errors
def sum_of_squared_errors(alpha,beta,x,y):
	return sum(error(alpha,beta,x_i,y_i)
			   for x_i,y_i in zip(x,y))

def least_squares_fit(x,y):
	"""
	Given individual training examples
	"""
	beta  = correlation(x,y) * standard_deviation(y) / standard_deviation(x)
	alpha = mean(y) - beta * mean(x)
	return alpha,beta

alpha,beta = least_squares_fit(num_friends_good, daily_minutes_good)

#alpha = 22.95
#beta  = 0.903


#measure goodness of fit using coefficient of determination
def total_sum_of_squares(y):
	return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
	"""
	fraction of variation in y captured by model
	"""
	return 1.0 - sum(sum_of_squared_errors(alpha, beta, x, y)
					 / total_sum_of_squares(y))

#Alternatively it's possible to use gradient descent

def squared_error(x_i,y_i,theta):
	alpha, beta = theta
	return error(alpha,beta,x_i,y_i) ** 2

def squared_error_gradient(x_i, y_i, theta):
	alpha, beta = theta
	return [-2 * error(alpha, beta, x_i, y_i), #alpha partial derivative
			-2 * error(alpha,beta,x_i,y_i) * x_i] #beta partial derivative

random.seed(0)
theta =[random.random(),random.random()]
alpha, beta = minimize_stochastic(squared_error,
								  squared_error_gradient,
								  num_friends_good,
								  daily_minutes_good,
								  theta,
								  0.0001)
print alpha, beta