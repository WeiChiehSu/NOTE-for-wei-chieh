import numpy

# Two-Dimensional Arrays

print("Two-Dimensional Arrays TEST : ")

x = [1.0, 2.0, 3.0],[4.0, 5.0, 6.0]

matrix = numpy.array(x)

print(matrix)

big = matrix.shape

print(big)

zz = matrix[0,0]

print(zz)

zt = matrix[0,2]

print(zt)

oo = matrix[1,1]

print(oo)

row = matrix[0,:]

print(row)

column = matrix[:,1]

print(column)

# 2D Energy Array

print("2D Energy Array:")

y = [-4.0, -2.0, 0.0],[1.0, 3.0, 5.0],[2.0, 4.0, 6.0]

test = numpy.array(y)

shape_test = test.shape

print("Shape: ",shape_test)

first_row = test[0,:]

print("first_row: ",first_row)

second_column = test[:,1]

print("second_column",second_column)

row3column2 = test[2,1]

print("Selected element:",row3column2)

arr = numpy.mean(test)

print("Average energy: ",arr)

%runfile C:/Users/user/Downloads/untitled2.py --wdir
Two-Dimensional Arrays TEST : 
[[1. 2. 3.]
 [4. 5. 6.]]
(2, 3)
1.0
3.0
5.0
[1. 2. 3.]
[2. 5.]
2D Energy Array:
Shape:  (3, 3)
first_row:  [-4. -2.  0.]
second_column [-2.  3.  4.]
Selected element: 4.0
Average energy:  1.6666666666666667
