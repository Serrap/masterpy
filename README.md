# masterpy
Pipeline to estimate angular power spectra of masked Healpix maps. 
Based on the Monte Carlo Apodized Spherical Transform EstomatoR (MASTER), 
Hivon et al. (2001), see: https://arxiv.org/pdf/astro-ph/0105302.pdf

All python files are in /make_files/

Files:
compute_cls.py:
Main, interactive file to start the pipeline. It runs in python3.
You must input the values for lmax (ex: lmax = 2048),
the binning Delta required for the final output spectra
(ex: Delta = 64), the name of the maps/masks files. All maps/mask
must be in the directory /data.
If the option 'auto' is selected it computes CIB auto-spectra (at 353, 545, 857 GHz).
Selecting the option 'cross', it computes cross-spectra between CIB maps and
a given tracer of the dark matter field (a lensing map in the standard case).

cross.py:
Contains the routine to compute and output Cls of both the masks and the masked maps.

makeinv.py:
Contain the routine to compute and invert the Matrix M_ll'
(see Eq. A31 of Hivon et al. 2001). The beam power spectrum
is provided for both CIB auto-spectra and CIBxlensing cross-spectra.

wigner_func.py:
Contains all routines to compute Wigner-3j symbols for the M_ll' matrix

output.py:
Contain the main routine to compute and output pseudo-power spectra at the
given resolution Delta. Output files are created in /RESULTS/

plot.py
Contains the routine to plot output power spectra to be computed with a given
input for cross-checking purposes.

Files to be added:
makebeam.py -> It computes beam and window power spectra
make_spectra.py: It computes CIB and CIBx[external_tracer] power spectra to
make simulated maps
