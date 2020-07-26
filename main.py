import configparser
import csv
import os
from typing import List

from src.library.logger.Logger import Logger
from src.model.Shoes import Shoes
from src.repository.StardogRepository import StardogRepository
from src.service.ModelService import ModelService


def find_all_shoes():
    repository = StardogRepository()
    service = ModelService(repository)

    response = service.find_all_shoes()

    for item in response:
        print(item)


def similarity(id="nike_casual"):
    repository = StardogRepository()
    service = ModelService(repository)

    shoes: Shoes = Shoes(
        id=id,
        name="",
        properties=[]
    )

    response = service.similarity(shoes)
    for item in response:
        print(item)


def insert():
    repository = StardogRepository()
    service = ModelService(repository)

    shoes: Shoes = Shoes(
        id="novo_nike2",
        name="Novo tenis nike2",
        properties=[
            ":Nike",
            ":Red",
            ":Casual"
        ]
    )

    service.insert(shoes)


def read_csv(csv_name="./resources/samples/shoes.csv"):
    array: List[Shoes] = []

    with open(csv_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader, None)  # ignore header
        for row in reader:
            array.append(
                Shoes(
                    id=row[0],
                    name=row[1],
                    properties=[row[i] for i in range(2, len(row))]
                )
            )
        return array


def insert_array(array_shoes: List[Shoes]):
    repository = StardogRepository()
    service = ModelService(repository)

    for shoes in array_shoes:
        service.insert(shoes)


def insert_from_csv():
    array_shoes = read_csv()
    insert_array(array_shoes)


def main():
    find_all_shoes()


if __name__ == "__main__":
    configuration = configparser.ConfigParser()
    configuration.read("./application.ini")

    environment: str = os.getenv("ENVIRONMENT", "DEV")
    Logger.info(f"Running with environment: {environment}")

    for key, value in configuration[environment].items():
        if not os.getenv(key.upper(), None):
            os.environ[key.upper()] = str(value)

    similarity("nike_social_1")
