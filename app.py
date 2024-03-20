import streamlit as st

st.title("This is streamlit practice website")
st.header("streamlit prep")
st.text("streamlit example test")
st.success("Success")
st.warning("Warning")
st.info("streamlit info")
st.error("error")
if st.checkbox("Select/Unselect"):
   st.text("User selected")
else:
   st.text("User deslect")


state = st.radio("Whats your fav color?",('Red','Green','Yellow'))

if state == "Green":
   st.success(f"fav color is {state}")

occupation = st.selectbox("What do you do?",("Student","Vlogger","Engineer"))

if st.button("Example is button"):
   st.error("You clicked iyt")


st.sidebar.header("heading of sidebar")