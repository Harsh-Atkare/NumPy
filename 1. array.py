import numpy as np
print(np.__version__)

# array using list
a=np.array([1,2,3,4,5,5])
print(a)
print(type(a)) #ndarray

# array using tuple
b= np.array((1,2,1,3,4,4,5))
print(b)
print(type(b))

# 0D array
c=np.array(5)
print(c)
print(type(c))

# 2D array
e=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(e[0][2])

# 3D array
f=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(f)
# check dimension of array
print(f.ndim)

a=np.array([1,2,3,4,5,5])
print(a[1]+a[4])

g=np.array([1,2,3,4,5,6,7,8,0])
print(g[1:4])
print(g[1:8:2])
print(g[:2])
print(g[-1:])


h=np.array([1,2,3,4,5,6,7,8,0])
print(h[-3:-1])

print(h[::2]) #odd numbers
print(h[::3])

# slicing in 2D array
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[1,1:3])
print(a[1:3,2])

# array datatypes
