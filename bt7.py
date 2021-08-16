_1tuple = (1,2,3,4,5,6,7,8,9,0)
_2tuple = (4,6,9,0,0,0,0,0)
k = 0
for item in _1tuple:
	if item in _2tuple:
		k = 1
		break
print('co phan tu trung nhau') if k == 1 else print('k trung nhau')