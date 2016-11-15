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


class NR_data:
  '''Class that hosts imported data from NR simulations'''
  def __init__(self, nrtype, nrid, lmax=2):
    self.lmax = lmax
    self.nrid = nrid
    self.nrtype = nrtype
    self.Psi4modes = []

  def populate_modes(self, lmax):
    '''Populate modes with data for l<=lmax'''
    modelist = []
    llist = arange(lmax-1) + 2
    for l in llist:
      modelist.append()
      mlist = arange(2*l+1) - l
      for m in mlist:
      thisNR_mode = NR_mode(l, m, nrtype)
        
    self.Psi4modes = modelist

    
  def Psi4mode(self, l, m):
    '''Get the mode (l,m)'''
    return



class NR_mode: 
  '''Class that holds NR data for one (l,m) mode of Psi4'''
  def __init__(self, l, m, nrtype, source=None):
    self.l = l
    self.m = m
    self.nrtype = nrtype
    if abs(m) > l:
      print "ERROR: Cannot generate mode with |m| > l. Exiting..."
      sys.exit(-1)
    if source is not None:
      self.write_data(source)

  def write_data(self, source):
    '''write data to mode'''
    loadmodefunc = loadFuncDict[self.nrtype]
    nrtime, Psi4C = loadmodefunc(source)
    #sanity checks
    self.t = nrtime
    self.Psi4C = Psi4C
    


if __name__ == "__main__":

parser.add_argument('-t', '--NRtype', type=str, dest='NRtype', required=True, nargs=1, choices=['Uli','GRChombo'], help='Type of NR data to be imported. Currently supported: {"Uli", "GRChombo"}')
parser.add_argument('-m', '--mode', type=int, nargs=2)



# Load Data
input_path = "/store/DAMTP/cjm96/public_html/Modes/"
#data = LoadUliData(input_path)

# Save Data
output_path = "$HOME/Desktop/"
output_file = "test.h5"

data = np.zeros((100,2))
data[:,0] = np.arange(0,10,0.1)
data[:,1] = np.sin(data[:,0])

SaveData(data, output_file, output_path)
