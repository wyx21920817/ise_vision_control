#
# zeros.py - creating and resizing an array 
#
import numpy as np
print('\nZERO ARRAY\n') 
zeroarray = np.zeros((3,3,3))

# update values here

print('Zero array size: ', np.size(zeroarray)) 
print('Zero array shape: ', np.shape(zeroarray), '\n')
zeroarray[0][0] = [0,0,2]
zeroarray[1][0] = [1,1,1]
zeroarray[2][0] = [2,2,0]
print(zeroarray[0][0])
print(zeroarray)

zeroarray.resize((1,27))
print('\nZero array size: ', np.size(zeroarray)) 
print('Zero array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)

zeroarray.resize((3,9))
print('\nZero array size: ', np.size(zeroarray)) 
print('Zero array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)