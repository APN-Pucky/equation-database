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


@equation(latex=r"p = p_1 + p_2")
def equation_2_10(
    p_1=sympy.Symbol("p_1"),
    p_2=sympy.Symbol("p_2"),
):
    return p_1 + p_2


@equation(latex=r"p_1 = z p + k_T")
def equation_2_11(
    k_T=sympy.Symbol("k_T"),
    p=sympy.Symbol("p"),
    z=sympy.Symbol("z"),
):
    return k_T + p * z


@equation(latex=r"p_2 = (1-z) p - k_T")
def equation_2_12(
    k_T=sympy.Symbol("k_T"),
    p=sympy.Symbol("p"),
    z=sympy.Symbol("z"),
):
    return -k_T + p * (1 - z)


@equation(
    latex=r"\rho = \frac{W_{\text{pair}}}{W_{\gamma}} = \frac{2 \alpha}{3 \pi}     \int_{2m_e}^E \,\mathrm{d}{M_{ee}} \left(\frac{k'}{k}\right) \frac{(E+M_R)^2 + M_R^2 -M_{ee}^2}{(E+M_R)^2 + M_R^2}    \\\cdot    \sqrt{ 1 - \frac{4 m_e^2}{M_{ee}^2}} \left( 1 + \frac{2 m_e^2}{M_{ee}^2}\right)    \left[ \frac{R_T}{M_{ee}} + \frac{2(E+M_R)^2 M_{ee} }{(2EM_R +E^2 + M_{ee}^2)^2}R_L\right]"
)
def equation_2_1(
    rho=sympy.Symbol("rho"),
    W_pair=sympy.Symbol("W_pair"),
    W_gamma=sympy.Symbol("W_gamma"),
    alpha=sympy.Symbol("alpha"),
    m_e=sympy.Symbol("m_e"),
    E=sympy.Symbol("E"),
    M_ee=sympy.Symbol("M_ee"),
    k_prime=sympy.Symbol("k_prime"),
    k=sympy.Symbol("k"),
    M_R=sympy.Symbol("M_R"),
    R_T=sympy.Symbol("R_T"),
    R_L=sympy.Symbol("R_L"),
):
    ratio = W_pair / W_gamma
    integrand = (
        (k_prime / k)
        * ((E + M_R) ** 2 + M_R**2 - M_ee**2)
        / ((E + M_R) ** 2 + M_R**2)
        * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
        * (1 + 2 * m_e**2 / M_ee**2)
        * (
            R_T / M_ee
            + 2 * (E + M_R) ** 2 * M_ee / ((2 * E * M_R + E**2 + M_ee**2) ** 2) * R_L
        )
    )
    integral_form = (
        2 * alpha / (3 * sympy.pi) * sympy.Integral(integrand, (M_ee, 2 * m_e, E))
    )
    return (sympy.Eq(rho, ratio), sympy.Eq(ratio, integral_form))


@equation(
    latex=r"p^2 = M_{ee}^2 = 2m_e^2 + 2 p_1\cdot{}p_2 =  2m_e^2 + 2  ( z (1-z) p^2 - k_T^2 - (2z-1) p\cdot{}k_T)"
)
def equation_2_13(
    p=sympy.Symbol("p"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    p_dot_p2=sympy.Symbol("p_dot_p2"),  # p·p_2
    p_dot_kT=sympy.Symbol("p_dot_kT"),  # p·k_T
    z=sympy.Symbol("z"),
    k_T=sympy.Symbol("k_T"),
):
    lhs = p**2
    middle = 2 * m_e**2 + 2 * p_dot_p2
    rhs = 2 * m_e**2 + 2 * (z * (1 - z) * p**2 - k_T**2 - (2 * z - 1) * p_dot_kT)
    return (sympy.Eq(lhs, M_ee**2), sympy.Eq(M_ee**2, middle), sympy.Eq(middle, rhs))


@equation(latex=r"p_1^2 = m_e^2 = z^2 p^2 + k_T^2 + 2 z p \cdot{} k_T")
def equation_2_14(
    p_1=sympy.Symbol("p_1"),
    m_e=sympy.Symbol("m_e"),
    z=sympy.Symbol("z"),
    p=sympy.Symbol("p"),
    p_dot_kT=sympy.Symbol("p_dot_kT"),  # p·k_T
    k_T=sympy.Symbol("k_T"),
):
    return sympy.Eq(p_1**2, m_e**2), sympy.Eq(
        m_e**2, z**2 * p**2 + k_T**2 + 2 * z * p_dot_kT
    )


@equation(
    latex=r"M_{ee}^2 =  2m_e^2 + 2  ( z (1-z) M_{ee}^2 - k_T^2 ) - \frac{2z-1}{z}  (m_e^2 - z^2 M_{ee}^2  - k_T^2  )"
)
def equation_2_15(
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    z=sympy.Symbol("z"),
    k_T=sympy.Symbol("k_T"),
):
    rhs = (
        2 * m_e**2
        + 2 * (z * (1 - z) * M_ee**2 - k_T**2)
        - (2 * z - 1) / z * (m_e**2 - z**2 * M_ee**2 - k_T**2)
    )
    return sympy.Eq(M_ee**2, rhs)


@equation(
    latex=r"z = \frac 1 2  \pm \frac 1 2  \sqrt{ 1 - 4 \frac{m_e^2}{M_{ee}^2} + 4k_T^2 }"
)
def equation_2_16(
    z=sympy.Symbol("z"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
    k_T=sympy.Symbol("k_T"),
):
    sqrt_term = sympy.sqrt(1 - 4 * m_e**2 / M_ee**2 + 4 * k_T**2)
    z_plus = sympy.Rational(1, 2) + sympy.Rational(1, 2) * sqrt_term
    z_minus = sympy.Rational(1, 2) - sympy.Rational(1, 2) * sqrt_term
    return (sympy.Eq(z, z_plus), sympy.Eq(z, z_minus))


@equation(
    latex=r"\frac{\,\mathrm{d} \mathcal P_{\gamma \to ee}}{\,\mathrm{d} M_{ee}^2}  =\frac{\alpha e_e^2}{3\pi} \frac{1}{M_{ee}^2}  \left(  1  + \frac{m_e^2}{M_{ee}^2}\right)  \sqrt{1 - \frac{4 m_{e}^{2}}{M_{ee}^{2}}}"
)
def equation_2_17(
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
    dP_gamma_to_ee=sympy.Symbol("dP_gamma_to_ee"),
    dM_ee_sq=sympy.Symbol("dM_ee_sq"),
):
    lhs = dP_gamma_to_ee / dM_ee_sq
    rhs = (
        alpha
        * e_e**2
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * (1 + m_e**2 / M_ee**2)
        * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
    )
    return sympy.Eq(lhs, rhs)


@equation(
    latex=r"\approx \frac{\alpha e_e^2}{3\pi} \frac{1}{M_{ee}^2}  \,\mathrm{d} N_{\gamma^*} \left( 1 - \frac{m_e^2}{M_{ee}^2} - 4 \frac{m_e^4}{M_{ee}^4} \right)"
)
def equation_2_18(
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    dN_gamma_star=sympy.Symbol("dN_gamma_star"),
):
    rhs = (
        alpha
        * e_e**2
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * dN_gamma_star
        * (1 - m_e**2 / M_ee**2 - 4 * m_e**4 / M_ee**4)
    )
    return rhs


@equation(
    latex=r"P_{\gamma\to ee}^m = e_e^2 \left( 1- 2z+ 2z^2 + 2\frac{m_e^2}{M_{ee}^2}\right)"
)
def equation_2_19(
    P_gamma_to_ee=sympy.Symbol("P_gamma_to_ee"),
    e_e=sympy.Symbol("e_e"),
    z=sympy.Symbol("z"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
):
    rhs = e_e**2 * (1 - 2 * z + 2 * z**2 + 2 * m_e**2 / M_ee**2)
    return sympy.Eq(P_gamma_to_ee, rhs)


@equation(
    latex=r"\frac{1}{N_{\gamma^*}} \frac{\,\mathrm{d} N_{ee}}{\,\mathrm{d} M_{ee}} = \frac{2 \alpha}{3 \pi} \frac{1}{M_{ee}} \sqrt{ 1 - \frac{4 m_e^2}{M_{ee}^2}} \left( 1 + \frac{2 m_e^2}{M_{ee}^2}\right)S\approx \frac{1}{M_{ee}}"
)
def equation_2_2(
    N_gamma_star=sympy.Symbol("N_gamma_star"),
    dN_ee=sympy.Symbol("dN_ee"),
    dM_ee=sympy.Symbol("dM_ee"),
    alpha=sympy.Symbol("alpha"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    S=sympy.Symbol("S"),
):
    lhs = (1 / N_gamma_star) * (dN_ee / dM_ee)
    middle = (
        2
        * alpha
        / (3 * sympy.pi)
        * (1 / M_ee)
        * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
        * (1 + 2 * m_e**2 / M_ee**2)
        * S
    )
    rhs = 1 / M_ee
    return (sympy.Eq(lhs, middle), sympy.Eq(middle, rhs))


@equation(
    latex=r"\frac{\,\mathrm{d} \mathcal P^m_{\gamma \to ee}}{\,\mathrm{d} M_{ee}^2}  = \frac{\alpha}{2\pi} \frac{1}{M_{ee}^2}  \int_{y_{-}}^{y_+}P^m_{\gamma \to ee}(z) \,\mathrm{d} z"
)
def equation_2_20(
    alpha=sympy.Symbol("alpha"),
    M_ee=sympy.Symbol("M_ee"),
    y_minus=sympy.Symbol("y_minus"),
    y_plus=sympy.Symbol("y_plus"),
    z=sympy.Symbol("z"),
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
    dP_gamma_to_ee=sympy.Symbol("dP_gamma_to_ee"),
    dM_ee_sq=sympy.Symbol("dM_ee_sq"),
):
    lhs = dP_gamma_to_ee / dM_ee_sq
    rhs = (
        alpha
        / (2 * sympy.pi)
        * (1 / M_ee**2)
        * sympy.Integral(P_gamma_to_ee(z), (z, y_minus, y_plus))
    )
    return sympy.Eq(lhs, rhs)


@equation(
    latex=r"=\frac{\alpha e_e^2}{3\pi} \frac{1}{M_{ee}^2}  \left(  1  + 2\frac{m_e^2}{M_{ee}^2}\right)  \sqrt{1 - \frac{4 m_{e}^{2}}{M_{ee}^{2}}}"
)
def equation_2_21(
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
):
    rhs = (
        alpha
        * e_e**2
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * (1 + 2 * m_e**2 / M_ee**2)
        * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
    )
    return rhs


@equation(latex=r"M_{ee}^2 = Q^2 = \frac{p_T^2}{z(1-z)}")
def equation_2_22(
    M_ee=sympy.Symbol("M_ee"),
    Q=sympy.Symbol("Q"),
    p_T=sympy.Symbol("p_T"),
    z=sympy.Symbol("z"),
):
    return (sympy.Eq(M_ee**2, Q**2), sympy.Eq(Q**2, p_T**2 / (z * (1 - z))))


@equation(
    latex=r"\,\mathrm{d} \Phi^{\text{FF}}_\text{ant} = \frac{1}{16 \pi^2} f^{\text{FF}}_\text{Källén} s_{IK} \Theta(\Gamma_{ijk}) \,\mathrm{d} y_{ij} \,\mathrm{d} y_{jk}  \frac{\,\mathrm{d} \phi}{2 \pi}"
)
def equation_2_23(
    dPhi_FF_ant=sympy.Symbol("dPhi_FF_ant"),
    f_FF_Kallen=sympy.Symbol("f_FF_Kallen"),
    s_IK=sympy.Symbol("s_IK"),
    Gamma_ijk=sympy.Symbol("Gamma_ijk"),
    dy_ij=sympy.Symbol("dy_ij"),
    dy_jk=sympy.Symbol("dy_jk"),
    dphi=sympy.Symbol("dphi"),
):
    rhs = (
        (1 / (16 * sympy.pi**2))
        * f_FF_Kallen
        * s_IK
        * sympy.Heaviside(Gamma_ijk, 1)
        * dy_ij
        * dy_jk
        * (dphi / (2 * sympy.pi))
    )
    return sympy.Eq(dPhi_FF_ant, rhs)


@equation(
    latex=r"\bar{a}_{e/\gamma}^{\text{FF},\gamma} = \frac{1}{s_{IK}} \frac 1 2 \frac{1}{y_{ij} + 2 \mu_e^2} \left[y_{ik}^2 + y_{jk}^2 + \frac{2 \mu_e^2}{y_{ij} + 2 \mu_e^2}\right]"
)
def equation_2_24(
    a_bar_e_gamma=sympy.Symbol("a_bar_e_gamma"),
    s_IK=sympy.Symbol("s_IK"),
    y_ij=sympy.Symbol("y_ij"),
    y_ik=sympy.Symbol("y_ik"),
    y_jk=sympy.Symbol("y_jk"),
    mu_e=sympy.Symbol("mu_e"),
):
    rhs = (
        (1 / s_IK)
        * sympy.Rational(1, 2)
        * (1 / (y_ij + 2 * mu_e**2))
        * (y_ik**2 + y_jk**2 + 2 * mu_e**2 / (y_ij + 2 * mu_e**2))
    )
    return sympy.Eq(a_bar_e_gamma, rhs)


@equation(
    latex=r"\frac{\,\mathrm{d} \mathcal P_{\gamma \to ee}^m}{\,\mathrm{d} M_{ee}^2} \propto 4 \pi \alpha e_e^2 \frac 1 2 \frac{1}{M_{ee}^2} \left[y_{ik}^2 + y_{jk}^2 + \frac{2 m_e^2}{M_{ee}^2}\right] \frac{1}{16 \pi^2} f^{\text{FF}}_\text{Källén} \Theta(\Gamma_{ijk}) \,\mathrm{d} y_{jk}  \frac{\,\mathrm{d} \phi}{2 \pi}"
)
def equation_2_25(
    dP_gamma_to_ee=sympy.Symbol("dP_gamma_to_ee"),
    dM_ee_sq=sympy.Symbol("dM_ee_sq"),
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    M_ee=sympy.Symbol("M_ee"),
    y_ik=sympy.Symbol("y_ik"),
    y_jk=sympy.Symbol("y_jk"),
    m_e=sympy.Symbol("m_e"),
    f_FF_Kallen=sympy.Symbol("f_FF_Kallen"),
    Gamma_ijk=sympy.Symbol("Gamma_ijk"),
    dy_jk=sympy.Symbol("dy_jk"),
    dphi=sympy.Symbol("dphi"),
):
    lhs = dP_gamma_to_ee / dM_ee_sq
    rhs = (
        4
        * sympy.pi
        * alpha
        * e_e**2
        * sympy.Rational(1, 2)
        * (1 / M_ee**2)
        * (y_ik**2 + y_jk**2 + 2 * m_e**2 / M_ee**2)
        * (1 / (16 * sympy.pi**2))
        * f_FF_Kallen
        * sympy.Heaviside(Gamma_ijk, 1)
        * dy_jk
        * (dphi / (2 * sympy.pi))
    )
    return sympy.Eq(lhs, rhs)  # Note: using Eq instead of proportional


@equation(
    latex=r"0< \Gamma_{ijk} = y_{ij} y_{jk} y_{ik} - y_{jk} \mu_i^2 - y_{ik} \mu_j^2"
)
def equation_2_26(
    Gamma_ijk=sympy.Symbol("Gamma_ijk"),
    y_ij=sympy.Symbol("y_ij"),
    y_jk=sympy.Symbol("y_jk"),
    y_ik=sympy.Symbol("y_ik"),
    mu_i=sympy.Symbol("mu_i"),
    mu_j=sympy.Symbol("mu_j"),
):
    rhs = y_ij * y_jk * y_ik - y_jk * mu_i**2 - y_ik * mu_j**2
    return (sympy.Gt(0, Gamma_ijk), sympy.Eq(Gamma_ijk, rhs))


@equation(latex=r"z = \frac 1 2 \pm \frac 1 2 \sqrt{1-\frac{4m_e^2}{M_{ee}^2}}")
def equation_2_27(
    z=sympy.Symbol("z"),
    m_e=sympy.Symbol("m_e"),
    M_ee=sympy.Symbol("M_ee"),
):
    sqrt_term = sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
    z_plus = sympy.Rational(1, 2) + sympy.Rational(1, 2) * sqrt_term
    z_minus = sympy.Rational(1, 2) - sympy.Rational(1, 2) * sqrt_term
    return (sympy.Eq(z, z_plus), sympy.Eq(z, z_minus))


@equation(latex=r"1 = y_{ij} + 2 \mu_e^2 + y_{jk} + y_{ik}")
def equation_2_28(
    y_ij=sympy.Symbol("y_ij"),
    mu_e=sympy.Symbol("mu_e"),
    y_jk=sympy.Symbol("y_jk"),
    y_ik=sympy.Symbol("y_ik"),
):
    return sympy.Eq(1, y_ij + 2 * mu_e**2 + y_jk + y_ik)


@equation(
    latex=r"y_\pm =  \frac{\pm\sqrt{\left(M_{ee}^{2} - 2 m_{e}^{2}\right)^{-1} \left(M_{ee}^{2} - s\right) \left(M_{ee}^{4} - 2 M_{ee}^{2} m_{e}^{2} - M_{ee}^{2} s + 6 m_{e}^{2} s\right)} + \left(- M_{ee}^{2} + s\right) }{2 s }"
)
def equation_2_29(
    y_plus=sympy.Symbol("y_plus"),
    y_minus=sympy.Symbol("y_minus"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    s=sympy.Symbol("s"),
):
    discriminant = (
        (M_ee**2 - 2 * m_e**2) ** (-1)
        * (M_ee**2 - s)
        * (M_ee**4 - 2 * M_ee**2 * m_e**2 - M_ee**2 * s + 6 * m_e**2 * s)
    )
    sqrt_term = sympy.sqrt(discriminant)
    common_term = (-(M_ee**2) + s) / (2 * s)

    y_plus_val = sqrt_term + common_term
    y_minus_val = -sqrt_term + common_term

    return (sympy.Eq(y_plus, y_plus_val), sympy.Eq(y_minus, y_minus_val))


@equation(
    latex=r"\frac{\,\mathrm{d}^2 N_{ee}}{\,\mathrm{d} M_{ee}^2} = \frac{\alpha}{3 \pi} \frac{1}{M_{ee}^2}  \sqrt{ 1 - \frac{4 m_e^2}{M_{ee}^2}} \left( 1 + \frac{2 m_e^2}{M_{ee}^2}\right) \,\mathrm{d} N_{\gamma^*}"
)
def equation_2_3(
    d2N_ee=sympy.Symbol("d2N_ee"),
    dM_ee_sq=sympy.Symbol("dM_ee_sq"),
    alpha=sympy.Symbol("alpha"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    dN_gamma_star=sympy.Symbol("dN_gamma_star"),
):
    lhs = d2N_ee / dM_ee_sq
    rhs = (
        alpha
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * sympy.sqrt(1 - 4 * m_e**2 / M_ee**2)
        * (1 + 2 * m_e**2 / M_ee**2)
        * dN_gamma_star
    )
    return sympy.Eq(lhs, rhs)


@equation(
    latex=r"\frac{\,\mathrm{d} \mathcal P_{\gamma \to ee}}{\,\mathrm{d} M_{ee}^2}  =\frac{\alpha e_e^2}{3\pi} \frac{1}{M_{ee}^2}  \left( 1 - \frac{M_{ee}^2}{s}\right)^3"
)
def equation_2_31(
    dP_gamma_to_ee=sympy.Symbol("dP_gamma_to_ee"),
    dM_ee_sq=sympy.Symbol("dM_ee_sq"),
    alpha=sympy.Symbol("alpha"),
    e_e=sympy.Symbol("e_e"),
    M_ee=sympy.Symbol("M_ee"),
    s=sympy.Symbol("s"),
):
    lhs = dP_gamma_to_ee / dM_ee_sq
    rhs = alpha * e_e**2 / (3 * sympy.pi) * (1 / M_ee**2) * (1 - M_ee**2 / s) ** 3
    return sympy.Eq(lhs, rhs)


@equation(
    latex=r"\approx \frac{\alpha}{3\pi} \frac{1}{M_{ee}^2} \left( 1 - 6 \frac{m_e^4}{M_{ee}^4} - 8 \frac{m_e^6}{M_{ee}^6} \right)  \,\mathrm{d} N_{\gamma^*}"
)
def equation_2_4(
    alpha=sympy.Symbol("alpha"),
    M_ee=sympy.Symbol("M_ee"),
    m_e=sympy.Symbol("m_e"),
    dN_gamma_star=sympy.Symbol("dN_gamma_star"),
):
    rhs = (
        alpha
        / (3 * sympy.pi)
        * (1 / M_ee**2)
        * (1 - 6 * m_e**4 / M_ee**4 - 8 * m_e**6 / M_ee**6)
        * dN_gamma_star
    )
    return rhs


@equation(latex=r"P_{g \to qq}(z) =  T_F ( z^2 + (1-z)^2)")
def equation_2_5(
    P_g_to_qq=sympy.Function("P_g_to_qq"),
    T_F=sympy.Symbol("T_F"),
    z=sympy.Symbol("z"),
):
    rhs = T_F * (z**2 + (1 - z) ** 2)
    return sympy.Eq(P_g_to_qq(z), rhs)


@equation(latex=r"P_{\gamma \to ee}(z) =  e_e^2 ( z^2 + (1-z)^2)")
def equation_2_6(
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
    e_e=sympy.Symbol("e_e"),
    z=sympy.Symbol("z"),
):
    rhs = e_e**2 * (z**2 + (1 - z) ** 2)
    return sympy.Eq(P_gamma_to_ee(z), rhs)


@equation(
    latex=r"\,\mathrm{d} \mathcal P_{\gamma \to ee} = \frac{\alpha}{2\pi} \frac{\,\mathrm{d} Q^2}{Q^2}  P_{\gamma \to ee}(z) \,\mathrm{d} z"
)
def equation_2_7(
    dP_gamma_to_ee=sympy.Symbol("dP_gamma_to_ee"),
    alpha=sympy.Symbol("alpha"),
    dQ_sq=sympy.Symbol("dQ_sq"),
    Q=sympy.Symbol("Q"),
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
    z=sympy.Symbol("z"),
    dz=sympy.Symbol("dz"),
):
    rhs = alpha / (2 * sympy.pi) * (dQ_sq / Q**2) * P_gamma_to_ee(z) * dz
    return sympy.Eq(dP_gamma_to_ee, rhs)


@equation(
    latex=r"\frac{\,\mathrm{d} \mathcal P_{\gamma \to ee}}{\,\mathrm{d} M_{ee}^2} = \frac{\alpha}{2\pi} \frac{1}{M_{ee}^2}  P_{\gamma \to ee}(z) \,\mathrm{d} z"
)
def equation_2_8(
    dP_gamma_to_ee=sympy.Symbol("dP_gamma_to_ee"),
    dM_ee_sq=sympy.Symbol("dM_ee_sq"),
    alpha=sympy.Symbol("alpha"),
    M_ee=sympy.Symbol("M_ee"),
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
    z=sympy.Symbol("z"),
    dz=sympy.Symbol("dz"),
):
    lhs = dP_gamma_to_ee / dM_ee_sq
    rhs = alpha / (2 * sympy.pi) * (1 / M_ee**2) * P_gamma_to_ee(z) * dz
    return sympy.Eq(lhs, rhs)


@equation(
    latex=r"\frac{\,\mathrm{d} \mathcal P_{\gamma \to ee}}{\,\mathrm{d} M_{ee}^2}  = \frac{\alpha}{2\pi} \frac{1}{M_{ee}^2}  \int_{y_{-}}^{y_+}P_{\gamma \to ee}(z) \,\mathrm{d} z"
)
def equation_2_9(
    dP_gamma_to_ee=sympy.Symbol("dP_gamma_to_ee"),
    dM_ee_sq=sympy.Symbol("dM_ee_sq"),
    alpha=sympy.Symbol("alpha"),
    M_ee=sympy.Symbol("M_ee"),
    y_minus=sympy.Symbol("y_minus"),
    y_plus=sympy.Symbol("y_plus"),
    P_gamma_to_ee=sympy.Function("P_gamma_to_ee"),
    z=sympy.Symbol("z"),
):
    lhs = dP_gamma_to_ee / dM_ee_sq
    rhs = (
        alpha
        / (2 * sympy.pi)
        * (1 / M_ee**2)
        * sympy.Integral(P_gamma_to_ee(z), (z, y_minus, y_plus))
    )
    return sympy.Eq(lhs, rhs)
