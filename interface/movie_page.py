import streamlit as st

from services.movie_service import MovieService


movie_service = MovieService()


def movie_page():

    st.title(

        "Danh sách phim"

    )

    keyword = st.text_input(

        "Tìm phim"

    )

    if keyword:

        movie = (

            movie_service

            .binary_search(

                keyword

            )
        )

        if movie:

            st.write(movie)

        else:

            st.warning(

                "Không tìm thấy"

            )

    st.subheader(

        "Toàn bộ phim"

    )

    movies = (

        movie_service

        .get_movies()

    )

    for movie in movies:

        with st.container():

            st.write(

                "Tên:",

                movie["title"]

            )

            st.write(

                "Thể loại:",

                movie["genre"]

            )

            st.write(

                "Doanh thu:",

                movie["revenue"]

            )

            if st.button(

                f"Đặt vé "

                f"{movie['movie_id']}"

            ):

                st.session_state[

                    "booking"

                ] = movie

                st.switch_page(

                    "interface/booking_page.py"

                )
