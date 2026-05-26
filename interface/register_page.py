import streamlit as st

from services.auth_service import AuthService

from utils.validator import Validator


auth = AuthService()


def register_page():

    st.title(

        "Đăng ký"

    )

    username = st.text_input(

        "Username"

    )

    password = st.text_input(

        "Password",

        type="password"

    )

    if st.button(

        "Tạo tài khoản"

    ):

        if not Validator.username(

            username

        ):

            st.error(

                "Username >=4 ký tự"

            )

            return

        if not Validator.password(

            password

        ):

            st.error(

                "Password yếu"

            )

            return

        ok = auth.register(

            username,

            password,

            "customer"

        )

        if ok:

            st.success(

                "Đăng ký thành công"

            )

        else:

            st.error(

                "Username tồn tại"

            )
