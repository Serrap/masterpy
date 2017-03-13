'''
Function to compute the Mll' matrix and invert it
'''

import numpy as np
import healpy as hp
import math
import pdb
import wigner_func
import pandas as pd 

def inv(lmax, freq, delta, beam):
    lfr = len(freq)
    ll = np.arange(lmax)
    ellm = np.arange(lmax)
    nellm = len(ellm)
    m = np.zeros([nellm, nellm])
    for i in range(lfr):
        clmask = hp.fitsfunc.read_cl("../products/clmask_" + freq[i] + ".fits")
        pixel = hp.fitsfunc.read_cl("../products/" + beam + freq[i] + ".fits")
        num = len(clmask)
        clm = clmask[0: lmax]
        pxw = pixel[0: lmax]
        lnwpro = wigner_func.master_wigner_init(len(ll))
# Matrix M_l1_l2
        m = np.zeros([nellm, nellm])
        c = np.zeros(num)
        c = (2.0 * ellm + 1.0) * clmask[0: lmax]
        for l1 in range(nellm):
            for l2 in range(l1, nellm):
                m[l1, l2] = np.sum(c * wigner_func.master_wigner3j2(ellm[l1], ellm[l2], ellm, lnwpro))
        for l1 in range(nellm):
            for l2 in range(l1 + 1):
                m[l1, l2] = m[l2, l1]

        for l2 in range(nellm):
            m[:,l2] *= (2.0 * ellm[l2] + 1.0) / (4. * math.pi) * pxw[l2]**2
# binning the power spectra, see Hivon++ eqs. 20-21  
        matp, matq, lbins = wigner_func.master_make_pq(delta, lmax)
        matbin = np.zeros([len(lbins), len(lbins)])
        matbin = np.dot(np.dot(matp, m), matq)
        nb = int(lmax / delta)
        invM = np.zeros([nb, nb])
        invM = np.linalg.inv(matbin)
        df = pd.DataFrame(data = invM.astype('double'))
        df.to_csv('../products/Minv_' + freq[i] + '.txt', sep=' ', header = False, index = False) 
