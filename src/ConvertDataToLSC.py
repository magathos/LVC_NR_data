#!/bin/python
from pylab import *
import os
import sys
import argparse as ap

parser = ap.ArgumentParser()
sys.path.insert(0, './export/')
sys.path.insert(0, './import/')

from NR_Import import *
from NR_Export import *

def modesuptolmax(lmax):
  res = []
  for l in arange(lmax-1) +2:
    for m in arange(2*l+1)-lmax:
      res.append((l,m))
  return set(res)

def check_modelist(modelist, lmax=None):
  '''modelist is list of (l,m) tuples. Check whether all modes up to lmax are included.'''
  if lmax is None:
    lmax = max(array(modelist)[:,0])
  return len(set(modelist) - modesuptolmax(lmax))

class NR_data:
#  Class that hosts imported data from NR simulations
  def __init__(self, nrtype, nrid, sourcedir, lmax=None, rlist=None):
    self.lmax = lmax
    self.nrid = nrid
    self.nrtype = nrtype
    self.sourcedir = sourcedir
    self.Psi4modes = []
    if lmax is None:
      self.readmodelist()
    else:
      self.llist = arange(self.lmax-1) + 2
      for l in self.llist:
        mlist = arange(2*l+1) - l
        modedict[l] = {}
    if rlist is None:
      self.readrlist()

  def parse_params(self):
    '''Read parameter file(s)'''
    

  def read_modelist(self):
    '''Read list of modes available in source directory'''
    modelist = []
    loc = self.sourcedir
        


  def populate_modes(self, lmax, rlist):
    '''Populate modes with data for l<=lmax'''
    modedict = {}
    if lmax is None:
      print "Importing all available modes... not implemented yet, exiting..."
      sys.exit(-1)
    for l in llist:
      mlist = arange(2*l+1) - l
      modedict[l] = {}
      for m in mlist:
        for r in rlist:
          thisNR_mode = NR_mode(l, m, r, self.nrtype, self.sourcedir)
          thisNR_mode.load_data()
          modedict[l][m] = thisNR_mode
        
    self.Psi4modes = modelist

    
  def Psi4mode(self, l, m):
    '''Get the mode (l,m)'''
    if l not in self.Psi4modes.keys():
      print "Mode l=",l,", m=",m," do not exist. Exiting..."
      sys.exit(-1)
    elif m not in self.Psi4modes[l].keys():
      print "Mode l=",l,", m=",m," does not exist. Exiting..."
      sys.exit(-1)
    return self.Psi4modes[l][m]



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
      self.write_data(source)

  def load_data(self, source=None):
    '''Write Psi4 time series data to mode'''
    loadmodefunc = loadDataFDict[self.nrtype]
    nrtime, Psi4C = loadmodefunc(self.l, self.m, self.r, self.sourcedir)
    #sanity checks
    self.t = nrtime
    self.Psi4C = Psi4C
    


if __name__ == "__main__":

  parser.add_argument('-t', '--NRtype', type=str, dest='NRtype', required=True, nargs=1, choices=['Uli','GRChombo'], help='Type of NR data to be imported. Currently supported: {"Uli", "GRChombo"}')
  parser.add_argument('-m', '--mode', type=int, nargs=2)
  parser.add_argument('-l', '--lmax', type=int, nargs=1)
  parser.add_argument('-i', '--inputdir', dest='inputdir', type=str, nargs=1)
  parser.add_argument('-o', '--outputdir', dest='outputdir', type=str, nargs=1)
  
  # Hardcoded list of modes (FIXME)
  modelist = [[2,2]]

  NRtype = parser.NRtype
  
  # Load Data
  input_path = parser.inputdir
  #data = LoadUliData(input_path)
  
  
  # Save Data
  output_path = parser.outputdir
  output_file = os.path.join(output_path,"test.h5")
  
  data = NR_data(NRtype, NRID, input_path, lmax)

  data = np.zeros((100,2))
  data[:,0] = np.arange(0,10,0.1)
  data[:,1] = np.sin(data[:,0])
  
  SaveData(data, output_file, output_path)
