import numpy as np
import os
import sys

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

def LoadUliParams(inputdir, paramfile=None):
  '''Load simulation parameters from Uli's param file'''
  if paramfile is None:
    # convention is using parent directory name as root for parameter filename
    paramfile = os.path.splitdrive(inputdir)[-1]+'.par'

  filename = os.path.join(inputdir, paramfile)
  return filename
  
def ListUliModes(inputdir):
  '''Populate list of available modes for Psi4 from Uli's data directory'''
  flist = os.listdir(loc)
  modes = []
  for f in flist:
    fdec = f.split('_')
    if fdec[0]+'_'+fdec[1] == 'Psi4_vars':
      l=fdec[2][1:]
      m=fdec[3][1:]
      reslist.append[(l,m)]
  return modes

def LoadGRChomboParams(inputdir, paramfile=None):
  '''Load simulation parameters from GRChombo param file'''
  return

def LoadGRChomboData(l, m, rex, inputdir, root='Psi4_vars'):
  '''Load NR data for Psi4(t) from GRChombo output file'''
  filename = os.path.join(inputdir, root+'_l'+str(l)+'_m'+str(m)+'_rex'+str(rex).zfill(2))
  sys.exit(-1)

def ListGRChomboModes(inputdir):
  '''Populate list of available modes for Psi4 from GRChombo data directory'''
  return



loadDataFDict = {'Uli':LoadUliData, 'GRChombo':LoadGRChomboData}
loadParamsFDict = {'Uli':LoadUliParams, 'GRChombo':LoadGRChomboParams}
listModesFDict = {'Uli':ListUliModes, 'GRChombo':ListGRChomboModes}


