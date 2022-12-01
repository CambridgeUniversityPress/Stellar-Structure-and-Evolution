# Chapter 4: Stellar Energy Transport

Figures from Chapter 4 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
    <dd>Figure 4.1 - Solar interior ionization
    <dd>Figure 4.2 - Iron and oxygen opacity for solar metallicity
    <dd>Figure 4.3 - Rosseland mean opacity for solar metallicity
    <dd>Figure 4.5 - Hydrogen and helium ionization state and adiabatic index
</dl>

## Data Files

### Figure 4.1 - Model solar interior

<dl>
   <dd>BP2004_solarInterior.txt - Bahcall & Pinsonnealt 2004 standard solar model interior
</dl>

### Figure 4.2 - Oxygen and iron opacity

The `Kappa/` folder contains models calculated by Dr. Franck Delahaye, LERMA - Observatoire de Paris., Site de Meudon for oxygen and iron
opacities in solar metallicity gas.  See the 00Readme.txt file in that folder for details and the filename convention.

### Figure 4.3 - Rosseland Mean Opacity

The `Rosseland/` folder contains models of rosseland mean opacity as a function of temperature for gas of solar abundance (photosphere: X=0.749, Y=0.238, Z=0.013)
calculated for different densities from the [Opacity Project OPserver](opacities.osc.edu/rmos.shtml).

Files have names
<dl>
<dd>Rosseland_OP_rho<##>.txt - where <##> is the log10 density (+2, 0, -2, -4, -6, -10)
</dl>

### Figure 4.4 - H and He ionization and adiabatic index

Data files for Figure 4.1:
<dl>
   <dd>HHe_IonFraction.txt - Hydrogen and helium ionization fractions as a function of temperature
   <dd>HHe_AdiabaticIndex.txt - adiabatic index (gamma) as a function of temperature for X=0.72, Y=0.28, density 10<sup>-7</sup>g/cm<sup>3</sup>
</dl>

## Images

### Figure 4.4 - Solar granulation

Multi-conjugate adaptive optics (MCAO) images of the Sun from the New Solar Telescope of the Big Bear Solar Observatory. 
Source: Schmidt et al. 2017, A&A, 597, L8, Figure 1 upper left panel, with permission.

## Revision History

 * 2022 Dec 1 - First page created, template was ISM/IGM Chapter 4 [rwp/osu]
