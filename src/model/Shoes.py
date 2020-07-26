from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Shoes:
    id: str
    name: str
    properties: List[str]
