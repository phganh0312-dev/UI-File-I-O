import streamlit as st

from services.admin_service import AdminService

from services.statistic_service import StatisticService


admin = AdminService()

stat = StatisticService()


def admin_page():

    user = (

        st.session_state

        .get(

            "user"

        )
    )

    if (

        not user

        or

        user["role"]

        != "admin"

    ):

        st.error(

            "Không có quyền"

        )

        return

    st.title(

        "Admin"

    )

    tab1,tab2,tab3 = (

        st.tabs(

            [

                "Phim",

                "Suất",

                "Thống kê"

            ]

        )
    )

    with tab1:

        movie_id = (

            st.text_input(

                "Movie ID"

            )
        )

        title = (

            st.text_input(

                "Tên phim"

            )
        )

        genre = (

            st.text_input(

                "Genre"

            )
        )

        if st.button(

            "Thêm phim"

        ):

            admin.add_movie(

                movie_id,

                title,

                genre

            )

            st.success(

                "Đã thêm"

            )

    with tab2:

        sid = st.text_input(

            "Showtime ID"

        )

        time = st.text_input(

            "Time"

        )

        mid = st.text_input(

            "Movie ID "

        )

        rows = st.number_input(

            "Rows",

            1

        )

        cols = st.number_input(

            "Cols",

            1

        )

        if st.button(

            "Thêm suất"

        ):

            admin.add_showtime(

                sid,

                time,

                mid,

                rows,

                cols

            )

            st.success(

                "Xong"

            )

    with tab3:

        st.metric(

            "Tổng doanh thu",

            stat.total_revenue()

        )

        hot = (

            stat.hot_movies()

        )

        st.write(

            hot
        )
