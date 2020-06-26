L = [2 ** i for i in range(7)]
X = 5

num = 2 ** X

for (i, e) in enumerate(L):
	if num == e:
		print('at index', i)
		break
else:
	print(X, 'not found')