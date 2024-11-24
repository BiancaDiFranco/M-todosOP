import pandas as pd
import geopandas as gpd
from shapely import Point
import matplotlib.pyplot as plt


#Manzanas
url = 'https://raw.githubusercontent.com/BiancaDiFranco/M-todosOP/refs/heads/main/Trabajo%20final/datasets%20complementarios/manzanas.gml'
dfmanzanas = gpd.read_file(url)

gdf = gpd.GeoDataFrame(dfmanzanas, geometry="geometry")
gdf.set_crs('EPSG:4326', inplace=True)
ax = gdf.plot(figsize=(10, 10), facecolor='none', edgecolor='black')
ax.set_title('Mapa Geoespacial de Manzanas de Rosario', fontsize=15)
#plt.show()

#Autopistas
url2 = 'https://raw.githubusercontent.com/BiancaDiFranco/M-todosOP/refs/heads/main/Trabajo%20final/datasets%20complementarios/autopistas.gml'

dfautopistas = gpd.read_file(url2)
gdf2 = gpd.GeoDataFrame(dfautopistas, geometry="geometry")
gdf2.set_crs('EPSG:4326', inplace=True)
ax = gdf2.plot(figsize=(10, 10), facecolor='none', edgecolor='red')
ax.set_title('Mapa Geoespacial de Autopistas de Rosario', fontsize=15)
#plt.show()

#Zonas inundables

url3 = 'https://raw.githubusercontent.com/BiancaDiFranco/M-todosOP/refs/heads/main/Trabajo%20final/datasets%20complementarios/zonas_inundables_saladillo.gml'

dfinundaciones = gpd.read_file(url3)
gdf3 = gpd.GeoDataFrame(dfinundaciones, geometry="geometry")
gdf3.set_crs('EPSG:4326', inplace=True)
ax = gdf3.plot(figsize=(10, 10), facecolor='none', edgecolor='blue')
ax.set_title('Mapa Geoespacial de Zonas Inundables en Rosario', fontsize=15)
#plt.show()

#esot no estaria funcionando
gdf_combined = gpd.overlay(gdf, gdf2, how='union',keep_geom_type=False)
gdf_combined.plot()