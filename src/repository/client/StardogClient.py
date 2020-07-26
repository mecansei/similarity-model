import os

import stardog


class StardogClient:
    def __init__(self, database: str):
        self.__credentials = {
            'endpoint': os.getenv("STARDOG_ENDPOINT"),
            'username': os.getenv("STARDOG_USERNAME"),
            'password': os.getenv("STARDOG_PASSWORD")
        }

        self.__database = database

    def select(self, query: str, reasoning: bool = False):
        with stardog.Connection(self.__database, **self.__credentials) as conn:
            results = conn.select(query, reasoning=reasoning)
            return results["results"]["bindings"]

    def update(self, query: str):
        with stardog.Connection(self.__database, **self.__credentials) as conn:
            conn.update(query)
