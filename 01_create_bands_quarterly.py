#%%
import os
import fnmatch
import numpy as np
import geowombat as gw
import geopandas as gpd
import matplotlib.pyplot as plt
import cultionet
import torch
from torch_geometric.data import Data
from pathlib import Path
import re
#%%
# Changing to parent directory
OR_PATH = os.getcwd()
os.chdir("/home/ubuntu/Geography/Capstone")

DATA_DIR = os.getcwd() + os.path.sep + 'Data' + os.path.sep
sep = os.path.sep
os.chdir(OR_PATH)

#%%
# Reading Quarterly Chunks
QUARTERLY = DATA_DIR + 'Quarterly_Chunks' + sep

# /home/ubuntu/Geography/Capstone/Data/Quarterly_Bands/evi

evi_dir = DATA_DIR + 'Quarterly_Bands/evi' + os.path.sep
#red_dir = DATA_DIR + 'Quarterly_Bands/red' + os.path.sep
#blue_dir = DATA_DIR + 'Quarterly_Bands/blue' + os.path.sep
#green_dir = DATA_DIR + 'Quarterly_Bands/green' + os.path.sep
#with gw.config.update(sensor='l7')

#evi = ds.gw.evi(sensor='bgrn', scale_factor=0.0001)

#bands = ["B2", "B3", "B4", "B8"]

#%%

# ############
# 2021_Q01
# ###########
# Open a Sentinel 2 image
image = QUARTERLY + 'S2_SR_2021_Q01-0000000000-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021001.tif',
            num_workers=4,
            overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q01-0000000000-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021002.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q01-0000016384-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021003.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q01-0000016384-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021004.tif',
                  num_workers=4,
                  overwrite=True)

#%%
# 2021_Q02
image = QUARTERLY + 'S2_SR_2021_Q02-0000000000-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021101.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q02-0000000000-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021102.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q02-0000016384-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021103.tif',
                  num_workers=4,
                  overwrite=True)


image = QUARTERLY + 'S2_SR_2021_Q02-0000016384-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021104.tif',
                  num_workers=4,
                  overwrite=True)
#%%
# ############
# 2021_Q03
# ############

image = QUARTERLY + 'S2_SR_2021_Q03-0000000000-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021191.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q03-0000000000-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021192.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q03-0000016384-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021193.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q03-0000016384-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021194.tif',
                  num_workers=4,
                  overwrite=True)


#%%
# ############
# 2021_Q04
# ############

image = QUARTERLY + 'S2_SR_2021_Q04-0000000000-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021281.tif',
            num_workers=4,
            overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q04-0000000000-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021282.tif',
            num_workers=4,
            overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q04-0000016384-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021283.tif',
            num_workers=4,
            overwrite=True)

image = QUARTERLY + 'S2_SR_2021_Q04-0000016384-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2021284.tif',
            num_workers=4,
            overwrite=True)

#%%
# ############
# 2022_Q01
# ###########
# Open a Sentinel 2 image
image = QUARTERLY + 'S2_SR_2022_Q01-0000000000-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022001.tif',
            num_workers=4,
            overwrite=True)

image = QUARTERLY + 'S2_SR_2022_Q01-0000000000-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022031.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2022_Q01-0000016384-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022061.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2022_Q01-0000016384-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022081.tif',
                  num_workers=4,
                  overwrite=True)


#%%
# ############
# 2022_Q02
# ############
image = QUARTERLY + 'S2_SR_2022_Q02-0000000000-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022101.tif',
                  num_workers=4,
                  overwrite=True)


image = QUARTERLY + 'S2_SR_2022_Q02-0000000000-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022131.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2022_Q02-0000016384-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022151.tif',
                  num_workers=4,
                  overwrite=True)


image = QUARTERLY + 'S2_SR_2022_Q02-0000016384-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022171.tif',
                  num_workers=4,
                  overwrite=True)

#%%
# ############
# 2022_Q03
# ############
image = QUARTERLY + 'S2_SR_2022_Q03-0000000000-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022191.tif',
                  num_workers=4,
                  overwrite=True)


image = QUARTERLY + 'S2_SR_2022_Q03-0000000000-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022211.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2022_Q03-0000016384-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022241.tif',
                  num_workers=4,
                  overwrite=True)


image = QUARTERLY + 'S2_SR_2022_Q03-0000016384-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022261.tif',
                  num_workers=4,
                  overwrite=True)
#%%
# ############
# 2022_Q04
# ############
image = QUARTERLY + 'S2_SR_2022_Q04-0000000000-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022281.tif',
                  num_workers=4,
                  overwrite=True)


image = QUARTERLY + 'S2_SR_2022_Q04-0000000000-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022301.tif',
                  num_workers=4,
                  overwrite=True)

image = QUARTERLY + 'S2_SR_2022_Q04-0000016384-0000000000.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022331.tif',
                  num_workers=4,
                  overwrite=True)


image = QUARTERLY + 'S2_SR_2022_Q04-0000016384-0000016384.tif'
with gw.open(image) as src:
    # Use built-in normalization methods, such as the EVI
    evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
    gw.save(evi, evi_dir + '2022361.tif',
                  num_workers=4,
                  overwrite=True)

#%%


#%%
# ^(?!._)
#   if fnmatch.fnmatch(filename, 'S2_SR_2021_Q01'):
pattern = re.compile(r'^(?!._)S2_SR_.*$')
pattern2021_Q1 = re.compile(r'^.*2021_Q01.*$')
for filename in os.listdir(QUARTERLY):
    try:
        matches = pattern.match(filename).group()
        if pattern2021_Q1.match(matches):
            print(matches)
        else:
            pass
    except AttributeError:
        matches = pattern.match(filename)


    #if re.match('2021_Q01', pattern):
    #    print(filename)

#%%
pattern = re.compile(r'^(?!._)S2_SR_.*$')
pattern2021_Q1 = re.compile(r'^.*2021_Q01.*$')
pattern2021_Q2 = re.compile(r'^.*2021_Q02.*$')
pattern2021_Q3 = re.compile(r'^.*2021_Q03.*$')
pattern2021_Q4 = re.compile(r'^.*2021_Q04.*$')
pattern2022_Q1 = re.compile(r'^.*2022_Q01.*$')
pattern2022_Q2 = re.compile(r'^.*2022_Q02.*$')
pattern2022_Q3 = re.compile(r'^.*2022_Q03.*$')
pattern2022_Q4 = re.compile(r'^.*2022_Q04.*$')

for filename in os.listdir(QUARTERLY):
    try:
        matches = pattern.match(filename).group()
        with gw.open(matches) as src:
            evi = src.gw.evi(sensor='bgrn', scale_factor=0.0001)
            if pattern2021_Q1.match(matches):
                i = 0
                while gw.save(evi,
                              evi_dir + f'202100{i}.tif',
                              num_workers=4,
                              overwrite=True):
                    i+=1

            elif pattern2021_Q2.match(matches):
                i = 0
                while gw.save(evi,
                              evi_dir + f'202110{i}.tif',
                              num_workers=4,
                              overwrite=True):
                    i+=1

            elif pattern2021_Q3.match(matches):
                i = 0
                while gw.save(evi,
                              evi_dir + f'202119{i}.tif',
                              num_workers=4,
                              overwrite=True):
                    i+=1

            elif pattern2021_Q4.match(matches):
                i = 0
                while gw.save(evi,
                              evi_dir + f'202128{i}.tif',
                              num_workers=4,
                              overwrite=True):
                    i+=1

            elif pattern2022_Q1.match(matches):
                i = 0
                while gw.save(evi,
                              evi_dir + f'202200{i}.tif',
                              num_workers=4,
                              overwrite=True):
                    i += 1

            elif pattern2022_Q2.match(matches):
                i = 0
                while gw.save(evi,
                              evi_dir + f'202210{i}.tif',
                              num_workers=4,
                              overwrite=True):
                    i += 1

            elif pattern2022_Q3.match(matches):
                i = 0
                while gw.save(evi,
                              evi_dir + f'202219{i}.tif',
                              num_workers=4,
                              overwrite=True):
                    i += 1

            elif pattern2022_Q4.match(matches):
                i = 0
                while gw.save(evi,
                              evi_dir + f'202228{i}.tif',
                              num_workers=4,
                              overwrite=True):
                    i+=1

    except AttributeError:
        matches = pattern.match(filename)

#%%
fig, ax = plt.subplots(dpi=150)
evi.plot(robust=True, ax=ax)
#%%
#
fig, ax = plt.subplots(dpi=200)
#["B2","B3","B4","B8"]
with gw.open(image) as src:
    src.where(src != 0).sel(band=[3,2,1]).gw.imshow(robust=True, ax=ax)
    plt.tight_layout(pad=1)
#%%

with gw.open(image) as src:
    print(src)


#%%

