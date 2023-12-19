import streamlit as st
import pandas as pd

# st.title("Welcome to my page!")
# st.header("Python")
# st.subheader("Java")
# st.markdown("I LOVE PYTHON")
# st.code(""" for i in range(1,5,1):
#               print("Hello")
#       """)
# dataset = pd.read_csv("cars.csv")
# st.dataframe(dataset)
name = st.text_input("Enter your Name :")
father_name = st.text_input("Enter your Father's Name :")
address = st.text_area("Enter your Address :")
Class = st.selectbox("Enter your class :", (1, 2, 3, 4, 5, 6))
button = st.button("Done")
if button:
    st.markdown(f""" 
    Name : {name}
    Father Name: {father_name}
    Address : {address}
    class : {Class} """)
