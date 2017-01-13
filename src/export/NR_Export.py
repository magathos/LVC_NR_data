import numpy as np
import cmath
import h5py
import os
import sys

sys.path.append(os.path.abspath('../romspline/'))
import romSpline

def SaveData(data, output_file, output_path):

    filename = os.path.join(output_path, output_file)
    fp = h5py.File(filename, 'w')

    Lmax = 2
    r = "08"
    for l in np.arange(2, Lmax+1):
        for m in np.arange(-l, l+1):
            mode = data.Psi4mode(l,m,r)
            Time   = mode.t
            Psi4   = mode.Psi4C

            amp   = np.array([ abs(p) for p in Psi4 ])
            phase = np.array([ cmath.phase(p) for p in Psi4 ])

            spline = romSpline.ReducedOrderSpline(Time, amp, verbose=False)
            group  = fp.create_group( 'amp_l'+str(l)+'_m'+str(m) )
            spline.write( group )

            spline = romSpline.ReducedOrderSpline(Time, phase, verbose=False)
            group  = fp.create_group( 'phase_l'+str(l)+'_m'+str(m) )
            spline.write( group )

    for attr in set(data.metadata.__dict__)-set(["metadatadict"]):
        fp.attrs[attr] = data.metadata.__dict__[attr]

    for attr in data.metadata.metadatadict:
        fp.attrs[attr] = data.metadata.metadatadict[attr]

    status = fp.close()
    return status

