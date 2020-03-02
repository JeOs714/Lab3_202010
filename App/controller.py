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
import model
import csv
from ADT import list as lt
from ADT import map as map

from DataStructures import listiterator as it
from Sorting import mergesort as sort
from time import process_time 
import time as tt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Funcionaes utilitarias

def printList (lst):
    iterator = it.newIterator(lst)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)



def compareratings (movie1, movie2):
    return ( float(movie1['vote_average']) > float(movie2['vote_average']))


# Funciones para la carga de datos 

def loadMoviesCasting (catalog, sep=';'):
    """
    Carga las peliculas del archivo.  Por cada pelicula se toman sus directores y por 
    cada uno de ellos, se crea en la lista de directores, a dicho director y una
    referencia a la pelicula que se esta procesando.
    """
    t1_start = process_time() #tiempo inicial
    booksfile = cf.data_dir + 'GoodReads/AllMoviesCastingRaw.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(booksfile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            # Se adiciona el libro a la lista de libros
            model.addDirectorName(catalog, row)
            model.addDirectorId(catalog, row)
            model.addActorName(catalog, row)
            #model.addActorId(catalog, row)
            # Se adiciona el libro al mapa de libros (key=title)
            #model.addActorMap(catalog, row)
            # Se obtienen los autores del libro 
            #directors = row['director_name'].split(",")
            # Cada autor, se crea en la lista de autores del catalogo, y se 
            # adiciona un libro en la lista de dicho autor (apuntador al libro)
            #for director in directors:
                #model.addDirector (catalog, director.strip(), row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga directores y actores:",t1_stop-t1_start," segundos")  


def loadMovies (catalog, sep=';'):
    """
    Carga las películas del archivo.  Por cada libro se toman sus autores y por 
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    t1_start = process_time() #tiempo inicial
    moviefile = cf.data_dir + 'GoodReads/AllMoviesDetailsCleaned.csv'
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(moviefile, encoding="utf-8-sig") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            # Se adiciona el libro a la lista de libros
            model.addMovieList(catalog, row)
            # Se adiciona el libro al mapa de libros (key=title)
            model.addMovieMapTitle(catalog, row)
            model.addMovieMapId(catalog, row)
            # Se obtienen los autores del libro
            #authors = row['director_name'].split(",")
            # Cada autor, se crea en la lista de autores del catalogo, y se 
            # adiciona un libro en la lista de dicho autor (apuntador al libro)
            
            model.addGenre(catalog, row["genres"], row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución carga películas:",t1_stop-t1_start," segundos")   



def initCatalog ():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalogMovies()
    return catalog



def loadDataBooks (catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadBooks(catalog)

def loadDataMovies (catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    
    loadMovies(catalog)
    loadMoviesCasting(catalog)
    

# Funciones llamadas desde la vista y enviadas al modelo


def getMovieInfo(catalog, movieTitle):
    t1_start = tt.time() #tiempo inicial
    #book=model.getBookInList(catalog, bookTitle)
    movie=model.getMovieInMapTitle(catalog, movieTitle)
    t1_stop = tt.time() #tiempo final
    print("Tiempo de ejecución buscar pelicula:",t1_stop-t1_start," segundos")   
    if movie:
        return movie
    else:
        return None   

def getDirectorInfo(catalog, directorName):
    #author=model.getAuthorInfo(catalog, authorName)
    
    director=model.getDirectorInfo(catalog, directorName)
    if director:
        return director
    else:
        return None    
def getActorInfo(catalog, directorName):
    #author=model.getAuthorInfo(catalog, authorName)
    
    director=model.getActorInfo(catalog, directorName)
    if director:
        return director
    else:
        return None    
        
def getMoviesbyDirectorVote(catalog, directorName):
    t1_start = tt.time() #tiempo inicial
    director= getDirectorInfo(catalog, directorName)
    t1_stop = tt.time() #tiempo final
    print("Tiempo de ejecución buscar pelicula:",t1_stop-t1_start," segundos")
    if director:
        return model.getMoviesbyDirectorVote(catalog, director)
    else:
        return None

def getMoviebyName(catalog, movieTitle):
    movie= getMovieInfo(catalog, movieTitle)
    if movie:
        return model.getMoviebyName(catalog, movieTitle)
    else: 
        return None

def AllmoviesDirector(catalog, dirname):
    director= getDirectorInfo(catalog, dirname)
    if director:
        return model.AllmoviesDirector(catalog, dirname, director)
    else:
        return None

def AllmoviesActor(catalog, dirname):
    director= getActorInfo(catalog, dirname)
    if director:
        return model.AllmoviesActor(catalog, dirname, director)
    else:
        return None
def getGenre(catalog, name):
    genre= model.getGenre(catalog, name)
    if genre:
        return genre
    else:
        return None
        





