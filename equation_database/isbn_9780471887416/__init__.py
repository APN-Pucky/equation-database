import sympy

s = sympy.Symbol('s')
"""Mandelstam variable s"""
t = sympy.Symbol('t')
"""Mandelstam variable t"""
u = sympy.Symbol('u')
"""Mandelstam variable u"""
e = sympy.Symbol('e')
"""Elementary charge"""

equation_6_30 = 2*e**4 * (s**2 + u **2)/t**2
"""unpolarized e-mu- -> e-mu- scattering amplitude"""
equation_6_31 = 2*e**4 * (t**2 + u **2)/s**2
"""unpolarized e-e+ -> mu-mu+ scattering amplitude"""

equation_6_113 = 2*e**4 * (- u/s - s/u)
"""spin averaged Compton amplitude"""

bibtex : str = """
@book{Halzen:1984mc,
  added-at = {2009-01-13T13:43:30.000+0100},
  address = {New York, USA},
  author = {Halzen, Francis and Martin, Alan},
  biburl = {https://www.bibsonomy.org/bibtex/25aff683e444ad48a1a6b91fce38498fb/clange},
  interhash = {0f0942dd05c5962377caa1eb7519cd9c},
  intrahash = {5aff683e444ad48a1a6b91fce38498fb},
  keywords = {textbook},
  publisher = {John Wiley \& Sons},
  timestamp = {2012-04-23T15:13:29.000+0200},
  title = {Quarks \& Leptons: An introductory course in modern particle physics},
  year = 1984
}
"""