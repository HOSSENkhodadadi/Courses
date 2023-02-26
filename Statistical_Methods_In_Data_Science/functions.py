# =============================================================================
# Import libraries and packages 
# =============================================================================

import numpy as np 
np.random.seed(10)
import matplotlib.pyplot as plt
from scipy.special import digamma
from scipy.special import polygamma
from scipy.stats import norm
from scipy.stats import t 
from scipy.linalg import cholesky
from scipy.linalg.lapack import dtrtri

def MoME(name_dist, X): 
    if name_dist == "Gaussian" :
        mu_bar       = np.mean(X, axis=1)
        sigma2_bar   = np.mean((X.transpose() - mu_bar)**2, axis=0)  
        return mu_bar, sigma2_bar
    if name_dist == "Bernoulli" or name_dist == "Exponential" or name_dist == "Poisson": 
        mu_bar      = np.mean(X, axis=1)
        return mu_bar 
    if name_dist == "Gamma":
        moment1     = np.mean(X, axis=1)
        moment2     = np.mean((X**2), axis=1)  
        alpha_bar   = moment1**2 / (moment2 - moment1**2)
        beta_bar    = moment1 / (moment2 - moment1**2)
        return alpha_bar, beta_bar 
    
def Gamma_MLE(X):
    niter       = 100
    n           = len(X)
    alpha_bar   = np.zeros((n,))
    beta_bar    = np.zeros((n,))
    for i in range(n): 
        x               = X[i,:]
        a               = Gamma_newton_update(0.5, x, niter)
        if a != False: 
            b           = a / np.mean(x)
        elif a == False:
            print("Newton's Method did not converge")
            break
        alpha_bar[i]    = a
        beta_bar[i]     = b
    return alpha_bar, beta_bar 
    
def Gamma_score(a, N, x, x_bar):
    l1 = - N * digamma(a) - N * np.log(x_bar) + N * np.log(a) + sum(np.log(x))
    l2 = - N * polygamma(n=1, x=a) + N/a
    return - l1 / l2

def Gamma_newton_update(a0, x, N_iter):  
    N = len(x)
    x_bar = np.mean(x)
    a_vals = np.zeros((N_iter,))  
    a_vals[0] = a0
    num_it = 0  
    sol_found = False   
    for i in range(1,N_iter):        
        num_it += 1        
        a = a_vals[i-1]
        a_new = a + Gamma_score(a, N, x, x_bar)
        a_vals[i] = a_new        
        if abs(a_new - a) < 1e-9 : 
            sol_found = True            
            break   
    if sol_found == True :    
        return a_new 
    elif sol_found == False :     
        return sol_found 

def inv_posdef(M):
    M_chol = cholesky(M, lower=False)
    M_chol_inv = dtrtri(M_chol)[0]
    M_inv = M_chol_inv.dot( M_chol_inv.transpose() )
    return M_inv

def plots(name_dist, n, X, theta_bar, crlb_bar, true_theta, crlb_theta):   
    if name_dist == "Gamma": 
        mean_convergence    = np.cumsum(X[0,:]) / np.arange(1,n+1,1)
        mean_rvs            = np.mean(X, axis=1)    
        title               = "Parameter estimation of " + name_dist 
        N                   = len(mean_convergence)
        x                   = np.arange(1,N+1,1)
        y                   = np.repeat(true_theta[0]/true_theta[1], N)
        s                   = np.sqrt( (true_theta[0]/true_theta[1])/np.sqrt(n) )  
        sda                 = np.sqrt(crlb_theta[0,0]) 
        vala                = np.linspace(norm.ppf(0.01, loc=true_theta[0], scale=sda), 
                                          norm.ppf(0.99, loc=true_theta[0], scale=sda), 
                                          100)
        norm_pdfa           = norm.pdf(vala, loc = true_theta[0], scale = sda)    
        CI                  = norm.interval(0.95, loc=theta_bar[0][0], scale=np.sqrt(crlb_bar[0,0]))
        
        fig, ax = plt.subplots(1, 3, figsize=(18,4))
        fig.suptitle(title, fontsize=22)
        ax[0].plot(x, mean_convergence, 'r-', lw=1, alpha=1)
        ax[0].plot(x, y, 'b-', lw=1, alpha=1)
        ax[0].set_ylim(true_theta[0]/true_theta[1] - s, true_theta[0]/true_theta[1] + s)
        ax[0].set_xlim(0, n+1)
        ax[0].grid(True)         
        ax[1].hist(mean_rvs, bins=100, density=True, alpha=0.5, facecolor='green')
        ax[1].axvline(x=true_theta[0]/true_theta[1], c="r", lw=1, alpha=1)    
        ax[2].plot(vala, norm_pdfa, lw=1, alpha=1)
        ax[2].axvline(x=true_theta[0], c="r", lw=1, alpha=1) 
        ax[2].axvline(x=CI[0], c="g", lw=1, alpha=1) 
        ax[2].axvline(x=CI[1], c="g", lw=1, alpha=1)    
        return fig        
    
    mean_convergence    = np.cumsum(X[0,:]) / np.arange(1,n+1,1)
    mean_rvs            = np.mean(X, axis=1)    
    title               = "Parameter estimation of " + name_dist 
    N                   = len(mean_convergence)
    x                   = np.arange(1,N+1,1)
    y                   = np.repeat(true_theta, N)
    s                   = np.sqrt( true_theta/np.sqrt(n) )  
    sd                  = np.sqrt(crlb_theta) 
    val                 = np.linspace(norm.ppf(0.01, loc=true_theta, scale=sd), 
                                      norm.ppf(0.99, loc=true_theta, scale=sd), 
                                      100)
    norm_pdf            = norm.pdf(val, loc = true_theta, scale = sd)        
    CI                  = norm.interval(0.95, loc=theta_bar[0], scale=np.sqrt(crlb_bar))
    
    fig, ax = plt.subplots(1, 3, figsize=(18,4))
    fig.suptitle(title, fontsize=22)
    ax[0].plot(x, mean_convergence, 'r-', lw=1, alpha=1)
    ax[0].plot(x, y, 'b-', lw=1, alpha=1)
    ax[0].set_ylim(true_theta - s, true_theta + s)
    ax[0].set_xlim(0, n+1)
    ax[0].grid(True)
    ax[1].hist(mean_rvs, bins=100, density=True, alpha=0.5, facecolor='green')
    ax[1].axvline(x=true_theta, c="r", lw=1, alpha=1)    
    ax[2].plot(val, norm_pdf, lw=1, alpha=1)
    ax[2].axvline(x=true_theta, c="r", lw=1, alpha=1) 
    ax[2].axvline(x=CI[0], c="g", lw=1, alpha=1) 
    ax[2].axvline(x=CI[1], c="g", lw=1, alpha=1)     
    return fig 

    