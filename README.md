# IGRF-MAP
Mapa da intensidade do campo magnético utilizando dados do IGRF
Created on Thu Mar 21 14:36:08 2024

@author: amanda
mapa formato oval da terra
"""

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load data from the CVC file
data = np.genfromtxt('your_file.cvc', delimiter=',')

# Extract latitude, longitude, and totalintensity
lat = data[:, 1]
lon = data[:, 2]
totalintensity = data[:, 4]

# Define coordinates for station points (example coordinates)
station_lats = [latitude_of_station_1, latitude_of_station_2, latitude_of_station_3]
station_lons = [longitude_of_station_1, longitude_of_station_2, longitude_of_station_3]

# Create a grid for plotting
lon_grid, lat_grid = np.meshgrid(np.unique(lon), np.unique(lat))
totalintensity_grid = totalintensity.reshape(len(np.unique(lat)), len(np.unique(lon)))

# Invert the grid
totalintensity_grid = np.flipud(totalintensity_grid)

# Create a contour plot with more levels of Cividis colormap and contour lines
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.Mollweide())
ax.add_feature(cfeature.COASTLINE)
contour = ax.contourf(lon_grid, lat_grid, totalintensity_grid, transform=ccrs.PlateCarree(), cmap='cividis', levels=20)
plt.colorbar(contour, label='Totalintensity (nT)')

# Add contour lines
contour_lines = ax.contour(lon_grid, lat_grid, totalintensity_grid, transform=ccrs.PlateCarree(), colors='black', levels=20, linewidths=0.5)

# Add station points
ax.scatter(station_lons, station_lats, color='red', marker='o', s=50, transform=ccrs.PlateCarree(), label='Stations')

plt.title('Contour Map of Magnetic Field Totalintensity with Stations (Mollweide Projection)')
plt.legend()
plt.show()
