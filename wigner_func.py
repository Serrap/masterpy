import numpy as np
import healpy as hp
import math
import pdb
from scipy.special import gammaln

def master_wigner_init(lmax):
    k = np.arange(2 + lmax * 3)
    lnwpro = gammaln(2 * k + 1.) - 2 * gammaln(k + 1.)
    return lnwpro
                           
def master_wigner3j2(il1, il2, il3, lnwpro):
    l1 = np.long(il1)
    l2 = np.long(il2)
    l3 = il3 #np.int(il3)
    L = l1 + l2 + l3
    L_2 = L / 2
    #L_2 = L_2.astype(int)
    min = abs(l1 - l2)
    max = l1 + l2
    c = l3 * 0.
    w = np.logical_and(np.logical_and((L_2 * 2 - L) == 0., l3 >= min), l3 <= max)
    #w = np.logical_and((L_2 * 2 - L) == 0, (l3 >= min), (l3 <= max))
    #for i in range(len(w)):
    if w[0] == True:
        lnw1 = lnwpro[L_2[0] - l1]
        lnw2 = lnwpro[L_2[0] - l2]
        lnw3 = lnwpro[L_2[0] - l3[0]]
        lnwl = lnwpro[L_2[0]]
        lnc = - math.log(L[0] + 1.0) - lnwl + lnw1 + lnw2 + lnw3
        c = math.exp(lnc)
    return c

def master_make_pq(delta, lmax):
    nbin = int(lmax / delta)
    llim = np.arange(nbin + 1) * delta
    llim[nbin] = lmax
    llim[0] = 2
    ell = np.arange(lmax)
    matp  = np.zeros([nbin, lmax])
    matq  = np.zeros([lmax, nbin])
    for i in range(nbin):
        for ll in range(max(2, llim[i]), llim[i+1]):
            matp[i, ll] = 1.0 / 2.0 / math.pi * (ll * (ll + 1.0)) / np.longdouble(llim[i+1] - llim[i])
            matq[ll, i] = 2.0 * math.pi / np.longdouble(ll * (ll + 1.))
    lbins = np.arange(nbin)
    lbins = [np.mean([llim[i], llim[i + 1]]) for i in range(nbin)]
    return matp, matq, lbins
