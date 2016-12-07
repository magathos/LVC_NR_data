import os
import sys
#sys.path.append(os.path.abspath("/home/ma748/projects/LVC_NR/src"))
import ConvertDataToLSC as lsc

modelist = lsc.ListUliModes("../../data/Uli/alpha030_h48/Modes")

print modelist.keys()
print modelist['03']

for rex in modelist.keys():
  print "Checking list of modes at extraction radius " + rex
  diff=  lsc.check_modelist(modelist[rex])
  print diff


print lsc.modesuptolmax(4)
print len(lsc.modesuptolmax(4))

nrd = lsc.NR_data("Uli", "123", "../../data/Uli/alpha030_h48/Modes")
nrd.populate_modes()
print nrd.Psi4modes.keys()

mode22 = nrd.Psi4mode(2,2,"03")
print mode22.l
print mode22.m
print mode22.radius
print mode22.sourcedir
print mode22.nrtype
print mode22.t[:10]
print mode22.Psi4C[:10]

print nrd.Psi4mode(4,3,"02").Psi4C[:20]
