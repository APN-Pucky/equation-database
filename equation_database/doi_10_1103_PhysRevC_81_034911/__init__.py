import sympy as sp

from equation_database.util.doc import bib, equation

# M = sp.Symbol("M")
# """mass of the virtual photon"""
## M2 = sp.Symbol('M^2')
# M2 = M**2  # sp.Symbol('M2')
#
# N_gamma = sp.Symbol("N_gamma")
# """yield of virtual photons"""
#
## N_ee = sp.Function('N_ee')(M2, N_gamma)
# N_ee = sp.Symbol("N_ee")
# """electron pair yield"""
#
# alpha = sp.Symbol("alpha")
# """fine structure constant"""
#
# L = sp.Function("L")(M)


@equation()
def equation_B1(
    N_ee=sp.Symbol("N_ee"),
    M=sp.Symbol("M"),
    L=sp.Function("L"),
    N_gamma=sp.Symbol("N_gamma"),
    alpha=sp.Symbol("alpha"),
):
    """


    Args:
        N_ee: electron pair yield
        M: mass of the virtual photon
        L: leptonic corrections
        N_gamma: yield of virtual photons
        alpha: fine structure constant
    """
    return sp.Eq(
        sp.Derivative(N_ee, M, 2), (alpha) / (3 * sp.pi) * (L(M) / M**2)
    ) * sp.Integral(N_gamma)


@bib()
def bibtex():
    return r"""
@article{PHENIX:2009gyd,
    author = "Adare, A. and others",
    collaboration = "PHENIX",
    title = "{Detailed measurement of the $e^+ e^-$ pair continuum in $p+p$ and Au+Au collisions at $\sqrt{s_{NN}} = 200$ GeV and implications for direct photon production}",
    eprint = "0912.0244",
    archivePrefix = "arXiv",
    primaryClass = "nucl-ex",
    doi = "10.1103/PhysRevC.81.034911",
    journal = "Phys. Rev. C",
    volume = "81",
    pages = "034911",
    year = "2010"
}
"""
