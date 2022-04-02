import numpy as np
from math import sin, pi

def sir(x, t, beta, gamma):
    s,i,r = x
    
    dsdt = - beta * s * i
    didt = + beta * s * i - gamma * i
    drdt = + gamma * i
    
    return np.array([dsdt, didt, drdt])


def sir_vs(x, t, n, beta, gamma, alpha, zeta, xi):
    s,i,r = x
    
    _lambda = beta * (1 + xi * sin(2*pi*t/365))
    _eta    = zeta if s > zeta else s
    
    dsdt = - _lambda * s * i - _eta + alpha * r
    didt = + _lambda * s * i - gamma * i
    drdt = + gamma * i + _eta - alpha * r 
    
    return np.array([dsdt, didt, drdt])