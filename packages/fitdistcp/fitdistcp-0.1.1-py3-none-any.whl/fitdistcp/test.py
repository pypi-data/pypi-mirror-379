import numpy as np
from pprint import pprint

from . import norm as cp_norm
from . import lnorm as cp_lnorm
from . import gumbel as cp_gumbel
from . import gamma as cp_gamma
from . import weibull as cp_weibull
from . import expon as cp_expon
from . import genextreme as cp_genextreme
from . import genextreme_p1 as cp_genextreme_p1
from . import genextreme_p12 as cp_genextreme_p12
from . import genpareto as cp_genpareto
from . import test_example_data as data


'''
Mostly intended to run to check nothing crashes.
'''


def ppf():
    i = 1
    q = [
        cp_norm.ppf(data.norm[i], logscores=True, unbiasedv=True, waicscores=True, ru=True),
        cp_lnorm.ppf(data.lnorm[i], logscores=True, means= True, waicscores=True, ru=True),
        cp_gamma.ppf(data.gamma[i], means=True, waicscores=True, ru=True),
        cp_gumbel.ppf(data.gumbel[i], logscores=True, means=True, waicscores=True, ru=True),
        cp_weibull.ppf(data.weibull[i], logscores=True, means=True, waicscores=True, ru=True),
        cp_genpareto.ppf(data.gpd[i], means=True, waicscores=True, ru=True),
        cp_expon.ppf(data.expon[i], logscores=True, means=True, waicscores=True, ru=True),
        #cp_genextreme.ppf(data.gev[0], means=True, waicscores=True, ru=True),
        #cp_genextreme_p1.ppf(data.gev_p1[0], data.gev_p1_t, t0=21, means=True, waicscores=True, ru=True),
        #cp_genextreme_p12.ppf(data.gev_p12[0], data.gev_p12_t1, data.gev_p12_t2, t01=0, t02=0, ru=True)
    ]
    return q

def rvs():
    y = [
        #cp_expon.rvs(10000, data.expon[0], ru=True),
        #cp_norm.rvs(100000, data.norm[0], ru=True),
        #cp_lnorm.rvs(100000, data.lnorm[0], ru=True),
        #cp_gamma.rvs(100000, data.gamma[1], ru=True),
        #cp_gumbel.rvs(100000, data.gumbel[0], ru=True),
        #cp_weibull.rvs(100000, data.weibull[0], ru=True),
        cp_genpareto.rvs(500000, data.gpd[0], ru=True),
        #cp_genextreme.rvs(10000, data.gev[0], ru=True),
        #cp_genextreme_p1.rvs(10000, data.gev_p1[0], data.gev_p1_t, t0=21, ru=True),
        #cp_genextreme_p12.rvs(10000, data.gev_p12[0], data.gev_p12_t1, data.gev_p12_t2, t01=0, t02=0, ru=True)
    ]
    return y

def pdf():
    d = [
        cp_norm.pdf(data.norm[0], y=[0], ru=True),
        cp_lnorm.pdf(data.lnorm[0], ru=True),
        cp_gamma.pdf(data.gamma[1], ru=True),
        cp_gumbel.pdf(data.gumbel[0],  ru=True),
        cp_weibull.pdf(data.weibull[0],ru=True),
        cp_expon.pdf(data.expon[0],ru=True),
        cp_genpareto.pdf(data.gpd[0], ru=True),
        cp_genextreme.pdf(data.gev[0], ru=True),
        cp_genextreme_p1.pdf(data.gev_p1[0], data.gev_p1_t, t0=21, ru=True),
        cp_genextreme_p12.pdf(data.gev_p12[0], data.gev_p12_t1, data.gev_p12_t2, t01=0, t02=0, ru=True)
    ]
    return d

def cdf():
    q = [
        #cp_norm.cdf(data.norm[0], ru=True),
        #cp_lnorm.cdf(data.lnorm[0], ru=True),
        #cp_gamma.cdf(data.gamma[1], ru=True),
        #cp_gumbel.cdf(data.gumbel[0], ru=True),
        #cp_weibull.cdf(data.weibull[0], ru=True),
        cp_expon.cdf(data.expon[0], ru=True),
        cp_genpareto.cdf(data.gpd[0], ru=True),
        #cp_genextreme.cdf(data.gev[0], ru=True),
        #cp_genextreme_p1.cdf(data.gev_p1[0], data.gev_p1_t[0], t0=21, ru=True),
        #cp_genextreme_p12.cdf(data.gev_p12[0], data.gev_p12_t1, data.gev_p12_t2, t01=0, t02=0, ru=True)
    ]
    return q

def tsf():
    n = 100
    r = [
        cp_norm.tsf(n, data.norm[0]),
        cp_lnorm.tsf(n, data.lnorm[0]),
        cp_gamma.tsf(n, data.gamma[1]),
        cp_gumbel.tsf(n, data.gumbel[0]),
        cp_weibull.tsf(n, data.weibull[0]),
        cp_expon.tsf(n, data.expon[0]),
        cp_genextreme.tsf(n, data.gev[0]),
        cp_genpareto.tsf(n, data.gpd[0]),
        cp_genextreme_p1.tsf(n, data.gev_p1[0], data.gev_p1_t),
        #cp_genextreme_p12.tsf(n, data.gev_p12[0], data.gev_p12_t1, data.gev_p12_t2)
    ]
    return r


#q = ppf()
#p = cdf()
#c = cdf()
#r = rvs()  
#t = tsf()