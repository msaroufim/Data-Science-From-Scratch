import json

serialized = """ {
	"title": "Data Science Book",
	"author": "Joel Grus",
	"publicationYear":"2014",
	"topics":["data","science","data science"]
}
"""

deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
	print deserialized