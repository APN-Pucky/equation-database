import sympy

from equation_database.util.doc import bib, equation

s = sympy.Symbol('s')
"""Mandelstam variable s"""
t = sympy.Symbol('t')
"""Mandelstam variable t"""
u = sympy.Symbol('u')
"""Mandelstam variable u"""
e = sympy.Symbol('e')
"""Elementary charge"""

equation_6_30 = 2*e**4 * (s**2 + u **2)/t**2
@equation()
def get_equation_6_30(): 
    """unpolarized $e^-\\mu^- \\to e^-\\mu^-$ scattering amplitude"""
    return equation_6_30

equation_6_31 = 2*e**4 * (t**2 + u **2)/s**2
@equation()
def get_equation_6_31(): 
    """unpolarized $e^-e^+ \\to \\mu^-\\mu^+$ scattering amplitude"""
    return equation_6_31

equation_6_113 = 2*e**4 * (- u/s - s/u)
@equation()
def get_equation_6_113(): 
    """spinaveraged Compton amplitude"""
    return equation_6_113

N = sympy.Symbol('N')
"""Normalization factor"""
x_q = sympy.Symbol('x_q')
"""Quark momentum fraction"""
x_qbar = sympy.Symbol('x_qbar')
"""Antiquark momentum fraction"""
x_g = sympy.Symbol('x_g')
"""Gluon momentum fraction"""

equation_11_35 = N * (x_q**2 + x_qbar**2)/((1-x_q)*(1-x_qbar))
@equation()
def get_equation_11_35(): 
    """spin and color averaged matrix element for electron-positron annihilation into quark-antiquark-gluon final state"""
    return equation_11_35

bibtex : str = """
@book{Halzen:1984mc,
    author = "Halzen, F. and Martin, Alan D.",
    title = "{QUARKS AND LEPTONS: AN INTRODUCTORY COURSE IN MODERN PARTICLE PHYSICS}",
    isbn = "978-0-471-88741-6",
    year = "1984"
}
"""
@bib()
def get_bibtex(): 
    return bibtex