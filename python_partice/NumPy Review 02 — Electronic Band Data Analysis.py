import numpy

print("NumPy Review 02 — Electronic Band Data Analysis")

x = [[-4.0, -1.0, 1.0, 3.0],[-3.0, -0.5, 2.0, 4.0],[-2.0,  0.0, 2.5, 5.0]]

energy = numpy.array(x)

print("Energy array:",energy)

print("Shape: ",numpy.shape(energy))

print("Second k-point: ",energy[1,:])

print("Third band: ",energy[:,2])

print("Average energy of third band: ",numpy.mean(energy[:,2]),"ev")

a = energy >= -1; b = energy <= 1; c = energy < 0;

print("Negative energies: ",energy[c])

print("Selected energies: ",energy[a & b])

print("Maximum energy: ",numpy.max(energy),"ev","Minimum energy: ",numpy.min(energy),"eV")

print("Third band (meV):",1000*energy[:,2])

%runfile C:/Users/user/Downloads/untitled2.py --wdir
NumPy Review 02 — Electronic Band Data Analysis
Energy array: [[-4.  -1.   1.   3. ]
 [-3.  -0.5  2.   4. ]
 [-2.   0.   2.5  5. ]]
Shape:  (3, 4)
Second k-point:  [-3.  -0.5  2.   4. ]
Third band:  [1.  2.  2.5]
Average energy of third band:  1.8333333333333333 ev
Negative energies:  [-4.  -1.  -3.  -0.5 -2. ]
Selected energies:  [-1.   1.  -0.5  0. ]
Maximum energy:  5.0 ev Minimum energy:  -4.0 eV
Third band (meV): [1000. 2000. 2500.]
