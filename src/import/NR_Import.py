from pylab import *
import os
import sys

def LoadUliMode(filename):
    dat = genfromtxt(filename)
    Time = array(dat[:,0])
    Re   = dat[:,1]
    Im   = dat[:,2]
    Psi4C = array(Re + Im*1j)
    return Time, Psi4C

def LoadUliData(l, m, rex, inputdir, root='Psi4_vars'):
  '''Load NR data for Psi4(t) from Uli's output file'''
  filename = os.path.join(inputdir, root+'_l'+str(l)+'_m'+str(m)+'_rex'+str(rex).zfill(2))
  return LoadUliMode(filename)

def LoadUliParams(inputdir, paramfile=None):
  '''Load simulation parameters from Uli's param file'''
  if paramfile is None:
    # convention is using parent directory name as root for parameter filename
    paramfile = os.path.split(os.path.normpath(inputdir))[-1]+'.par'
  filename = os.path.join(inputdir, paramfile)
  return os.path.abspath(filename)
  
def ListUliModes(inputdir):
  '''Populate list of available modes for Psi4 from Uli's data directory'''
  flist = os.listdir(inputdir)
  modes = {}
  for f in flist:
    fdec = f.split('_')
    if os.path.isfile(os.path.join(inputdir,f)) and fdec[0]+'_'+fdec[1] == 'Psi4_vars':
    #  print f
      l=fdec[2][1:]
      m=fdec[3][1:]
      rex=fdec[4][3:]
      if rex not in modes.keys():
        modes[rex]=[]
      modes[rex].append((int(l),int(m)))
  return modes

def readrlist(self):
  '''Get list of extraction radii from the param file'''




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


