lst = [1,2,3,4,5,{1,2,3}, 'a,b', 'a', (1,2,3), [23,3]]

count_ = 0
while type(lst[count_]) != tuple:
	count_ += 1
print('dem duoc', count_ + 1, 'phan tu cho den tuple')