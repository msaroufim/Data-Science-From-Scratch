#scale.py
import sys

sys.path.insert(0,'../Library')


def scale(data_matrix):
	num_rows,num_cols = shape(data_matrix)
	means  = [mean(get_column(data_matrix,j)) for j in range(num_cols)]
	stdevs = [standard_deviation(get_column(data_matrix,j)) for j in range(num_cols)]
	return means,stdevs

def rescale(data_matrix):
	means,stdevs = scale(data_matrix)

	def rescaled(i,j):
		if stdevs[j] > 0:
			return (data_matrix[i][j] - means[j]) / stdevs[j]
		else:
			return data_matrix[i][j]

	num_rows,num_cols = shape(data_matrix)
	return make_matrix(num_rows,num_cols,rescaled)