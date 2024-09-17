import sympy

from equation_database.util.doc import bib, equation

x_1 = sympy.Symbol('x_1')
"""quark momentum fraction"""
x_2 = sympy.Symbol('x_2')
"""antiquark momentum fraction"""

alpha_C = sympy.Symbol('alpha_C')
"""Colour charge"""
alpha = sympy.Symbol('alpha')
"""Fine structure constant"""
Q = sympy.Symbol('Q')
"""Mass of the electron pair (virtual photon)"""

sum_e_q_squared = sympy.Symbol('sum_e_q_squared')
"""Sum of electric charges of quarks squared"""

sigma_pt = sympy.Symbol('sigma_pt')
"""Parton cross section"""

sigma = sympy.Symbol('sigma')
"""Cross section""" 

equation_2_8 = sympy.Eq(
    sigma_pt,
    4* sympy.pi * alpha**2 / Q**2 * sum_e_q_squared
)
@equation()
def get_equation_2_8(): return equation_2_8

equation_2_9 = sympy.Eq(
  sympy.Derivative(sigma, x_1, x_2)/sigma_pt,
  2*alpha_C/3/sympy.pi * (x_1**2 + x_2**2)/((1-x_1)*(1-x_2))
)
@equation()
def get_equation_2_9(): return equation_2_9

bibtex : str = """
@article{DeGrand:1977sy,
    author = "DeGrand, Thomas A. and Ng, Yee Jack and Tye, S. H. H.",
    title = "{Jet Structure in e+ e- Annihilation as a Test of QCD and the Quark-Confining String}",
    reportNumber = "SLAC-PUB-1950",
    doi = "10.1103/PhysRevD.16.3251",
    journal = "Phys. Rev. D",
    volume = "16",
    pages = "3251",
    year = "1977"
}
"""
@bib()
def get_bibtex(): 
    return bibtex