#
# nci.py, a tiny script to display plots from Nciplot in PyMOL
#
#get Nciplot at http://gatsby.ucmerced.edu/wiki/Nciplot
#
#Nciplot references:
#
# J. Contreras-Garcia, E. Johnson, S. Keinan, R. Chaudret, J-P Piquemal, D. Beratan, W. Yang, J. Chem. Theor. Comp. 7, 625 (2011).
# E R. Johnson, S. Keinan, P. Mori-Sanchez, J. Contreras-Garcia, A J. Cohen, and W. Yang, J. Am. Chem. Soc., 132, 6498 (2010).
#
#
#Usage:
#
#Load the molecular geometry and the two cube files (-grad and -dens) into pymol
#
#load the script in pymol (for instance, using file->run and selecting the nci.py from the PyMOL GUI)
#
#Run the script by typing:   nci  basename
#in pymol, where basename is the first part, before the dash, of the name of the cube files (i.e. basename-dens.cube)


#
#This python script is in the public domain.
#

from pymol import cmd, stored
 
def nci( arg1 ):
	densf=arg1+"-dens"
	gradf=arg1+"-grad"
#	gdens=open(densf+".cube","r")
#	grad=open(gradf+".cube","r")
	cmd.isosurface("grad",gradf, 0.5)
	cmd.ramp_new("ramp", densf, [-5,5], "rainbow")
	cmd.set("surface_color", "ramp", "grad")
	cmd.set('two_sided_lighting',value=1)
 
cmd.extend( "nci", nci );
