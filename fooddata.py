import json
from pathlib import Path


class FoodData:
    alimentos = {}

    def __init__(self):
        data_file = Path(__file__).resolve().parent / "data" / "alimentos.json"
        with data_file.open(encoding="utf-8") as load:
            self.alimentos = json.load(load)

    async def get_ingredients(self, skip, total):
        return {"Alimentos ": self.alimentos['alimentos'][skip: skip + total]}

    async def get_allingredients(self):
        return {"Alimentos " : self.alimentos['alimentos']}
    
    async def get_ingredient(self, ingrediente_id: int):
        alimento = None
        for item in self.alimentos["alimentos"]:
            if item["id"] == ingrediente_id:
                alimento = item
                break
        return alimento
