# Chapter 8: Evolved Stars: After the Main Sequence

Figures from Chapter 8 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
  <dd>Figure 8.1 - Open Cluster H-R diagrams
  <dd>Figure 8.2 - Interior structure on the zero age main sequence (ZAMS)
  <dd>Figure 8.3 - Core hydrogen mass fraction evolution in 1 and 4M<sub>sun</sub> stars from ZAMS to TAMS
  <dd>Figure 8.4 - Hydrogen mass fraction in non-rotating terminal age main sequence (TAMS) stars
  <dd>Figure 8.5 - Evolutionary tracks for 1, 3, 10, and 30 M<sub>sun</sub> stars
  <dd>Figure 8.6 - Dredge-up in cluster NGC 6397
  <dd>Figure 8.7 - Density-temperature plot for helium core burning stars
  <dd>Figure 8.8 - Luminosity profiles for helium core burning stars
  <dd>Figure 8.9 - Globular cluster H-R diagrams
  <dd>Figure 8.12 - White dwarf initial-final mass relation
</dl>

## Data Files

### Figure 8.1 - Open Cluster H-R diagrams

The `OpenClusters/` folder has Gaia DR2 color-magintude data for 4 open clusters: h Persei, M92, NGC188, and Praesepe

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
  <dd>abund_1M_*age*.txt - 1M<sub>sun</sub> star, age = (zams, 1, 4, 5, 8, 10 Gyr)
  <dd>abund_4m_*age*.txt - 4M<sub>sun</sub> star, age = (zams, 25, 50, 75, 100, 125, 150 Myr)
</dl>


## Revision History

 * 2022 Dec 1 - First page created [rwp/osu]
