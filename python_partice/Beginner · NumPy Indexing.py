import numpy

x = [-5.0, -3.0, -1.0, 0.0, 2.0, 4.0]

energy = numpy.array(x)

for i in range(len(energy)):
    print(energy,energy[i])
    
print(energy[-1])
print(energy[-2])
print(energy[1:4])
print(energy[2:])
print(energy[:4])
print(energy[:])

#test

print("test:")
print("First energy = ",energy[0])
print("Final energy = ",energy[-1])

y = energy[1:4]

mev = y*1000

print("selected energy = ",y)
print("Remaining energies =",energy[2:])
print("Selected energies (meV) = ",mev)

%runfile 'C:/Users/wei-chieh Su/.spyder-py3/temp.py' --wdir
[-5. -3. -1.  0.  2.  4.] -5.0
[-5. -3. -1.  0.  2.  4.] -3.0
[-5. -3. -1.  0.  2.  4.] -1.0
[-5. -3. -1.  0.  2.  4.] 0.0
[-5. -3. -1.  0.  2.  4.] 2.0
[-5. -3. -1.  0.  2.  4.] 4.0
4.0
2.0
[-3. -1.  0.]
[-1.  0.  2.  4.]
[-5. -3. -1.  0.]
[-5. -3. -1.  0.  2.  4.]
test:
First energy =  -5.0
Final energy =  4.0
selected energy =  [-3. -1.  0.]
Remaining energies = [-1.  0.  2.  4.]
Selected energies (meV) =  [-3000. -1000.     0.]
