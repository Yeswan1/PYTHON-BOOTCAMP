import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name=st.text_input("Enter your name")

age=st.slider("select your age ",0,100,25)
st.write(f"your age is {age}")

options=["python","java","c++","c"]

choice=st.selectbox("choose your favoite language ",options)
st.write(f"selected language is {choice}")
if name:
    st.write(f"hello ,{name}")

data={
    "name":["yash","manoj","ramkamal"],
    "age":[12,13,14]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("choose a csv language",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)