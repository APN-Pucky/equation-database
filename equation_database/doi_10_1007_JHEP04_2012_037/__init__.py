from sympy import Symbol, Function, log, Eq, Sum, Rational, pi
from equation_database.util.math import Li2
from equation_database.util.doc import bib, equation


@equation()
def equation_3_4(
    mathcal_Q_EW=Symbol(r"\mathcal{Q}_{EW}"),
    s=Symbol("s"),
    q=Function("q"),
    Q_EW=Symbol(r"Q_{EW}"),
    beta=Function("beta"),
    xi_C=Symbol("xi_C"),
    mu_F=Symbol(r"\mu_F"),
    i=Symbol("i"),
    f_plus=Symbol("f_+"),
    f_minus=Symbol("f_-"),
    n_final=Symbol(r"n_{\mathrm final}"),
):
    """
    One of the singular contributions to the EW virtual part.

    Args:
        mathcal_Q_EW : one of the singular contributions to the EW virtual part
        s            : Mandelstamm variable s
        q            : charge of a particle
        Q_EW         : energy scale of the process
        beta         : magnitude of the particles three momentum divided by the energy/0-component of the four vector.
        xi_C         : arbitrary parameter (e.g. set to one)
        mu_F         : factorization scale
        i            : index of the i final state particle
        f_plus       : index of the plus incoming particle
        f_minus      : index of the minus incoming particle
        n_final      : number of final state particles
    """
    return Eq(
        mathcal_Q_EW,
        -Sum(
            q(i) ** 2
            * (
                log(xi_C**2 * s / (2 * Q_EW**2))
                - 1 / (beta(i)) * log((1 + beta(i)) / (1 - beta(i)))
            ),
            (i, 1, n_final),
        )
        - log(mu_F**2 / (Q_EW**2))
        * ((q(f_plus) ** 2 + q(f_minus) ** 2) * (Rational(3, 2) + 2 * log(xi_C))),
    )


@equation()
def equation_3_5(
    mathcal_H=Symbol(r"\mathcal{H}"),
    q=Function("q"),
    k=Function("k", commutative=False),
    E=Function("E"),
    sigma=Function(r"\sigma"),
    s=Symbol("s"),
    Q_EW=Symbol(r"Q_{EW}"),
    xi_C=Symbol("xi_C"),
    i=Symbol("i"),
    j=Symbol("j"),
    n_massless=Symbol(r"n_{\mathrm massless}"),
):
    """

    Args:
        s                  : Mandelstamm variable s
        sigma              : +1 for incomign fermions and outgoing anti-fermions. -1 for outgoing fermions and incoming anti-fermions
        q                  : charge of a particle
        k                  : four momentum of a particle
        E                  : energy of a particle
        Q_EW               : energy scale of the process
        i                  : index of the i massless particle
        j                  : index of the j massless particle
        xi_C               : arbitrary parameter (e.g. set to one)
        n_massless         : number of (charged implied by equation) massless particles

    """
    kk_2EE = k(i) * k(j) / (2 * E(i) * E(j))
    return Eq(
        mathcal_H,
        -Sum(
            Sum(
                q(i)
                * q(j)
                * sigma(i)
                * sigma(j)
                * (
                    Rational(1, 2) * log(xi_C**2 * s / (Q_EW**2)) ** 2
                    + log(xi_C**2 * s / (Q_EW**2)) * log(kk_2EE)
                    - Li2(kk_2EE)
                    + Rational(1, 2) * log(kk_2EE) ** 2
                    - log(1 - kk_2EE) * log(kk_2EE)
                ),
                (j, i + 1, n_massless),
            ),
            (i, 1, n_massless),
        ),
    )


@equation()
def equation_3_6(
    mathcal_J=Symbol(r"\mathcal{J}"),
    q=Function("q"),
    k=Function("k"),
    E=Function("E"),
    sigma=Function(r"\sigma"),
    s=Symbol("s"),
    Q_EW=Symbol(r"Q_{EW}"),
    xi_C=Symbol("xi_C"),
    I_0=Function("I_0"),
    I_epsilon=Function(r"I_\epsilon"),
    m=Symbol("m"),
    l=Symbol("l"),  # noqa: E741
    n_massless=Symbol(r"n_{\mathrm massless}"),
    n_massive=Symbol(r"n_{\mathrm massive}"),
):
    """

    Args:
        I_0          : (see :func:`~equation_database.doi_10_1007_JHEP06_2010_043.equation_A_23`)
        I_epsilon    : (see :func:`~equation_database.doi_10_1007_JHEP06_2010_043.equation_A_24`)
        m            : index of the m massive particle
        l            : index of the l massless particle
        n_massless   : number of (charged implied by equation) massless particles
        n_massive    : number of (charged implied by equation) massive particles

    .. warning::
        There is a typo in this equation. The sign infront of the I_\epsilon term should also be negative as in :func:`~equation_database.doi_10_1007_JHEP06_2010_043.equation_A_28`.

    """
    return Eq(
        mathcal_J,
        -Rational(1, 2)
        * Sum(
            Sum(
                q(m)
                * q(l)
                * sigma(m)
                * sigma(l)
                * (
                    log(Q_EW**2 / (s * xi_C**2)) ** 2
                    - pi**2 / 6
                    - I_0(k(l), k(m)) * log(Q_EW**2 / (s * xi_C**2))
                    + I_epsilon(k(l), k(m))
                ),
                (l, 1, n_massless),
            ),
            (m, 1, n_massive),
        ),
    )


@equation()
def equation_3_7(
    mathcal_K=Symbol(r"\mathcal{K}"),
    q=Function("q"),
    k=Function("k"),
    E=Function("E"),
    sigma=Function(r"\sigma"),
    s=Symbol("s"),
    Q_EW=Symbol(r"Q_{EW}"),
    xi_C=Symbol("xi_C"),
    m=Symbol("m"),
    n=Symbol("n"),
    I_0=Function("I_0"),
    I_epsilon=Function(r"I_\epsilon"),
    n_massive=Symbol(r"n_{\mathrm massive}"),
):
    """

    Args:
        I_0 : (see :func:`~equation_database.doi_10_1007_JHEP06_2010_043.equation_A_41`)
        I_epsilon : (see :func:`~equation_database.doi_10_1007_JHEP06_2010_043.equation_A_50`)
        n_massive    : number of (charged implied by equation) massive particles
    """
    return Eq(
        mathcal_K,
        -Rational(1, 2)
        * Sum(
            Sum(
                q(m)
                * q(n)
                * sigma(m)
                * sigma(n)
                * (
                    -I_0(k(m), k(n)) * log(Q_EW**2 / (s * xi_C**2))
                    - I_epsilon(k(m), k(n))
                ),
                (m, n + 1, n_massive),
            ),
            (n, 1, n_massive),
        ),
    )


@bib()
def bibtex():
    bibtex: str = r"""
@article{Barze:2012tt,
    author = "Barze, Luca and Montagna, Guido and Nason, Paolo and Nicrosini, Oreste and Piccinini, Fulvio",
    title = "{Implementation of electroweak corrections in the POWHEG BOX: single W production}",
    eprint = "1202.0465",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "CERN-PH-TH-2012-025, FNT-2012-01, LPN12-031",
    doi = "10.1007/JHEP04(2012)037",
    journal = "JHEP",
    volume = "04",
    pages = "037",
    year = "2012"
}
    """
    return bibtex
