import sympy
from equation_database.util.parse import frac
Q = sympy.Symbol('Q')
"""Mass of the virtual photon"""

u = sympy.Symbol('u')
"""Mandelstam variable u"""
t = sympy.Symbol('t')
"""Mandelstam variable t"""

g_s = sympy.Symbol('g_s')
"""strong coupling constant"""
alpha_s = sympy.Symbol('alpha_s')
"""strong coupling constant"""
alpha = sympy.Symbol('alpha')
"""fine structure constant"""
e = sympy.Symbol('e')
"""electric charge """
e_q = sympy.Symbol('e_q')
"""electric charge of the quark """

sigma = sympy.Symbol('sigma')
"""cross section"""
sigma_0 = sympy.Symbol('sigma_0')
"""norm cross section"""

x_1 = sympy.Symbol('x_1')
"""quark momentum fraction"""
x_2 = sympy.Symbol('x_2')
"""antiquark momentum fraction"""
Q = sympy.Symbol('Q')
"""mass of the virtual photon"""

equation_2_1_30 = sympy.Eq(
  sigma_0,
  3 * alpha*e_q**2*Q
)
"""cross section for gamma* -> q qbar"""

equation_2_3_32 = sympy.Eq(
  sympy.Derivative(sigma, x_1, x_2)/sigma_0,
  2*alpha_s/3/sympy.pi * (x_1**2 + x_2**2)/((1-x_1)*(1-x_2))
)
"""
differentiated cross section for e+e- -> q qbar g

Warning: sigma_0 usage and reference is wrong in the reference!
"""

equation_4_3_20 = e**2*e_q**2* g_s**2 *frac("4/8")*frac("1/2") * 8 * (u/t + t/u + 2*Q**2*(u+t+Q**2)/(t*u))
""" gamma* gluon -> q qbar scattering averaged matrix element"""


# https://www.desy.de/~jung/qcd_and_mc_2009-2010/R.Field-Applications-of-pQCD.pdf
bibtex : str = """
@book{field1995applications,
  title={Applications Of Perturbative Qcd},
  author={Field, R.D. and Pines, D.},
  isbn={9780201483628},
  lccn={89000138},
  url={https://books.google.de/books?id=2eWnAAAACAAJ},
  year={1995},
  publisher={Avalon Publishing}
}
"""
"""Bibtex citation"""

