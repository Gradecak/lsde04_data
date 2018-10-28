import geopandas as gpd
import sys
import os


for filename in os.listdir("./"):
  df = gpd.read_file(filename)
  print(df.crs)
  x = df.to_crs(epsg=4326)
  print(x.crs)
  outfile = "p%s" % filename
  x.to_file(filename=outfile, driver="GeoJSON")
