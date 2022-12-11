# Chapter 12: Binary Stars

Figures from Chapter 12 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
    <dd>Figure 12.1 - Stellar multiplicity
    <dd>Figure 12.2 - Periods and eccentricties of G-dwarf binary stars
    <dd>Figure 12.3 - Binary Star Equipotential Contours
    <dd>Figure 12.4 - Binary star evolution
    <dd>Figure 12.5 - Astrometric orbit of Algol AB
    <dd>Figure 12.7 - IUE UV spectrum of HR Delphinus
    <dd>Figure 12.8b - Globular cluster NGC6397 color-magnitude diagram
</dl>

## Data Files

### Figure 12.1 - Stellar multiplicity

`Multiplicity_Moe_DiStefano_2017.txt` contains data on stellar multiplicity statistics derived from 
Moe and DiStefano 2017, ApJS, 230, 15, Table 13

### Figure 12.2 - G-dwarf binaries

`SB9_Gprimary.txt` contains orbital data on G-dwarf spectroscopic binary stars from the 
[9th Catalog of Spectroscopic Binaries aka SB9](https://sb9.astro.ulb.ac.be/) developed by the
late Dimitri Pourbaix (Porbaix et al. 2004, A&A, 424, 727).  We extracted a subset of binaries
with G-dwarf primary stars and added a basic column header to assist reading.

### Figure 12.5 - Algol astrometric orbit

`CHARA_Algol_BC.txt` contains interferometric positions of Algol B relative to Algol A measured by the CHARA interferometer, 
derived from Baron, F. et al. 2012 ApJ, 752, 20, Tables 3 and 6.

### Figure 12.7 - IUE UV spectrum of HR Del

`HRDel_IUE.fits` is a FITS-format far UV IUE spectrum of HR Del from Selvelli & Gilmozzi 2013, A&A, 560, 49 retrieved from 
VizieR [J/A+A/560/A49](https://cdsarc.cds.unistra.fr/viz-bin/cat/J/A+A/560/A49) in FITS format.  The Jupyter notebook
uses the `astroph.io.fits` package to read the original FITS file.

### Figure 12.8b - NGC6397 color-magnitude diagram

`ngc6397phot.txt` contains *Hubble Space Telescope* photometry of globular cluster NGC6397.

Data are from the Padova Globular Cluster Photometry [PGCP Database](http://groups.dfa.unipd.it/ESPG/hstphot.html), 
Piotto et al. 2002 A&A, 391, 945, but the data are also available from [VizieR](http://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/A+A/391/945).
Data reformatted as ASCII text for the Jupyter notebook.

## Revision History

 * 2022 Dec 11 - checked and added Jupyter notebooks [rwp/osu]
 * 2022 Dec 1 - First page created [rwp/osu]
 
