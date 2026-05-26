import streamlit as st

from services.auth_service import AuthService


auth = AuthService()


def login_page():

    st.title("Đăng nhập")

    username = st.text_input(

        "Tên đăng nhập"

    )

    password = st.text_input(

        "Mật khẩu",

        type="password"

    )

    if st.button(

        "Đăng nhập"

    ):

        user = auth.login(

            username,

            password

        )

        if user:

            st.session_state[

                "user"

            ] = user

            st.success(

                "Đăng nhập thành công"

            )

            st.rerun()

        else:

            st.error(

                "Sai thông tin"

            )
