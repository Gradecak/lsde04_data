import geopandas as gpd
import sys

fname = sys.argv[1]
outfile = sys.argv[2]
df = gpd.read_file(fname)
print(df.crs)
x = df.to_crs(epsg=4326)
print(x.crs)
x.to_file(filename=outfile, driver="GeoJSON")
