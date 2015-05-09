class Table:
	def __init__(self,columns):
		self.columns = columns
		self.rows    = []

	def __repr__(self):
		return str(self.columns) + "\n" + "\n".join(map(str,self.rows))


	def insert(self,row_values):
		"""
		each row is a dictionary that you append to a
		list of rows
		"""
		if len(row_values) != len(self.columns):
			raise TypeError("wrong number of elements")
		row_dict = dict(zip(self.columns,row_values))
		self.rows.append(row_dict)


#users = Table(["user_id", "name", "num_friends"])


def update(self,updates,predicate):
	"""
	updates is a dictionary that with key column index
	and a new value for key
	"""
	for row in self.rows:
		if predicate(row):
			for column, new_value in updates.iteritems():
				row[column] = new_value

#usage
#users.update({'num_friends' : 3},
#			   lambda row: row['users_id'] == 1)

def delete(self,predicate=lambda row: True):
	self.rows = [row for row in self.rows if not(predicate(row))]



def select(self,keep_columns=None, additional_columns=None):
	"""
	Additional columns is a dictionary of lambdas to compute 
	new columns
	Keep columns is a list of column indices you want to keep
	"""
	if keep_columns is None:
		keep_columns = self.columns

	if additional_columns is None:
		additional_columns = {}

	result_table = Table(keep_columns + additional_columns.keys())
	for row in self.rows:
		new_row = [row[column] for column in keep_columns]
		for column_name, calculation in additional_columns.iteritems():
			new_row.append(calculation(row))
		result_table.insert(new_row)
	return result_table

#Select user_id From Users
#users.select(keep_columns=["user_id"])


def where(self,predicate=lambda row: True):
	where_table = Table(self.columns)
	where_table.rows = filter(predicate,self.rows)
	return where_table

def limit(self,num_rows):
	"""
	Return first num_rows rows
	"""
	limit_table 	  = Table(self.columns)
	limit_table.rows  = self.rows[:num_rows]
	return limit_table

def group_by(self, group_by_columns, aggregates, having=None):
	grouped_rows = defaultdict(list)

	#populate groups
	for row in self.rows:
		key = tuple(row[column] for column in group_by_columns)
		grouped_rows[key].append(row)

	#group_by_columns and aggregates
	result_table = Table(group_by_columns + aggregates.keys())

	for key, rows in grouped_rows.iteritems():
		if having is None or having(rows):
			new_row = list(key)
			for agggregate_name, aggregate_fn in aggregates.iteritems():
				new_row.append(aggregate_fn(rows))
			result_table.insert(new_row)

	return result_table

def order_by(self,order):
	new_table = self.select()
	new_table.rows.sort(key=order)
	return new_table

def join(self,other_table,left_join=False):
	join_on_columns = [c for c in self.columns
					   if c in other_table.columns]

	additional_columns = [c for c in other_table.columns
						  if c not in join_on_columns]

	#all columns from left table + additional_columns from right table
	join_table = Table(self.columns + additional_columns)

	for row in self.rows:
		def is_join(other_row):
			return all(other_row[c] == row[c] for c in join_on_columns)

		other_rows = other_table.where(is_join).rows

		#each other row that matches this one produces a result row
		for other_row in other_rows:
			join_table.insert([row[c] for c in self.columns]
							  + [other_row[c] for c in additional_columns])

		#if no rows match and left join, output with Nones
		if left_join and not other_rows:
			join_table.insert([row[c] for c in self.columns] +
							  None for c in additional_columns)