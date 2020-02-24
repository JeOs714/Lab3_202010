"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from ADT import map as map
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de peliculas. Retorna el catalogo inicializado.
    """
    catalog = {'booksList':None, 'authors':None, 'booksMap': None}
    catalog['booksList'] = lt.newList("ARRAY_LIST")
    catalog['booksMap'] = map.newMap (5003, maptype='CHAINING')#10000 books
    catalog['authors'] = map.newMap (12007, maptype='PROBING') #5841 authors
    return catalog


def newCatalogMovies():
    """
    Inicializa el catálogo de peliculas. Retorna el catalogo inicializado.
    """
    catalog = {'moviesList':None, 'directors':None, 'moviesMapTitle': None, 'moviesMapId': None,  "actors": None}
    catalog['moviesList'] = lt.newList("ARRAY_LIST")
    catalog['moviesMapTitle'] = map.newMap (170003, maptype='CHAINING')
    catalog['moviesMapId'] = map.newMap (170003, maptype='CHAINING')#329044 movies
    catalog['directors'] = map.newMap (175003, maptype='PROBING') #85929 directors
    catalog['actors']=map.newMap (131011, maptype='CHAINING')#260861 actors 

    return catalog

def newBook (row):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    book = {"book_id": row['book_id'], "title":row['title'], "average_rating":row['average_rating'], "ratings_count":row['ratings_count']}
    return book

def newMovie (row):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """

    movie= {"id": row['id'], "title":row['title'], "vote_average": float(row['vote_average']), "genres":row['genres']}
    return movie

def newDirector (row):
    """
    Crea una nueva estructura para modelar un autor y sus libros
    """
    director = {'name':"", "directorMovies":None,  "sum_average_rating":0}
    director ['name'] = row['director_name']
    #director['sum_average_rating'] = float(row['vote_average'])
    director ['directorMovies'] = lt.newList('ARRAY_LIST')
    lt.addLast(director['directorMovies'],row['id'])
    return director

def newActor (row):
    """
    Crea una nueva estructura para modelar un autor y sus libros
    """
    director = {'name':"", "ActorMovies":None,  "sum_average_rating":0}
    director ['name'] = name
    director['sum_average_rating'] = float(row['vote_average'])
    director ['directorMovies'] = lt.newList('SINGLE_LINKED')
    lt.addLast(director['directorMovies'],row['id'])
    return director


def addBookList (catalog, row):
    """
    Adiciona libro a la lista
    """
    books = catalog['booksList']
    book = newBook(row)
    lt.addLast(books, book)

def addMovieList (catalog, row):
    """
    Adiciona pelicula a la lista
    """
    movies = catalog['moviesList']
    movie = newMovie(row)
    lt.addLast(movies, movie)



def addBookMap (catalog, row):
    """
    Adiciona libro al map con key=title
    """
    books = catalog['booksMap']
    book = newBook(row)
    map.put(books, book['title'], book, compareByKey)

def addMovieMapTitle (catalog, row):
    """
    Adiciona película al map con key=title
    """
    movies = catalog['moviesMapTitle']
    movie = newMovie(row)
    map.put(movies, movie['title'], movie, compareByKey)

def addMovieMapId (catalog, row):
    """
    Adiciona película al map con key=id
    """
    movies = catalog['moviesMapId']
    movie = newMovie(row)
    map.put(movies, movie['id'], movie, compareByKey)

def addActorMap (catalog, row):
    """
    Adiciona actor al map con key=title
    """
    actors = catalog['actors']
    actor = newActor(row)
    map.put(actors, actor['actor'], actor, compareByKey)

    

def addDirectorMap(catalog, row):
    """
    Adiciona un autor al map y sus libros
    """
    directors = catalog['directors']
    director=map.get(directors,row["director_name"],compareByKey)
    if director:
        lt.addLast(director['directorMovies'],row['id'])
        #director['sum_average_rating'] += float(row['vote_average'])
    else:
        director = newDirector(row)
        map.put(directors, director['name'], director, compareByKey)


# Funciones de consulta


def getBookInList (catalog, bookTitle):
    """
    Retorna el libro desde la lista a partir del titulo
    """
    pos = lt.isPresent(catalog['booksList'], bookTitle, compareByTitle)
    if pos:
        return lt.getElement(catalog['booksList'],pos)
    return None

def getMovieInList (catalog, movieTitle):
    """
    Retorna la pelicula desde la lista a partir del titulo
    """
    pos = lt.isPresent(catalog['movieList'], movieTitle, compareByTitle)
    if pos:
        return lt.getElement(catalog['moviesList'],pos)
    return None


def getBookInMapTitle (catalog, bookTitle):
    """
    Retorna el libro desde el mapa a partir del titulo (key)
    """
    return map.get(catalog['booksMapTitle'], bookTitle, compareByKey)

def getBookInMapId (catalog, Id):
    """
    Retorna el libro desde el mapa a partir del titulo (key)
    """
    return map.get(catalog['booksMapId'], Id, compareByKey)

def getMovieInMapTitle (catalog, movieTitle):
    """
    Retorna la pelicula desde el mapa a partir del titulo (key)
    """
    return map.get(catalog['moviesMapTitle'], movieTitle, compareByKey)

def getMovieInMapId (catalog, Id):
    """
    Retorna la pelicula desde el mapa a partir del titulo (key)
    """
    return map.get(catalog['moviesMapId'], Id, compareByKey)



def getDirectorInfo (catalog, directorName):
    """
    Retorna el director a partir del nombre
    """
    return map.get(catalog['directors'], directorName, compareByKey)

def getMoviesbyDirector(catalog, director):
    """
    Busca las películas con votación mayor o igual a 6 del director dado
    """
    
    Bestmovies= lt.newList("ARRAY_LIST")
    Id= director["directorMovies"]
    for movie in Id["elements"]:
        pelicula= getMovieInMapId(catalog, movie)
        if pelicula["vote_average"] >= 6:
            lt.addLast(Bestmovies, pelicula)
    return Bestmovies

# Funciones de comparacion

def compareByKey (key, element):
    return  (key == element['key'] )  

def compareByTitle(movieTitle, element):
    return  (movieTitle == element['title'] )
