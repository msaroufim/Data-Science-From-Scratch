def word_count_old(documents):
	return Counter(word
		for document in documents
		for word in tokenize(documents))

def wc_mapper(documents):
	for word in tokenize(document):
		yield(word,1)

def wc_reducer(word,counts):
	yield (word, sum(counts))


def word_count(documents):

	collector = defaultdict(list)

	for document in documents:
		for word, count in wc_mapper(document):
			collector[word].append(count)

	return [output
			for word, counts in collector.iteritems()
			for output in wc_reducer(word,counts)]

def map_reduce(inputs,mapper,reducer):
	collector = defaultdict(list)

	for input in inputs:
		for key, value in mapper(input):
			collector[key].append(value)
	return [output
			for key, values in collector.iteritems()
			for output in reducer(key,values)]

word_counts = map_reduce(documents,wc_mapper,wc_reducer)

def reduce_values_using(aggregation_fn, key, values):
	yield (key,aggregation_fn(values))

def values_reducer(aggregation_fn):
	return partial(reduce_values_using, aggregation_fn)

sum_reducer = values_reducer(sum)
max_reducer = values_reducer(max)
min_reducer = values_reducer(min)
count_distinct_reducer = values_reducer(lambda values: len(set(values)))




def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc