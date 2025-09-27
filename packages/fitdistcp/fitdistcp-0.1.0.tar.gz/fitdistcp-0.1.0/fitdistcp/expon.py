import numpy as np
import scipy.stats
from scipy.stats import expon
from rusampling import Ru

from . import expon_libs as exp_libs
from . import utils as cp_utils
from . import reltest_libs


def ppf(x, p=np.arange(0.1, 1.0, 0.1), 
        means=False, waicscores=False, logscores=False, 
        ru=False, ru_nsamples=100000):
    
    """
    Exponential Distribution Predictions Based on a Calibrating Prior

    Parameters
    ----------
    x : array_like
        Observed data, must be non-negative and finite.
    p : array_like, optional
        Probabilities at which to compute quantiles (default: np.arange(0.1, 1.0, 0.1)).
    means : bool, optional
        Whether to compute means (default: False).
    waicscores : bool, optional
        Whether to compute WAIC scores (default: False).
    logscores : bool, optional
        Whether to compute log scores (default: False).
    ru: bool, optional
        Whether to use Ratio of Uniforms method to calculate additional quantiles (default: False).
    ru_nsamples: int, optional
        Number of samples to use in RU method (default: 100000).
    debug : bool, optional
        If True, print debug information (default: False).

    Returns
    -------
    dict
        Dictionary containing ML and calibrating prior quantiles, means, scores, and method information.

    Notes
    -----
    The exponential distribution has exceedance distribution function
    S(x;λ)=exp(-λ x), x ≥ 0, λ > 0.
    The calibrating prior is the right Haar prior: π(λ) ∝ 1/λ,
    as given in Jewson et al. (2025).
    """

    x = cp_utils.to_array(x)
    p = cp_utils.to_array(p)
    
    # 1 intro
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert np.all(np.isfinite(p)) and not np.any(np.isnan(p)), "p must be finite and not NaN"
    assert np.all(p > 0) and np.all(p < 1), "p must be between 0 and 1"
    assert not np.any(x < 0), "x must be non-negative"
    
    alpha = 1 - p
    nx = len(x)
    sumx = np.sum(x)
    
    # 2 ml param estimate
    v1hat = nx / sumx   # 1/mean = 1/scale = rate = lambda
    ml_params = v1hat
    
    # 3 aic
    ml_value = np.sum(scipy.stats.expon.logpdf(x, scale=1/v1hat))
    maic = cp_utils.make_maic(ml_value, nparams=1)
    
    # 4 ml quantiles (vectorized over alpha)
    ml_quantiles = scipy.stats.expon.ppf(1-alpha, scale=1/v1hat)
    ldd = "only relevant for DMGS models, not analytic models"
    lddi = "only relevant for DMGS models, not analytic models"
    expinfmat = nx / (v1hat * v1hat)
    expinfmati = 1 / expinfmat
    standard_errors = np.sqrt(expinfmati)
    
    # 5 rh_quantiles (vectorized over alpha)
    rh_quantiles = sumx * ((alpha**(-1/nx)) - 1)
    
    # 6 means (might as well always calculate)
    ml_mean = 1 / v1hat
    rh_mean = sumx / (nx - 1)
    
    # 7 waicscores
    waic = exp_libs.exp_waic(waicscores, x, v1hat)
    waic1 = waic['waic1']
    waic2 = waic['waic2']
    
    # 8 logscores
    logscores_result = exp_libs.exp_logscores(logscores, x)
    ml_oos_logscore = logscores_result['ml_oos_logscore']
    rh_oos_logscore = logscores_result['rh_oos_logscore']
    
    # 9 rust
    ru_quantiles = "ru not selected"
    if ru:
        rusim = rvs(ru_nsamples, x, ru=True, mlcp=False)
        ru_quantiles = cp_utils.makeq(rusim['ru_deviates'], p)
    
    # return
    return {
        'ml_params': ml_params,
        'ml_value': ml_value,
        'standard_errors': standard_errors,
        'ml_quantiles': ml_quantiles,
        'cp_quantiles': rh_quantiles,
        'ru_quantiles': ru_quantiles,
        'maic': maic,
        'waic1': waic1,
        'waic2': waic2,
        'ml_oos_logscore': ml_oos_logscore,
        'cp_oos_logscore': rh_oos_logscore,
        'ml_mean': ml_mean,
        'cp_mean': rh_mean,
        'cp_method': cp_utils.analytic_cpmethod()
    }

def rvs(n, x, ru=False, mlcp=True):
    """
    Random number generation for exponential calibrating prior

    Parameters
    ----------
    n : int
        Number of random variates to generate.
    x : array_like
        Observed data, must be non-negative and finite.
    ru : bool, optional
        Whether to use the Ratio Uniforms simulation method (default: False).
    mlcp : bool, optional
        Whether to use ML and calibrating prior (default: True).
    debug : bool, optional
        If True, print debug information (default: False).

    Returns
    -------
    dict
        Dictionary containing ML, calibrating prior, and ru deviates, parameters, and method information.
    """

    x = cp_utils.to_array(x)
    
    # stopifnot(is.finite(n),!is.na(n),is.finite(x),!is.na(x),!x<0)
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert not np.any(x < 0), "x must be non-negative"
    
    ml_params = "mlcp not selected"
    ml_deviates = "mlcp not selected"
    cp_deviates = "mlcp not selected"
    ru_deviates = "ru not selected"
    
    if mlcp:
        q = ppf(x, np.random.uniform(size=n))
        ml_params = q['ml_params']
        ml_deviates = q['ml_quantiles']
        cp_deviates = q['cp_quantiles']
    
    if ru:
        th = tsf(n, x)['theta_samples']
        ru_deviates = np.zeros(n)
        for i in range(n):
            ru_deviates[i] = np.random.exponential(scale=1/th[i])
    
    op = {
        'ml_params': ml_params,
        'ml_deviates': ml_deviates,
        'cp_deviates': cp_deviates,
        'ru_deviates': ru_deviates,
        'cp_method': cp_utils.analytic_cpmethod()
    }
    
    return op

def pdf(x, y=None, ru=False, ru_nsamples=1000):
    """
    Density function for exponential calibrating prior

    Parameters
    ----------
    x : array_like
        Observed data, must be non-negative and finite.
    y : array_like, optional
        Points at which to evaluate the density (default: x).
    ru : bool, optional
        Whether to use the Ratio Uniforms simulation method (default: False).
    ru_nsamples : int, optional
        Number of simulations for Ratio Uniforms (default: 1000).
    debug : bool, optional
        If True, print debug information (default: False).

    Returns
    -------
    dict
        Dictionary containing ML, calibrating prior, and ru densities, parameters, and method information.
    """
    x = cp_utils.to_array(x)
    if y is None:
        y = x
    else:
        y = cp_utils.to_array(y)
        
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert np.all(np.isfinite(y)) and not np.any(np.isnan(y)), "y must be finite and not NaN"
    assert not np.any(x < 0), "x must be non-negative"
    assert not np.any(y < 0), "y must be non-negative"
    
    dd = exp_libs.dexpsub(x=x, y=y)
    ru_pdf = "ru not selected"
    if ru:
        th = tsf(ru_nsamples, x)['theta_samples']
        ru_pdf = np.zeros(len(y))
        for ir in range(ru_nsamples):
            ru_pdf += scipy.stats.expon.pdf(y, scale=1/th[ir])
        ru_pdf = ru_pdf / ru_nsamples
    
    op = {
        'ml_params': dd['ml_params'],
        'ml_pdf': dd['ml_pdf'],
        'cp_pdf': dd['rh_pdf'],
        'ru_pdf': ru_pdf,
        'cp_method': cp_utils.analytic_cpmethod()
    }
    return op

def cdf(x, y=None, ru=False, ru_nsamples=1000):
    """
    Cumulative distribution function for exponential calibrating prior

    Parameters
    ----------
    x : array_like
        Observed data, must be non-negative and finite.
    y : array_like, optional
        Points at which to evaluate the CDF (default: x).
    ru : bool, optional
        Whether to use the Ratio Uniforms simulation method (default: False).
    ru_nsamples : int, optional
        Number of simulations for Ratio Uniforms (default: 1000).
    debug : bool, optional
        If True, print debug information (default: False).

    Returns
    -------
    dict
        Dictionary containing ML, calibrating prior, and ru CDFs, parameters, and method information.
    """

    x = cp_utils.to_array(x)
    if y is None:
        y = x
    else:
        y = cp_utils.to_array(y)
        
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert np.all(np.isfinite(y)) and not np.any(np.isnan(y)), "y must be finite and not NaN"
    assert not np.any(x < 0), "x must be non-negative"
    assert not np.any(y < 0), "y must be non-negative"
    
    dd = exp_libs.dexpsub(x=x, y=y)
    ru_cdf = "ru not selected"
    if ru:
        th = tsf(ru_nsamples, x)['theta_samples']
        ru_cdf = np.zeros(len(y))
        for ir in range(ru_nsamples):
            ru_cdf += scipy.stats.expon.cdf(y, scale=1/th[ir])
        ru_cdf = ru_cdf / ru_nsamples
    
    op = {
        'ml_params': dd['ml_params'],
        'ml_cdf': dd['ml_cdf'],
        'cp_cdf': dd['rh_cdf'],
        'ru_cdf': ru_cdf,
        'cp_method': cp_utils.analytic_cpmethod()
    }
    return op

def tsf(n, x, debug=False):
    """
    Theta sampling for exponential calibrating prior

    Parameters
    ----------
    n : int
        Number of samples to generate.
    x : array_like
        Observed data, must be non-negative and finite.
    debug : bool, optional
        If True, print debug information (default: False).

    Returns
    -------
    array of float
        Theta samples.
    """
    x = cp_utils.to_array(x)
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert not np.any(x < 0), "x must be non-negative"
    
    ics = [1/np.mean(x)]
    t = Ru(exp_libs.exp_logf, x=x, ics=ics)
    if debug:
        t.info()
    print('Parameter sampled is the rate = lambda = 1/mean = 1/scale')
    
    return {'theta_samples': t.rvs(n=n)}


def reltest_libs(plot=True, ntrials=100, nx=30, p=0.0001*np.asarray(range(1,10000)), rate=1, plot_option='tail'):
    '''
    Reliability test.

    Parameters
    ----------
    plot: bool (default = True)
        Create a plot of the results immediately.
    desired_p : array_like
        Probabilities at which to calculate quantiles.
    ntrials : int
        Number of trials to average over.
    nx : int
        Number of samples per trial.
    rate: float (default = 1)
        Scale parameter = lambda = 1/mean.
    plot_option: str (default='tail')
        For use when plot=True, determines which graph to output.
        Options are 'unformatted', 'b', 'd', 'tail', 'i', 'all'.
        'tail' demonstrates tail probabilities the best.
    
    Returns
    -------
    dict
        Dictionary with keys:
            'actual_p_ml' : array_like
                Achieved probabilities using ML quantiles.
            'actual_p_cp' : array_like
                Achieved probabilities using CP quantiles.

    Each trial generates nx samples and calculates quantiles using the two methods.
    The difference between the methods is clearest when nx is in the range of 20-60.
    Increasing ntrials reduces the effect of random variations in the trials (100 is sufficient for many purposes).
    '''

    p_actual_ml_total = np.zeros(len(p))
    p_actual_cp_total = np.zeros(len(p))

    for i in range(ntrials):
        x = expon.rvs(scale=1/rate, size=nx)

        info_cp = ppf(x, p)
        q_cp = info_cp['cp_quantiles']
        q_ml = info_cp['ml_quantiles']

        # feed back in for the actual probability
        p_actual_ml_total += expon.cdf(q_ml, scale=1/rate)
        p_actual_cp_total += expon.cdf(q_cp, scale=1/rate)

    p_actual_ml_avg = p_actual_ml_total / ntrials
    p_actual_cp_avg = p_actual_cp_total / ntrials

    result = {
        'actual_p_ml' : np.ndarray.tolist(p_actual_ml_avg), 
        'actual_p_cp': np.ndarray.tolist(p_actual_cp_avg), 
        'p': np.ndarray.tolist(p)
        }

    if plot:
        reltest_libs.plot(result, plot_option)

    return result