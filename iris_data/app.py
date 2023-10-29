import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

st.title("Iris Species")
st.markdown('สร้าง `scatter plot` แสดงผลข้อมูล '
            '**Iris\'s Species** กัน')

choices = ['sepal.length',
           'sepal.width',
           'petal.length',
           'petal.width']

# https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
# 1. สร้าง st.selectbox ของ ตัวเลือก แกน x และ y จาก choices
selected_x_var = st.selectbox(
    'Choose x-coordinate would you like to ? ', choices)
selected_y_var = st.selectbox(
    'Choose y-coordinate would you like to ? ', choices)

# https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
# # 2. สร้าง st.file_uploader เพื่อให้เลือกไฟล์ .csv เท่านั้น จากเครื่องผู้ใช้งาน
iris_file = st.file_uploader("Choose a csv file")

if iris_file is not None:
    iris_df = pd.read_csv(iris_file)
else:
    st.stop()

st.subheader('ข้อมูลตัวอย่าง')
st.write(iris_df)

st.subheader('แสดงผลข้อมูล')
sns.set_style('darkgrid')
markers = {"Setosa": "v", "Versicolor": "s", "Virginica": 'o'}

fig, ax = plt.subplots()
ax = sns.scatterplot(data=iris_df,
                     x=selected_x_var, y=selected_y_var,
                     hue='variety', markers=markers, style='variety')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Iris's Species Data")
st.pyplot(fig)
