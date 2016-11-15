import numpy as np


def LoadUliMode(filename):
    dat = np.loadtxt(filename)
    Time = dat[:,0]
    Re   = dat[:,1]
    Im   = dat[:,2]
    return [Time, Re, Im]

def LoadUliData():
    LoadUliMode("/store/DAMTP/cjm96/public_html/Modes/Psi4_vars_l2_m0_rex02")



