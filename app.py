import streamlit as st
from rm_bg import *

with st.sidebar:
    st.markdown("## 📁 Upload and Download")

    uploaded_file = st.file_uploader(label="Please upload your image", 
    type=["jpg", "png"])

    if uploaded_file:
        uploaded_file = uploaded_file.read()
        rm_img = rm_bg_fn(uploaded_file)
    else:
        rm_img = False

    if rm_img:
        st.markdown("")
        st.download_button(label="Download processed image", data=rm_img,
        file_name="rm_bg.png")

st.markdown("# ⚙️ Remove background from your image")
st.markdown("")

col1, col2 = st.columns(2)
with col1:
    if uploaded_file:
        st.markdown("📸 Original image")
        st.image(uploaded_file)

with col2:
    if rm_img:
        st.markdown("🤖 Removed background image")
        st.image(rm_img)