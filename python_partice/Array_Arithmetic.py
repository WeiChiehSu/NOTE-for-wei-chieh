import numpy

a = [1,2,3,4,5]
b = [6,9,4,7,3]
c = [0,0,0,0,0]

a_1 = numpy.array(a)
b_1 = numpy.array(b)

print(a_1+b_1)
print(a_1-b_1)
print(a_1*b_1)
print(a_1/b_1)
print(a_1%b_1)
print(a_1**2)

# Kinetic energy test

for i in range(len(a)):
    c[i]= a[i]+b[i]
print(c)

velocity = [1.0, 2.0, 3.0, 4.0]

v = numpy.array(velocity)
k = 0.5*0.2*(v**2)

print(f"Velocity (m/s):{v}")
print(f"Kinetic energy (J): {k}")

%runfile C:/Users/user/Downloads/untitled2.py --wdir
[ 7 11  7 11  8]
[-5 -7 -1 -3  2]
[ 6 18 12 28 15]
[0.16666667 0.22222222 0.75       0.57142857 1.66666667]
[1 2 3 4 2]
[ 1  4  9 16 25]
[7, 11, 7, 11, 8]
Velocity (m/s):[1. 2. 3. 4.]
Kinetic energy (J): [0.1 0.4 0.9 1.6]
