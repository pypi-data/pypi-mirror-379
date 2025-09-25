
// src/accurpy/_fm.c
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>
#include <stdint.h>
#include <stddef.h>
#include <string.h>

#ifndef M_PI
#define M_PI 3.141592653589793238462643383279502884
#endif

#ifndef HAVE_FMA
#  if defined(__STDC_VERSION__) && (__STDC_VERSION__ >= 199901L)
#    define HAVE_FMA 1
#  endif
#endif
#ifndef HAVE_FMA
#  if defined(_MSC_VER)
#    pragma function(fma)
#  endif
static inline double fma(double a, double b, double c){ return a*b + c; }
#endif

static inline int nint_tieeven(double x){
#if defined(_MSC_VER)
    double r = nearbyint(x);
    return (int)r;
#else
    return (int)lrint(x);
#endif
}

static PyObject* alloc_double_bytearray(size_t n){
    PyObject* ba = PyByteArray_FromStringAndSize(NULL, (Py_ssize_t)(n * sizeof(double)));
    if (!ba) return NULL;
    return ba;
}

/* ---------------------- Double-double core (STRICT) ---------------------- */

typedef struct { double hi, lo; } dd;
static const double SPLITTER = 134217729.0; /* 2^27+1 */

static inline void two_sum(double a, double b, double* s, double* e){
    double sum = a + b;
    double bb = sum - a;
    double err = (a - (sum - bb)) + (b - bb);
    *s = sum; *e = err;
}
static inline void split(double a, double* hi, double* lo){
    double c = SPLITTER * a;
    double ahi = c - (c - a);
    double alo = a - ahi;
    *hi = ahi; *lo = alo;
}
static inline void two_prod(double a, double b, double* p, double* e){
    double prod = a * b;
    double a_hi, a_lo, b_hi, b_lo;
    split(a, &a_hi, &a_lo);
    split(b, &b_hi, &b_lo);
    double err = ((a_hi * b_hi - prod) + a_hi * b_lo + a_lo * b_hi) + a_lo * b_lo;
    *p = prod; *e = err;
}
static inline dd dd_norm(double hi, double lo){
    double s, e; two_sum(hi, lo, &s, &e);
    dd r = {s, e}; return r;
}
static inline dd dd_add_dd(dd A, dd B){
    double s, e; two_sum(A.hi, B.hi, &s, &e);
    double t, f; two_sum(A.lo, B.lo, &t, &f);
    double u, g; two_sum(e, t, &u, &g);
    double v, h; two_sum(s, u, &v, &h);
    return dd_norm(v, (f + g) + h);
}
static inline dd dd_add_d(dd A, double c){
    double s, e; two_sum(A.hi, c, &s, &e);
    return dd_norm(s, A.lo + e);
}
static inline dd dd_sub_dd(dd A, dd B){
    dd nB = { -B.hi, -B.lo };
    return dd_add_dd(A, nB);
}
static inline dd dd_mul_d_strict(dd A, double x){
    double p, pe; two_prod(A.hi, x, &p, &pe);
    double q = A.lo * x;
    double s, se; two_sum(pe, q, &s, &se);
    double hi, lo; two_sum(p, s, &hi, &lo);
    return dd_norm(hi, lo + se);
}
static inline dd dd_mul_dd_strict(dd A, dd B){
    double p, pe; two_prod(A.hi, B.hi, &p, &pe);
    double q1 = A.hi * B.lo;
    double q2 = A.lo * B.hi;
    double s, se; two_sum(pe, q1 + q2, &s, &se);
    double hi, lo; two_sum(p, s, &hi, &lo);
    return dd_norm(hi, lo + se + A.lo * B.lo);
}
static inline dd dd_div_dd_strict(dd A, dd B){
    double q1 = A.hi / B.hi;
    dd t = dd_mul_d_strict(B, q1);
    dd r = dd_sub_dd(A, t);
    double q2 = (r.hi + r.lo) / B.hi;
    double s, e; two_sum(q1, q2, &s, &e);
    return dd_norm(s, e);
}
static inline dd dd_div_d_strict(dd A, double d){
    double q1 = A.hi / d;
    dd t = (dd){ q1 * d, 0.0 };
    dd r = dd_sub_dd(A, t);
    double q2 = (r.hi + r.lo) / d;
    double s, e; two_sum(q1, q2, &s, &e);
    return dd_norm(s, e);
}
static inline dd dd_ldexp_strict(dd A, int n){
    return dd_norm(ldexp(A.hi, n), ldexp(A.lo, n));
}
static inline double dd_to_double_rn(dd A){
    double s, e; two_sum(A.hi, A.lo, &s, &e);
    (void)e; return s;
}
static inline dd dd_sqrt_one_step(double a){
    double y = sqrt(a);
    dd ydd = (dd){ y, 0.0 };
    dd ay  = dd_div_dd_strict((dd){a, 0.0}, ydd);
    dd s   = dd_add_dd(ydd, ay);
    return dd_mul_d_strict(s, 0.5);
}
static inline double cbrt_seed(double x){
    double ax = x < 0 ? -x : x;
    double y = pow(ax, 1.0/3.0);
    return x < 0 ? -y : y;
}
static inline dd dd_cbrt_two_steps(dd a){
    double y0 = cbrt_seed(a.hi);
    dd y = (dd){ y0, 0.0 };
    for (int i=0;i<2;i++){
        dd y2 = dd_mul_dd_strict(y,y);
        dd y3 = dd_mul_dd_strict(y2,y);
        dd num = dd_sub_dd(y3, a);
        dd den = dd_mul_d_strict(y2, 3.0);
        dd corr = dd_div_dd_strict(num, den);
        y = dd_sub_dd(y, corr);
    }
    return y;
}

/* ---------------------- Double-double (OPT path) ---------------------- */

static inline dd dd_add_dd_opt(dd A, dd B){
    return dd_add_dd(A,B);
}
static inline dd dd_add_d_opt(dd A, double c){
    return dd_add_d(A,c);
}
static inline dd dd_mul_dd_opt(dd A, dd B){
    double p1 = A.hi * B.hi;
    double p2 = fma(A.hi, B.hi, -p1);
    p2 += A.hi * B.lo + A.lo * B.hi;
    double s1 = p1 + p2;
    double s2 = p2 - (s1 - p1);
    s2 += A.lo * B.lo;
    return dd_norm(s1, s2);
}
static inline dd dd_mul_d_opt(dd A, double x){
    double p1 = A.hi * x;
    double p2 = fma(A.hi, x, -p1);
    p2 += A.lo * x;
    double s1 = p1 + p2;
    double s2 = p2 - (s1 - p1);
    return dd_norm(s1, s2);
}
static inline dd dd_div_dd_opt(dd A, dd B){
    double q1 = A.hi / B.hi;
    dd t = dd_mul_d_opt(B, q1);
    dd r = dd_sub_dd(A, t);
    double q2 = (r.hi + r.lo) / B.hi;
    double s1 = q1 + q2;
    double s2 = q2 - (s1 - q1);
    return dd_norm(s1, s2);
}
static inline dd dd_div_d_opt(dd A, double d){
    double q1 = A.hi / d;
    dd t = (dd){ q1 * d, 0.0 };
    dd r = dd_sub_dd(A, t);
    double q2 = (r.hi + r.lo) / d;
    double s1 = q1 + q2;
    double s2 = q2 - (s1 - q1);
    return dd_norm(s1, s2);
}
static inline dd dd_ldexp_opt(dd A, int n){
    return dd_norm(ldexp(A.hi, n), ldexp(A.lo, n));
}
static inline dd dd_cbrt_one_step(dd a){
    double y0 = cbrt(a.hi);
    dd y = (dd){ y0, 0.0 };
    dd y2 = dd_mul_dd_opt(y,y);
    dd y3 = dd_mul_dd_opt(y2,y);
    dd num = dd_sub_dd(y3, a);
    dd den = dd_mul_d_opt(y2, 3.0);
    dd corr = dd_div_dd_opt(num, den);
    y = dd_sub_dd(y, corr);
    return y;
}

/* ---------------------- Coefficients ---------------------- */

typedef struct { double hi, lo; } ddcoef;
static const ddcoef P_DD[15] = {
  {  1.8749082122049241,              3.798113512403328e-17 },
  { -9.1222716817901741,             -6.6351487245618461e-16 },
  { 17.586727655830863,               1.4804514541980087e-15 },
  { -16.102588313401167,              1.2197047530118353e-15 },
  {  5.6177013015037156,              3.1973984685436460e-16 },
  {  1.1481950515634161,             -1.0503578270005708e-16 },
  { -0.8030753035650664,              1.6654409999873632e-17 },
  { -0.47057420513667686,            -1.7827539364823433e-17 },
  {  0.24973974165973462,            -1.2642073177291289e-17 },
  {  0.050913557712850249,           -3.3918202116485434e-18 },
  { -0.024537324494281674,            1.3502110126972669e-18 },
  { -0.0075528294186967574,           1.5987425304577664e-19 },
  {  0.0021739332538168398,          -1.7223466435509686e-19 },
  {  0.00030955310077826346,         -4.7675826884737134e-21 },
  { -6.2549286976660982e-05,         -5.9300107318619718e-21 }
};
static const ddcoef Q_DD[15] = {
  {  1.0,                              0.0 },
  { -4.6347432604662329,             -8.8788973131530606e-17 },
  {  8.3662736165283516,              2.4809733777669983e-16 },
  { -6.9140176143937149,             -2.0123272215843871e-16 },
  {  1.8857923466608759,              1.5304275522883476e-17 },
  {  0.55013805902549406,             3.1899845225272705e-17 },
  {  0.025525626894088164,           -1.3039113529010309e-18 },
  { -0.42183191476812748,             1.1574969665396163e-17 },
  {  0.12395101647676726,             4.8580299607974401e-18 },
  {  0.027213151947812902,           -6.9012823202960699e-19 },
  { -0.0032033317996006737,          -1.9061636095185189e-19 },
  { -0.0063433832421557782,          -1.3417812337405574e-19 },
  {  0.001185878206541492,           -5.6958565678840369e-21 },
  {  7.60079159202465e-05,           -4.7583995752306207e-21 },
  { -1.0773580801014191e-05,         -8.2099994974544744e-22 }
};

static inline dd dd_from_coef(ddcoef c){ dd r = {c.hi, c.lo}; return r; }

static inline dd poly14_dd_estrin(const ddcoef* c, dd u,
                                  dd (*mul)(dd,dd),
                                  dd (*add_dd)(dd,dd)){
    dd u2 = mul(u,u);
    dd u4 = mul(u2,u2);
    dd u8 = mul(u4,u4);

    dd e0 = add_dd(dd_from_coef(c[0]), mul(dd_from_coef(c[2]), u2));
    dd e1 = add_dd(dd_from_coef(c[4]), mul(dd_from_coef(c[6]), u2));
    dd e2 = add_dd(dd_from_coef(c[8]), mul(dd_from_coef(c[10]),u2));
    dd e3 = add_dd(dd_from_coef(c[12]),mul(dd_from_coef(c[14]),u2));
    dd E0 = add_dd(e0, mul(e1, u4));
    dd E1 = add_dd(e2, mul(e3, u4));
    dd Pe = add_dd(E0, mul(E1, u8));

    dd o0 = add_dd(dd_from_coef(c[1]), mul(dd_from_coef(c[3]), u2));
    dd o1 = add_dd(dd_from_coef(c[5]), mul(dd_from_coef(c[7]), u2));
    dd o2 = add_dd(dd_from_coef(c[9]), mul(dd_from_coef(c[11]),u2));
    dd o3 = dd_from_coef(c[13]);
    dd O0 = add_dd(o0, mul(o1, u4));
    dd O1 = add_dd(o2, mul(o3, u4));
    dd Po = add_dd(O0, mul(O1, u8));

    dd uPo = mul(u, Po);
    return add_dd(Pe, uPo);
}

/* ---------------------- exp(-x) in DD ---------------------- */

static const double LOG2E = 1.44269504088896340735992468100189214;
static const double LN2_HI = 0.693147180559945309417232121458176568;
static const double LN2_LO = 2.319046813846299558417771099e-17;

static inline dd dd_exp_reduced_strict(dd r){
    static const double INV_FACT[23] = {
      1.0,1.0,5e-1,1.6666666666666667e-1,4.1666666666666667e-2,8.3333333333333333e-3,
      1.3888888888888889e-3,1.9841269841269841e-4,2.4801587301587302e-5,2.7557319223985891e-6,
      2.7557319223985891e-7,2.5052108385441719e-8,2.0876756987868099e-9,1.6059043836821615e-10,
      1.1470745597729725e-11,7.6471637318198165e-13,4.7794773323873853e-14,2.8114572543455208e-15,
      1.5619206968586226e-16,8.2206352466243297e-18,4.1103176233121649e-19,1.9572941063391261e-20,
      8.8967913924505733e-22
    };
    dd val = (dd){ INV_FACT[22], 0.0 };
    for (int k=21;k>=0;--k){
        val = dd_mul_dd_strict(val, r);
        val = dd_add_d(val, INV_FACT[k]);
    }
    return val;
}
static inline dd dd_exp_reduced_opt(dd r){
    static const double INV_FACT[23] = {
      1.0,1.0,5e-1,1.6666666666666667e-1,4.1666666666666667e-2,8.3333333333333333e-3,
      1.3888888888888889e-3,1.9841269841269841e-4,2.4801587301587302e-5,2.7557319223985891e-6,
      2.7557319223985891e-7,2.5052108385441719e-8,2.0876756987868099e-9,1.6059043836821615e-10,
      1.1470745597729725e-11,7.6471637318198165e-13,4.7794773323873853e-14,2.8114572543455208e-15,
      1.5619206968586226e-16,8.2206352466243297e-18,4.1103176233121649e-19,1.9572941063391261e-20,
      8.8967913924505733e-22
    };
    dd val = (dd){ INV_FACT[22], 0.0 };
    for (int k=21;k>=0;--k){
        val = dd_mul_dd_opt(val, r);
        val = dd_add_d_opt(val, INV_FACT[k]);
    }
    return val;
}

static inline dd dd_exp_neg_strict(double x){
    double y = -x;
    int n = nint_tieeven(y * LOG2E);
    dd r = dd_sub_dd((dd){y,0.0}, dd_mul_d_strict((dd){LN2_HI,0.0}, n));
    r = dd_sub_dd(r, dd_mul_d_strict((dd){LN2_LO,0.0}, n));
    dd er = dd_exp_reduced_strict(r);
    return dd_ldexp_strict(er, n);
}
static inline dd dd_exp_neg_opt(double x){
    double y = -x;
    int n = nint_tieeven(y * LOG2E);
    dd r = dd_sub_dd((dd){y,0.0}, dd_mul_d_opt((dd){LN2_HI,0.0}, n));
    r = dd_sub_dd(r, dd_mul_d_opt((dd){LN2_LO,0.0}, n));
    dd er = dd_exp_reduced_opt(r);
    return dd_ldexp_opt(er, n);
}

/* ---------------------- Core map (STRICT / OPT) ---------------------- */

static const double BmA = 1.0 - 2.0e-16;

static inline dd approx_core_strict(double x){
    dd xdd = (dd){x, 0.0};
    dd one_plus_x = dd_add_d(xdd, 1.0);
    dd y = dd_div_dd_strict(xdd, one_plus_x);
    dd t = dd_cbrt_two_steps(y);
    dd two_t = dd_mul_d_strict(t, 2.0);
    dd num = dd_add_d(two_t, -1.0);
    dd u   = dd_div_d_strict(num, BmA);

    dd P = poly14_dd_estrin(P_DD, u, dd_mul_dd_strict, dd_add_dd);
    dd Q = poly14_dd_estrin(Q_DD, u, dd_mul_dd_strict, dd_add_dd);
    dd R = dd_div_dd_strict(P, Q);

    dd t2 = dd_mul_dd_strict(t, t);
    dd sroot = dd_sqrt_one_step(one_plus_x.hi);
    dd s = dd_mul_dd_strict(t2, sroot);
    return dd_div_dd_strict(R, s);
}

static inline dd approx_core_opt(double x){
    dd xdd = (dd){x, 0.0};
    dd one_plus_x = dd_add_d_opt(xdd, 1.0);
    dd y = dd_div_dd_opt(xdd, one_plus_x);
    dd t = dd_cbrt_one_step(y);
    dd two_t = dd_mul_d_opt(t, 2.0);
    dd num = dd_add_d_opt(two_t, -1.0);
    dd u   = dd_div_d_opt(num, BmA);

    dd P = poly14_dd_estrin(P_DD, u, dd_mul_dd_opt, dd_add_dd_opt);
    dd Q = poly14_dd_estrin(Q_DD, u, dd_mul_dd_opt, dd_add_dd_opt);
    dd R = dd_div_dd_opt(P, Q);

    dd t2 = dd_mul_dd_opt(t, t);
    dd sroot = dd_sqrt_one_step(one_plus_x.hi);
    dd s = dd_mul_dd_opt(t2, sroot);
    return dd_div_dd_opt(R, s);
}

/* ---------------------- Public kernels ---------------------- */

static inline double fm_with_exp_strict(double x){
    dd core = approx_core_strict(x);
    dd tmp  = dd_mul_d_strict(core, x);
    dd e    = dd_exp_neg_strict(x);
    dd out  = dd_mul_dd_strict(tmp, e);
    return dd_to_double_rn(out);
}
static inline double fm_skipexp_strict(double x){
    dd core = approx_core_strict(x);
    dd out  = dd_mul_d_strict(core, x);
    return dd_to_double_rn(out);
}
static inline double fm_with_exp_opt(double x){
    dd core = approx_core_opt(x);
    dd tmp  = dd_mul_d_opt(core, x);
    dd e    = dd_exp_neg_opt(x);
    dd out  = dd_mul_dd_opt(tmp, e);
    return dd_to_double_rn(out);
}
static inline double fm_skipexp_opt(double x){
    dd core = approx_core_opt(x);
    dd out  = dd_mul_d_opt(core, x);
    return dd_to_double_rn(out);
}

/* ---------------------- Python wrappers (scalar) ---------------------- */

static PyObject* py_with_exp_strict(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_with_exp_strict(x));
}
static PyObject* py_skipexp_strict(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_skipexp_strict(x));
}
static PyObject* py_with_exp_opt(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_with_exp_opt(x));
}
static PyObject* py_skipexp_opt(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_skipexp_opt(x));
}

/* ---------------------- Python wrappers (buffer arrays) ---------------------- */

static int parse_inbuf(PyObject* obj, Py_buffer* view){
    int flags = PyBUF_SIMPLE;
    if(PyObject_GetBuffer(obj, view, flags) != 0) return -1;
    if ((view->len % (Py_ssize_t)sizeof(double)) != 0){
        PyErr_SetString(PyExc_ValueError, "input buffer length is not a multiple of 8");
        PyBuffer_Release(view);
        return -1;
    }
    return 0;
}
typedef double (*kernel_t)(double);

static PyObject* run_buf(PyObject* obj, kernel_t fn){
    Py_buffer view;
    if (parse_inbuf(obj, &view) != 0) return NULL;
    size_t n = (size_t)(view.len / (Py_ssize_t)sizeof(double));
    const double* xin = (const double*)view.buf;

    PyObject* ba = alloc_double_bytearray(n);
    if (!ba){ PyBuffer_Release(&view); return NULL; }
    double* out = (double*)PyByteArray_AsString(ba);
    for (size_t i=0;i<n;++i) out[i] = fn(xin[i]);

    PyBuffer_Release(&view);
    return ba;
}

static PyObject* py_with_exp_strict_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_with_exp_strict);
}
static PyObject* py_skipexp_strict_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_skipexp_strict);
}
static PyObject* py_with_exp_opt_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_with_exp_opt);
}
static PyObject* py_skipexp_opt_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_skipexp_opt);
}

/* ---------------------- Module def ---------------------- */

static PyMethodDef Methods[] = {
    {"fm_with_exp_strict",      py_with_exp_strict,      METH_VARARGS, "STRICT: (P/Q)/s * x * exp(-x)"},
    {"fm_skipexp_strict",       py_skipexp_strict,       METH_VARARGS, "STRICT: (P/Q)/s * x"},
    {"fm_with_exp_opt",         py_with_exp_opt,         METH_VARARGS, "OPT:    (P/Q)/s * x * exp(-x)"},
    {"fm_skipexp_opt",          py_skipexp_opt,          METH_VARARGS, "OPT:    (P/Q)/s * x"},

    {"fm_with_exp_strict_buf",  py_with_exp_strict_buf,  METH_VARARGS, "STRICT array: input buffer of float64, return bytearray of float64"},
    {"fm_skipexp_strict_buf",   py_skipexp_strict_buf,   METH_VARARGS, "STRICT array: input buffer of float64, return bytearray of float64"},
    {"fm_with_exp_opt_buf",     py_with_exp_opt_buf,     METH_VARARGS, "OPT array:    input buffer of float64, return bytearray of float64"},
    {"fm_skipexp_opt_buf",      py_skipexp_opt_buf,      METH_VARARGS, "OPT array:    input buffer of float64, return bytearray of float64"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef Module = {
    PyModuleDef_HEAD_INIT,
    "_fm",
    "AccurPy FM_new kernels (STRICT ≤1 ULP, OPT fast)",
    -1,
    Methods
};

PyMODINIT_FUNC PyInit__fm(void){
    return PyModule_Create(&Module);
}
