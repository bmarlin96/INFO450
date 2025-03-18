pip install streamlit seaborn

# Import libraries
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the penguins dataset
penguins = sns.load_dataset('penguins')

penguins.head()

# Commented out IPython magic to ensure Python compatibility.
# 
# %%writefile app.py
# # Set the title of the app
# import streamlit as st
# st.title('Penguin Data Explorer')
# 
# # Display the first few rows of the dataset
# st.write(penguins.head())
# 
# 
# # Create a scatter plot
# st.subheader('Scatter Plot')
# x_axis = st.selectbox('X-axis', penguins.columns)
# y_axis = st.selectbox('Y-axis', penguins.columns)
# 
# # Add a color option based on a column
# color_option = st.selectbox('Color by', ['None'] + list(penguins.columns))
# 
# # Create the plot
# fig, ax = plt.subplots()
# 
# if color_option == 'None':
#     sns.scatterplot(x=x_axis, y=y_axis, data=penguins, ax=ax)
# else:
#     sns.scatterplot(x=x_axis, y=y_axis, data=penguins, hue=color_option, ax=ax)
# 
# st.pyplot(fig)
# 
# 
# # Display data summary statistics
# st.subheader('Summary Statistics')
# st.write(penguins.describe())
# 
# # Display a histogram of a selected column
# st.subheader("Histogram")
# hist_column = st.selectbox("Choose a column for the histogram", penguins.select_dtypes(include=['number']).columns)
# fig, ax = plt.subplots()
# sns.histplot(data=penguins, x=hist_column, kde=True, ax=ax)
# st.pyplot(fig)
#
