lst = [(2, 5), (4, 1), (0, 0)]
length = len(lst)
for i in range(length-1):
	for j in range(i+1,length):
		if lst[j][-1] <= lst[i][-1]:
			lst[j], lst[i] = lst[i], lst[j]
print(lst)
