import csv
import os


class CSVHandler:

    @staticmethod
    def load(file_path):

        if not os.path.exists(file_path):

            return []

        with open(

            file_path,

            "r",

            encoding="utf-8",

            newline=""

        ) as file:

            reader = csv.DictReader(file)

            return list(reader)

    @staticmethod
    def overwrite(

        file_path,

        data,

        headers

    ):

        with open(

            file_path,

            "w",

            encoding="utf-8",

            newline=""

        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=headers

            )

            writer.writeheader()

            writer.writerows(data)

    @staticmethod
    def append(

        file_path,

        row,

        headers

    ):

        file_exists = os.path.exists(file_path)

        write_header = True

        if file_exists:

            write_header = (

                os.path.getsize(file_path)

                == 0

            )

        with open(

            file_path,

            "a",

            encoding="utf-8",

            newline=""

        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=headers

            )

            if write_header:

                writer.writeheader()

            writer.writerow(row)
