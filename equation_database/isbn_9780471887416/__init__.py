import sympy

from equation_database.util.doc import bib, equation


@equation()
def equation_6_30(
    e=sympy.Symbol("e"), s=sympy.Symbol("s"), t=sympy.Symbol("t"), u=sympy.Symbol("u")
):
    """
    unpolarized $e^-\\mu^- \\to e^-\\mu^-$ scattering amplitude

    Args:
        e: Elementary charge
        s: Mandelstam variable s
        t: Mandelstam variable t
        u: Mandelstam variable u
    """
    return 2 * e**4 * (s**2 + u**2) / t**2


@equation()
def equation_6_31(
    e=sympy.Symbol("e"), s=sympy.Symbol("s"), t=sympy.Symbol("t"), u=sympy.Symbol("u")
):
    """
    unpolarized $e^-e^+ \\to \\mu^-\\mu^+$ scattering amplitude

    Args:
        e: Elementary charge
        s: Mandelstam variable s
        t: Mandelstam variable t
        u: Mandelstam variable u
    """
    return 2 * e**4 * (t**2 + u**2) / s**2


@equation()
def equation_6_32(
    sigma=sympy.Symbol("sigma"),
    Omega=sympy.Symbol("Omega"),
    alpha=sympy.Symbol("alpha"),
    s=sympy.Symbol("s"),
    theta=sympy.Symbol("theta"),
):
    """
    Differential cross section for $e^+e^- \\to \\mu^+\\mu^-$ in the center of mass frame

    Args:
        sigma: cross section
        Omega: solid angle
        alpha: fine structure constant
        s: Mandelstam variable s
        theta: scattering angle of the muons
    """
    return sympy.Eq(
        sympy.Derivative(sigma, Omega),
        alpha**2 / (4 * s) * (1 + sympy.cos(theta) ** 2),
    )


@equation()
def equation_6_33(
    sigma=sympy.Symbol("sigma"),
    alpha=sympy.Symbol("alpha"),
    s=sympy.Symbol("s"),
):
    """
    Cross section for $e^+e^- \\to \\mu^+\\mu^-$

    Args:
        sigma: cross section
        alpha: fine structure constant
        s: Mandelstam variable s
    """
    return sympy.Eq(sigma, alpha**2 / (3 * s) * 4 * sympy.pi)


@equation()
def equation_6_113(e=sympy.Symbol("e"), s=sympy.Symbol("s"), u=sympy.Symbol("u")):
    """
    spin averaged Compton amplitude

    Args:
        e: Elementary charge
        s: Mandelstam variable s
        u: Mandelstam variable u
    """
    return 2 * e**4 * (-u / s - s / u)


@equation()
def equation_11_35(
    N=sympy.Symbol("N"), x_q=sympy.Symbol("x_q"), x_qbar=sympy.Symbol("x_qbar")
):
    """
    spin and color averaged matrix element for electron-positron annihilation into quark-antiquark-gluon final state

    Args:
        N: Normalization factor
        x_q: Quark momentum fraction
        x_qbar: Antiquark momentum fraction
    """
    return N * (x_q**2 + x_qbar**2) / ((1 - x_q) * (1 - x_qbar))


@bib()
def bibtex():
    bibtex: str = """
@book{Halzen:1984mc,
    author = "Halzen, F. and Martin, Alan D.",
    title = "{QUARKS AND LEPTONS: AN INTRODUCTORY COURSE IN MODERN PARTICLE PHYSICS}",
    isbn = "978-0-471-88741-6",
    year = "1984"
}
"""
    return bibtex
