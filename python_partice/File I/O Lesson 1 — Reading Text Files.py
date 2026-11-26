file = open("nb_report.txt","r")

data = file.readlines()

print(data)

print(data[0])
print(data[1])
print(data[-1])

p = data[0:2]

print(data[1:-1])

print(len(data))

for i in range(len(data)):
    print(data[i])

file.close()

# test

print("test")

file_2 = open("phonon_report.txt","r")

data_2_1 = file_2.read()
file_2.seek(0)
data_2_2 = file_2.readlines()
file_2.close()

print(data_2_2)
print("First line: ",data_2_2[0])
print("Last line: ",data_2_2[-1])
print("Number of lines: ",len(data_2_2))

for i in range(len(data_2_2)):
    print(data_2_2[i])  %runfile 'C:/Users/wei-chieh Su/Downloads/file_test.py' --wdir
['Material: Nb\n', 'Method: DFPT\n', 'Electron-phonon coupling: 0.90\n', 'Logarithmic phonon frequency: 180.0 K\n', 'Critical temperature: 10.54 K\n']
Material: Nb

Method: DFPT

Critical temperature: 10.54 K

['Method: DFPT\n', 'Electron-phonon coupling: 0.90\n', 'Logarithmic phonon frequency: 180.0 K\n']
5
Material: Nb

Method: DFPT

Electron-phonon coupling: 0.90

Logarithmic phonon frequency: 180.0 K

Critical temperature: 10.54 K

test
['Material: Nb\n', 'Calculation: Phonon\n', 'Frequency unit: THz\n', 'Minimum frequency: -0.5\n', 'Maximum frequency: 6.0\n']
First line:  Material: Nb

Last line:  Maximum frequency: 6.0

Number of lines:  5
Material: Nb

Calculation: Phonon

Frequency unit: THz

Minimum frequency: -0.5

Maximum frequency: 6.0 
