from sympy import Rational, Symbol, Function, log, Eq, Abs, sqrt
from equation_database.util.doc import bib, equation
from equation_database.util.math import Li2


@equation()
def equation_A_21(
    p=Symbol("p"),
    p_0=Symbol("p_0"),
    phat=Symbol(r"\hat{p}"),
    m=Symbol("m"),
    mhat=Symbol(r"\hat{m}"),
    m_0=Symbol("m_0"),
    mvec=Symbol(r"\vec{m}"),
    beta=Symbol("beta"),
):
    """

    Args:
        p : massless four momentum
        m : massive four momentum
    """
    return Eq(phat, p / p_0), Eq(mhat, m / m_0), Eq(beta, Abs(mvec) / m_0)


@equation()
def equation_A_23(
    I_0=Function("I_0"),
    p=Symbol("p", commutative=False),
    m=Symbol("m", commutative=False),
    phat=Symbol(r"\hat{p}", commutative=False),
    mhat=Symbol(r"\hat{m}", commutative=False),
):
    """

    Args:
        p : massless four momentum
        m : massive four momentum
        phat : normalized p momentum (see :meth:`~equation_A_21`)
        mhat : normalized m momentum (see :meth:`~equation_A_21`)
    """
    return Eq(I_0(p, m), log((phat * mhat) ** 2 / (mhat**2)))


@equation()
def equation_A_24(
    I_epsilon=Function(r"I_\epsilon"),
    p=Symbol("p", commutative=False),
    m=Symbol("m", commutative=False),
    phat=Symbol(r"\hat{p}", commutative=False),
    beta=Symbol("beta"),
):
    """

    Args:
        p    : massless four momentum
        m    : massive four momentum
        phat : normalized p momentum (see :meth:`~equation_A_21`)
        beta : normalized m three momentum (see :meth:`~equation_A_21`)
    """
    pm_1pb = phat * m / (1 + beta)
    pm_1mb = phat * m / (1 - beta)
    return Eq(
        I_epsilon(p, m),
        -2
        * (
            Rational(1, 4) * log((1 - beta) / (1 + beta)) ** 2
            + log(pm_1pb) * log(pm_1mb)
            + Li2(1 - pm_1pb)
            + Li2(1 - pm_1mb)
        ),
    )


@equation()
def equation_A_41(
    I_0=Function("I_0"),
    k_1=Symbol("k_1", commutative=False),
    k_2=Symbol("k_2", commutative=False),
    beta=Symbol("beta"),
):
    """

    Args:
        k1  : massive four momentum
        k2  : massive four momentum
    """
    return Eq(I_0(k_1, k_2), 1 / beta * log((1 + beta) / (1 - beta))), Eq(
        beta, sqrt(1 - (k_1**2 * k_2**2) / (k_1 * k_2) ** 2)
    )


@equation()
def equation_A_50(
    I_epsilon=Function(r"I_\epsilon"),
    K=Function("K"),
    a=Symbol("a"),
    b=Symbol("b"),
    k_1=Symbol("k_1", commutative=False),
    k_2=Symbol("k_2", commutative=False),
    vec_beta_1=Symbol(r"\vec{\beta}_1", commutative=False),
    vec_beta_2=Symbol(r"\vec{\beta}_2", commutative=False),
    z_1=Symbol("z_1"),
    z_2=Symbol("z_2"),
):
    """

    Args:
        k1  : massive four momentum
        k2  : massive four momentum

    """
    return Eq(
        I_epsilon(k_1, k_2),
        (K(z_2) - K(z_1)) * (1 - vec_beta_1 * vec_beta_2) / (sqrt(a * (1 - b))),
    )


@bib()
def bibtex():
    bibtex: str = """
@article{Alioli:2010xd,
    author = "Alioli, Simone and Nason, Paolo and Oleari, Carlo and Re, Emanuele",
    title = "{A general framework for implementing NLO calculations in shower Monte Carlo programs: the POWHEG BOX}",
    eprint = "1002.2581",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "DESY-10-018, SFB-CPP-10-22, IPPP-10-11, DCPT-10-22",
    doi = "10.1007/JHEP06(2010)043",
    journal = "JHEP",
    volume = "06",
    pages = "043",
    year = "2010"
}
    """
    return bibtex
