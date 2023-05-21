from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

v0 = [40.0074, 32.8442] 
v1 = [39.9821, 32.8071]
v2 = [39.9895, 32.7556]
v3 = [39.9440, 32.7614]
v4 = [39.9658, 32.8282]
v5 = [39.9306, 32.8874]
v6 = [39.9624, 32.9087]
lats_vect = np.array([v0[0],v1[0],v2[0],v3[0],v4[0],v5[0],v6[0]])
lons_vect = np.array([v0[1],v1[1],v2[1],v3[1],v4[1],v5[1],v6[1]])
x, y = 39.9620, 32.90 # x = Lat, y = Lon


lons_lats_vect = np.column_stack((lons_vect, lats_vect)) # Reshape coordinates
polygon = Polygon(lons_lats_vect) # create polygon
point = Point(y,x) # create point
print(polygon.contains(point)) # check if polygon contains point
print(point.within(polygon)) # check if a point is in the polygon 



ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img() 

# Append first vertex to end of vector to close polygon when plotting
lats_vect = np.append(lats_vect, lats_vect[0])
lons_vect = np.append(lons_vect, lons_vect[0])
plt.plot([lons_vect[0:-1], lons_vect[1:]], [lats_vect[0:-1], lats_vect[1:]],
         color='black', linewidth=1, 
         transform=ccrs.Geodetic(),
         )   

plt.plot(y, x, 
        '*',          # marker shape
        color='blue',  # marker colour
        markersize=5  # marker size
        )  

plt.show()  