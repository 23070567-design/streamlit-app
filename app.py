import streamlit as st
import pandas as pd 
import numpy as np

#displaying text content
st.title("My First Streamlit App")
st.write("Hello Jayesh")
st.text("Lets start")

#creating charts using pandas and numpy
df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("pahad")
st.image("https://static.vecteezy.com/vite/assets/photo-masthead-375-BoK_p8LG.webp",caption ="video")
st.video("https://www.youtube.com/watch?v=xEALTVLxrDw&list=RDxEALTVLxrDw&start_radio=1")

#file upload(csv)
upload_file=st.file_uploader("upload a csv file",type=["csv","txt"])

if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)

#taking user input
name=st.text_input("Enter name: ")
if st.button("welcome"):
    st.success(f"hello,{name}")

#text and markdown formatting
st.header("this is a header")
st.subheader("this is a subheader")

st.markdown("**Bold**,*Italic*,'code',[link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")


st.text_input("what is your name?")
st.text_area("write something...")
st.number_input("pick a number",min_value=0,max_value=100)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["Apple","Banana","mango"])
st.multiselect("choose toppings",["cheese","tomato","olives"])
st.radio("pick one",["option A","option B"])
st.checkbox("I agree to the terms")


#matplotlib integration

import matplotlib.pyplot as plt

fig,ax=plt.subplots()
ax.plot([1,2,3],[1,4,9])

st.pyplot(fig)