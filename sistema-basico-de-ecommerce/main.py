# Imports
from func import *
from productos import *
from color import *

# Main
def main():

    # Variables
    flag = True # Para el ciclo WHILE
    cantidadTickets = 0 # Cantidad de Tickets Generados
    carrito = [] # Conjunto de Tickets de la Compra
    precioTotal = 0 # Precio Total de la Compra

    print(f'\n{yellow}============================================================={reset}')
    nombreUsuario = ingresar_usuario() # Ingresar Nombre de Usuario

    while flag:
        print(f'\n{yellow}============================================================={reset}')
        imprimir_productos() # Imprimir Productos
        print(f'\n{yellow}============================================================={reset}')
        productoAComprar = ingresar_producto() # Elegir Producto
        print(f'\n{yellow}============================================================={reset}')
        cantidadProductoAComprar = ingresar_cantidad(productoAComprar) # Elegir Cantidad
        print(f'\n{yellow}============================================================={reset}')

        # Crear Ticket
        ticket = crear_ticket(nombreUsuario, productoAComprar, cantidadProductoAComprar)
        cantidadTickets += 1 # Aumento la Cantidad de Tickets
        carrito.append(ticket) # Agrego un Ticket el Carrito
        precioTotal += ticket['precioTicket'] # Aumento el Precio Total
        print(f'\n{blue}Ticket {cantidadTickets}:{reset}')
        print(f'\n{ticket}') # Imprimo el Ticket

        # Seguir Comprando
        print(f'\n{yellow}============================================================={reset}')
        respuesta = seguir_comprando()

        if respuesta == 'NO':
            flag = False # Salgo del Ciclo WHILE

    print(f'\n{yellow}============================================================================{reset}')
    print(f'{yellow}============================================================================{reset}')
    print(f'{yellow}============================================================================{reset}')
    imprimir_carrito(cantidadTickets, carrito, precioTotal) # Imprimir Carrito
    print(f'\n{yellow}============================================================================{reset}')
    print(f'{yellow}============================================================================{reset}')
    print(f'{yellow}============================================================================{reset}\n')

main()