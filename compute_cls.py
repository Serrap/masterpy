import numpy as np
import healpy as hp
import math
import cross
import makeinv
import output
import pdb
import plot

lmax = int(input("What lmax ? "))
Delta_bin = int(input("Which l-Delta_bin for the output spectra (ex: 32, 64, 128...)? "))
if type(lmax / Delta_bin) != int:
    raise RuntimeError("lmax must be multiple of Delta!")
freqs = ["353", "545", "857"]
in_map = input("Name of input map (no freq nor .fits extension, ex: 'input_map' or 'CIBmap2048'): ")
name1 = 'cib'
auto_or_x = input("'auto' or 'cross' power spectrum? Ex: 'auto': ")
if auto_or_x == 'cross':
    in_map2 = input("Name of second input map, ex: 'input_map2' or 'kappa_map_2048': ")
    name2 = 'phi'
    beam = "sqrtbeamxwin_" # beam name to be used in the makeinv file
else:
    in_map2 = in_map
    name2 = name1
    beam = "win_" 
in_mask = input("Name of input mask, default is: 'cross_mask': ")

# compute the Cls of the mask and the masked maps
cross.cross_maps(lmax, freqs, in_map, in_map2, in_mask, auto_or_x)

# compute the inverse matrix
makeinv.inv(lmax, freqs, Delta_bin, beam)

# deconvolve using the inverse matrix
output.master(lmax, freqs, Delta_bin, name1, name2)

# cross-check! Plot input and output spectra 
plot.plot_cl(lmax, freqs, Delta_bin, name1, name2)
