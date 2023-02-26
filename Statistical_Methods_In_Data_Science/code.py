import os
os.chdir("C:/Users/yiphi/anaconda3/PhD/Teaching/01TWWSM_Stats_for_DS/Year2022/Lab/")

import numpy as np
np.random.seed(10)

from scipy.stats import bernoulli
from scipy.stats import expon
from scipy.stats import poisson
from scipy.stats import gamma 

from scipy.special import polygamma

from functions import MoME, Gamma_MLE, inv_posdef, plots


# =============================================================================
# Answers to worksheet 
# =============================================================================

n           = 10000
N           = 5000

p           = 0.5
X           = bernoulli.rvs(p, size = (N,n)) 
ber_mome    = MoME("Bernoulli", X)
ber_crlb    = p*(1-p)/n
ber_crlb_bar = ber_mome[0]*(1-ber_mome[0])/n
plots("Bernoulli", n, X, ber_mome, ber_crlb_bar, p, ber_crlb)

mu          = 1
X           = poisson.rvs(mu, size = (N,n)) 
poi_mome    = MoME("Poisson", X)
poi_crlb    = mu/n
poi_crlb_bar = poi_mome[0]/n
plots("Poisson", n, X, poi_mome, poi_crlb_bar, mu, poi_crlb)

mu          = 1
X           = expon.rvs(size = (N,n), scale = mu)
exp_mome    = MoME("Exponential", X)
exp_crlb    = mu**2/n
exp_crlb_bar = exp_mome[0]**2/n
plots("Exponential", n, X, exp_mome, exp_crlb_bar, mu, exp_crlb)

alpha                       = 1 
beta                        = 2
X                           = gamma.rvs(a=alpha, scale=1/beta, size=(N,n))
gamma_mome                  = MoME("Gamma", X)
gamma_mle                   = Gamma_MLE(X)
gamma_fisher                = -1*np.array([[ -n*polygamma(n=1,x=alpha), n/beta], [ n/beta, -n*alpha/(beta**2)]])
gamma_crlb                  = inv_posdef(gamma_fisher) 
alpha_mle, beta_mle         = gamma_mle
gamma_fisher_bar            = -1*np.array([[ -n*polygamma(n=1,x=alpha_mle[0]), n/beta_mle[0]], [ n/beta_mle[0], -n*alpha_mle[0]/(beta_mle[0]**2)]])
gamma_crlb_bar              = inv_posdef(gamma_fisher_bar) 
plots("Gamma", n, X, gamma_mle, gamma_crlb_bar, (alpha,beta), gamma_crlb)
