lst = [(1,2,3), (3,4,5), (345,34,233,4), (-3,3,5)]
min_ = lst[0]
for item in lst:
	if item[1] <= min_[1]:
		min_ = item
print(min_)