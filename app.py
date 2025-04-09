import streamlit as st # type: ignore
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Data Visualization")

# Create sample data
data = pd.DataFrame({
    'Year': [2015, 2016, 2017, 2018, 2019, 2020],
    'Sales': [100, 150, 200, 180, 300, 400]
})

# Display charts
st.line_chart(data.set_index('Year'))
st.bar_chart(data.set_index('Year'))

# Using Matplotlib
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Sales'], marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Sales')
ax.set_title('Sales Over Years')
st.pyplot(fig)