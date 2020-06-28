var = 99

def local():
	var = 0 
	#print("in local()")
	
def glob1():
	global var 
	var += 1
	#print("in glob1()")

def glob2():
	var = 0
	import thismod
	thismod.var +=1
	#print("in glob2()")
	
def glob3():
	var = 0
	import sys
	glob = sys.modules['thismod']
	glob.var += 1
	#print("in glob3()")


def test():
	print(var)
	local(); glob1(); glob2(); glob3()
	print(var)



#test()