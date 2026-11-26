import numpy

print("Beginner — Comprehensive Review")

def main():
    x = [-2.0, -0.5, 0.0, 1.5, 2.0, 3.5, 5.0, 6.0]
    frequency = numpy.array(x)
    positive, negitive,averge_positive,max_f = analyze_phonon(frequency)
    print("Phonon frequencies: ",frequency)
    print("Negative frequencies: ",negitive)
    print("Positive frequencies: ",positive)
    print("Average positive frequency: ",averge_positive,"THz")
    print("Maximum frequency: ",max_f,"THz")
    
    n_n = 0;  n_z = 0; n_p = 0
    n_n,n_p,n_z = count_phonon(frequency,n_n,n_p,n_z)
    print("Number of negative frequencies: ",n_n)
    print("Number of zero frequencies: ",n_z)
    print("Number of positive frequencies: ",n_p)
    
    s_f = select_phonon(frequency)
    print("Selected frequencies:",s_f)
    
def analyze_phonon(frequency):
    a = frequency > 0
    positive = frequency[a]
    b = frequency < 0
    negitive = frequency[b]
    averge_positive = numpy.mean(positive)
    max_f = numpy.max(positive)
    return positive, negitive,averge_positive,max_f

def count_phonon(frequency,n_n,n_p,n_z):
    for i in range(len(frequency)):
        if frequency[i] > 0:
            n_p = n_p + 1
        elif frequency[i] == 0:
            n_z = n_z + 1
        else:
            n_n = n_n + 1
    return n_n,n_p,n_z

def select_phonon(frequency):
    while True:
        ft = float(input("nter a positive frequency threshold (THz): "))
        if ft < 0:
            print("Invalid threshold")
            continue
        elif ft == 0:
            print("Invalid threshold")
            continue
        else:
            a = frequency >= ft
            s_f = frequency[a]
            return s_f
            break

main() 

%runfile 'C:/Users/wei-chieh Su/.spyder-py3/temp.py' --wdir
Beginner — Comprehensive Review
Phonon frequencies:  [-2.  -0.5  0.   1.5  2.   3.5  5.   6. ]
Negative frequencies:  [-2.  -0.5]
Positive frequencies:  [1.5 2.  3.5 5.  6. ]
Average positive frequency:  3.6 THz
Maximum frequency:  6.0 THz
Number of negative frequencies:  2
Number of zero frequencies:  1
Number of positive frequencies:  5
nter a positive frequency threshold (THz): 3
Selected frequencies: [3.5 5.  6. ]

%runfile 'C:/Users/wei-chieh Su/.spyder-py3/temp.py' --wdir
Beginner — Comprehensive Review
Phonon frequencies:  [-2.  -0.5  0.   1.5  2.   3.5  5.   6. ]
Negative frequencies:  [-2.  -0.5]
Positive frequencies:  [1.5 2.  3.5 5.  6. ]
Average positive frequency:  3.6 THz
Maximum frequency:  6.0 THz
Number of negative frequencies:  2
Number of zero frequencies:  1
Number of positive frequencies:  5
nter a positive frequency threshold (THz): 6
Selected frequencies: [6.]
