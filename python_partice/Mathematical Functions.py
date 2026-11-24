import numpy

# Mathematical Functions

x = [1.0, 4.0, 9.0, 16.0]

y = [-5.0, -2.0, 0.0, 2.0, 5.0]

# Square root

s = numpy.sqrt(x)

print("Square root",s)

# Absolute value

ab = numpy.abs(y)

print("Absolute value",ab)

# Exponential

ex = numpy.exp(ab)

print("Exponential",ex)

# Natural logarithm

lo = numpy.log(x)

print("Natural logarithm",lo)

# thete 

the = [0,numpy.pi/2,numpy.pi]

sin_1 = numpy.sin(the)

cos_1 = numpy.cos(the)

print(sin_1)

print(cos_1)

# Practice Mathematical Functions

print("Practice Mathematical Functions")

a = [1.0, 4.0, 9.0, 16.0]

b = [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0]

c = [0,numpy.pi/2,numpy.pi]

a1 = numpy.sqrt(a)

print("Square root: ",a1)

b1 = numpy.abs(y)

print("Absolute value: ",b1)

b2 = numpy.exp(b)

print("Exponential: ",b2)

a2 = numpy.log(a)

%runfile C:/Users/user/Downloads/untitled2.py --wdir
Square root [1. 2. 3. 4.]
Absolute value [5. 2. 0. 2. 5.]
Exponential [148.4131591   7.3890561   1.          7.3890561 148.4131591]
Natural logarithm [0.         1.38629436 2.19722458 2.77258872]
[0.0000000e+00 1.0000000e+00 1.2246468e-16]
[ 1.000000e+00  6.123234e-17 -1.000000e+00]
Practice Mathematical Functions
Square root:  [1. 2. 3. 4.]
Absolute value:  [5. 2. 0. 2. 5.]
Exponential:  [ 0.04978707  0.13533528  0.36787944  1.          2.71828183  7.3890561
 20.08553692]
Natural logarithm:  [0.         1.38629436 2.19722458 2.77258872]
Sine:  [0.0000000e+00 1.0000000e+00 1.2246468e-16]
Cosine:  [ 1.000000e+00  6.123234e-17 -1.000000e+00]
