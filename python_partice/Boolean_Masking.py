import numpy

# Boolean Masking

x = [-5,-3,-1,0,2,4]

total = 0

n = 0

energy = numpy.array(x)

a = energy < 0

ne = energy[a]

arravge = numpy.mean(ne)

b = energy >=-2

c= energy <= 2

s = energy[b & c]

print("Boolean Masking test")

print(a)

print(ne)

print("Average negative energy:",arravge)

print(s)

# if test 

print("if test")

for i in range(len(x)):
    if x[i] < 0 :
        total = total + x[i]
        n = n + 1
        print("TRUE")
    else:
        print("FALSE")
        
ar = total/n

print("Average negative energy:",ar)


# Practice 06: Energy Filtering

print("Practice : Energy Filtering")

x_1 = [-6.0, -4.0, -2.0, 0.0, 1.0, 3.0, 5.0]

energy_1 = numpy.array(x_1)

a_1 = energy_1 > 0

po = energy_1[a_1]

a_2 = energy_1 < 0

ne_1 = energy_1[a_2]

arr1 = numpy.mean(ne_1)

a_3 = energy_1 <= 3

a_4 = energy_1 >= -2

range1 = energy_1[a_3 & a_4]

print("Negative energy: ",ne_1)

print("Positive energy: ",po)

print("Selected energy: ",range1)

print("Average negative energy:",arr1,"ev")

%runfile C:/Users/user/Downloads/untitled2.py --wdir
Boolean Masking test
[ True  True  True False False False]
[-5 -3 -1]
Average negative energy: -3.0
[-1  0  2]
if test
TRUE
TRUE
TRUE
FALSE
FALSE
FALSE
Average negative energy: -3.0
Practice : Energy Filtering
Negative energy:  [-6. -4. -2.]
Positive energy:  [1. 3. 5.]
Selected energy:  [-2.  0.  1.  3.]
Average negative energy: -4.0 ev
