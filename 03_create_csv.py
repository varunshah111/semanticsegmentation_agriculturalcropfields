#%%
import pandas as pd
import os
#%%
data = pd.read_csv('https://raw.githubusercontent.com/mmann1123/ym_field_boundaries/main/regions.csv')

#%%

OR_PATH = os.getcwd()
os.chdir("/home/ubuntu/Geography/Capstone")

DATA_DIR = os.getcwd() + os.path.sep + 'Data' + os.path.sep
sep = os.path.sep
os.chdir(OR_PATH)

#%%
regions = pd.DataFrame(data)

#%%
regions.to_csv(DATA_DIR+'regions.csv')

#%%
