import streamlit as st
import time

with st.spinner("AI soch raha hai..."):
    time.sleep(3)  # Yahan aapka heavy code aayega (e.g., model.generate)
    
st.success("Response taiyaar hai!")