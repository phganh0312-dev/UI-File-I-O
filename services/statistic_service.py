from utils.csv_handler import CSVHandler


MOVIE_FILE="data/movies.csv"


class StatisticService:

    def quicksort(

        self,

        movies

    ):

        if len(movies)<=1:

            return movies

        pivot=(

            int(

                movies[0]

                ["revenue"]

            )
        )

        left=[]

        right=[]

        equal=[]

        for movie in movies:

            revenue=int(

                movie["revenue"]

            )

            if revenue>pivot:

                left.append(

                    movie

                )

            elif revenue<pivot:

                right.append(

                    movie

                )

            else:

                equal.append(

                    movie

                )

        return (

            self.quicksort(

                left

            )

            +

            equal

            +

            self.quicksort(

                right

            )

        )

    def hot_movies(self):

        movies=(

            CSVHandler.load(

                MOVIE_FILE

            )
        )

        return (

            self.quicksort(

                movies

            )
        )

    def total_revenue(self):

        movies=(

            CSVHandler.load(

                MOVIE_FILE

            )
        )

        total=0

        for movie in movies:

            total+=(

                int(

                    movie["revenue"]

                )
            )

        return total
