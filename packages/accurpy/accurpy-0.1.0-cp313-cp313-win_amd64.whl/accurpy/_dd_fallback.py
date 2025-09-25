\
# -*- coding: utf-8 -*-
# Python DD fallback (STRICT) – identical operation ordering

from math import copysign, fabs, ldexp, sqrt

_SPLITTER = 134217729.0  # 2^27 + 1

def _two_sum(a: float, b: float):
    s = a + b
    bb = s - a
    err = (a - (s - bb)) + (b - bb)
    return s, err

def _split(a: float):
    c = _SPLITTER * a
    a_hi = c - (c - a)
    a_lo = a - a_hi
    return a_hi, a_lo

def _two_prod(a: float, b: float):
    p = a * b
    a_hi, a_lo = _split(a)
    b_hi, b_lo = _split(b)
    err = ((a_hi * b_hi - p) + a_hi * b_lo + a_lo * b_hi) + a_lo * b_lo
    return p, err

def _dd_normalize(hi: float, lo: float):
    s, e = _two_sum(hi, lo)
    return s, e

def _dd_add_dd(a_hi, a_lo, b_hi, b_lo):
    s, e = _two_sum(a_hi, b_hi)
    t, f = _two_sum(a_lo, b_lo)
    u, g = _two_sum(e, t)
    v, h = _two_sum(s, u)
    return _dd_normalize(v, (f + g) + h)

def _dd_add_d(a_hi, a_lo, c):
    s, e = _two_sum(a_hi, c)
    return _dd_normalize(s, a_lo + e)

def _dd_sub_dd(a_hi, a_lo, b_hi, b_lo):
    return _dd_add_dd(a_hi, a_lo, -b_hi, -b_lo)

def _dd_mul_d(a_hi, a_lo, x):
    p, pe = _two_prod(a_hi, x)
    q = a_lo * x
    s, se = _two_sum(pe, q)
    hi, lo = _two_sum(p, s)
    return _dd_normalize(hi, lo + se)

def _dd_mul_dd(a_hi, a_lo, b_hi, b_lo):
    p, pe = _two_prod(a_hi, b_hi)
    q1 = a_hi * b_lo
    q2 = a_lo * b_hi
    s, se = _two_sum(pe, q1 + q2)
    hi, lo = _two_sum(p, s)
    return _dd_normalize(hi, lo + se + a_lo * b_lo)

def _dd_div_dd(a_hi, a_lo, b_hi, b_lo):
    q1 = a_hi / b_hi
    t_hi, t_lo = _dd_mul_d(b_hi, b_lo, q1)
    r_hi, r_lo = _dd_sub_dd(a_hi, a_lo, t_hi, t_lo)
    q2 = (r_hi + r_lo) / b_hi
    return _dd_add_d(q1, 0.0, q2)

def _dd_div_d(a_hi, a_lo, d):
    q1 = a_hi / d
    t_hi, t_lo = _dd_mul_d(d, 0.0, q1)
    r_hi, r_lo = _dd_sub_dd(a_hi, a_lo, t_hi, t_lo)
    q2 = (r_hi + r_lo) / d
    return _dd_add_d(q1, 0.0, q2)

def _dd_ldexp(a_hi, a_lo, n):
    return _dd_normalize(ldexp(a_hi, n), ldexp(a_lo, n))

def _dd_to_double_rn(hi, lo):
    s, _ = _two_sum(hi, lo)
    return s

def _dd_sqrt_one_step_from_double(a: float):
    y = sqrt(a)
    y_hi, y_lo = y, 0.0
    ay_hi, ay_lo = _dd_div_dd(a, 0.0, y_hi, y_lo)
    s_hi, s_lo = _dd_add_dd(y_hi, y_lo, ay_hi, ay_lo)
    return _dd_mul_d(s_hi, s_lo, 0.5)

def _cbrt_seed_double(x: float):
    return copysign(abs(x) ** (1.0 / 3.0), x)

def _dd_cbrt_two_steps_from_dd(a_hi: float, a_lo: float):
    y0 = _cbrt_seed_double(a_hi)
    y_hi, y_lo = y0, 0.0
    for _ in range(2):
        y2_hi, y2_lo = _dd_mul_dd(y_hi, y_lo, y_hi, y_lo)
        y3_hi, y3_lo = _dd_mul_dd(y2_hi, y2_lo, y_hi, y_lo)
        num_hi, num_lo = _dd_sub_dd(y3_hi, y3_lo, a_hi, a_lo)
        den_hi, den_lo = _dd_mul_d(y2_hi, y2_lo, 3.0)
        corr_hi, corr_lo = _dd_div_dd(num_hi, num_lo, den_hi, den_lo)
        y_hi, y_lo = _dd_sub_dd(y_hi, y_lo, corr_hi, corr_lo)
    return y_hi, y_lo

P_DD = [
  ( 1.8749082122049241,  3.798113512403328e-17),
  (-9.1222716817901741, -6.6351487245618461e-16),
  (17.586727655830863,   1.4804514541980087e-15),
  (-16.102588313401167,  1.2197047530118353e-15),
  ( 5.6177013015037156,  3.1973984685436460e-16),
  ( 1.1481950515634161, -1.0503578270005708e-16),
  (-0.8030753035650664,  1.6654409999873632e-17),
  (-0.47057420513667686,-1.7827539364823433e-17),
  ( 0.24973974165973462,-1.2642073177291289e-17),
  ( 0.050913557712850249,-3.3918202116485434e-18),
  (-0.024537324494281674, 1.3502110126972669e-18),
  (-0.0075528294186967574,1.5987425304577664e-19),
  ( 0.0021739332538168398,-1.7223466435509686e-19),
  ( 0.00030955310077826346,-4.7675826884737134e-21),
  (-6.2549286976660982e-05,-5.9300107318619718e-21),
]
Q_DD = [
  ( 1.0,                   0.0),
  (-4.6347432604662329,   -8.8788973131530606e-17),
  ( 8.3662736165283516,    2.4809733777669983e-16),
  (-6.9140176143937149,   -2.0123272215843871e-16),
  ( 1.8857923466608759,    1.5304275522883476e-17),
  ( 0.55013805902549406,   3.1899845225272705e-17),
  ( 0.025525626894088164, -1.3039113529010309e-18),
  (-0.42183191476812748,   1.1574969665396163e-17),
  ( 0.12395101647676726,   4.8580299607974401e-18),
  ( 0.027213151947812902, -6.9012823202960699e-19),
  (-0.0032033317996006737,-1.9061636095185189e-19),
  (-0.0063433832421557782,-1.3417812337405574e-19),
  ( 0.001185878206541492, -5.6958565678840369e-21),
  (  7.60079159202465e-05, -4.7583995752306207e-21),
  (-1.0773580801014191e-05,-8.2099994974544744e-22),
]

def _poly14_dd_estrin_unrolled(coeffs, u_hi, u_lo):
    u2_hi, u2_lo = _dd_mul_dd(u_hi, u_lo, u_hi, u_lo)
    u4_hi, u4_lo = _dd_mul_dd(u2_hi, u2_lo, u2_hi, u2_lo)
    u8_hi, u8_lo = _dd_mul_dd(u4_hi, u4_lo, u4_hi, u4_lo)
    def lin2(i, j):
        ai, al = coeffs[i]
        bj, bl = coeffs[j]
        t_hi, t_lo = _dd_mul_dd(bj, bl, u2_hi, u2_lo)
        return _dd_add_dd(ai, al, t_hi, t_lo)
    e0_hi, e0_lo = lin2(0, 2)
    e1_hi, e1_lo = lin2(4, 6)
    e2_hi, e2_lo = lin2(8,10)
    e3_hi, e3_lo = lin2(12,14)
    t_hi, t_lo = _dd_mul_dd(e1_hi, e1_lo, u4_hi, u4_lo)
    E0_hi, E0_lo = _dd_add_dd(e0_hi, e0_lo, t_hi, t_lo)
    t_hi, t_lo = _dd_mul_dd(e3_hi, e3_lo, u4_hi, u4_lo)
    E1_hi, E1_lo = _dd_add_dd(e2_hi, e2_lo, t_hi, t_lo)
    t_hi, t_lo = _dd_mul_dd(E1_hi, E1_lo, u8_hi, u8_lo)
    Pe_hi, Pe_lo = _dd_add_dd(E0_hi, E0_lo, t_hi, t_lo)
    o0_hi, o0_lo = lin2(1, 3)
    o1_hi, o1_lo = lin2(5, 7)
    o2_hi, o2_lo = lin2(9,11)
    o3_hi, o3_lo = coeffs[13]
    t_hi, t_lo = _dd_mul_dd(o1_hi, o1_lo, u4_hi, u4_lo)
    O0_hi, O0_lo = _dd_add_dd(o0_hi, o0_lo, t_hi, t_lo)
    t_hi, t_lo = _dd_mul_dd(o3_hi, o3_lo, u4_hi, u4_lo)
    O1_hi, O1_lo = _dd_add_dd(o2_hi, o2_lo, t_hi, t_lo)
    t_hi, t_lo = _dd_mul_dd(O1_hi, O1_lo, u8_hi, u8_lo)
    Po_hi, Po_lo = _dd_add_dd(O0_hi, O0_lo, t_hi, t_lo)
    uPo_hi, uPo_lo = _dd_mul_dd(u_hi, u_lo, Po_hi, Po_lo)
    return _dd_add_dd(Pe_hi, Pe_lo, uPo_hi, uPo_lo)

_LOG2E = 1.44269504088896340735992468100189214
_LN2_HI = 0.693147180559945309417232121458176568
_LN2_LO = 2.319046813846299558417771099e-17
_INV_FACT = [1.0]
for k in range(1, 23): _INV_FACT.append(_INV_FACT[-1] / k)

def _dd_exp_reduced(r_hi: float, r_lo: float):
    val_hi, val_lo = _INV_FACT[22], 0.0
    for k in range(21, -1, -1):
        val_hi, val_lo = _dd_mul_dd(val_hi, val_lo, r_hi, r_lo)
        val_hi, val_lo = _dd_add_d(val_hi, val_lo, _INV_FACT[k])
    return val_hi, val_lo

def _dd_exp_neg(x: float):
    y = -x
    n = int(round(y * _LOG2E))
    y_hi, y_lo = y, 0.0
    t_hi, t_lo = _dd_mul_d(_LN2_HI, 0.0, n)
    r_hi, r_lo = _dd_sub_dd(y_hi, y_lo, t_hi, t_lo)
    t_hi, t_lo = _dd_mul_d(_LN2_LO, 0.0, n)
    r_hi, r_lo = _dd_sub_dd(r_hi, r_lo, t_hi, t_lo)
    er_hi, er_lo = _dd_exp_reduced(r_hi, r_lo)
    return _dd_ldexp(er_hi, er_lo, n)

_BmA = 1.0 - 2.0e-16

def _approx_core_dd(x: float):
    x_hi, x_lo = x, 0.0
    one_plus_x_hi, one_plus_x_lo = _dd_add_d(x_hi, x_lo, 1.0)
    y_hi, y_lo = _dd_div_dd(x_hi, x_lo, one_plus_x_hi, one_plus_x_lo)
    t_hi, t_lo = _dd_cbrt_two_steps_from_dd(y_hi, y_lo)
    two_t_hi, two_t_lo = _dd_mul_d(t_hi, t_lo, 2.0)
    num_hi, num_lo      = _dd_add_d(two_t_hi, two_t_lo, -1.0)
    u_hi, u_lo          = _dd_div_d(num_hi, num_lo, _BmA)
    P_hi, P_lo = _poly14_dd_estrin_unrolled(P_DD, u_hi, u_lo)
    Q_hi, Q_lo = _poly14_dd_estrin_unrolled(Q_DD, u_hi, u_lo)
    R_hi, R_lo = _dd_div_dd(P_hi, P_lo, Q_hi, Q_lo)
    t2_hi, t2_lo = _dd_mul_dd(t_hi, t_lo, t_hi, t_lo)
    sqrt_hi, sqrt_lo = _dd_sqrt_one_step_from_double(1.0 + x)
    s_hi, s_lo = _dd_mul_dd(t2_hi, t2_lo, sqrt_hi, sqrt_lo)
    return _dd_div_dd(R_hi, R_lo, s_hi, s_lo)

def approx_FM_new(x: float, skip_exp: bool = False) -> float:
    core_hi, core_lo = _approx_core_dd(x)
    if skip_exp:
        scaled_hi, scaled_lo = _dd_mul_d(core_hi, core_lo, x)
    else:
        tmp_hi, tmp_lo = _dd_mul_d(core_hi, core_lo, x)
        e_hi, e_lo     = _dd_exp_neg(x)
        scaled_hi, scaled_lo = _dd_mul_dd(tmp_hi, tmp_lo, e_hi, e_lo)
    return _dd_to_double_rn(scaled_hi, scaled_lo)
