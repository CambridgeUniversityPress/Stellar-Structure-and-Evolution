# Chapter 1: Properties of Stars

Figures from Chapter 1 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
    <dd>Figure 1.2 - Solar irradiance
    <dd>Figure 1.3 - Solar spectrum
    <dd>Figure 1.4 - Solar abundances
    <dd>Figure 1.6 - Alpha Centauri A,B orbit
    <dd>Figure 1.7 - P-Cygni star spectral line profile
    <dd>Figure 1.8 - MK spectral types
    <dd>Figure 1.9 - GALAH DR3 abundances
    <dd>Figure 1.10 - Gaia EDR3 H-R diagrams
    <dd>Figure 1.11 - Mass-loss H-R diagram
    <dd>Figure 1.12 - Main sequence M-L relation
    <dd>Figure 1.13 - Main sequence M-R relation
    <dd>Figure 1.14 - Pleiades cluster H-R and Prot diagrams
</dl>

## Data Files

### Figure 1.2 - Solar irradiance

`sorce_tsi_L3_c24h_latest.txt` raw SORCE TIM Total Solar Irradiance data.  Source: http://lasp.colorado.edu/home/sorce/data/.  
This version was downloaded on 2021 July 11.  We used the daily file version 3.19.

### Figure 1.3 - Solar spectrum

`Sun_ASTME-490-00.txt` - the [ASTM E-490-00 solar spectrum](https://www.nrel.gov/grid/solar-resource/spectra-astm-e490.html)
solar spectrum from the US Department of Energy's [National Renewable Energy Laboratory](https://www.nrel.gov/index.html).

### Figure 1.4 - Solar abundances

`Lodders2020.txt` - solar abundace vs. atomic number from Lodders 2020, Solar Elemental Abundances, in The Oxford Research 
Encyclopedia of Planetary Science, Oxford University Press. doi:10.1093/acrefore/9780190647926.013.145, Table 8, reformmated
for the notebook.

### Figure 1.6 - Alpha Cen AB orbit

`AlphaCenAB_Obs_See1893.txt` - data from See (1893, MNRAS, 54, 102) expressed as angular separation and position angle of B from A, converted 
to projected x,y coordinates in arcseconds.

`AlphaCenAB_Eph.txt` - orbital ephemeris transformed into the alpha Cen A reference frame.

### Figure 1.8 - MK spectral types

The folder `MKTypes` contains the spectra of dwarf stars, types O5 thru M5, from A Library of Stellar Spectra by Jacoby, Hunter, & Christian 
1984, ApJ, 56, 257. Data are rescaled to unity flux at 5500A and shifted by an arbitrary constant so that they will plot vertically stacked
without overlaps, provided they are plotted in order. 

Spectra are in individual ASCII text files named by star.  The `mkData.txt` is a list of spectral times for each spectrum file.  
The Jupyter notebook uses this file to label the spectra.

### Figure 1.9 - GALAH DR3 abundances

`GALAH_DR3.txt` - abundances for 85,000 main sequence stars observed with the [GALAH survey Third Data Release](https://www.galah-survey.org/dr3/overview/).
The desired subset of data were reformatted into a convenient ASCII column format for this plot.

### Figure 1.10 - Gaia EDR3 H-R diagram

`Gaia_EDR3_HR.txt` - color-magnitude data for 226,635 local stars extracted from the from Gaia EDR3 database. See the Jupyter notebook for
details on the search query and contents.

### Figure 1.11 - Mass-loss H-R diagram

`Cranmer_Saar_2011.txt` - data from Cranmer & Saar 2011 ApJ, 741, 54 and references therein.

### Figure 1.12 and 1.13 - Main sequence masses, luminosities, and radii 

`MainSequence_MLR.txt` - Main-sequence mass, luminosity, and radius data derived from Eker et al. 2018, MNRAS, 479, 5491.

### Figure 1.14 - Pleiades cluster H-R and P<sub>rot</sub> diagrams

`Pleiades_Gaia_EDR3.txt` - Pleiades Gaia EDR3 photometry from Heyl et al. 2022, ApJ, 926, 132

`Pleiades_Prot_Godoy.txt` - Pleiades Gaie DR2 photometry and rotation periods from Godoy-Rivera et al. 2021 ApJ, 257, 46.
    
## Images
The grayscale images in Figures 1.1 and 1.5 were created from original color images.

### Figure 1.1 - The Sun
Solar Dynamics Explorer HMI 6173A image for UTC 2022 May 20 19:52:39 [20220520_195238_4096_HMII.jpg](https://sdo.gsfc.nasa.gov/data/aiahmi/)

### Figure 1.5a - Betelgeuse visible light
VLT + SPHERE + ZIMPOL image of Betelgeuse at 645nm: [ESO 2003b](https://www.eso.org/public/images/eso2003b/)

### Figure 1.5b - Betelgeuse UV light
*Hubble Space Telescope* UV images from [Uitenbroek et al. 1998, AJ, 116, 2501, Figure 12](https://iopscience.iop.org/article/10.1086/300596/fulltext)

## Revision History

 * 2022 Dec 1 - First page created, template was ISM/IGM Chapter 1 [rwp/osu]
