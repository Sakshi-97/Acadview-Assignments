# Q.1 - Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the
# elements using basic numpy functions.
import numpy
x = numpy.random.rand(10,1)
m = numpy.mean(x)
print x
print("mean of the above numbers is: ",m)

#Q.2 - Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard
#  deviation of the elements.
import numpy
a = numpy.random.rand(20,1)
b = numpy.std(a)
c = numpy.var(a)
print(a)
print("standard deviation  of above elements is: ",b)
print("varience  of above elements is: ",c)

#Q.3 - Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the
#  matrix multiplication of A and B. The shape of the new matrix should be (10,25). Using basic numpy math functions
#  only find the sum of all the elements of the new matrix.
import numpy
x = numpy.random.rand(10,20)
print("array A is: ",x)
y = numpy.random.rand(20,25)
print("array B is: ",y)
z = numpy.matmul(x,y)
print("the multiplication of array is :",z)
s = z.sum()
print(s)
