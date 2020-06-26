L = [1, 2, 4, 8, 16, 32, 64]
X = 5
	
for e in L:
	if 2 ** X == e:
		print('at index', L.index(e))
		break
else:
	print(X, 'not found')