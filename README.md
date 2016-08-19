**Wrappers for the SPLASH SPH plotting code**
=============================================

If you are working with data from someone else's astrophysical Smoothed Particle Hydrodynamics (SPH) simulations, and having trouble reading it/analysing it, then this repo may be useful.


I created this repo during the Comparing Apples to Apples Workshop at the Lorentz Center in Leiden:

http://www.lorentzcenter.nl/lc/web/2016/802/info.php3?wsid=802&venue=Snellius

There was a desire amongst those who create synthetic observations from SPH data for better tools to convert between different file formats, and generally make SPH data easier to read.  The tools already exist, and are well known to those who develop SPH code and run the simulations, but are less well known to those who only post-process and analyse them.

This is a very simple set of scripts that allow you to run some of the utilities offered by Daniel Price's SPLASH:

http://users.monash.edu.au/~dprice/splash/

SPLASH is principally a plotting program for SPH data, but it also contains several helpful tools for:

i) converting SPH data from one file format to another,

ii) Binning SPH data into a cartesian grid

and others - see the SPLASH userguide for more.

I've written these scripts as a wrapper - you don't need to know how to operate SPLASH, just ensure that all of its binaries are installed locally.  This works best when you install the software from source rather than using e.g. MacPorts.

If you find yourself using these scripts a lot, then tell Daniel Price! He may decide to develop these tools in SPLASH further for the non-expert SPH community.  You can find his email at the above URL.
