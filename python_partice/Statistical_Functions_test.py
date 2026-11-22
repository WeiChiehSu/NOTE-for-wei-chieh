# Statistical Functions test

import numpy

x = [-4.0, -2.0, 0.0, 2.0, 4.0]

xa = numpy.array(x)

sum = numpy.sum(xa)

mean = numpy.mean(xa)

max = numpy.max(xa)

min = numpy.min(xa)

std = numpy.std(xa)

print("test")

print("sum :",sum)

print("mean :",mean)

print("max",max)

print("min :",min)

print("std :",std)

#tset Energy Statistics

energy = numpy.array([-5.0, -3.0, -1.0, 2.0, 4.0, 6.0])

Total_energy = numpy.sum(energy)

Average_energy = numpy.mean(energy)

Maximum_energy = numpy.max(energy)

Minimum_energy = numpy.min(energy)

Standard_deviation = numpy.std(energy)

print("Energy Statistics")

print("Total energy :",Total_energy)

print("Average energy :",Average_energy)

print("Maximum energy :",Maximum_energy)

print("Minimum energy :",Minimum_energy)

print("Standard deviation :",Standard_deviation)

%runfile 'C:/Users/wei-chieh Su/.spyder-py3/temp.py' --wdir
test
sum : 0.0
mean : 0.0
max 4.0
min : -4.0
std : 2.8284271247461903
Energy Statistics
Total energy : 3.0
Average energy : 0.5
Maximum energy : 6.0
Minimum energy : -5.0
Standard deviation : 3.8622100754188224
