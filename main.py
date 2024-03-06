import streamlit as st
import numpy as np
import pandas as pd



# Creating a sample 3D plot
st.title('3D Plot in Streamlit')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create data
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Show the plot in Streamlit
st.pyplot(fig)

st.write("Randomly Generated Time Series Data")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
