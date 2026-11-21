import numpy

#arange test

x = numpy.arange(0,10,2)

print("arange test",x)

# for arange test

y = [0,0,0,0,0]
y_1 = -2

for i in range(len(y)):
    y_1 = y_1 + 2
    y[i] = y_1
    
print("for arange test",y)

# linspace test

x_1 = numpy.linspace(0, 10,6)
print("linspace test",x_1)

# Practice — Energy Grid Generation

arange = numpy.arange(-5,5,1)

print("arange: ",arange)

linspace = numpy.linspace(-5,5,11)

print("linspace:",linspace)

squard = linspace**2

print("Squared: ",squard)

%runfile 'C:/Users/wei-chieh Su/.spyder-py3/temp.py' --wdir
arange test [0 2 4 6 8]
for arange test [0, 2, 4, 6, 8]
linspace test [ 0.  2.  4.  6.  8. 10.]
arange:  [-5 -4 -3 -2 -1  0  1  2  3  4]
linspace: [-5. -4. -3. -2. -1.  0.  1.  2.  3.  4.  5.]
Squared:  [25. 16.  9.  4.  1.  0.  1.  4.  9. 16. 25.]
