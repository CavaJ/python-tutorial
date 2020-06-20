y = input("Enter integer:")
y = int(y) # convert to integer

x = y // 2

while x > 1:
	if y % x == 0: 
		print("%s has a factor %s" % (y, x))
		break
	x -= 1
else:
	print("%s is prime" % y)