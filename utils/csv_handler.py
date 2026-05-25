# utils/csv_handler.py

import csv
import os

class CSVHandler:

    @staticmethod
    def load_csv(file):

        if not os.path.exists(file):

            return []

        with open(
            file,
            'r',
            newline='',
            encoding='utf-8'
        ) as f:

            return list(csv.DictReader(f))


    @staticmethod
    def save_csv(file,data,headers):

        with open(
            file,
            'w',
            newline='',
            encoding='utf-8'
        ) as f:

            writer=csv.DictWriter(
                f,
                fieldnames=headers
            )

            writer.writeheader()

            writer.writerows(data)


    @staticmethod
    def append_csv(file,data,headers):

        exists=os.path.exists(file)

        with open(
            file,
            'a',
            newline='',
            encoding='utf-8'
        ) as f:

            writer=csv.DictWriter(
                f,
                fieldnames=headers
            )

            if not exists:

                writer.writeheader()

            writer.writerow(data)
