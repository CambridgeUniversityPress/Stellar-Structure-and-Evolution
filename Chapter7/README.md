# Chapter 7: Star Formation: Before the Main Sequence

Figures from Chapter 7 of Pinsonneault & Ryden, *Stellar Structure and Evolution*.

## Jupyter Notebooks
<dl>
    <dd>Figure 7.2 - Pre-main sequence evolution tracks
    <dd>Figure 7.3 - Chabrier initial mass function
    <dd>Figure 7.4 - Luminosity evolution of low-mass stars
</dl>

## Data Files

### Figure 7.2 - PMS evolution models

The `MIST/` folder has evolutionary tracks and isochrones for pre-main sequence (PMS) stars
compute using MIST/MESA:

Evolutionary tracks for different masses:

`pms_M#.##_track.txt` - where #.## = (0.10, 0.25, 0.50, 1.00, 2.00, 4.00, 6.00) M<sub>sun</sub>

Isochrones for these masses for different ages:

`pms_t###_iso.txt` - where ### = (1e5, 1e6, 1e7, and 1e8) years.

The file `MIST_FeH0_ZAMS.txt` contains the data for the Zero-Age Main Sequence plotted in this figure.
    
### Figure 7.4 - Low-mass star luminosity evolution
    
The `Burrows93/` folder has data from Burrows et al. 1993 and 1997 from www.astro.princeton.edu/~burrows. Filenames converted to the form 

`burrows93_M###.txt` - where ### is the mass in units units of 0.001M<sub>sun</sub>.

The original data were converted into units of Myr vs luminosity in L<sub>sun</sub>.

## Revision History

 * 2022 Dec 11 - checked and added Jupyter notebooks [rwp/osu]
 * 2022 Dec 1 - First page created [rwp/osu]
