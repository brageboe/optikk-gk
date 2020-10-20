**Chapter 10: Fibre Optics**

**A slab waveguide is modeled as a three-layered thin film.**

Problems are given in Assignment_4.pdf, submitted solution in Optikk_GK_Assignment_4.pdf. Code files a4-1-multimode-TE.py and a4-2-multimode-TM.py are identical except for solving different mode relation equations and field components whose equations can be found in both pdf-files.

User can choose the following parameters:
  * system wavelength 
  * refractive indices of core (slab) n_1 and outer cladding n_2 (n_1 > n_2 to ensure total internal reflection)
  * the number of modes to look for
  
The program plots the mode dispersion relation, and from the resulting plot the user can choose which of the plotted slab thicknesses to calculate and plot the transversal field component and its modes.
  * First figure, mode dispersion relation
    * Blue lines are the right-hand side of the mode dispersion relation equation, valid for any multitude of pi (user chooses how many multitudes).
    * Red lines are the left-hand side of the same equation, calculated for a series of slab thicknesses appropriate for the user-chosen pi multitudes of the right-hand side.
    * The amount of intersections between a specific red line with the blue lines tells us how many modes the transversal field will have.
    * Each mode (intersection) has a corresponding effective refractive index N.
    * The user chooses (from user input in terminal) which of the slab thicknesses (red lines) to calculate the transversal field.
  * Second figure, transversal field 
    * Transversal field is calculated for the given value slab thickness.
    * E_y (for TE) or H_y (for TM) is plotted with respect to the confinement direction x, so field propagation direction (+z) is into the page.
    * Black horizontal lines represent the core/cladding interfaces.
