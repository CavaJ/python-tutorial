L = [1, 2, 4, 8, 16, 32, 64]
X = 5

num = 2 ** X

for e in L:
	if num == e:
		print('at index', L.index(e))
		break
else:
	print(X, 'not found')