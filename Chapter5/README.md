# Chapter 5: Stars as Fusion Reactors

Figures from Chapter 5 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
    <dd>Figure 5.1 - Nuclear binding energy for stable nuclei
    <dd>Figure 5.2 - Astrophysical S-factor for <sup>14</sup>N+p to <sup>15</sup>O+gamma nuclear reaction
    <dd>Figure 5.3 - Boltzman and Gamow factors for hydrogen gas
    <dd>Figure 5.4 - <sup>3</sup>He fraction as a function of mass fraction in the BP2004 standard non-rotating solar model
    <dd>Figure 5.6 - Solar neutrino particle flux at 1 au from the Sun
    <dd>Figure 5.8 - pp and CNO cycle specific energy generation rate vs. temperature
    <dd>Figure 5.9 - <sup>12</sup>C, <sup>14</sup>N, and <sup>16</sup>O fractions in the sun
</dl>

## Data Files

### Figure 5.1 - Nuclear binding energy

`AME2020.txt` from the [Atomic Mass Data Center website](https://www-nds.iaea.org/amdc/)

### Figure 5.2 - Astrophysical S-factor

Data are from laboratory experiments, models adapted from Xu et al. 2013, Figure 79.

`14Npg15O_data.txt` - experimental data

`14Npg15O_model.txt` - model calculations

### Figure 5.4 and 5.8 - BP2004 Solar Model

`BP2004_Standard.txt` - Data file from Bahcall and Pinsonneault 2004, astro-ph/0402114

### Figure 5.6 - Solar neutrino data

The data files are from [John Bahcall's Neutrino Software and Data](http://www.sns.ias.edu/~jnb/SNdata/sndata.html).  The text files used to plot
the energy spectra are as follows:
<dl>
 <dd>pp.txt - p-p chain data
 <dd>hep.txt - HEP channel data
 <dd>boron8.txt - <sup>8</sup>B channel data
 <dd>nitrogen13.txt - <sup>13</sup>N channel data
 <dd>oxygen15.txt - <sup>15</sup>O channel data
 <dd>fluorine17.txt  <sup>17</sup>F channel data
</dl>
Some reformatting was required to get all of these different data files into a common file format for this plot.

## Revision History

 * 2022 Dec 1 - First page created [rwp/osu]
