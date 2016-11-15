import numpy as np

from NR_Import import *
from NR_Export import *

# Load Data
input_path = "/store/DAMTP/cjm96/public_html/Modes/"
data = LoadUliData(input_path)

# Save Data
output_path = "$HOME/Desktop/"
output_file = "test.h5"
SaveData(data, output_file, output_path)
