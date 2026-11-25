def main():
    import numpy
    x = [0.3, 0.5, 0.8, 1.0, 1.4, 1.8]
    lambda_ep = numpy.array(x)
    av_ep,max_ep,min_ep,s_ep = analyze_epc(lambda_ep)
    re = classify_epc(av_ep)
    print("EPC values:",lambda_ep)
    print("Average EPC: ",av_ep)
    print("Maximum EPC: ",max_ep)
    print("Minimum EPC: ",min_ep)
    print("Strong coupling values: ",s_ep)
    print("Average EPC classification: ",re)
    
def analyze_epc(lambda_ep):
    import numpy
    av_ep = numpy.mean(lambda_ep)
    max_ep = numpy.max(lambda_ep)
    min_ep = numpy.min(lambda_ep)
    a = lambda_ep >= 1.0
    s_ep = lambda_ep[a]
    return av_ep, max_ep, min_ep, s_ep

def classify_epc(av_ep):
    if av_ep >= 1.0 :
        re = "Strong coupling"
        return re
    elif 1.0 > av_ep >= 0.5:
        re = "Moderate coupling"
        return re
    else:
        re = "Weak coupling"
        return re
main()
 %runfile C:/Users/user/Downloads/untitled2.py --wdir
EPC values: [0.3 0.5 0.8 1.  1.4 1.8]
Average EPC:  0.9666666666666667
Maximum EPC:  1.8
Minimum EPC:  0.3
Strong coupling values:  [1.  1.4 1.8]
Average EPC classification:  Moderate coupling
