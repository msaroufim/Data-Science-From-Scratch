from functools import partial

def sum_of_squares(v):
	return sum(v_i ** 2 for v_i in v)


def difference_quotient(f,x,h):
	return (f(x+h) - f(x))/ h

def square(x):
	return x * x

def derivative(x):
	return 2 * x
 
derivative_estimate = partial(difference_quotient,square,h=0.00001)

# import matplotlib.pyplot as plt 
# x = range(-10,10)
# plt.title("Actual derivates vs estimates")
# plt.plot(x,map(derivative,x),'rx',label='Actual')
# plt.plot(x,map(derivative_estimate,x),'b+',label='Estimate')
# plt.plot(x,map(square,x),'g-',label='Square')
# plt.legend(loc=9)
# plt.show()

def partial_difference_quotient(f,v,i,h):
	"""
	Keep vector untouched except at relevant position
	i for the partial derivative
	"""
	w = [v_j + (h if j == i else 0)
		 for j,v_j in enumerate(v)]

	return (f(w) - f(v)) / h

"""
no difference in performance since the values
of v have to be copied into w anyway
"""
def partial_difference_quotient(f,v,i,h):
	for j,v_j in enumerate(v):
		if j == i:
			w.append(v_j + h)
		else:
			w.append(v_j)

	return (f(w) - f(v))/h


def estimate_gradient(f,v,h=0.00001):
	"""
	Return a vector of the partial difference quotients
	"""
	return [partial_difference_quotient(f,v,i,h)
			for i, _ in enumerate(v)]




def step(self,v,direction,step_size):
	return [v_i + step_size * direction_i
			for v_i,direction in zip(v,direction)]

def sum_of_squares_gradient(v):
	return [2 * v_i for v_i in v]

def solve(tolerance=0.00001):
	#pick a random starting point
	v = [random.randint(-10,10) for i in range(3)]
	while True:
		gradient = sum_of_squares_gradient(v)
		next_v   = step(v,gradient,-0.01)
		if distance(next_v,v) < tolerance:
			break
		v = next_v

def safe(f):
	"""
	returns same function as f except that it uses
	infinity instead of an error
	"""
	def safe_f(*args,**kwargs):
		try:
			return f(*args,**kwargs)
		except:
			return float('inf')
	return safe_f

def minimize_batch(target_fn,gradient_fn,theta_0,tolerance = 0.00001):
	step_sizes = [100,10,1,0.1,0.01,0.001.0.0001]
	theta      = theta_0
	target_fn  = safe(target_fn)
	value      = target_fn(theta)
	while True:
		gradient    = gradient_fn(theta)
		next_thetas = [step(theta,gradient,-step_size) for step_size in 			   step_sizes]
		next_thetas = min(next_thetas,key=target_fn)
		next_value  = target_fn(next)

		if abs(value - next_value) < tolerance:
			return theta
		else:
			theta, value = next_theta, next_value

def negate(f):
	return lambda *args,**kwargs: -f(*args,**kwargs)

def negate_all(f):
	return lambda *args, **kwargs: [-y for y in f(*args,**kwargs)]

def maximize_batch(target_fn,gradient_fn,theta_0,tolerance=0.00001):
	return minimize_batch(negate(target_fn),
						  negate_all(gradient_fn),
						  theta_0,
						  tolerance)

def in_random_order(data):
	indexes = [i for i,_ in enumerate(data)] #create a list of indexes
	random.shuffle(indexes)
	for i in indexes:
		yield data[i]

def minimize_stochastic(target_fn,gradient_fn,x,y,theta_0,alpha_0=0.01):
	data = zip(x,y)
	theta = theta_0 #initial guess
	alpha = alpha_0 #initial step size
	min_theta, min_value = None, float("inf")
	iterations_with_no_improvement = 0

	while iterations_with_no_improvement < 100:
		value = sum(target_fn(x_i,y_i,theta) for x_i,y_i in data)
		"""
		change learning rate to intial learning rate if 
		improvement is made
		"""
		if value < min_value:
			min_theta ,min_value = theta,value
			iterations_with_no_improvement = 0
			alpha = alpha_0
		else:
			iterations_with_no_improvement += 1
			alpha = 0.9

		for x_i,y_i in in_random_order(data):
			gradient_i = gradient_fn(x_i,y_i,theta)
			theta      = vector_substract(theta,scalar_multiply(alpha,gradient_i)) 

		return min_theta

def maximize_stochastic(target_fn,gradient_fn,x,y,theta_0,alpha_0=0.01):
	return minimize_stochastic(negate(target_fn),
							   negate_all(gradient_fn),
							   x,y,theta_0,alpha_0)

