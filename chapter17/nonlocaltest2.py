def func():
	x = 'old'
	print(x)
	def func2():
		#print(x)
		#nonlocal x; 
		x = 'new'
		print(x)
	
	func2()
	print(x)


func()

#func().func2() does not work => since func2 behaves like a local variable
#import nonlocaltest2.func => does not work as well