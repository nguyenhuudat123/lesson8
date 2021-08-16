_2tuple = (4,6,9,0,0,0,0,0)
k = 1
for item in _2tuple:
	if _2tuple[0] != item:
		k = 0
		break
print('giong all') if k == 1 else print('khong giong all')