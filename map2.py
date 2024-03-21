# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:06:55 2024

@author: amand
"""

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import LinearSegmentedColormap

# Load data from the CVC file
data = np.genfromtxt('dataigrf.csv', delimiter=',')

# Extract latitude, longitude, and totalintensity
lat = data[:, 1]
lon = data[:, 2]
totalintensity = data[:, 4]

# Create a grid for plotting
lon_grid, lat_grid = np.meshgrid(np.unique(lon), np.unique(lat))
totalintensity_grid = totalintensity.reshape(len(np.unique(lat)), len(np.unique(lon)))

# Invert the grid
totalintensity_grid = np.flipud(totalintensity_grid)

# Define custom levels and colors
levels = [0, 25000, 35000, 45000, 55000, 65000, 70000]
colors = ['blue'] * 5 + ['orange'] * 5 + ['yellow'] * 5 + ['red'] * 5
cmap_name = 'custom_map'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=20)
# Create a contour plot with the custom colors
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
contour = ax.contourf(lon_grid, lat_grid, totalintensity_grid, transform=ccrs.PlateCarree(), levels=levels, colors=colors)
plt.colorbar(contour, label='Totalintensity (nT)', ticks=levels)
plt.title('Contour Map of Magnetic Field Totalintensity')
plt.show()

