import numpy

x = [1,2],[3,4]

y = [4,5],[6,7]

h = [2,1+2j],[1-2j,3]

A = numpy.array(x)

B = numpy.array(y)

H = numpy.array(h)

C = A @ B

HC = numpy.conjugate(H)

HD = numpy.conjugate(H).T

check = numpy.allclose(HD, H)

HT = (A+numpy.conjugate(A).T)/2

ev,ef = numpy.linalg.eigh(H)

E = ef[:,1]

D = numpy.diag(ev)

D_test = ef.T@H@ef

A_inv = numpy.linalg.inv(A)

I = A@A_inv

g = numpy.linalg.solve(A, B)

print(D)
print(D_test)

print(C)

AT = A.T
