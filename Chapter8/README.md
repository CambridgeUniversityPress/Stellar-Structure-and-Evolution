# Chapter 8: Evolved Stars: After the Main Sequence

Figures from Chapter 8 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
  <dd>Figure 8.1 - Open Cluster H-R diagrams
  <dd>Figure 8.2 - Interior structure on the zero age main sequence (ZAMS)
  <dd>Figure 8.3 - Core hydrogen mass fraction evolution in 1 and 4M<sub>sun</sub> stars from ZAMS to TAMS
  <dd>Figure 8.4 - Hydrogen mass fraction in non-rotating terminal-age main sequence (TAMS) stars
  <dd>Figure 8.5 - Evolutionary tracks for 1, 3, 10, and 30 M<sub>sun</sub> stars
  <dd>Figure 8.6 - Dredge-up in cluster NGC 6397
  <dd>Figure 8.7 - Density-temperature plot for helium core burning stars
  <dd>Figure 8.8 - Luminosity profiles for helium core burning stars
  <dd>Figure 8.9 - Globular cluster H-R diagrams
  <dd>Figure 8.12 - White dwarf initial-final mass relation
</dl>

## Data Files

### Figure 8.1 - Open Cluster H-R diagrams

The `OpenClusters/` folder has Gaia DR2 color-maginitude data for 4 open clusters: h Persei, M92, NGC188, and Praesepe

### Figure 8.2 - ZAMS interior models 

The `ZAMS/` folder has these files extracted from MESA interiors calculations:
<dl>
  <dd>l50r50zams.txt - 50% luminosity and depth points at M/M<sub>sun</sub>
  <dd>convLower.txt - contour of the convection zone boundary at low mass (M<0.3M<sub>sun</sub>)
  <dd>convUpper.txt - contour of the convection zone boundary at high masses (M>1.2M<sub>sun</sub>)
</dl>

### Figure 8.3 - MESA core abundance data

The `CoreAbund/` folder has core abundance profiles for 1 and 4 M<sub>sun</sub> stars at a range
of stellar ages starting from the ZAMS:
<dl>
  <dd>abund_1M_age.txt - 1M<sub>sun</sub> star, age = (zams, 1, 4, 5, 8, 10 Gyr)
  <dd>abund_4m_age.txt - 4M<sub>sun</sub> star, age = (zams, 25, 50, 75, 100, 125, 150 Myr)
</dl>

### Figure 8.4 - Terminal Age Main Sequence (TAMS) hydrogen profiles

The `TAMS/` folder has core abundance profiles for 0.3, 1, 3, 10, and 30 M<sub>sun</sub> stars in a single CSV folder named `TAMS_Xprofiles.csv`

### Figure 8.5 - Evolutionary H-R diagrams

The `HREvolution/` folder has H-R Diagrams showing the evolution of stars with mass M = 1, 3, 10, and 30 M<sub>sun<sub>.  There are 5 files
<dl>
<dd>HRDiagrams_##Msun.csv - data for an ##= (1, 3, 10, 30) M<sub>sun</sub> stars.
<dd>HRDiagrams_all.csv - merged version of the 4 named CSV files
</dl>
Data were calculated using MESA and converted into convenient form for these notebooks.

### Figure 8.6 - Dredge-up in cluster NGC6397

The CSV file `Li_DredgeUp_NGC6397.csv` contains data from Data are from Lind et al. 2009, A&A, 503, 545 for cluster NGC6397.

### Figure 8.7 and 8.8 - Core He-burning Stars

The file `ZAHB/He_rhoT_zahb.csv` contains the zero-age helium-burning model density and temperature data for stars with masses of 1, 3, 10, and 30 M<sub>sun</sub>,
and 1 and 3 M<sub>sun</sub> red giants at core helium ignition plotted in Figure 8.7

The file `ZAHB/He_ML_zahb.csv` contains the zero-age helium-burning model luminosity profile data for stars with masses of 1, 3, 10, and 30 M<sub>sun</sub> plotted in
Figure 8.8

### Figure 8.9 - Globular Cluster H-R diagrams

The `Globulars/` folder has Gaia EDR3 color-maginitude data for globular clusters 47 Tucanae and M92

### Figure 8.12 - White dwarf initial-final mass relation

The file `WD_Mf_Mi_Cummings2018_Table1.txt` has data from white dwarf initial and final masses derived from Cummings et al. 2018, ApJ, 866, 21, Table 1, reformatted
to make plotting more convenient for the notebook.

## Revision History

 * 2022 Dec 1 - First page created [rwp/osu]
