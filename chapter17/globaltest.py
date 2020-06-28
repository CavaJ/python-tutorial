#x = 'old'
#print(x)

def func():
	global x; x = 'new'
	print(x)

func()
print(x)