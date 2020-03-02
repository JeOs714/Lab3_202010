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
import sys
import controller as controller
import csv
from ADT import list as lt
from ADT import map as map

from DataStructures import listiterator as it

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido al Laboratorio 3")
    print("1- Cargar información")
    print("2- Buscar películas con votación positiva por director")
    print("3- Buscar información de autor por nombre ...")
    print("4- Requerimiento 3 ...")
    print("4- Requerimiento 4 ...")
    print("0- Salir")


def initCatalog ():
    """
    Inicializa el catalogo de peliculas
    """
    return controller.initCatalog()


def loadData (catalog):
    """
    Carga las peliculas en la estructura de datos
    """
    controller.loadDataMovies(catalog)

def printMovies (movies):
    if movies:
        print (' Estas son las peliculas: ')
        for movie in movies["movies"]["elements"]:

            print ('Titulo: ' + movie['title'] + ' Rating: ' + str(movie['vote_average']))
    else:
        print ('No se encontraron peliculas')


"""
Menu principal
"""
while True:
    printMenu()
    inputs =input('Seleccione una opción para continuar\n')
    if int(inputs[0])==1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog ()
        loadData (catalog)
        print ('Mapa peliculas cargadas: ' + str(map.size(catalog['moviesMapTitle'])))
        print ('Lista peliculas cargadas: ' + str(lt.size(catalog['moviesList'])))
        print ('Directores cargados: ' + str(map.size(catalog['directorsName'])))
        
    elif int(inputs[0])==2:
        movieTitle = input("Nombre del director a buscar: ")
        movie = controller.getMoviesbyDirectorVote(catalog, movieTitle)
        if movie:
            print("El número de películas del director "+movieTitle+" con votación positiva es: "+ str(lt.size(movie)))
        else:
            print("Director no encontrado")    
    elif int(inputs[0])==3:
        movie_name= input("Ingrese el nombre exacto de la película que desea buscar: ")
        movie=  controller.getMoviebyName(catalog, movie_name)
        if movie:
            print("La película ", movie_name, " tiene: ")
            print("Promedio de Votación: ",movie["vote_average"], "Votos totales", movie["vote_count"], "y fue dirigida por: ", movie["director"] )
        else:
            print("Nombre de película no encontrada") 
    elif int(inputs[0])==4:
        directorName = input("Nombre del director a buscar: ")
        director = controller.AllmoviesDirector(catalog, directorName)
        if director:
            print("Peliculas del director", directorName,":",lt.size(director['directorMovies']))
            print("Promedio de Votación: ",(director['sum_average_rating']/lt.size(director['directorMovies'])))
            printMovies(director)
        else:
            print("Director No encontrado")    
 
    elif int(inputs[0])==5:
        ActorName = input("Nombre del director a buscar: ")
        actor = controller.AllmoviesActor(catalog, ActorName)
        if actor:
            print("Peliculas del director", ActorName,":",lt.size(actor['ActorMovies']))
            print("Promedio de Votación: ",(actor['sum_average_rating']/lt.size(actor['ActorMovies'])))
            print("El director que más lo ha dirigido es", actor["dir"])
            printMovies(actor)
        else:
            print("Director No encontrado")  
    elif int(inputs[0])==6:
        label = input (" ")
        pass
    elif int(inputs[0])==7:
        label = input (" ")
        pass
    else:
        sys.exit(0)
sys.exit(0)