# services/auth_service.py

import hashlib

from utils.csv_handler import CSVHandler


USER_FILE="data/users.csv"


class AuthService:

    def register(
        self,
        username,
        password,
        role="user"
    ):

        users=CSVHandler.load_csv(USER_FILE)

        for user in users:

            if user["username"]==username:

                return False

        password=hashlib.sha256(
            password.encode()
        ).hexdigest()

        CSVHandler.append_csv(

            USER_FILE,

            {
                "username":username,
                "password":password,
                "role":role
            },

            [
                "username",
                "password",
                "role"
            ]
        )

        return True


    def login(
        self,
        username,
        password
    ):

        users=CSVHandler.load_csv(USER_FILE)

        password=hashlib.sha256(
            password.encode()
        ).hexdigest()

        for user in users:

            if(
                user["username"]==username
                and
                user["password"]==password
            ):

                return user

        return None
