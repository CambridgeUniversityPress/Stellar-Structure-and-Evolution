#
# python stub to read the model files
#

import numpy as np
import pandas as pd
 
inFile='profile_m30_zams.txt'
data = pd.read_csv(inFile,sep=r'\s+',header=4)
 
colheads = np.array(data.columns).tolist()
print(colheads)

mass = np.array(data['mass'])
print(mass)
