import numpy as np
import os

loadFuncDict = {'Uli':LoadUliData, 'GRChombo':LoadGRChomboData}

def LoadUliMode(filename):
    dat = np.genfromtxt(filename)
    Time = array(dat[:,0])
    Re   = dat[:,1]
    Im   = dat[:,2]
    Psi4C = array(Re + Im*1j)
    return Time, Psi4C

def LoadUliData(l, m, rex, inputdir, root='Psi4_vars'):
  '''Load NR data for Psi4(t) from Uli's output file'''
  filename = os.path.join(inputdir, root+'_l'+str(l)+'_m'+str(m)+'_rex'+str(rex).zfill(2))
  LoadUliMode(filename)



