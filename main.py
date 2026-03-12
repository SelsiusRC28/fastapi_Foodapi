from fastapi import FastAPI
from fastapi import Response, status
from docs import tags_metadata
from fooddata import FoodData

app = FastAPI(
    title= "FoodApi",
    description="ApiRestFul para la gestión de alimentos y planes nutricionales",
    version="0.0.2",
    contact={
        "name":"Erick 2828",
        "url":"http://www.udemy.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


@app.get('/')
def read_root():
    return { "Hola" : "Pakito"}

@app.get('/ingredientes', tags=['ingredientes'])
async def get_ingredients():
     return await FoodData().get_ingredients()

@app.get('/ingredientes/{ingrediente_id}', tags=['ingredientes'], status_code=status.HTTP_200_OK)
async def get_ingredient(ingrediente_id : int, response : Response):
    
    ingredient = await FoodData().get_ingredient(ingrediente_id)
    if ingredient :
        return ingredient
    else : 
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "error " : str(ingrediente_id) + " no encontrado"
        }
