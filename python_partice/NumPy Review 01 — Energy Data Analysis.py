import numpy

# NumPy Review 01 — Energy Data Analysis

print("NumPy Review 01 — Energy Data Analysis")

x = numpy.linspace(-5, 5, 21)

print("energy grid: ",x)

x_high = x > 0; x_high_value = x[x_high]

print("Positive energies:",x_high_value)

x_less = x < 0; x_less_value = x[x_less]

print("Negative energies:",x_less_value)

a = x >= -1; b = x <= 1; x_mid = x[a & b]

print("Selected energies:",x_mid)

arr_less = numpy.mean(x_less_value)

print("Average negative energy: ",arr_less,"eV")

max_o = numpy.max(x); min_o = numpy.min(x)

print("Maximum energy: ",max_o,"eV ;","Minimum energy: ",min_o,"eV")

mev = x_mid*1000

print("Selected energies (meV):",mev)

%runfile C:/Users/user/Downloads/untitled2.py --wdir
NumPy Review 01 — Energy Data Analysis
energy grid:  [-5.  -4.5 -4.  -3.5 -3.  -2.5 -2.  -1.5 -1.  -0.5  0.   0.5  1.   1.5
  2.   2.5  3.   3.5  4.   4.5  5. ]
Positive energies: [0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5. ]
Negative energies: [-5.  -4.5 -4.  -3.5 -3.  -2.5 -2.  -1.5 -1.  -0.5]
Selected energies: [-1.  -0.5  0.   0.5  1. ]
Average negative energy:  -2.75 eV
Maximum energy:  5.0 eV ; Minimum energy:  -5.0 eV
Selected energies (meV): [-1000.  -500.     0.   500.  1000.]
