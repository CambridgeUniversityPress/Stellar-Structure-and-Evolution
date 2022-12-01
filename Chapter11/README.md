# Chapter 11: Pulsating Stars

Figures from Chapter 11 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
    <dd>Figure 11.2 - Large Magellanic Cloud Cepheid P-L Relation
    <dd>Figure 11.3 - Radial displacement modes of an n=3 Polytrope
    <dd>Figure 11.4 - Multi-mode cepheid light curve
    <dd>Figure 11.6 - Carnot heat engine cycle
    <dd>Figure 11.7 - Adiabatic Non-Radial Pulsations in the standard solar model
    <dd>Figure 11.8 - Kepler power spectrum of 16 Cygni A
    <dd>Figure 11.9 - Kepler star light curves and power spectra
    <dd>Figure 11.10 - Radii and masses observed by Kepler
</dl>

## Data Files

### Figure 11.2 - LMC Cepheid P-L relation

`LMC_Cepheids_OGLE.txt` contains data for LMC Cepheids from Udalski et al. 1999, AcA, 49, 223, extracted from the electronic data tables in the VizieR database
into a convenient form to use with the Jupyter notebook.

### Figure 11.3 - Radial displacement nods of an n=3 polytrope

`Schwarzschild_1941.txt` contains radial displacements arbitrarily normalized to unity at r=R<sub>star</sub> for
the first three modes in an n=3 polytrope with gamma=5/3. Data are from from Schwarzschild 1941, ApJ, 94, 245.

### Figure 11.4 - multi-mode cepheid light curve

Light curve of multi-mode classical Cepheid star OGLE-LMC-CEP-0832 phased to the fundamental period, then the isolated 
light curves for the fundamental and first-overtone modes.  Data are from See Soszynski et al. 2008, AcA, 58, 163
<dl>
    <dd>OGLE-LMC-CEP-0832.txt - full light curve
    <dd>OGLE-LMC-CEP-0832_a.txt - isolated light curve of the fundamental mode
    <dd>OGLE-LMC-CEP-0832_b.txt - isolated light curve of the first-overtone mode
</dl>

### Figure 11.8 - Kepler power spectrum of 16 Cygni A

Kepler data for 16 Cygni A are in 2 files:

`KIC12069424.txt` - Kepler ower spectrum density file of 16 Cyg A = KIC12069424, derived from the FAMED pipeline tutorial data set

`16CygA_Metcalfe_Table1.txt` - measured frequencies of the different ell-modes from Metcalfe, et al. 2012, ApJ, L10, 749 Table 1

The original PSD data for 16 Cyg A are elusive online, and even the original authors did not have the data anymore, but we found a copy
squirreled away among the tutorials used to test the for the FAMED pipeline code for automated extraction and mode identification of oscillation 
frequencies for solar-like pulsators (Corsaro et al. 2022, A&A, 640, 130).

### Figure 11.9 - Kepler star light curves and power spectra

The `KeplerStars/` folder contains light curves and power spectrum density (PSD) files for 4 Kepler stars: KIC2166940, KIC2425375, KIC5858947, and KIC9332840. 
There are 2 data files for each star:
<dl>
  <dd>KIC#######_LC.txt - light curve data for star KIC#######
  <dd>KIC#######_PSD.txt - power spectrum density data for star KIC#######
</dl>
Data files were reduced and provided to the authors by Dr. Mathieu Vrard, then a postdoc at OSU.

### Figure 11.10 - Radii and masses observed by Kepler

Data are from Pinsonneault, M., et al. 2022, in prep, in 2 CSV files:

`RM_Kepler_RG.csv` - radius/mass data from Red Giant stars observed with Kepler

`RM_Kepler_RC.csv` - radius/mass data for Red Clump stars observed with Kepler

## Revision History

 * 2022 Dec 1 - First page created [rwp/osu]
