import streamlit as st
from shapely.geometry import Point, Polygon
import numpy as np
import os
# Simple test polygon (square)
poly = Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])

# Generate some test points
x = np.array([1, 5, 15])
y = np.array([1, 5, 5])

# Check if each point is inside the polygon
points = [Point(x[i], y[i]) for i in range(len(x))]
mask = [poly.contains(pt) for pt in points]

st.subheader("Points inside polygon:")
for i, inside in enumerate(mask):
    st.write(f"Point ({x[i]}, {y[i]}) → {'Inside' if inside else 'Outside'}")


st.subheader("Installed Python Packages")
packages = os.popen("pip list").read()
st.code(packages)
