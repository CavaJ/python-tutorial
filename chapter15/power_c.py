L = [1, 2, 4, 8, 16, 32, 64]
X = 5


num = 2 ** X

if num in L:
	print('at index', L.index(num))
else:
	print(X, 'not found')