import streamlit as st

from services.booking_service import BookingService


service = BookingService()


def history_page():

    if (

        "user"

        not in

        st.session_state

    ):

        return

    user = (

        st.session_state

        ["user"]

    )

    history = (

        service.history(

            user

            ["username"]

        )
    )

    st.title(

        "Lịch sử vé"

    )

    for ticket in history:

        st.write(

            ticket
        )
