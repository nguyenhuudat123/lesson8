para_ = input('nha[ 1 cau tu ban phim')

k = 0
max_ = 0
ele_max = ''
for i in range(len(para_)):
	if para_[i] != ' ':
		k += 1
	else:
		if k >= max_:
			max_ = k
			ele_max = i
			k = 0
print(max_)
print('tu dai nhat la:', para_[ele_max - max_: ele_max]) # tis hoi