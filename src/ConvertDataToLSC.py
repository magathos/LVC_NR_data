#!/bin/python
from pylab import *
import os
import sys
import argparse as ap

parser = ap.ArgumentParser()

sys.path.insert(0, os.path.abspath('/home/ma748/projects/LVC_NR/src/import/'))
sys.path.insert(0, os.path.abspath('/home/ma748/projects/LVC_NR/src/export/'))

from NR_Import import *
from NR_Export import *


# Function Definitions

def modesuptolmax(lmax):
  '''Returns a set of (l,m) tuples from l=2 up to lmax'''
  res = []
  for l in arange(lmax-1) +2:
    for m in arange(2*l+1)-l:
      res.append((l,m))
  return set(res)

def get_lmax(modelist):
  '''Returns max value of l in the list of modes'''
  return max(array(modelist)[:,0])

def check_modelist(modelist, lmax=None):
  '''modelist is list of (l,m) tuples. Check whether all modes up to lmax are included.'''
  if lmax is None:
    lmax = get_lmax(modelist)
  return len(set(modelist) - modesuptolmax(lmax))


# Class Definitions

class NR_data:
#  Class that hosts imported data from NR simulations
  def __init__(self, nrtype, nrid, sourcedir, lmax=None, rlist=None):
    self.lmax = lmax
    self.nrid = nrid
    self.nrtype = nrtype
    self.sourcedir = os.path.abspath(sourcedir)
    self.Psi4modes = {}
    if lmax is None:
      self.read_modelists()
    else:
      if rlist is None:
        print "ERROR: Extraction radii not given! Exiting..."
        sys.exit(-1)
      self.modelist_dict = {}
      for rex in rlist:
        self.modelist[rex] = modesuptolmax(lmax)
    if rlist is None:
      self.extraction_radii = self.modelist_dict.keys()
    else:
      self.extraction_radii = rlist

  def parse_params(self):
    '''Read parameter file(s)'''
    loadParamsFDict[self.nrtype](self.sourcedir) # Currently just prints stuff
    
  def read_modelists(self):
    '''Read dictionary of lists of modes available in source directory (per rex)'''
    self.modelist_dict = {}
    loc = self.sourcedir
    self.modelist_dict = listModesFDict[self.nrtype](loc)
    


  def populate_modes(self):
    '''Populate modes with data'''
    modedict = {}
    for rex in self.modelist_dict.keys():
      modedict[rex] = {}
      for (l,m) in self.modelist_dict[rex]:
        thisNR_mode = NR_mode(l, m, rex, self.nrtype, self.sourcedir)
        thisNR_mode.load_data()
        modedict[rex][(l,m)] = thisNR_mode
        
    self.Psi4modes = modedict

    
  def Psi4mode(self, l, m, r):
    '''Get the mode (l,m)'''
    if r not in self.Psi4modes.keys():
      print "Extraction radius ",r," does not exist. Exiting..."
      sys.exit(-1)
    elif (l,m) not in self.Psi4modes[r].keys():
      print "Mode l=",l,", m=",m," does not exist at extraction radius ",r,". Exiting..."
      sys.exit(-1)
    return self.Psi4modes[r][(l,m)]



class NR_mode: 
  '''Class that holds NR data for one (l,m) mode of Psi4'''
  def __init__(self, l, m, r, nrtype, sourcedir, source=None):
    self.l = l
    self.m = m
    self.radius = r
    self.sourcedir = sourcedir
    self.nrtype = nrtype
    if abs(m) > l:
      print "ERROR: Cannot generate mode with |m| > l. Exiting..."
      sys.exit(-1)
    if source is not None:
      print "Not implemented!"
      self.load_data(source)

  def load_data(self, source=None):
    '''Write Psi4 time series data to mode'''
    loadmodefunc = loadDataFDict[self.nrtype]
    nrtime, Psi4C = loadmodefunc(self.l, self.m, self.radius, self.sourcedir)
    #sanity checks
    self.t = nrtime
    self.Psi4C = Psi4C

  # def scale_data(self, mass):
  #   '''Scales data by <mass>'''
  #   self.radius = mass*self.radius
  #   self.t = mass*self.t
  #   self.Psi4c = 
    


if __name__ == "__main__":

  parser.add_argument('-t', '--NRtype', type=str, dest='NRtype', required=True, choices=['Uli','GRChombo'], help='Type of NR data to be imported. Currently supported: {"Uli", "GRChombo"}')
  parser.add_argument('-m', '--mode', type=int, dest='mode', nargs=2, default=None)
  parser.add_argument('-l', '--lmax', type=int, default=None)
  parser.add_argument('-n', '--NRID', dest='NRID', required=True, type=str)
  parser.add_argument('-i', '--inputdir', dest='inputdir', type=str)
  parser.add_argument('-o', '--outputdir', dest='outputdir', type=str)
  
  args = parser.parse_args()
  # Hardcoded list of modes (FIXME)
  # modelist = [[2,2]]
  print args.NRtype
  NRtype = args.NRtype
  NRID = args.NRID
  lmax = args.lmax
  mode = args.mode

  # Load Data
  input_path = os.path.abspath(args.inputdir)
  if not os.path.isdir(input_path):
    print "ERROR", input_path, " does not exist! Exiting..."
    sys.exit(-1)
  #data = LoadUliData(input_path)
  
  
  # Save Data
  output_path = os.path.abspath(args.outputdir)
  if not os.path.isdir(output_path):
    os.makedirs(output_path)
  output_file = os.path.join(output_path,"test.h5")
  

  nrdata = NR_data(NRtype, NRID, input_path, lmax)
  #nrdata.parse_params()
  nrdata.populate_modes()

  print "Imported the following modes:"
  print nrdata.modelist_dict
  for rex in nrdata.Psi4modes.keys():
    for (l,m) in nrdata.Psi4modes[rex].keys():
      print rex, l, m


  print "Saving modes to file..."
  SaveData(nrdata, output_file, output_path)

  print "DONE!"
