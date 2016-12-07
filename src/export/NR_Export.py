import numpy as np
import cmath
import h5py
import os
import romspline

def SaveData(data, output_file, output_path):

    filename = os.path.join(output_path, output_file)
    fp = h5py.File(filename, 'w')

    Lmax = 3
    r = "02"
    for l in np.arange(2, Lmax+1):
        for m in np.arange(-l, l+1):
            mode = data.Psi4mode(l,m,r)
            Time   = mode.t
            Psi4   = mode.Psi4C

            amp   = np.array([ abs(p) for p in Psi4 ])
            phase = np.array([ cmath.phase(p) for p in Psi4 ])

            spline = romspline.ReducedOrderSpline(Time, amp, verbose=False)
            group  = fp.create_group( 'amp_l'+str(l)+'_m'+str(m) )
            spline.write( group )

            spline = romspline.ReducedOrderSpline(Time, phase, verbose=False)
            group  = fp.create_group( 'phase_l'+str(l)+'_m'+str(m) )
            spline.write( group )

    fp.close()
    return 1

