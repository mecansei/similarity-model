from typing import List

from src.model.Shoes import Shoes
from src.repository.StardogRepository import StardogRepository


class ModelService:
    def __init__(self, repository: StardogRepository):
        self.__repository = repository

    def find_all_shoes(self) -> List[Shoes]:
        return self.__repository.find_shoes()

    def similarity(self, shoes: Shoes) -> List[Shoes]:
        return self.__repository.similar_to(shoes)

    def insert(self, shoes: Shoes):
        self.__repository.insert(shoes)
