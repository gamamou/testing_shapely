import streamlit as st
from shapely.geometry import Point, Polygon
from shapely.vectorized import contains
import numpy as np

# Simple test polygon (square)
poly = Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])

# Generate some test points
x = np.array([1, 5, 15])
y = np.array([1, 5, 5])

# Use shapely.vectorized.contains to test
mask = contains(poly, x, y)

st.write("Points inside polygon:", mask)
