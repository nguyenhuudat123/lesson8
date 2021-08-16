#in ra đuôi domain

lst = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
for item in lst:
	element_ = 0
	while item[element_] != '.':
		element_ -= 1
	print(item[element_:])