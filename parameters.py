import sympy as sym
from numpy import pi

# Performance parameters
# Taken from MIT AeroAstro 16.01 Unified Engineering I, II, III, & IV course
# https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-01-unified-engineering-i-ii-iii-iv-fall-2005-spring-2006/

# Electrical Flight Power
P_elec_J = sym.symbols("P_elec")
eta_p_, eta_m_ = sym.symbols("eta_p eta_m")
W_N, rho_kgpm3, S_m2 = sym.symbols("W rho S")
CDA0_m2, CL_, cd_, AR_ = sym.symbols("CDA_0 C_L c_d AR")

P_elec_J = (1 / eta_m_ * eta_p_) * sym.sqrt((2 * W_N**3) / (rho_kgpm3 * S_m2)) * \
            (((CDA0_m2 / S_m2) / (CL_ ** 3/2)) + \
            (cd_ / (CL_ ** 3/2)) + \
            ((CL_ ** 1/2)/(pi * AR_)))