for i in range(10):
	print("Hi, python")

import numpy as np

list = [1, 2, 3]
print(list)
print(type(list))
nplist = np.asarray(list)
print(nplist)
print(type(nplist))
print(nplist.shape)


import test2
test2._pycache_test() #bytecode file of test2.py is only updated when source code of test2.py is updated, not the other scripts

#print("bytecode file is not updated in _pycache_ folder since test2.py source code is not updated")