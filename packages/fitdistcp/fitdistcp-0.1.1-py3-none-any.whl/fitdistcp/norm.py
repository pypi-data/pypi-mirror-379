import numpy as np
import scipy.stats as stats
from rusampling import Ru

from . import norm_libs
from . import utils as cp_utils
from . import reltest_libs


def ppf(x, p=np.arange(0.1, 1.0, 0.1), 
        means=False, waicscores=False, logscores=False, 
        ru=False, ru_nsamples=100000,
        unbiasedv=False):
    """
    Normal Distribution Predictions Based on a Calibrating Prior
    
    Parameters
    ----------
    x : array-like
        Training data
    p : array-like, default np.arange(0.1, 1.0, 0.1)
        Probability levels for quantiles
    means : bool, default False
        Whether to calculate means
    waicscores : bool, default False
        Whether to calculate WAIC scores
    logscores : bool, default False
        Whether to calculate log scores
    unbiasedv : bool, default False
        Whether to use unbiased variance
    debug : bool, default False
        Debug flag
        
    Returns
    -------
    dict
        Dictionary containing quantiles and other statistics
    """
    # 1 intro
    x = cp_utils.to_array(x)
    p = cp_utils.to_array(p)
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x))
    assert np.all(np.isfinite(p)) and not np.any(np.isnan(p))
    assert np.all(p > 0) and np.all(p < 1)
    
    alpha = 1 - p
    nx = len(x)
    nalpha = len(alpha)
    
    # 2 ml param estimate
    ml_params = norm_libs.norm_ml_params(x)
    v1hat = ml_params[0]
    v2hat = ml_params[1]
    uv_params = "unbiasedv not selected"
    if unbiasedv:
        uv_params = norm_libs.norm_unbiasedv_params(x)
    
    # 3 aic
    ml_value = np.sum(stats.norm.logpdf(x, loc=v1hat, scale=v2hat))
    maic = cp_utils.make_maic(ml_value, nparams=2)
    
    # 4 ml quantiles (vectorized over alpha)
    ml_quantiles = stats.norm.ppf(1 - alpha, loc=v1hat, scale=v2hat)
    uv_quantiles = "unbiasedv not selected"
    if unbiasedv:
        uv_quantiles = stats.norm.ppf(1 - alpha, loc=uv_params[0], scale=uv_params[1])
    
    # 5 rhp quantiles (vectorized over alpha)
    mu = v1hat
    
    # first, convert sigma from maxlik to unbiased
    sgu = v2hat * np.sqrt(nx / (nx - 1))
    # then, convert sigma to predictive sigma
    sg = sgu * np.sqrt((nx + 1) / nx)
    
    temp = stats.t.ppf(1 - alpha, df=nx - 1)
    rh_quantiles = mu + temp * sg
    
    ldd = "only relevant for DMGS models, not analytic models"
    lddi = "only relevant for DMGS models, not analytic models"
    expinfmat = np.zeros((2, 2))
    expinfmat[0, 0] = nx / (v2hat * v2hat)
    expinfmat[1, 1] = 2 * nx / (v2hat * v2hat)
    expinfmati = np.linalg.inv(expinfmat)
    standard_errors = np.zeros(2)
    standard_errors[0] = np.sqrt(expinfmati[0, 0])
    standard_errors[1] = np.sqrt(expinfmati[1, 1])
    
    # test of gg code (for future implementation of mpd theory, as a test of the mpd code)
    # norm_gg(nx,v1hat,v2hat)
    
    # 6 means (might as well always calculate)
    ml_mean = v1hat
    rh_mean = v1hat
    
    # 7 waicscores
    waic = norm_libs.norm_waic(waicscores, x, v1hat, v2hat)
    waic1 = waic['waic1']
    waic2 = waic['waic2']
    
    # 8 logscores
    logscores_result = norm_libs.norm_logscores(logscores, x)
    ml_oos_logscore = logscores_result['ml_oos_logscore']
    rh_oos_logscore = logscores_result['rh_oos_logscore']
    
    # 9 ru
    ru_quantiles = "ru not selected"
    if ru:
        rusim = rvs(ru_nsamples, x, ru=True, mlcp=False)
        ru_quantiles = cp_utils.makeq(rusim['ru_deviates'], p)
    
    return {
        'ml_params': ml_params,
        'ml_value': ml_value,
        'uv_params': uv_params,
        # 'ldd': ldd,
        # 'lddi': lddi,
        # 'expinfmat': expinfmat,
        # 'expinfmati': expinfmati,
        'standard_errors': standard_errors,
        'ml_quantiles': ml_quantiles,
        'cp_quantiles': rh_quantiles,
        'ru_quantiles': ru_quantiles,
        'uv_quantiles': uv_quantiles,
        'maic': maic,
        'waic1': waic1,
        'waic2': waic2,
        'ml_oos_logscore': ml_oos_logscore,
        'cp_oos_logscore': rh_oos_logscore,
        'ml_mean': ml_mean,
        'cp_mean': rh_mean,
        'cp_method': cp_utils.analytic_cpmethod()
    }

def rvs(n, x, ru=False, mlcp=True, debug=False):
    """
    Random number generation for normal distribution with calibrating prior
    
    Parameters
    ----------
    n : int
        Number of samples
    x : array-like
        Training data
    ru : bool, default False
        Whether to use Ratio of Uniforms method
    mlcp : bool, default True
        Whether to use ML/CP method
    debug : bool, default False
        Debug flag
        
    Returns
    -------
    dict
        Dictionary containing random deviates
    """
    # stopifnot(is.finite(n),!is.na(n),is.finite(x),!is.na(x))
    x = cp_utils.to_array(x)
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x))
    
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
            ru_deviates[i] = np.random.normal(loc=th[i, 0], scale=th[i, 1])
    
    op = {
        'ml_params': ml_params,
        'ml_deviates': ml_deviates,
        'cp_deviates': cp_deviates,
        'ru_deviates': ru_deviates,
        'cp_method': cp_utils.analytic_cpmethod()
    }
    return op

def pdf(x, y=None, ru=False, ru_nsamples=1000, debug=False):
    """
    Density function for normal distribution with calibrating prior
    
    Parameters
    ----------
    x : array-like
        Training data
    y : array-like, optional
        Test points (default: same as x)
    ru : bool, default False
        Whether to use Ratio of Uniforms method
    ru_nsamples : int, default 1000
        Number of Ratio of Uniforms samples
    debug : bool, default False
        Debug flag
        
    Returns
    -------
    dict
        Dictionary containing density values
    """
    x = cp_utils.to_array(x)
    if y is None:
        y = x
    y = cp_utils.to_array(y)
    
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x))
    assert np.all(np.isfinite(y)) and not np.any(np.isnan(y))
    
    dd = norm_libs.dnormsub(x=x, y=y)
    ru_pdf = "ru not selected"
    if ru:
        th = tsf(ru_nsamples, x)['theta_samples']
        ru_pdf = np.zeros(len(y))
        for ir in range(ru_nsamples):
            ru_pdf = ru_pdf + stats.norm.pdf(y, loc=th[ir, 0], scale=th[ir, 1])
        ru_pdf = ru_pdf / ru_nsamples
    
    op = {
        'ml_params': dd['ml_params'],
        'ml_pdf': dd['ml_pdf'],
        'cp_pdf': dd['rh_pdf'],
        'ru_pdf': ru_pdf,
        'cp_method': cp_utils.analytic_cpmethod()
    }
    return op

def cdf(x, y=None, ru=False, ru_nsamples=1000, debug=False):
    """
    Cumulative distribution function for normal distribution with calibrating prior
    
    Parameters
    ----------
    x : array-like
        Training data
    y : array-like, optional
        Test points (default: same as x)
    ru : bool, default False
        Whether to use Ratio of Uniforms method
    ru_nsamples : int, default 1000
        Number of Ratio of Uniforms samples
    debug : bool, default False
        Debug flag
        
    Returns
    -------
    dict
        Dictionary containing CDF values
    """
    x = cp_utils.to_array(x)
    if y is None:
        y = x
    y = cp_utils.to_array(y)
    
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x))
    assert np.all(np.isfinite(y)) and not np.any(np.isnan(y))
    
    dd = norm_libs.dnormsub(x=x, y=y)
    ru_cdf = "ru not selected"
    if ru:
        th = tsf(ru_nsamples, x)['theta_samples']
        ru_cdf = np.zeros(len(y))
        for ir in range(ru_nsamples):
            ru_cdf = ru_cdf + stats.norm.cdf(y, loc=th[ir, 0], scale=th[ir, 1])
        ru_cdf = ru_cdf / ru_nsamples
    
    op = {
        'ml_params': dd['ml_params'],
        'ml_cdf': dd['ml_cdf'],
        'cp_cdf': dd['rh_cdf'],
        'ru_cdf': ru_cdf,
        'cp_method': cp_utils.analytic_cpmethod()
    }
    return op

def tsf(n, x):
    """
    Theta sampling for normal distribution with calibrating prior
    
    Parameters
    ----------
    n : int
        Number of samples
    x : array-like
        Training data
        
    Returns
    -------
    array of float
        Theta samples.
    """
    x = cp_utils.to_array(x)
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x))
    
    t = Ru(norm_libs.norm_logf, x=x, d=2, ics=[np.mean(x), np.std(x)])
    
    return {'theta_samples': t.rvs(n=n)}


def reltest_libs(plot=True, ntrials=50, nx=30, p=0.0001*np.asarray(range(1,10000)), loc=0, scale=1, plot_option='tail'):
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
    loc: float (default = 0)
        Loc parameter to test.
    scale: float (default = 1)
        Scale parameter to test.
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
        x = stats.norm.rvs(loc=loc, scale=scale, size=nx)

        info_cp = ppf(x, p)
        q_cp = info_cp['cp_quantiles']
        q_ml = info_cp['ml_quantiles']

        # feed back in for the actual probability
        p_actual_ml_total += stats.norm.cdf(q_ml, loc=loc, scale=scale)
        p_actual_cp_total += stats.norm.cdf(q_cp, loc=loc, scale=scale)

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