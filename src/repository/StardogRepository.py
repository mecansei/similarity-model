import os
from typing import List

from src.library.logger.Logger import Logger
from src.model.Shoes import Shoes
from src.repository.client.StardogClient import StardogClient


class StardogRepository:
    def __init__(self, database: str = None):
        self.__database = database if database else os.getenv("MECANSEI_DATABASE")
        self.__client = StardogClient(self.__database)

    def similar_to(self, shoes: Shoes) -> List[Shoes]:
        query: str = '''
            SELECT ?shoes ?shoes_name ?characteristic
            FROM <http://mecansei.com/ontology/v1>{
                :''' + shoes.id + ''' :similar ?shoes .
                ?shoes :has_characteristic ?characteristic;
                    :name ?shoes_name .
            }
            ORDER BY ?shoes ?shoes_name ?characteristic
        '''
        Logger.info(query)

        response = self.__client.select(query, reasoning=True)
        return self.__build_shoes_array(response)

    def find_shoes(self) -> List[Shoes]:
        query: str = """
            SELECT ?shoes ?shoes_name ?characteristic 
            FROM <http://mecansei.com/ontology/v1>{
                ?shoes a :Shoes;
                    :has_characteristic ?characteristic;
                    :name ?shoes_name .
            }
            ORDER BY ?shoes ?shoes_name ?characteristic 
        """
        Logger.info(query)

        response = self.__client.select(query)
        return self.__build_shoes_array(response)

    def insert(self, shoes: Shoes):
        properties: str = ""
        for prop in shoes.properties:
            properties += f" {prop},"
        properties = properties[:-1]

        query: str = """
            INSERT DATA {
                GRAPH <http://mecansei.com/ontology/v1> {
                    :""" + shoes.id + """ a :Shoes ;
                    :has_characteristic""" + properties + """ ;
                    :name '""" + shoes.name + """' .
                }
            }
        """
        Logger.info(query)

        self.__client.update(query)

    @staticmethod
    def __build_shoes_array(response):
        map_shoes = {}
        shoes: Shoes
        for item in response:
            if item["shoes"]["value"] not in map_shoes:
                map_shoes[item["shoes"]["value"]] = Shoes(
                    id=item["shoes"]["value"],
                    name=item["shoes_name"]["value"],
                    properties=[item["characteristic"]["value"]]
                )
                continue
            map_shoes[item["shoes"]["value"]].properties.append(item["characteristic"]["value"])

        arr: List[Shoes] = []
        for s in map_shoes.values():
            arr.append(s)

        return arr
