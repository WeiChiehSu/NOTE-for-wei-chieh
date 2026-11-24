import numpy

print("NumPy Review 03 — Superconducting Transition Temperature")

lambda_ep = numpy.array([0.5, 0.7, 0.9, 1.1, 1.3])

omega_log = numpy.array([200.0, 190.0, 180.0, 170.0, 160.0])

mu = 0.1

e = -(1.04*(1+lambda_ep))/(lambda_ep-mu*(1+0.62*lambda_ep))

tc = (omega_log/1.2)*(numpy.exp(e))

print("all Tc :",tc)

print("the average Tc :",numpy.mean(tc),"K")

print("Maximum Tc: ",numpy.max(tc),"K","Minimum Tc: ",numpy.min(tc),"K")

c = tc >10

print("Tc > 10 K: ",tc[c])

print("the corresponding $lambda$ :",lambda_ep[c])

%runfile C:/Users/user/Downloads/untitled2.py --wdir
NumPy Review 03 — Superconducting Transition Temperature
all Tc : [ 2.43112359  6.60795483 10.54271478 13.59396941 15.73666322]
the average Tc : 9.782485165397866 K
Maximum Tc:  15.736663219167843 K Minimum Tc:  2.4311235903130286 K
Tc > 10 K:  [10.54271478 13.59396941 15.73666322]
the corresponding $lambda$ : [0.9 1.1 1.3]
