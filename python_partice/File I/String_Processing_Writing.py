import numpy

file = open("nb_report.txt","r")
data = file.readlines()
file.close()
print("File I/O Lesson 2 — String Processing & Writing")
# strip() 
print(data)
for i in range(len(data)):
    line = data[i].strip()
    print(line)
# split()
x = "Electron-phonon coupling: 0.90"
y = x.split(":")
print(y)
value = y[1]
ep = float(value)
print(ep)
x_1 = "180.0 K"
y_1 = x_1.split()
print(y_1)
# write()
file_1 = open("result.txt","w")
file_1.close()

# my_test
test= open("nb_report.txt","r")
re = open("my_test.txt","w")
for i in range(2):
    test.readline()
infor = test.readlines()
value_2 = []
value_3 = {}
value_4 = [0,0,0]
test.close()
for i in range(len(infor)):
    split_1 = infor[i].strip().split(":")
    value_1 = split_1[1].split()
    name = split_1[0]
    print(value_1[0])
    good = float(value_1[0])
    value_2.append(good)
    value_3[name] = good
    value_4[i] = good
    re.write(f"{good}\n")
re.close()

# GPT_test

pd = open("phonon_report.txt","r")
data_pd = pd.readlines()
pd.close()
data_pd_value = data_pd[-2:]
data_pd_value_min = data_pd_value[0].strip().split(":")
data_pd_value_min_value = float(data_pd_value_min[1])
print("Minimum frequency: ",data_pd_value_min_value)
data_pd_value_max = data_pd_value[1].strip().split(":")
data_pd_value_max_value = float(data_pd_value_max[1])
print("Maximum frequency: ",data_pd_value_max_value)
Frequency_difference = numpy.abs(data_pd_value_max_value-data_pd_value_min_value)
print("Frequency difference: ",Frequency_difference)

phonon_result_txt = open("phonon_result.txt","w")
phonon_result_txt.write(f"Minimum frequency: {data_pd_value_min_value}\n")
phonon_result_txt.write(f"Maximum frequency: {data_pd_value_max_value}\n")
phonon_result_txt.write(f"Frequency difference: {Frequency_difference}\n")
phonon_result_txt.close()
 %runfile 'C:/Users/wei-chieh Su/Downloads/file_test.py' --wdir
File I/O Lesson 2 — String Processing & Writing
['Material: Nb\n', 'Method: DFPT\n', 'Electron-phonon coupling: 0.90\n', 'Logarithmic phonon frequency: 180.0 K\n', 'Critical temperature: 10.54 K\n']
Material: Nb
Method: DFPT
Electron-phonon coupling: 0.90
Logarithmic phonon frequency: 180.0 K
Critical temperature: 10.54 K
['Electron-phonon coupling', ' 0.90']
0.9
['180.0', 'K']
0.90
180.0
10.54
Minimum frequency:  -0.5
Maximum frequency:  6.0
Frequency difference:  6.5
