# -*- coding: utf-8 -*-

import json
import time
import os

def menu():
    lista = ["Bienvenido Admin", "1. Crear Película", "2. Eliminar Película", "3.Listar Película ","3.Ver Películas Vendidas ","3.Sillas Disponibles ", "Digite el número de la opción >>"]
    cadena = json.dumps(lista)
    return cadena


def crear(Id,Nombre,Costo,Sillas, Hora):
    lista = ["Ingrese ID de la pelicula","Ingrese nombre","Ingrese costo","Ingrese sillas","Ingrese Hora",]
    cadena = json.dumps(lista)
    return cadena

def eliminar():

    lista = ["Ingrese el ID  de la película que deseea eliminar"]
    peliculas.pop(Id)
    cadena = json.dumps(lista)
    return cadena

def Listar():
    cadena = json.dumps(peliculas)
    for i in list():
        print i


def Ver():





