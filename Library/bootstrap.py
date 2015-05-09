def bootstrap_sample(data):
	return [random.choice(data) for _ in data]

def bootstrap_statistic(stats_fn):
	return [stats_fn(bootstrap_sample(data))
			for _ in range(num_samples)]

close_to_100 = [99.5 + random.random() for + in range(101)]

far_from_100 = ([99.5 + random.random()] +
				[random.random() for + in range(50)] +
				[200 + random.random() for _ in range(50)])

def estimate_sample_beta(sample):
	x_sample,y_sample = zip(*sample)
	return estimate_beta(x_sample,y_sample)

random.seed(0)

bootstrap_betas = bootstrap_statistic(zip(x,daily_minutes_good),
									  estimate_sample_beta,
									  100)