import numpy as np
import healpy as hp
from pylab import *
import matplotlib.pyplot as plt
import pdb

# input
def plot_cl(lmax, freq, delta, name1, name2):
    # conversion factors from MJy to mK
    fact = [1.e6, 1.e6, 1.e6]
    nbins = int(lmax / delta)
    el_out = np.zeros(nbins)
    cl_out = np.zeros(nbins)
    nfr = len(freq)
    if name1 == name2:
        data = np.loadtxt("../RESULTS/cib_spectra.txt", unpack = False)
    else:
        data = np.loadtxt("../RESULTS/lensing_spectra.txt", unpack = False)
    ldata = len(data)
    el_in = data[:, 0]
    cls = np.zeros([ldata, nfr])
    for i in range(nfr):
        cls[:, i] = data[:, i + 1]
        el_out, cl_out = np.loadtxt("../RESULTS/" + name1 + "x" + name2 + "_" + freq[i] + "GHz.txt", unpack = True)
        fig = figure()
        ax = fig.add_subplot(111)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlabel('Multipole l')
        #ax.set_ylabel('C$_l$')
        plt.xlim((10, 2000))
        
        if name1 == name2:
            ax.plot(el_in, cls[:, i], color = "Blue", label = "Input spectrum " + freq[i] + " GHz")
            ax.set_ylabel('C$_l$')
            ax.plot(el_out, cl_out, color = "Red", label = "Output spectrum " + freq[i] + " GHz")
        else:
            el, cl, err_stat, err_tot = np.loadtxt("../RESULTS/Cl_" + freq[i] + ".dat", unpack = True)
            ax.set_ylabel('$l^3$C$_l$ ($\mu$K sr)')
            ax.plot(el_out, cl_out * fact[i], color = "Red", label = "Output spectrum " + freq[i] + " GHz")
            ax.errorbar(el, cl, yerr = err_tot, fmt = "o", color = "Red", ecolor = "Blue", capsize = 10, label = "Planck 2013",  barsabove=True)
#            ax.plot(el_out, cl_out * 1.e6, color = "Red", label = "Output spectrum " + freq[i] + " GHz")
        legend = ax.legend(loc='lower left', shadow=True)
        savefig('../RESULTS/' + name1 + "x" + name2 + '_test_' + freq[i] + '.pdf', format='pdf')
        plt.show()
