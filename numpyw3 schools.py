import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

print(np.__version__)
print (type(arr))
# 0-d array
#Create a 0-D array with value 42
a=np.array(42)
print(a)

'''1-D Arrays
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.'''
#Create a 1-D array containing the values 1,2,3,4,5:
arr=np.array([1,2,3,4,5])
print(arr)

'''2-D Arrays

An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.'''


#Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

a=np.array([[1,2,3],[4,5,6]])
print("yE HAI 2-D ARRAY \n",a)


'''3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.'''

#Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
td=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print("yE HAI 3-D ARRAY \n",td)

'''Check Number of Dimensions?'''
print(arr.ndim)
print(a.ndim)
print(td.ndim)


'''Higher Dimensional Arrays
An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.

Example
Create an array with 5 dimensions and verify that it has 5 dimensions:'''
nd=np.array([1,2,3,4], ndmin=5)
print("ye ahi 5 dinmensions array \n",nd)\





##CHANGING DATATYPE


arrr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i8')

print(newarr)
print(newarr.dtype)
        



