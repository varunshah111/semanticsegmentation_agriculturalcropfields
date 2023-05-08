#%%
# Rechunk image for inference

import geowombat as gw
import matplotlib.pyplot as plt
import geopandas as gpd
import os
from glob import glob

#%%
os.getcwd()
#%%
os.chdir("/home/ubuntu/Geography")


#%%
with gw.open('/home/ubuntu/Geography/inference/000016/evi/2021365.tif') as src:
    src.chunk({'band': -1, 'y': 64, 'x': 64}).gw.save(
    "/home/ubuntu/Geography/inference_rechunk/000016/evi/2021365.tif",
    overwrite=True
)
#%%