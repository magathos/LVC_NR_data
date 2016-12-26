#!/bin/python
#from pylab import *
from numpy import *
import os
import sys
import pyparsing as pp

def LeanParser(s):
  
  cls = pp.Word(pp.alphas, pp.alphanums+'_')
  attr = pp.Word(pp.alphas, pp.alphanums+'_')
  par = cls + '::' + attr
  scal = Word(pp.nums+'-'+'.'+'e'+'E'+'d')
  integ = Word(pp.nums+'-')
  par = cls + '::' + attr + pp.Optional("[" + integ + "]")
  
  # use QuotedString instead!  string = '"' + Word(pp.alphanums+'_'+pp.LineEnd()) + '"' 
  value = pp.Or(scal, pp.QuotedString(multiline=True), pp.alphanums)
  assign = par + "=" + value  
  p.setName("LeanParser")
  
  comment = pp.pythonStyleComment
  line = assign + pp.Optional(comment)
  SetResultsName()
  parseFile()
  

  

def LoadUliMode(filename):
    dat = genfromtxt(filename)
    Time = array(dat[:,0])
    Re   = dat[:,1]
    Im   = dat[:,2]
    Psi4C = array(Re + Im*1j)
    return Time, Psi4C

def LoadUliData(l, m, rex, inputdir, root='Psi4_vars'):
  '''Load NR data for Psi4(t) from Uli's output file'''
  filename = os.path.join(inputdir, "Modes", root+'_l'+str(l)+'_m'+str(m)+'_rex'+str(rex).zfill(2))
  return LoadUliMode(filename)

def LoadUliParams(inputdir, paramfile=None):
  '''Load simulation parameters from Uli's param file'''

  if paramfile is None:
    # convention is using parent directory name as root for parameter filename
    paramfile = os.path.split(os.path.normpath(inputdir))[-1]+'.par'
  filename = os.path.join(inputdir, paramfile)

  print "Loading parameters from file: ", filename
  
  f = open(filename, 'r')
  print f.read()
  #parsedict = LeanParser(f)
  

  paramdict = {}

  # Group/code info
  paramdict["NR-group"] = "DAMTP"
  paramdict["NR-code"] = "LEAN"
  paramdict["modification-date"] = os.path.getmtime(filename)
  paramdict["point-of-contact-email"] = "magathos@damtp.cam.ac.uk"
  paramdict["INSPIRE-bibtex-keys"] = "Sperhake:2006cy"
  paramdict["license"] = "LVC-internal"

  # Simulation setup info
  # paramdict["Lmax"] = "8"
  paramdict["simulation-type"] = "aligned-spins"
  paramdict["auxiliary-info"] = "LEAN_v1.1, Cactus_v3.2"
  paramdict["NR-techniques"] =  "BSSN"
  # Series info
  paramdict["files-in-error-series"] = ""
  paramdict["comparable-simulation"] = ""
  paramdict["production-run"] = 1

  # CBC parameters
  paramdict["object1"] = "BH"
  paramdict["object2"] = "BH"
  # paramdict["mass1"] = parserdict["BHInfo::bh_mass_ini[1]"]
  # paramdict["mass2"] = parserdict["BHInfo::bh_mass_ini[2]"]
  # paramdict["eta"] = float(parserdict["BHInfo::bh_mass_ini[1]"])/float(parserdict["BHInfo::bh_mass_ini[2]"])
  paramdict["f_low"] = 10.0
  paramdict["spin1x"] = 0.0
  paramdict["spin1y"] = 0.0
  paramdict["spin1z"] = 0.1
  paramdict["spin2x"] = 0.0
  paramdict["spin2y"] = 0.0
  paramdict["spin2z"] = -0.1
  paramdict["LNhatx"] = 0.0
  paramdict["LNhaty"] = 0.0
  paramdict["LNhatz"] = 1.0
  paramdict["nhatx"] = 0.0
  paramdict["nhaty"] = 0.0
  paramdict["nhatz"] = 1.0
  paramdict["Omega"] = 0.05
  paramdict["eccentricity"] = 0.0
  paramdict["mean_anomaly"] = -1
  #  paramdict[""] = 
  return paramfile, paramdict
  
def ListUliModes(inputdir):
  '''Populate list of available modes for Psi4 from Uli's data directory'''
  modesdir = os.path.join(inputdir, "Modes")
  flist = os.listdir(modesdir)
  modes = {}
  for f in flist:
    fdec = f.split('_')
    if os.path.isfile(os.path.join(modesdir,f)) and fdec[0]+'_'+fdec[1] == 'Psi4_vars':
      print f
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


