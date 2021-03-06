import numpy as np
import cmath
import h5py
import os
import sys

sys.path.append(os.path.abspath('../romspline/'))
import romspline

def SaveData(data, output_file, output_path):
    '''Save NR data to hdf5 file
    data [NR_data]
    output_file [filename]
    output_path [path to output directory]
    '''

    filename = os.path.join(output_path, output_file)
    with h5py.File(filename, 'w') as fp:

        Lmax = 2
        r = "08"
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
            
        group = fp.create_group('auxiliary-info')

        for attr in set(data.metadata.__dict__)-set(["metadatadict"]):
            fp.attrs[attr] = data.metadata.__dict__[attr]

        for attr in data.metadata.metadatadict:
            print attr
            if attr is 'auxiliary-info':
                attr.write( group )
            else:
                fp.attrs[attr] = data.metadata.metadatadict[attr]
            

#    status = fp.close()
    return filename

