L = []
for i in range(7): L.append(2 ** i)
X = 5


num = 2 ** X

if num in L:
	print('at index', L.index(num))
else:
	print(X, 'not found')