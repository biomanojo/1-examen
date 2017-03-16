from socket import socket
import funciones_cliente2
def main():
    server= socket()
    server.connect(('localhost', 9090))

    while True:
        #enviar mensaje del cliente

        mensaje_cliente = raw_input("Ingrese Mensaje al Servidor >> ")

        if mensaje_cliente:
            try:
                server.send(mensaje_cliente)
            except TypeError:
                server.send(bytes(mensaje_cliente, "utf-8"))

        #respuesta servidor

        #mensaje_servidor = server.recv(1024)
        #if mensaje_servidor:
         #   print mensaje_servidor

        mensaje_servidor = server.recv(1024)
        funciones_cliente2.imprimir(mensaje_servidor)


if __name__ == '__main__':
    main()






