"""
Program to read the input maps and masks, 
exclude bad values and cross-correlate 
both maps and masks. The outputs files are  
power spectra of the masks and 
power spectra of masked maps
"""

import numpy as np
import healpy as hp
from pylab import *
import matplotlib.pyplot as plt
import math
import pdb

def cross_maps(lmax, freqs, input_map, input_map2, input_mask, auto_or_x):
# currently taking Planck CIB maps
#    freqs = ["353", "545", "857"]
    if auto_or_x == 'cross':
        mapsx = hp.read_map("../data/" + input_map2 + ".fits")
    for i in range(len(freqs)):
        maps = hp.read_map("../data/" + input_map + "_" + freqs[i] + ".fits")
        bad_values_zero = np.where(maps == 0)
        bad_values_inf = np.where(maps == -1.63750E+30)
        mask = hp.read_map("../data/" + input_mask + "_" + freqs[i] + ".fits")
        bad_values = ~np.isfinite(mask)
        mask[bad_values] = 0.
        mask[np.where(mask <= 1e-8)] = 0.
        mask[bad_values_zero] = 0.0
        mask[bad_values_inf] = 0.0
        # plot the resulting map
        #hp.zoomtool.mollzoom(maps * mask)
        #plt.show()
        if auto_or_x == 'auto':
            clinv = hp.sphtfunc.anafast(maps * mask, lmax = lmax)
        else:
            clinv = hp.sphtfunc.anafast(maps * mask, mapsx * mask, lmax = lmax)
        clmask = hp.sphtfunc.anafast(mask, lmax = lmax)

        hp.fitsfunc.write_cl("../products/clinv_" + freqs[i] + ".fits", clinv)
        hp.fitsfunc.write_cl("../products/clmask_" + freqs[i] + ".fits", clmask)
