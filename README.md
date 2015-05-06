# Data-Science-From-Scratch

##Getting Data

###Reading Files

By using stdin and stdout it's easy to create unix like utilities for text processing and pipe them into each other. For example, to count the number of lines in a file that contain numbers:

```
cat someFile.txt | python egrep.py "[0-9]" | python line_count.py 
```

###Web Scraping

Be sure you've set up a virtual environment and then just use BeautifulSoup, Requests and html5lib. Please checkout  a page's robots.txt and terms before you do something like this.

```python
source_code_of_a_webpage = BeautifulSoup(requests.get(url_of_page).text,'html5lib')
```

When you're working with json, transform your data to a dictionary and be happy

```python
import json
deserialized = json.loads(serialized_json)
```

###Twitter API

Get some credentials at https://apps.twitter.com . Please don't check in your consumer_key and secret_key in your repo.

```
Web-Scraping/twitter.py

twitter.py CONSUMER_KEY SECRET_KEY
```

##Working with data

The size of the range of a feature should not affect its predictive power so it's usually a good idea to rescale your dataset to have mean 0 and variance 1.
```python
return (data_matrix[i,j] - means[j])/stdevs[j]
```

You don't want your parser to break if some value is not expected
```python
def try_or_none(f):
    def f_or_none(x):
        try: return f(x)
        except: return f_or_none
    return f_or_none
```

