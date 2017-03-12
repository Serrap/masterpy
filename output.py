import numpy as np
import healpy as hp
import math
import wigner_func
import pdb

def master(lmax, freq, delta, name1, name2):
    lfr = len(freq)
    for i in range(lfr):
        cl = hp.fitsfunc.read_cl("../products/clinv_" + freq[i] + ".fits")
        num = len(cl)
        ell = np.arange(num)
        ellm = ell[0: lmax]
        galcl =cl[0:lmax]
        nellm = len(ellm)
        invM = np.loadtxt("../products/Minv_" + freq[i] + ".txt")
        matp, matq, lbins = wigner_func.master_make_pq(delta, lmax)
        aone = np.ones(len(lbins))
        clgalend = np.dot(np.dot(invM, matp), galcl)
        if name1 == name2:
            binnedcl = (2.0 * math.pi * clgalend) / (lbins * (lbins + aone))
        else:
            binnedcl = (4.0 * math.pi * clgalend)/ np.square(lbins * (lbins + aone)) * np.square(lbins) * lbins

        outfile = open("../RESULTS/"+ name1 + "x" + name2 + "_" + freq[i] + "GHz.txt", "w")
        for i in range(len(lbins)):
            outfile.write(str(lbins[i]) + " " + " " + str(binnedcl[i]) + " " + " " + "\n")
