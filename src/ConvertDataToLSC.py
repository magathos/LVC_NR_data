import numpy as np
import sys
sys.path.insert(0, './export/')
sys.path.insert(0, './import/')

from NR_Import import *
from NR_Export import *

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
