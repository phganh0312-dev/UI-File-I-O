import streamlit as st

st.set_page_config(page_title="Movie Booking System", layout="wide")
st.title("Hệ thống Đặt vé Xem phim")

menu = st.sidebar.selectbox("Chức năng", ["Đăng nhập", "Đặt vé"])

if menu == "Đăng nhập":
    st.write("Giao diện đăng nhập sẽ nằm ở đây")