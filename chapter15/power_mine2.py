L = [2 ** i for i in range(7)]
X = 5
	
try:
	idx = L.index(2 ** X)
	print('at index', idx)
except ValueError:
	print(X, 'not found')