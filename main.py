from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
#instancia de fastapi
#uvicorn main:app --reload --port 5000 -host 0.0.0.0 
#con el comando de arriba estara disponible la app en los dispositivos de la red
app = FastAPI()
#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicacion con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"

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


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

#acceder por id
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['movies'])
#se añaden parametros ->()
def get_movies_by_category(category: str, year: int):
     return [ item for item in movies if item['category'] == category ]
#Añadir una nueva pelicula
@app.post('/movies', tags=['movies'])
def create_movie(id: int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies
#Actualizar una pelicula
@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
	for item in movies:
		if item["id"] == id:
			item['title'] = title,
			item['overview'] = overview,
			item['year'] = year,
			item['rating'] = rating,
			item['category'] = category
			return movies
#Eliminar una pelicula
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies