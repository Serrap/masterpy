# masterpy
Pipeline to estimate angular power spectra of temperature fluctuations 
on a limited sky-area of Healpix maps. Based on the Monte Carlo 
Apodized Spherical Transform EstomatoR (MASTER), 
Hivon et al. (2001), see: 
https://arxiv.org/pdf/astro-ph/0105302.pdf

It is based on a spherical harmonic transform of the un-masked map.

- Data files (input maps, masks, beams) must be in /data/
- Python files are in /make_files/
- Output files are in /RESULTS/

Files:

- compute_cls.py:
Main, interactive file to run the pipeline in python3 
(it's easy to make it compatible with python2.7). This is the only file 
you need to run in principle, and it calls all functions in the other files.

The code asks if you want to compute auto- or cross-power spectra.
If the option 'auto' is selected it computes CIB auto-spectra from maps at 353, 545, 857 GHz.
Selecting the option 'cross', it computes cross-spectra between the 3 CIB maps and
a given tracer of the dark matter field (a lensing map in the standard case).

You must input the values for lmax (ex: lmax = 2048),
the binning l-Delta for the final output spectra
(ex: Delta = 64), the name of the maps & masks files. 

Maps names are given without the .fits extension and without the frequency value so
if the name of your map is "CIBmap2048_353.fits", enter "CIBmap2048" as the map name.

- cross.py:
Contains the routine to compute and output Cls of both the masks and the masked maps.

- makeinv.py:
Contain the routine to compute and invert the Matrix M_ll'
(see Eq. A31 of Hivon et al. 2001). The beam power spectrum
is provided for both CIB auto-spectra and CIBxlensing cross-spectra.

- wigner_func.py:
Contains all routines to compute Wigner-3j symbols for the M_ll' matrix

- output.py:
Contain the main routine to compute and output pseudo-power spectra at the
given resolution Delta. Output files are created in /RESULTS/

- plot.py
Contains the routine to plot output power spectra to be computed with a given
input for cross-checking purposes.

- masterpy.tgz
.tgz file with all files and directories.

Files to be added:
- makebeam.py
It computes beam and window power spectra
- make_spectra.py
File to compute theoretical CIB Cls and CIBxexternal_tracer Cls. 
These can be compared to the output from the main pipeline
