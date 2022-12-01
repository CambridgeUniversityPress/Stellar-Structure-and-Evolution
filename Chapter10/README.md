# Chapter 10: Rotating Stars

Figures from Chapter 10 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
    <dd>Figure 10.4 - Core/envelope rotation of evolved stars
    <dd>Figure 10.5 - Rotational mixing of nitrogen
    <dd>Figure 10.7 - Flux variation in the Sun and Sun-like Kepler Stars
    <dd>Figure 10.8 - Open cluster star rotation periods
    <dd>Figure 10.9 - Kepler star mass-age-P<sub>rot<sub> diagram
</dl>

## Data Files

### Figure 10.4 - Core/envelope rotation

`CoreEnvelope.txt` contains a compilation of core/envelope rotation data derived from Aerts et al. 2019, ARA&A, 57, 35 (and references therein), 
and Deheuvels et al. 2020, A&A, 641, 117, compiled for the authors by Jamie Tayar (U Florida).

### Figure 10.5 - mixing of Nitrogen

The `RotationalMixing/` folder has data of surface mass fraction of <sup>14</sup>N as a function of 
age for non-rotating and rotating stars derived from MESA solar-abundance models computed by the authors:
<dl>
  <dd>nonRot_##Msun.csv - non-rotating stars, ## = (3,10,30) M<sub>sun</sub>
  <dd>rot_##Msun.csv - rotating stars, ## = (3,10,30) M<sub>sun</sub>
</dl>
The `RotationalMixing_All.csv` file merges the 6 files above into one, but is not used by the Jupyter notebook.

### Figure 10.7 - flux variation in the Sun and Sun-like Kepler stars

The `SunlikeStars/` folder has data for flux variations in the Sun and a subset of Sun-like stars observed with *Kepler*:
<dl>
  <dd>ActiveSun_Cycle23.txt - The Sun for 6 observing segments from the SOHO spacecraft during Solar Cycle 23 (Aug 1996 to Dec 2008)
  <dd>SunlikeKeplerStars.txt - Data for 6 sun-like Kepler stars: KIC2445004, KIC2718678, KIC5628737, KIC6034108, KIC6620375, and KIC6844155
</dl>
Data for the 6 Kepler stars were provided to the authors by Gibor Basri (UC Berkeley).  Figure 10.7 plots 4 of the 6.

### Figure 10.8 - Open Cluster star rotation

The `OpenClusters/` folder has data of rotation periods for stars from three open clusters:
<dl>
  <dd>Plieades_Prot.txt - Plieades stars (Godoy-Rivera et al. 2021)
  <dd>Praesepe_Prot.txt - Praesepe stars (Godoy-Rivera et al. 2021)
  <dd>UpperSco_Prot.txt - Upper Scorpius (Garcia et al. 2014)
</dl>

Data are from the Godoy-Rivera et al. 2021, ApJS, 257, 46 (Pleiades and Praesepe), and Garcia et al. 2014, A&A, 572, 34 
(Upper Scorpius, data from the VizieR database).

### Figure 10.9 - Kepler star mass-age-P<sub>rot</sub> diagram

`Kepler_AgeMassProt.txt` has ages, masses, and rotation periods from Claytor et al. 2020, ApJ, 888, 43 Table 3. 
We use a reduced version of the data file for simplicity of handling.

## Revision History

 * 2022 Dec 1 - First page created [rwp/osu]
