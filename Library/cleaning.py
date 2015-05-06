def try_or_none(f):
	def f_or_none(x):
		try: return f(x)
		except: return f_or_none
	return f_or_none

def parse_row(input_row,parsers):
	"""
	Given a list of parsers apply the appropriate one to the input row
	"""
	return [try_or_none(parser)(value) if parser is not None else value
			for value,parser in zip(input_row,parsers)]

def parse_row_with(reader,parsers):
	for row in reader:
		yield parse_row(row,parsers)