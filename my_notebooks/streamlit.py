#run
#$ streamlit run /home/or/Projects/python-for-data-science-and-machine-learning/my_notebooks/streamlit.py
import time
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

#---------------------------------------------------------
'iris_data'
iris_data = load_iris()

data= pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
fig = plt.figure()
sns.histplot(data = data, bins=20)
st.pyplot(fig)
#---------------------------------------------------------
'boxplot'
fig = plt.figure()
sns.boxplot(data = data)
st.pyplot(fig)
#---------------------------------------------------------
'scatterplot'
fig = plt.figure()
sns.scatterplot(data = data)
st.pyplot(fig)
#---------------------------------------------------------
animals = ['cat', 'cow', 'dog', 'tiger']
heights = [30, 150, 80, 60]
weights = [5, 400, 40, 50]

fig, ax = plt.subplots()

x = np.arange(len(heights))
width = 0.40

ax.bar(x-0.2, heights, width, color='red')
ax.bar(x+0.2, weights, width, color='orange')

ax.legend(['height', 'weight'])

ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)

'pi chart with explode'
explode = [0.2, 0.1, 0.1, 0.1]
plot_pie, ax = plt.subplots()
ax.pie(heights, explode=explode, labels=animals, autopct='%1.1f%%', shadow=True)
ax.axis('equal')
st.pyplot(plot_pie)

'pi chart'
fig, ax = plt.subplots()
ax.pie(heights, labels=animals)
st.pyplot(fig)

#---------------------------------------------------------
rows = np.random.randn(1,2)

'Growing Line Chart:'
chart = st.line_chart(rows)

for i in range(1, 100):
    new_row = rows[0] + np.random.randn(1,2)
    chart.add_rows(new_row)
    rows = new_row
    time.sleep(0.05)

#---------------------------------------------------------
values = np.random.randn(10)
"Matplotlib's Line Chart:"
fig, ax = plt.subplots()
ax.plot(values)
st.pyplot(fig)


#---------------------------------------------------------
col_names = ['column1', 'column2', 'column3']
data = pd.DataFrame(np.random.randint(30, size=(30,3)), columns=col_names)

'line graph:'
st.line_chart(data)

'bar graph:'
st.bar_chart(data)



