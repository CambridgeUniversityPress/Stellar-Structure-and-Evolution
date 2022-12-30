# *Stellar Structure and Evolution*

Jupyter notebooks, python code, and selected data files and sources for the figures from Pinsonneault &amp; Ryden, 
[*Stellar Structure and Evolution*](https://www.cambridge.org/highereducation/books/stellar-structure-and-evolution/C3124CC7EA3818B745B48121E13DCED1), coming in August 2023.

[!["SSE Cover"](Misc/SSE_Cover_512.png?raw=true "Stellar Structure and Evolution")](https://www.cambridge.org/highereducation/books/stellar-structure-and-evolution/B6F803BC5085E8736B640F9ED4A0FA27)

## Overview
*Stellar Structure and Evolution* by Marc Pinsonneault and Barbara S. Ryden is the second volume in *The Ohio State Astrophysics Series* of 
textbooks published by Cambridge University Press.  The audience for this series is graduate students and upper-level undergraduates studying
astronomy and physics.

Most of the figures in this book were created by the authors, the majority of which are plots of data or calculations made using
Python programs implemented as Jupyter notebooks. We are making all the notebooks available on GitHub as an ancillary 
to the book.

Instructors and students using *Stellar Structure and Evolution* are welcome to use these notebooks to make high-resolution versions
of the book figures for presentations, adapt them for use in class, or to use as the basis for problem sets or projects in courses 
adopting this book.  Over time we hope to collect and present other notebooks that will enable further explorations of topics in the book, 
become part of computational problem sets or individual and group projects, etc. This way, the figures become a starting point for learning
and new explorations rather than being frozen into print.

## Software Requirements

All notebooks were developed in Python 3 using the [Anaconda Python distribution](https://www.anaconda.com). 

Required packages are numpy, scipy, pandas, matplotlib, and astropy, all part of Anaconda.

LaTeX is required for math symbols in the notebooks.

### Optional Packages

A number of the figures in the book used the [Modules for Experiments in Stellar Astrophysics (MESA)](https://github.com/MESAHub/mesa)
package to compute stellar model data. Because MESA calculations can be computationally intensive and require careful setup, 
all notebooks that used MESA data to make figures have pre-computed MESA model output files associated with them that were
created by Dr. Pinsonneault and his students.

Another group of figures use pre-computed models from the [MESA Isochrones and Stellar Tracks (MIST)](https://waps.cfa.harvard.edu/MIST/) database.
Because MIST data files require a special python program to read (see the [MIST_codes](https://github.com/jieunchoi/MIST_codes)
GitHub repository), we extracted the subset of the MIST data we wanted to plot into ASCII tables so that the Jupyter notebooks for the figures
do not require you to install and use the MIST routines or download the very large MIST database files directly.

If you wish to explore these models beyond the illustrations chosen for this book, we highly recommend learning how to use these powerful resources
for making stellar models.

## Downloads

### Download and Install

To download a copy of this repository onto your local computer, go to the folder on your computer where you want to install it and type

> `git clone https://github.com/CambridgeUniversityPress/Stellar-Structure-and-Evolution`

This will create the `Stellar-Structure-and-Evolution` folder containing the entire repository.  You may rename this repository after
installation to shorten the name if you wish (e.g., `/path/to/wherever/SSE`).

### Update the notebooks and data

To update your copy, go into the top-level folder you created above (e.g., `/path/to/wherever/SSE`) and type

> `git pull`

If there are no updates, your local copy will be unaffected.

## Use and Attribution

The notebooks and their contents are original works of the authors and often include data obtained from public archives or from 
professional colleagues (always from published sources).  We ask that users preserve all literature citations to the original work
from which such data were derived, and give proper credit when using them. If you use these notebooks, please make
reference to the *Stellar Structure and Evolution* book and this repository.

### License Notice

All files in this repository are licensed under a [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/), 
to foster broader use of the notebooks and their data by teachers and students.
