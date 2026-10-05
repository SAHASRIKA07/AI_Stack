import streamlit as st
st.title("MRECW AI Application")
st.write("Welcome to MRECW!")
name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")
phno = st.text_input("Enter your phone number:")
year = st.selectbox("Select your year:", options=["1st Year", "2nd Year", "3rd Year", "4th Year"])
select = st.selectbox("Select your department:", ["CSE", "ECE", "EEE", "MECH", "CIVIL","AIML"])
hobbies = st.text_input("Share your hobbies:")
if st.button("Submit"):
    st.write("You are", name, "from", select, "department.")