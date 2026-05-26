# services/booking_service.py

from datetime import datetime

from utils.csv_handler import CSVHandler

TICKET_FILE="data/tickets.csv"


class BookingService:

    def book(

        self,
        username,
        movie,
        seat,
        price

    ):

        ticket={

            "username":username,

            "movie":movie,

            "seat":seat,

            "price":price,

            "time":str(
                datetime.now()
            )

        }

        CSVHandler.append_csv(

            TICKET_FILE,

            ticket,

            [
                "username",
                "movie",
                "seat",
                "price",
                "time"
            ]

        )

        return True
