#a program to construct confidence intervals using neyman construction

import sys
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from Rando.Random import Random

# main function for our neyman construction code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    #mean of lognorm 
    mux=0.75

    #sigma of lognorm
    sigx=0.25

    # default number of experiments and measurements
    Nmeas=10
    Nexp = 1

     # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-mux' in sys.argv:
        p = sys.argv.index('-mux')
        mutemp = float(sys.argv[p+1])
        if mutemp > 0:
            mux = mutemp
    if '-sigx' in sys.argv:
        p = sys.argv.index('-sigx')
        sigtemp = float(sys.argv[p+1])
        if sigtemp > 0:
            sigx = sigtemp

    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nm = int(sys.argv[p+1])
        if Nm > 0:
            Nmeas = Nm



    random = Random(seed)

    MU=[]
    for i in range(0,Nmeas):
        n=np.random.randint(1,300)
        MU.append(n)
    MUtrue=[]
    MUmeas=[]
    for n in MU:
        for i in range(0,Nexp):
            MUexp=[]
            for j in range(0, Nmeas):
                t=random.SkewNorm(n,sigx)
                MUexp.append(t)   
        
            AvgMU=sum(MUexp)/len(MUexp)

            MUmeas.append(AvgMU)
            MUtrue.append(n)

    x=MUtrue
    y=MUmeas

    plt.hist2d(x, y, bins=100)
    plt.xlabel('mu true')
    plt.ylabel('mu measured')
    plt.title('Plot of confidence intervals via Neyman contruction')
    plt.show()
