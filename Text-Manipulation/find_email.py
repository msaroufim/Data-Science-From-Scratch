import sys
from collections import Counter


def get_domain(email_address):
	return email_address.lower().split("@")[-1]

with open('email_addresses.txt','r') as f:
	domain_counts = Counter(get_domain(line.strip())
							for line in f
							if "@" in line)