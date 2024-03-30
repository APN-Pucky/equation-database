import sympy
from equation_database.util.parse import frac


s = sympy.Symbol('s')
"""Mandelstam variable s"""
t = sympy.Symbol('t')
"""Mandelstam variable t"""
u = sympy.Symbol('u')
"""Mandelstam variable u"""
g = sympy.Symbol('g')
"""Strong coupling constant"""

table_7_1_qqp_qqp = frac("4/9") * (s**2+u**2)/(t**2)
table_7_1_qqpb_qqpb = frac("4/9") * (s**2+u**2)/(t**2)
table_7_1_qq_qq = frac("4/9") * ( (s**2+u**2)/(t**2) + (s**2+t**2)/(u**2) ) - frac("8/27") * s**2/(u*t) 
table_7_1_qqb_qpqpb = frac("4/9") * ( (t**2+u**2)/(s**2) )
table_7_1_qqb_qqb = frac("4/9") * ( (s**2+u**2)/(t**2) + (t**2+u**2)/(s**2) ) - frac("8/27") * u**2/(s*t) 
table_7_1_qqb_gg = frac("32/27") *  (t**2+u**2)/(t*u) - frac("8/3") * (t**2+u**2)/(s**2) 
table_7_1_gg_qqb = frac("1/6") *  (t**2+u**2)/(t*u) - frac("3/8") * (t**2+u**2)/(s**2) 
table_7_1_gq_gq = frac("-4/9")  * (s**2+u**2)/(s*u) + (u**2+s**2)/t**2
table_7_1_gg_gg = frac("9/2")  * (3 - t*u/s**2 - s*u/t**2 - s*t/u**2)

bibtex : str = """
@book{Ellis_Stirling_Webber_1996,
    place={Cambridge},
    series={Cambridge Monographs on Particle Physics, Nuclear Physics and Cosmology},
    title={QCD and Collider Physics},
    publisher={Cambridge University Press},
    author={Ellis, R. K. and Stirling, W. J. and Webber, B. R.},
    year={1996}, collection={Cambridge Monographs on Particle Physics,
    Nuclear Physics and Cosmology}
} 
"""