import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
        width=8E6, height=8E6, 
        lat_0=45, lon_0=-100,)
m.etopo(scale=0.5, alpha=0.5)
