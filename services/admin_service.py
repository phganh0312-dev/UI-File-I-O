from utils.csv_handler import CSVHandler


MOVIE_FILE=(

    "data/movies.csv"

)

SHOWTIME_FILE=(

    "data/showtimes.csv"

)


class AdminService:

    def add_movie(

        self,

        movie_id,

        title,

        genre

    ):

        movie={

            "movie_id":
            movie_id,

            "title":
            title,

            "genre":
            genre,

            "revenue":
            0

        }

        CSVHandler.append(

            MOVIE_FILE,

            movie,

            [

                "movie_id",

                "title",

                "genre",

                "revenue"

            ]

        )

    def delete_movie(

        self,

        movie_id

    ):

        movies=(

            CSVHandler.load(

                MOVIE_FILE

            )
        )

        movies=[

            movie

            for movie

            in movies

            if movie

            ["movie_id"]

            !=movie_id

        ]

        CSVHandler.overwrite(

            MOVIE_FILE,

            movies,

            [

                "movie_id",

                "title",

                "genre",

                "revenue"

            ]

        )

    def add_showtime(

        self,

        showtime_id,

        time,

        movie_id,

        rows,

        cols

    ):

        showtime={

            "showtime_id":
            showtime_id,

            "time":
            time,

            "movie_id":
            movie_id,

            "rows":
            rows,

            "cols":
            cols

        }

        CSVHandler.append(

            SHOWTIME_FILE,

            showtime,

            [

                "showtime_id",

                "time",

                "movie_id",

                "rows",

                "cols"

            ]

        )
