import numpy as np
import romspline

def SaveData(data, output_file, output_path):
    filename = output_path + output_file

    spline = romspline.ReducedOrderSpline(data[:,0], data[:,1], verbose=False)

    print spline(np.pi)

    return 1
