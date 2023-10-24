from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
#Ayuda a crear un modelo, para ser escalable
from pydantic import BaseModel, Field
from typing import Optional, List

#instancia de fastapi
#uvicorn main:app --reload --port 5000 -host 0.0.0.0 
#con el comando de arriba estara disponible la app en los dispositivos de la red
app = FastAPI()
#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"

#clase movie/esquema
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating:float = Field(default=10, ge=1, le=10)
    category:str = Field(default='Categoría', min_length=5, max_length=15)

    model_config = {
     "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción"
                }
            ]
        }
    }

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar 2",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2010",
		"rating": 8.8,
		"category": "Acción"
	}
]

#endpoint
#los tags nos permite agrupar las rutas de la aplicacion
@app.get("/", tags=['home'])
def read_root():
    return HTMLResponse('<h1>Hello world</h1>')

#mostrar las peliculas
@app.get('/movies', tags=['movies'], response_model=List[Movie])
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies)

#acceder por id
@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(content=[])

#mostrar peliculas por categoria
@app.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [ item for item in movies if item['category'] == category ]
    return JSONResponse(content=data)

#Añadir una nueva pelicula
@app.post('/movies', tags=['movies'], response_model=dict)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content={"message": "Se ha registrado la película"})

#Actualizar una pelicula
@app.put('/movies/{id}', tags=['movies'], response_model=dict)
def update_movie(id: int, movie: Movie)-> dict:
	for item in movies:
		if item["id"] == id:
			item['title'] = movie.title
			item['overview'] = movie.overview
			item['year'] = movie.year
			item['rating'] = movie.rating
			item['category'] = movie.category
			return JSONResponse(content={"message": "Se ha modificado la película"})
          
#Eliminar una pelicula
@app.delete('/movies/{id}', tags=['movies'], response_model=dict)
def delete_movie(id: int)-> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "Se ha eliminado la película"})