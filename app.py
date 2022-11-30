import streamlit as st
num1=st.text_input("Enter num1 : ")
num2=st.text_input("Enter num2 : ")
n1=float(num1)
n2=float(num2)
st.write(f"Answer => {n1/n2}")