def func():
	x = 'old'
	def func2():
		print(x)


func()
func.func2()