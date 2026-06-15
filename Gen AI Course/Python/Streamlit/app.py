import streamlit as st

st.write("Hello World")

st.title("Hello Streamlit")
st.write("This is my first streamlit app")
st.header("Welcom to streamlit")
st.subheader("This is sub header")
st.text("This is plain text")

## Buttons, checkboes and sliders

if st.button("Click me"):
    st.write("Button cliked")
    
agree = st.checkbox("I agree")
if agree:
    st.write("You agreed")
    
level = st.slider("Select a level : 1,10,5")
st.write(f"Selct level: {level}")

uploaded_file=st.file_uploader("upload a file", type=["csv", "txt"])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head())