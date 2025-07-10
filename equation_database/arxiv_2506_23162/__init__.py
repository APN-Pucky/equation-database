import sympy
from equation_database.util.doc import bib, equation


@bib()
def bibtex():
    bibtex: str = r"""
@article{Jezo:2025jyu,
    author = "Je{\v{z}}o, Tom{\'a}{\v{s}} and Klasen, Michael and Puck Neuwirth, Alexander",
    title = "{Conversion of photons to dileptons in the Kroll-Wada and parton shower approaches}",
    eprint = "2506.23162",
    archivePrefix = "arXiv",
    primaryClass = "hep-ph",
    reportNumber = "MS-TP-25-18",
    month = "6",
    year = "2025"
}"""
    return bibtex


@equation()
def equation_2_1(
    alpha=sympy.Symbol("alpha"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
    dN_gamma_star=sympy.Symbol("dN_gamma_star"),
):
    """
    Original: $$\\frac{\\,\\mathrm{d}^2 N_{ee}}{\\,\\mathrm{d} M_{ee}^2} = \\frac{\\alpha}{3 \\pi} \\frac{1}{M_{ee}^2}  \\sqrt{ 1 - \\frac{4 m_e^2}{M_{ee}^2}} \\left( 1 + \\frac{2 m_e^2}{M_{ee}^2}\\right) \\,\\mathrm{d} N_{\\gamma^*}    \\\\    \\approx \\frac{\\alpha}{3\\pi} \\frac{1}{M_{ee}^2} \\left( 1 - 6 \\frac{m_e^4}{M_{ee}^4} - 8 \\frac{m_e^6}{M_{ee}^6} \\right)  \\,\\mathrm{d} N_{\\gamma^*}$$
    """
    exact = (
        alpha
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
        * (1 + 2 * m_e**2 / M_ee**2)
        * dN_gamma_star
    )
    approx = (
        alpha
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * (1 - 6 * m_e**4 / M_ee**4 - 8 * m_e**6 / M_ee**6)
        * dN_gamma_star
    )
    return (exact, approx)


@equation()
def equation_2_10(
    p_1=sympy.Symbol("p_1"),
    p_2=sympy.Symbol("p_2"),
    k_T=sympy.Symbol("k_T"),
    p=sympy.Symbol("p"),
    z=sympy.Symbol("z"),
):
    """
    Original: $$p = p_1 + p_2    \\,,\\\\    p_1 = z p + k_T    \\,,\\\\    p_2 = (1-z) p - k_T    $$
    """
    return (
        sympy.Eq(p, p_1 + p_2),
        sympy.Eq(p_1, k_T + p * z),
        sympy.Eq(p_2, -k_T + p * (1 - z)),
    )


@equation()
def equation_2_13(
    p=sympy.Symbol("p"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    p_1=sympy.Symbol("p_1"),
    p_2=sympy.Symbol("p_2"),
    z=sympy.Symbol("z"),
    k_T=sympy.Symbol("k_T"),
):
    """
    Original: $$p^2 = M_{ee}^2 = 2m_e^2 + 2 p_1\\cdot{}p_2 =  2m_e^2 + 2  ( z (1-z) p^2 - k_T^2 - (2z-1) p\\cdot{}k_T)    \\,,\\\\    p_1^2 = m_e^2 = z^2 p^2 + k_T^2 + 2 z p \\cdot{} k_T    \\,,\\\\    M_{ee}^2 =  2m_e^2 + 2  ( z (1-z) M_{ee}^2 - k_T^2 ) - \\frac{2z-1}{z}  (m_e^2 - z^2 M_{ee}^2  - k_T^2  )    $$
    """
    eq1 = sympy.Eq(p**2, M_ee**2)
    eq2 = sympy.Eq(M_ee**2, 2 * m_e**2 + 2 * p_1 * p_2)
    eq3 = sympy.Eq(
        M_ee**2, 2 * m_e**2 + 2 * (z * (1 - z) * p**2 - k_T**2 - (2 * z - 1) * p * k_T)
    )
    eq4 = sympy.Eq(p_1**2, m_e**2)
    eq5 = sympy.Eq(m_e**2, z**2 * p**2 + k_T**2 + 2 * z * p * k_T)
    eq6 = sympy.Eq(
        M_ee**2,
        2 * m_e**2
        + 2 * (z * (1 - z) * M_ee**2 - k_T**2)
        - (2 * z - 1) / z * (m_e**2 - z**2 * M_ee**2 - k_T**2),
    )
    return (eq1, eq2, eq3, eq4, eq5, eq6)


@equation()
def equation_2_14(
    z=sympy.Symbol("z"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
    k_T=sympy.Symbol("k_T"),
):
    """
    Original: $$z = \\frac 1 2  \\pm \\frac 1 2  \\sqrt{ 1 - 4 \\frac{m_e^2}{M_{ee}^2} + 4k_T^2 } $$
    """
    return (
        sympy.Eq(
            z,
            sympy.Rational(1, 2)
            + sympy.Rational(1, 2) * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2 + 4 * k_T**2),
        ),
        sympy.Eq(
            z,
            sympy.Rational(1, 2)
            - sympy.Rational(1, 2) * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2 + 4 * k_T**2),
        ),
    )


@equation()
def equation_2_16(
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
    dN_gamma_star=sympy.Symbol("dN_gamma_star"),
):
    """
    Original: $$\\frac{\\,\\mathrm{d} \\mathcal P_{\\gamma \\to ee}}{\\,\\mathrm{d} M_{ee}^2}  =\\frac{\\alpha e_e^2}{3\\pi} \\frac{1}{M_{ee}^2}  \\left(  1  + \\frac{m_e^2}{M_{ee}^2}\\right)  \\sqrt{1 - \\frac{4 m_{e}^{2}}{M_{ee}^{2}}}\\\\\\approx \\frac{\\alpha e_e^2}{3\\pi} \\frac{1}{M_{ee}^2}  \\,\\mathrm{d} N_{\\gamma^*} \\left( 1 - \\frac{m_e^2}{M_{ee}^2} - 4 \\frac{m_e^4}{M_{ee}^4} \\right)$$
    """
    exact = (
        alpha
        * e_e**2
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * (1 + m_e**2 / M_ee**2)
        * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
    )
    approx = (
        alpha
        * e_e**2
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * dN_gamma_star
        * (1 - m_e**2 / M_ee**2 - 4 * m_e**4 / M_ee**4)
    )
    return (exact, approx)


@equation()
def equation_2_18(
    M_ee=sympy.Symbol("M_ee"),
    Q=sympy.Symbol("Q"),
    p_T=sympy.Symbol("p_T"),
    z=sympy.Symbol("z"),
):
    """
    Original: $$M_{ee}^2 = Q^2 = \\frac{p_T^2}{z(1-z)}$$
    """
    return (sympy.Eq(M_ee**2, Q**2), sympy.Eq(Q**2, p_T**2 / (z * (1 - z))))


@equation()
def equation_2_2(
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
    y_minus=sympy.Symbol("y_minus"),
    y_plus=sympy.Symbol("y_plus"),
    z=sympy.Symbol("z"),
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
):
    """
    Original: $$\\frac{\\,\\mathrm{d} \\mathcal P^m_{\\gamma \\to ee}}{\\,\\mathrm{d} M_{ee}^2}  = \\frac{\\alpha}{2\\pi} \\frac{1}{M_{ee}^2}  \\int_{y_{-}}^{y_+}P^m_{\\gamma \\to ee}(z) \\,\\mathrm{d} z\\\\=\\frac{\\alpha e_e^2}{3\\pi} \\frac{1}{M_{ee}^2}  \\left(  1  + 2\\frac{m_e^2}{M_{ee}^2}\\right)  \\sqrt{1 - \\frac{4 m_{e}^{2}}{M_{ee}^{2}}}$$
    """
    integral_form = (
        alpha
        / (2 * sympy.pi)
        * (1 / M_ee**2)
        * sympy.Integral(P_gamma_to_ee(z), (z, y_minus, y_plus))
    )
    closed_form = (
        alpha
        * e_e**2
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * (1 + 2 * m_e**2 / M_ee**2)
        * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
    )
    return sympy.Eq(integral_form, closed_form)


@equation()
def equation_2_20(
    s_IK=sympy.Symbol("s_IK"),
    f_Kallen=sympy.Symbol("f_Kallen"),
    Gamma_ijk=sympy.Symbol("Gamma_ijk"),
    y_ij=sympy.Symbol("y_ij"),
    y_jk=sympy.Symbol("y_jk"),
    y_ik=sympy.Symbol("y_ik"),
    phi=sympy.Symbol("phi"),
    mu_e=sympy.Symbol("mu_e"),
    dPhi_ant=sympy.Symbol("dPhi_ant"),
    dy_ij=sympy.Symbol("dy_ij"),
    dy_jk=sympy.Symbol("dy_jk"),
    dphi=sympy.Symbol("dphi"),
    a_bar=sympy.Symbol("a_bar"),
):
    """
    Original: $$\\,\\mathrm{d} \\Phi^{\\text{FF}}_\\text{ant} = \\frac{1}{16 \\pi^2} f^{\\text{FF}}_\\text{Källén} s_{IK} \\Theta(\\Gamma_{ijk}) \\,\\mathrm{d} y_{ij} \\,\\mathrm{d} y_{jk}  \\frac{\\,\\mathrm{d} \\phi}{2 \\pi}    \\,,\\\\    \\bar{a}_{e/\\gamma}^{\\text{FF},\\gamma} = \\frac{1}{s_{IK}} \\frac 1 2 \\frac{1}{y_{ij} + 2 \\mu_e^2} \\left[y_{ik}^2 + y_{jk}^2 + \\frac{2 \\mu_e^2}{y_{ij} + 2 \\mu_e^2}\\right]    $$
    """
    dphi_ant_eq = sympy.Eq(
        dPhi_ant,
        1
        / (16 * sympy.pi**2)
        * f_Kallen
        * s_IK
        * sympy.Heaviside(Gamma_ijk, 0)
        * dy_ij
        * dy_jk
        * dphi
        / (2 * sympy.pi),
    )
    a_bar_eq = sympy.Eq(
        a_bar,
        1
        / s_IK
        * sympy.Rational(1, 2)
        * 1
        / (y_ij + 2 * mu_e**2)
        * (y_ik**2 + y_jk**2 + 2 * mu_e**2 / (y_ij + 2 * mu_e**2)),
    )
    return (dphi_ant_eq, a_bar_eq)


@equation()
def equation_2_21(
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    y_ik=sympy.Symbol("y_ik"),
    y_jk=sympy.Symbol("y_jk"),
    f_Kallen=sympy.Symbol("f_Kallen"),
    Gamma_ijk=sympy.Symbol("Gamma_ijk"),
    dy_jk=sympy.Symbol("dy_jk"),
    dphi=sympy.Symbol("dphi"),
):
    """
    Original: $$\\frac{\\,\\mathrm{d} \\mathcal P_{\\gamma \\to ee}^m}{\\,\\mathrm{d} M_{ee}^2} \\propto 4 \\pi \\alpha e_e^2 \\frac 1 2 \\frac{1}{M_{ee}^2} \\left[y_{ik}^2 + y_{jk}^2 + \\frac{2 m_e^2}{M_{ee}^2}\\right] \\frac{1}{16 \\pi^2} f^{\\text{FF}}_\\text{Källén} \\Theta(\\Gamma_{ijk}) \\,\\mathrm{d} y_{jk}  \\frac{\\,\\mathrm{d} \\phi}{2 \\pi}$$
    """
    return (
        4
        * sympy.pi
        * alpha
        * e_e**2
        * sympy.Rational(1, 2)
        * (1 / M_ee**2)
        * (y_ik**2 + y_jk**2 + 2 * m_e**2 / M_ee**2)
        * 1
        / (16 * sympy.pi**2)
        * f_Kallen
        * sympy.Heaviside(Gamma_ijk, 0)
        * dy_jk
        * dphi
        / (2 * sympy.pi)
    )


@equation()
def equation_2_22(
    Gamma_ijk=sympy.Symbol("Gamma_ijk"),
    y_ij=sympy.Symbol("y_ij"),
    y_jk=sympy.Symbol("y_jk"),
    y_ik=sympy.Symbol("y_ik"),
    mu_i=sympy.Symbol("mu_i"),
    mu_j=sympy.Symbol("mu_j"),
):
    """
    Original: $$0< \\Gamma_{ijk} = y_{ij} y_{jk} y_{ik} - y_{jk} \\mu_i^2 - y_{ik} \\mu_j^2    $$
    """
    return sympy.Eq(Gamma_ijk, y_ij * y_jk * y_ik - y_jk * mu_i**2 - y_ik * mu_j**2)


@equation()
def equation_2_23(
    z=sympy.Symbol("z"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
):
    """
    Original: $$z = \\frac 1 2 \\pm \\frac 1 2 \\sqrt{1-\\frac{4m_e^2}{M_{ee}^2}}    $$
    """
    return (
        sympy.Eq(
            z,
            sympy.Rational(1, 2)
            + sympy.Rational(1, 2) * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2),
        ),
        sympy.Eq(
            z,
            sympy.Rational(1, 2)
            - sympy.Rational(1, 2) * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2),
        ),
    )


@equation()
def equation_2_24(
    y_ij=sympy.Symbol("y_ij"),
    y_jk=sympy.Symbol("y_jk"),
    y_ik=sympy.Symbol("y_ik"),
    mu_e=sympy.Symbol("mu_e"),
):
    """
    Original: $$1 = y_{ij} + 2 \\mu_e^2 + y_{jk} + y_{ik}    $$
    """
    return sympy.Eq(1, y_ij + 2 * mu_e**2 + y_jk + y_ik)


@equation()
def equation_2_25(
    y_plus=sympy.Symbol("y_plus"),
    y_minus=sympy.Symbol("y_minus"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    s=sympy.Symbol("s"),
):
    """
    Original: $$y_\\pm =  \\frac{\\pm\\sqrt{\\left(M_{ee}^{2} - 2 m_{e}^{2}\\right)^{-1} \\left(M_{ee}^{2} - s\\right) \\left(M_{ee}^{4} - 2 M_{ee}^{2} m_{e}^{2} - M_{ee}^{2} s + 6 m_{e}^{2} s\\right)} + \\left(- M_{ee}^{2} + s\\right) }{2 s }$$
    """
    discriminant = (
        (M_ee**2 - 2 * m_e**2) ** (-1)
        * (M_ee**2 - s)
        * (M_ee**4 - 2 * M_ee**2 * m_e**2 - M_ee**2 * s + 6 * m_e**2 * s)
    )
    y_plus_expr = (sympy.sqrt(discriminant) + (-(M_ee**2) + s)) / (2 * s)
    y_minus_expr = (-sympy.sqrt(discriminant) + (-(M_ee**2) + s)) / (2 * s)
    return (sympy.Eq(y_plus, y_plus_expr), sympy.Eq(y_minus, y_minus_expr))


@equation()
def equation_2_3(
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    M_ee=sympy.Symbol("M_ee"),
    s=sympy.Symbol("s"),
):
    """
    Original: $$\\frac{\\,\\mathrm{d} \\mathcal P_{\\gamma \\to ee}}{\\,\\mathrm{d} M_{ee}^2}  =\\frac{\\alpha e_e^2}{3\\pi} \\frac{1}{M_{ee}^2}  \\left( 1 - \\frac{M_{ee}^2}{s}\\right)^3 $$
    """
    return alpha * e_e**2 / (3 * sympy.pi) * (1 / M_ee**2) * (1 - M_ee**2 / s) ** 3


@equation()
def equation_2_4(
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
    z=sympy.Symbol("z"),
    e_e=sympy.Symbol("e_e"),
):
    """
    Original: $$P_{\\gamma \\to ee}(z) =  e_e^2 ( z^2 + (1-z)^2)    $$
    """
    return sympy.Eq(P_gamma_to_ee(z), e_e**2 * (z**2 + (1 - z) ** 2))


@equation()
def equation_2_5(
    alpha=sympy.Symbol("alpha"),
    Q=sympy.Symbol("Q"),
    z=sympy.Symbol("z"),
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
):
    """
    Original: $$\\,\\mathrm{d} \\mathcal P_{\\gamma \\to ee} = \\frac{\\alpha}{2\\pi} \\frac{\\,\\mathrm{d} Q^2}{Q^2}  P_{\\gamma \\to ee}(z) \\,\\mathrm{d} z$$
    """
    return alpha / (2 * sympy.pi) * (1 / Q**2) * P_gamma_to_ee(z)


@equation()
def equation_2_6(
    alpha=sympy.Symbol("alpha"),
    M_ee=sympy.Symbol("M_ee"),
    z=sympy.Symbol("z"),
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
):
    """
    Original: $$\\frac{\\,\\mathrm{d} \\mathcal P_{\\gamma \\to ee}}{\\,\\mathrm{d} M_{ee}^2} = \\frac{\\alpha}{2\\pi} \\frac{1}{M_{ee}^2}  P_{\\gamma \\to ee}(z) \\,\\mathrm{d} z $$
    """
    return alpha / (2 * sympy.pi) * (1 / M_ee**2) * P_gamma_to_ee(z)


@equation()
def equation_2_7(
    alpha=sympy.Symbol("alpha"),
    M_ee=sympy.Symbol("M_ee"),
    y_minus=sympy.Symbol("y_minus"),
    y_plus=sympy.Symbol("y_plus"),
    z=sympy.Symbol("z"),
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
):
    """
    Original: $$\\frac{\\,\\mathrm{d} \\mathcal P_{\\gamma \\to ee}}{\\,\\mathrm{d} M_{ee}^2}  = \\frac{\\alpha}{2\\pi} \\frac{1}{M_{ee}^2}  \\int_{y_{-}}^{y_+}P_{\\gamma \\to ee}(z) \\,\\mathrm{d} z$$
    """
    return (
        alpha
        / (2 * sympy.pi)
        * (1 / M_ee**2)
        * sympy.Integral(P_gamma_to_ee(z), (z, y_minus, y_plus))
    )
