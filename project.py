import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

# Load data
df = pd.read_csv('iran_cities.csv')

# Setup map
fig = plt.figure(figsize=(12, 10))
ax = plt.axes(projection=ccrs.Mercator())
ax.set_extent([40, 70, 20, 45], crs=ccrs.PlateCarree())

# Add features
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.LAKES, facecolor='lightblue')
ax.add_feature(cfeature.RIVERS)

# Plot cities
for _, row in df.iterrows():
    city = row['City']
    lat = row['Latitude']
    lon = row['Longitude']
    pop = row['Population']

    ax.plot(lon, lat, 'o', color='red', markersize=np.sqrt(pop) / 500, transform=ccrs.PlateCarree())
    ax.text(lon + 0.2, lat + 0.2, city, fontsize=9, transform=ccrs.PlateCarree())

# Center of Iran (approximate)
iran_lat, iran_lon = 32.5, 53.0
ax.plot(iran_lon, iran_lat, marker='*', color='blue', markersize=12, transform=ccrs.PlateCarree())
ax.text(iran_lon + 0.5, iran_lat, 'Center of Iran', fontsize=10, color='blue', transform=ccrs.PlateCarree())

# Title
ax.set_title('Iran Cities with Population Circles and Central Coordinate')

plt.show()


# Convert decimal degrees to DMS
def decimal_to_dms(degree):
    d = int(degree)
    m = int((abs(degree) - abs(d)) * 60)
    s = (abs(degree) - abs(d) - m / 60) * 3600
    return f"{abs(d)}°{m}'{s:.2f}\" {'N' if degree >= 0 else 'S'}" if degree >= 0 else f"{abs(d)}°{m}'{s:.2f}\" {'S'}"


lat_dms = decimal_to_dms(iran_lat)
lon_dms = decimal_to_dms(iran_lon)

print(f"Approximate center of Iran is at coordinates: ({iran_lat}, {iran_lon})")
print(f"Which corresponds to the following in Degrees/Minutes/Seconds format:")
print(f"Latitude: {lat_dms}")
print(f"Longitude: {lon_dms}")

