from utils.csv_handler import CSVHandler


MOVIE_FILE = "data/movies.csv"


class MovieService:

    def get_movies(self):

        movies = CSVHandler.load(

            MOVIE_FILE

        )

        return sorted(

            movies,

            key=lambda x:

            x["title"].lower()

        )

    def binary_search(

        self,

        keyword

    ):

        movies = self.get_movies()

        left = 0

        right = (

            len(movies)-1

        )

        keyword = (

            keyword.lower()

        )

        while left <= right:

            mid = (

                left+right

            )//2

            title = (

                movies[mid]

                ["title"]

                .lower()

            )

            if title == keyword:

                return movies[mid]

            elif title < keyword:

                left = mid+1

            else:

                right = mid-1

        return None

    def get_movie(

        self,

        movie_id

    ):

        movies = (

            CSVHandler.load(

                MOVIE_FILE

            )
        )

        for movie in movies:

            if (

                movie["movie_id"]

                == movie_id

            ):

                return movie

        return None

    def update_revenue(

        self,

        movie_id,

        amount

    ):

        movies = (

            CSVHandler.load(

                MOVIE_FILE

            )
        )

        for movie in movies:

            if (

                movie["movie_id"]

                == movie_id

            ):

                current = int(

                    movie["revenue"]

                )

                movie["revenue"]=(

                    current+amount

                )

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
