# Data-Science-From-Scratch

##Reading Files

By using stdin and stdout it's easy to create unix like utilities for text processing and pipe them into each other. For example, to count the number of lines in a file that contain numbers:

```
cat someFile.txt | python egrep.py "[0-9]" | python line_count.py 
```
