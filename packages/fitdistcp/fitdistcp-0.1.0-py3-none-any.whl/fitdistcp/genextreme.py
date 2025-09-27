import numpy as np
from scipy import stats
from scipy.optimize import minimize
from scipy.stats import genextreme
from rusampling import Ru

from . import evaluate_dmgs_equation as cp_dmgs
from . import utils as cp_utils
from . import genextreme_libs as gev_libs
from . import genextreme_derivs as gev_derivs
from . import reltest_libs


def ppf(x, p = np.arange(0.1, 1.0, 0.1), ics=[0, 0, 0], fdalpha = 0.01,
        means = False, waicscores = False, extramodels = False, pdf = False,
        customprior: float = 0,
        dmgs=True, ru=False, ru_nsamples=100000,
        debug = False):
    """
    Passed data from the Generalized Extreme Value Distribution, returns quantiles and other results based on a Calibrating Prior.
    The calibrating prior we use is given by π(μ,σ,ξ) ∝ 1/σ as given in Jewson et al. (2025).

    Parameters
    ----------
    x : array_like
        Input data array.
    p : array_like, optional
        Probabilities for quantile calculation (default is np.arange(0.1, 1.0, 0.1)).
    ics : list of float, optional
        Initial parameter estimates for optimization (default is [0, 0, 0]).
    fdalpha : float, optional
        Finite difference step for PDF estimation (default is 0.01).
    means : bool, optional
        Whether to compute means for extra models (default is False).
    waicscores : bool, optional
        Whether to compute WAIC scores (default is False).
    extramodels : bool, optional
        Whether to compute extra models (default is False).
    pdf : bool, optional
        Whether to compute PDFs (default is False).
    customprior : float, optional
        Custom prior value for shape parameter (default is 0).
    dmgs : bool, optional
        Whether to use the DMGS method (default is True).
    debug : bool, optional
        If True, print debug information (default is False).

    Returns
    -------
    dict
        Dictionary containing ML parameters, quantiles, PDFs, means, WAIC scores, and other results.
    """
    
    # 1 intro
    # optional parameters removed until ru, pwm are implemented
    ru_nsamples = 1000
    pwm = False
    ru = False

    x = cp_utils.to_array(x)
    p = cp_utils.to_array(p)
    
    # Input validation
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert np.all(np.isfinite(p)) and not np.any(np.isnan(p)), "p must be finite and not NaN"
    assert np.all(p > 0) and np.all(p < 1), "p must be between 0 and 1"
    assert len(ics) == 3, "ics must have length 3"
    assert fdalpha < 1, "fdalpha must be less than 1"
    
    alpha = 1-p
    nx = len(x)
    
    if pdf:
        dalpha = np.minimum(fdalpha * alpha, fdalpha * (1 - alpha))
        alpham = alpha - dalpha
        alphap = alpha + dalpha
    

    # 2 ml param estimate
    ics = gev_libs.gev_setics(x, ics)
    
    # Use minimize instead of optim (with negative log-likelihood)
    opt1 = minimize(lambda params: -gev_libs.gev_loglik(params, x), ics, method='Nelder-Mead')
    v1hat = opt1.x[0]
    v2hat = opt1.x[1]  
    v3hat = opt1.x[2]
    ml_params = [v1hat, v2hat, v3hat]
    
    if debug:
        print(f"    v1hat,v2hat,v3hat={v1hat},{v2hat},{v3hat}")
    
    pw_params = "pwm not selected"
    if pwm:
        pw_params = gev_libs.gev_pwm_params(x)
    
    if abs(v3hat) >= 1:
        revert2ml = True
    else:
        revert2ml = False
    
    # 3 aic
    ml_value = -opt1.fun
    maic = cp_utils.make_maic(ml_value, nparams=3)
    
    # 4 calc ml quantiles and densities (vectorized over alpha)
    ml_quantiles = stats.genextreme.ppf(1 - alpha,-v3hat, loc=v1hat, scale=v2hat)
    
    if v3hat < 0:
        ml_max = v1hat - v2hat / v3hat
    else:
        ml_max = np.inf
    
    fhat = stats.genextreme.pdf(ml_quantiles, -v3hat, loc=v1hat, scale=v2hat)
    
    pw_quantiles = "pwm not selected"
    if pwm:
        pw_quantiles = stats.genextreme.ppf(1 - alpha,-pw_params[2],loc=pw_params[0], scale=pw_params[1])
    
    # dmgs
    standard_errors = "dmgs not selected"
    rh_flat_quantiles = "dmgs not selected"
    cp_quantiles = "dmgs not selected"
    ru_quantiles = "dmgs not selected"
    custom_quantiles = "dmgs not selected"
    ml_pdf = "dmgs not selected"
    rh_flat_pdf = "dmgs not selected"
    cp_pdf = "dmgs not selected"
    waic1 = "dmgs not selected"
    waic2 = "dmgs not selected"
    ml_mean = "dmgs not selected"
    rh_mean = "dmgs not selected"
    rh_flat_mean = "dmgs not selected"
    cp_mean = "dmgs not selected"
    cp_method = "dmgs not selected"
    custom_mean = "dmgs not selected"
    
    # 5 alpha pdf stuff
    if dmgs and not revert2ml:
        if debug:
            print(f"  ml_quantiles={ml_quantiles}")
        
        if pdf:
            ml_quantilesm = stats.genextreme.ppf(1 - alpham, -v3hat, loc=v1hat, scale=v2hat)
            ml_quantilesp = stats.genextreme.ppf(1 - alphap, -v3hat, loc=v1hat, scale=v2hat)
            fhatm = stats.genextreme.pdf(ml_quantilesm, -v3hat,loc=v1hat, scale=v2hat)
            fhatp = stats.genextreme.pdf(ml_quantilesp, -v3hat,loc=v1hat, scale=v2hat)
        
        # 7 ldd
        if debug:
            print("  calculate ldd")
        ldd = gev_derivs.gev_ldda(x, v1hat, v2hat, v3hat)
        lddi = np.linalg.inv(ldd)
        standard_errors = cp_utils.make_se(nx, lddi)
        
        # 8 lddd
        if debug:
            print("  calculate lddd")
        lddd = gev_derivs.gev_lddda(x, v1hat, v2hat, v3hat)
        
        # 9 mu1
        mu1 = gev_derivs.gev_mu1fa(alpha, v1hat, v2hat, v3hat)
        if pdf:
            mu1m = gev_derivs.gev_mu1fa(alpham, v1hat, v2hat, v3hat)
            mu1p = gev_derivs.gev_mu1fa(alphap, v1hat, v2hat, v3hat)
        
        # 10 mu2
        mu2 = gev_derivs.gev_mu2fa(alpha, v1hat, v2hat, v3hat)
        if pdf:
            mu2m = gev_derivs.gev_mu2fa(alpham, v1hat, v2hat, v3hat)
            mu2p = gev_derivs.gev_mu2fa(alphap, v1hat, v2hat, v3hat)
        
        # 13 model 4: rh_flat with flat prior on shape
        lambdad_rh_flat = np.asarray([0, -1/v2hat, 0])
        dq = cp_dmgs.dmgs(lddi, lddd, mu1, lambdad_rh_flat, mu2, dim=3)
        rh_flat_quantiles = ml_quantiles + dq / (nx * fhat)
        
        if pdf:
            dqm = cp_dmgs.dmgs(lddi, lddd, mu1m, lambdad_rh_flat, mu2m, dim=3)
            dqp = cp_dmgs.dmgs(lddi, lddd, mu1p, lambdad_rh_flat, mu2p, dim=3)
            quantilesm = ml_quantilesm + dqm / (nx * fhatm)
            quantilesp = ml_quantilesp + dqp / (nx * fhatp)
            ml_pdf = fhat
            rh_flat_pdf = -(alphap - alpham) / (quantilesp - quantilesm)
        else:
            ml_pdf = fhat
            rh_flat_pdf = "pdf not selected"
        
        # 15 model 6: custom prior on shape parameter
        if extramodels or means:
            lambdad_custom = np.asarray([0, -1/v2hat, customprior])
            dq = cp_dmgs.dmgs(lddi, lddd, mu1, lambdad_custom, mu2, dim=3)
            custom_quantiles = ml_quantiles + dq / (nx * fhat)
        else:
            custom_quantiles = "extramodels not selected"
            lambdad_custom = 0
        
        # 16 means
        # check that lambdad_custom=0 is the correct result if neither extramodels nor means holds
        means_result = gev_libs.gev_means(means, ml_params, lddi, lddd,
                                lambdad_rh_flat, lambdad_custom, nx, dim=3)
        ml_mean = means_result['ml_mean']
        rh_flat_mean = means_result['rh_flat_mean']
        custom_mean = means_result['custom_mean']
        
        # 17 waicscores
        waic = gev_libs.gev_waic(waicscores, x, v1hat, v2hat, v3hat, lddi, lddd, lambdad_rh_flat)
        waic1 = waic['waic1']
        waic2 = waic['waic2']
        
        # 19 ru
        ru_quantiles = "ru not selected"
        if ru:
            rusim = rvs(ru_nsamples, x, ru=True, mlcp=False)
            ru_quantiles = cp_utils.makeq(rusim['ru_deviates'], p)
        
        # end of if(dmgs)
    else:
        rh_flat_quantiles = ml_quantiles
        ru_quantiles = ml_quantiles
        pw_quantiles = ml_quantiles
        custom_quantiles = ml_quantiles
        rh_flat_pdf = ml_pdf
        rh_flat_mean = ml_mean
        custom_mean = ml_mean
    
    return {
        'ml_params': ml_params,
        'pw_params': pw_params,
        'ml_value': ml_value,
        'standard_errors': standard_errors,
        'ml_quantiles': ml_quantiles,
        'ml_max': ml_max,
        'revert2ml': revert2ml,
        'cp_quantiles': rh_flat_quantiles,
        'ru_quantiles': ru_quantiles,
        'pw_quantiles': pw_quantiles,
        'custom_quantiles': custom_quantiles,
        'ml_pdf': ml_pdf,
        'cp_pdf': rh_flat_pdf,
        'maic': maic,
        'waic1': waic1,
        'waic2': waic2,
        'ml_mean': ml_mean,
        'cp_mean': rh_flat_mean,
        'custom_mean': custom_mean,
        'cp_method': cp_utils.crhpflat_dmgs_cpmethod()
    }


def rvs(n, x, ics = [0, 0, 0], extramodels = False, mlcp = True, ru=False):
    """
    Passed data from the Generalized Extreme Value Distribution, generate random samples from the same distribution with calibrating prior.

    Parameters
    ----------
    n : int
        Number of samples to generate.
    x : array_like
        Input data array.
    ics : list of float, optional
        Initial parameter estimates for optimization (default is [0, 0, 0]).
    extramodels : bool, optional
        Whether to compute extra models (default is False).
    mlcp : bool, optional
        Whether to use ML and CP deviates (default is True).
    debug : bool, optional
        If True, print debug information (default is False).

    Returns
    -------
    dict
        Dictionary containing ML parameters, ML deviates, CP deviates, RU deviates, and method info.
    """

    x = cp_utils.to_array(x)
    
    assert np.isfinite(n) and not np.isnan(n), "n must be finite and not NaN"
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert len(ics) == 3, "ics must have length 3"
    
    ml_params = "mlcp not selected"
    ml_deviates = "mlcp not selected"
    cp_deviates = "mlcp not selected"
    ru_deviates = "ru not selected"
    
    if mlcp:
        q = ppf(x, np.random.uniform(0, 1, n), ics=ics, extramodels=extramodels, ru=ru)
        ml_params = q['ml_params']
        ml_deviates = q['ml_quantiles']
        ru_deviates = q['ru_quantiles']
        cp_deviates = q['cp_quantiles']
    
    if ru:
        th = tsf(n, x)['theta_samples']
        ru_deviates = np.zeros(n)
        for i in range(n):
            ru_deviates[i] = stats.genextreme.rvs(-th[i, 2], loc=th[i, 0], scale=th[i, 1])
    
    return {
        'ml_params': ml_params,
        'ml_deviates': ml_deviates,
        'cp_deviates': cp_deviates,
        'ru_deviates': ru_deviates,
        'cp_method': cp_utils.crhpflat_dmgs_cpmethod()
    }


def pdf(x, y = None, ics = [0, 0, 0], ru=False, ru_nsamples=10000):
    """
    Passed data from the Generalized Extreme Value Distribution, compute the density function for the GEV distribution with calibrating prior.

    Parameters
    ----------
    x : array_like
        Input data array.
    y : array_like, optional
        Points at which to evaluate the density (default is x).
    ics : list of float, optional
        Initial parameter estimates for optimization (default is [0, 0, 0]).
    extramodels : bool, optional
        Whether to compute extra models (default is False).
    debug : bool, optional
        If True, print debug information (default is False).

    Returns
    -------
    dict
        Dictionary containing ML parameters, ML PDF, RU PDF, and method info.
    """

    # optional parameters removed until ru is implemented
    ru = False
    ru_nsamples = 1000
    
    x = cp_utils.to_array(x)
    if y is None:
        y = x
    else:
        y = cp_utils.to_array(y)
    
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert np.all(np.isfinite(y)) and not np.any(np.isnan(y)), "y must be finite and not NaN"
    assert len(ics) == 3, "ics must have length 3"
    
    ics = gev_libs.gev_setics(x, ics)
    opt1 = minimize(lambda params: -gev_libs.gev_loglik(params, x), ics, method='Nelder-Mead')
    v1hat = opt1.x[0]
    v2hat = opt1.x[1]
    v3hat = opt1.x[2]
    
    if v3hat <= -1:
        revert2ml = True
    else:
        revert2ml = False
    
    dd = gev_libs.dgevsub(x=x, y=y, ics=ics)
    ru_pdf = "ru not selected"
    
    if ru and not revert2ml:
        th = tsf(ru_nsamples, x)['theta_samples']
        ru_pdf = np.zeros(len(y))
        for ir in range(ru_nsamples):
            ru_pdf = ru_pdf + stats.genextreme.pdf(y, -th[ir, 2],loc=th[ir, 0], scale=th[ir, 1])
        ru_pdf = ru_pdf / ru_nsamples
    else:
        ru_pdf = dd['ml_pdf']
    
    return {
        'ml_params': dd['ml_params'],
        'ml_pdf': dd['ml_pdf'],
        'revert2ml': revert2ml,
        'cp_pdf': ru_pdf,
        'cp_method': cp_utils.nopdfcdfmsg()
    }


def cdf(x, y = None,
           ics = [0, 0, 0],
           extramodels = False,
           ru=False, ru_nsamples=10000,
           debug = False):
    """
    Passed data from the Generalized Extreme Value Distribution, compute the cumulative distribution function for the GEV distribution with calibrating prior.

    Parameters
    ----------
    x : array_like
        Input data array.
    y : array_like, optional
        Points at which to evaluate the CDF (default is x).
    ics : list of float, optional
        Initial parameter estimates for optimization (default is [0, 0, 0]).
    extramodels : bool, optional
        Whether to compute extra models (default is False).
    debug : bool, optional
        If True, print debug information (default is False).

    Returns
    -------
    dict
        Dictionary containing ML parameters, ML CDF, RU CDF, and method info.
    """

    # optional parameters removed until ru is implemented
    ru = False
    ru_nsamples = 1000
    
    x = cp_utils.to_array(x)
    if y is None:
        y = x
    y = cp_utils.to_array(y)
    
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert np.all(np.isfinite(y)) and not np.any(np.isnan(y)), "y must be finite and not NaN"
    assert len(ics) == 3, "ics must have length 3"
    
    ics = gev_libs.gev_setics(x, ics)
    opt1 = minimize(lambda params: -gev_libs.gev_loglik(params, x), ics, method='Nelder-Mead').x
    shape = opt1[2]
    
    if shape <= -1:
        revert2ml = True
    else:
        revert2ml = False
    
    dd = gev_libs.dgevsub(x=x, y=y, ics=ics)
    ru_cdf = "ru not selected"
    
    if ru and not revert2ml:
        th = tsf(ru_nsamples, x)['theta_samples']
        ru_cdf = np.zeros(len(y))
        for ir in range(ru_nsamples):
            ru_cdf = ru_cdf + stats.genextreme.cdf(y, -th[ir, 2], loc=th[ir, 0], scale=th[ir, 1])
        ru_cdf = ru_cdf / ru_nsamples
    else:
        ru_cdf = dd['ml_cdf']
    
    return {
        'ml_params': dd['ml_params'],
        'ml_cdf': dd['ml_cdf'],
        'revert2ml': revert2ml,
        'cp_cdf': ru_cdf,
        'cp_method': cp_utils.nopdfcdfmsg()
    }


def tsf(n, x, ics=[0,0,0]):
    """
    Theta sampling for the GEV distribution with calibrating prior.

    Parameters
    ----------
    n : int
        Number of theta samples to generate.
    x : array_like
        Input data array.
    ics : list of float, optional
        Initial parameter estimates for optimization (default is [mean, std, 0]).

    Returns
    -------
    dict
        Dictionary containing theta samples.
    """

    x = cp_utils.to_array(x)
    
    assert np.all(np.isfinite(x)) and not np.any(np.isnan(x)), "x must be finite and not NaN"
    assert len(ics) == 3, "ics must have length 3"

    # Find ICS that lie in a permissible region
    ics_accept = False

    # attempt 0: (assuming xi=0)
    ics = gev_libs.gev_setics(x, ics) 

    # attempt 1:
    ics = minimize(lambda params: -gev_libs.gev_loglik(params, x), ics, method='Nelder-Mead').x
    ics_accept = ics[2] > -0.25 and not np.isnan(gev_libs.gev_loglik(ics, x))

    # attempt 2:
    #if not ics_accept:
    #    print('Attempting pwm')
    #    ics = gev_libs.gev_pwm_params(x)
    #    ics_accept = ics[2] < 0.5 and not np.isnan(gev_libs.gev_loglik(ics, x))

    
    t = Ru(gev_libs.gev_logf, x=x, d=3, ics=ics)
    
    return {'theta_samples': t.rvs(n=n)}


def reltest_libs(plot=True, ntrials=50, nx=30, p=0.0001*np.asarray(range(1,10000)), xi=0, loc=0, scale=1, plot_option='tail', disp=True):
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
    xi: float (default = 0)
        Shape parameter to test.
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
    if disp:
        print('Running reltest...')

    p_actual_ml_total = np.zeros(len(p))
    p_actual_cp_total = np.zeros(len(p))

    for i in range(ntrials):
        x = genextreme.rvs(-xi, loc=loc, scale=scale, size=nx)

        info_cp = ppf(x, p)
        q_cp = info_cp['cp_quantiles']
        q_ml = info_cp['ml_quantiles']

        # feed back in for the actual probability
        p_actual_ml_total += genextreme.cdf(q_ml, -xi, loc=loc, scale=scale)
        p_actual_cp_total += genextreme.cdf(q_cp, -xi, loc=loc, scale=scale)

        if i%20 ==0 and disp:
            print(f'\t{i/ntrials * 100}% complete')

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