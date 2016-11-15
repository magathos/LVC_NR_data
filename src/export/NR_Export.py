import numpy as np
import h5py
import romspline

def SaveData(data, output_file, output_path):
    filename = output_path + output_file

    spline = romspline.ReducedOrderSpline(data[:,0], data[:,1], verbose=False)

    Time = data[:,0]

    fp = h5py.File(filename, 'w')

    Lmax = 3

    for l in np.arange(2,Lmax+1):
        for m in np.arange(-l,l+1):
            Time  = data[:,0]
            amp   = data[:,1]
            phase = data[:,1]

            spline = romspline.ReducedOrderSpline(Time, amp, verbose=False)
            group = fp.create_group('amp_l'+str(l)+'_m'+str(m))
            spline.write(group)

            spline = romspline.ReducedOrderSpline(Time, phase, verbose=False)
            group = fp.create_group('phase_l'+str(l)+'_m'+str(m))
            spline.write(group)

    fp.close()

    return 1

