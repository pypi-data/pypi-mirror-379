'''
fitdistcp package. Visit fitdistcp.info for more information.
Provides modules 
    - genextreme: generalised extreme value distribution
    - genextreme_p1: generalised extreme value distribution, with one predictor
    - genpareto: generalised pareto distribution
'''

__all__ = [
    'genextreme', 
    'genextreme_p1', 
    'genextreme_p12',
    'genpareto',
    'expon',
	'gamma',
	'gumbel',
	'lnorm',
	'norm',
	'weibull'
]

from . import genextreme
from . import genextreme_p1
from . import genextreme_p12
from . import genpareto
from . import expon
from . import gamma
from . import gumbel
from . import lnorm
from . import norm
from . import weibull