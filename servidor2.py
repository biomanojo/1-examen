# -*- coding: utf-8 -*-

from socket import socket, error
from threading import Thread
import funciones_servidor2
import json


class Cliente(Thread):

    '''funcion que genera hilos'''
    def __init__(self, con, dire):
        Thread.__init__(self)
        self.conexion = con
        self.direccion= dire


    def run(self):
        menu = False
        while True:
            try:

                if (menu != True):
                    mensaje_cliente=self.conexion.recv(1024)
                    mensaje_cliente = funciones_servidor2.menu()
                    menu =True

                else:
                    mensaje_cliente = int(self.conexion.recv(1024))
                    operacion=mensaje_cliente

                    if operacion == 1:
                        mensaje_cliente = funciones_servidor2.getnum_1()
                        self.conexion.send(mensaje_cliente)
                        num_1 = int(self.conexion.recv(1024))

                        mensaje_cliente = funciones_servidor2.getnum_2()
                        self.conexion.send(mensaje_cliente)
                        num_2 = int(self.conexion.recv(1024))

                        mensaje_cliente = funciones_servidor2.suma(num_1,num_2)

                    if operacion == 2:

                        mensaje_cliente = funciones_servidor2.archivo()
                        self.conexion.send(mensaje_cliente)
                        archi = (self.conexion.recv(1024))
                        mensaje_cliente= funciones_servidor2.crear_txt(archi)

                    if operacion == 3:

                        mensaje_cliente = funciones_servidor2.listar()

                    menu =False

            except error:
                print("[%s] Error de lectura "%self.name)
                break
            else:
                if mensaje_cliente:
                    self.conexion.send(mensaje_cliente)



def main():
    server = socket()
    server.bind(("localhost", 9090))
    server.listen(1)


    while True:
        con, dire = server.accept()
        hilo= Cliente(con, dire)
        hilo.start()
        print("conexion de %s:%d " %dire)
        #hilo =Thread(target=funciones_servidor2.menu,args=())
        #hilo.start()

if __name__ == '__main__':
    main()

