L = [2 ** i for i in range(7)]
X = 5

num = 2 ** X

for e in L:
	if num == e:
		print('at index', L.index(e))
		break
else:
	print(X, 'not found')