"""
Created on Thu Nov 26 21:58:47 2026

@author: wei-chieh Su
"""
import numpy
print("File I/O Lesson 3 — NumPy Data Loading")
#data = numpy.loadtxt("dos_example.dat")
data = numpy.loadtxt("dos_example.dat",skiprows=1)
print(data)
energy = data[:,0]
print(energy)
dos = data[:,1]
print(dos)
max_dos = numpy.max(dos)
print("max dos = ",max_dos)
min_dos = numpy.min(dos)
print("min dos = ",min_dos)
numpy.savetxt("dos_result.dat", dos,fmt="%.2f")

# Practice 03 — Phonon DOS Data Analysis
print("Practice 03 — Phonon DOS Data Analysis")
ph_data = numpy.loadtxt("phonon_dos_practice.dat",skiprows=1)
print(ph_data,"Shape: ",ph_data.shape)
Frequency = data[:,0]
print("Frequency: ",Frequency)
Phonon_DOS = data[:,1]
print("Phonon DOS: ",Phonon_DOS)
Maximum_phonon_DOS = numpy.max(Phonon_DOS)
print("Maximum phonon DOS",Maximum_phonon_DOS)
Average_phonon_DOS = numpy.mean(Phonon_DOS)
print("Average phonon DOS",Maximum_phonon_DOS)
a = Frequency >= 3
Selected_frequencies = Frequency[a]
print("Selected frequencies",Selected_frequencies)
numpy.savetxt("selected_frequency.dat", Selected_frequencies,fmt="%.2f") %runfile 'C:/Users/wei-chieh Su/Downloads/file_test.py' --wdir
File I/O Lesson 3 — NumPy Data Loading
[[-3.   0.5]
 [-2.   1.2]
 [-1.   2. ]
 [ 0.   2.8]
 [ 1.   1.9]
 [ 2.   1.1]
 [ 3.   0.4]]
[-3. -2. -1.  0.  1.  2.  3.]
[0.5 1.2 2.  2.8 1.9 1.1 0.4]
max dos =  2.8
min dos =  0.4
Practice 03 — Phonon DOS Data Analysis
[[0.  0. ]
 [1.  0.4]
 [2.  1.2]
 [3.  2.5]
 [4.  3. ]
 [5.  1.8]
 [6.  0.6]] Shape:  (7, 2)
Frequency:  [-3. -2. -1.  0.  1.  2.  3.]
Phonon DOS:  [0.5 1.2 2.  2.8 1.9 1.1 0.4]
Maximum phonon DOS 2.8
Average phonon DOS 2.8
Selected frequencies [3.]
