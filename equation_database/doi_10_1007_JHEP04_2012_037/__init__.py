import sympy as sy
from equation_database.util.doc import bib, equation


@equation()
def equation_3_4(
    mathcal_Q_EW=sy.Symbol(r"\mathcal{Q}_{EW}"),
    s=sy.Symbol("s"),
    q=sy.Function("q"),
    Q_EW=sy.Function(r"Q_{EW}"),
    beta=sy.Function("beta"),
    xi_C=sy.Function("xi_C"),
    mu_F=sy.Symbol(r"\mu_F"),
    i=sy.Symbol("i"),
    f_plus=sy.Symbol("f_+"),
    f_minus=sy.Symbol("f_-"),
    n_final=sy.Symbol("n_final"),
):
    """

    Args:
        s       : Mandelstamm variable s
        q       : charge of a particle
        i       : index of the i final state particle
        beta    : magnitude of the particles three momentum divided by the energy/0-component of the four vector.
        mu_F    : factorization scale
        f_plus  : index of the plus incoming particle
        f_minus : index of the minus incoming particle
        n_final : number of final state particles
    """
    return sy.Eq(
        mathcal_Q_EW,
        sy.Sum(
            q(i) ** 2
            * sy.log(
                xi_C**2 * s / (2 * Q_EW**2)
                - 1 / (beta(i)) * sy.log((1 + beta(i)) / (1 - beta(i)))
            ),
            (i, 1, n_final),
        )
        - sy.log(mu_F**2 / (Q_EW**2))
        * ((q(f_plus) ** 2 + q(f_minus) ** 2) * (sy.Rational(3, 2)) + 2 * sy.log(xi_C)),
    )


@bib()
def bibtex():
    bibtex: str = """
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
