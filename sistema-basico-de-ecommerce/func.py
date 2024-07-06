# Varias funciones tienen una estructura similar, así que se podría optimizar en ese sentido

# Imports
from productos import *
from color import *

# Ingresar Nombre de Usuario
def ingresar_usuario():
    nombreUsuario = input(f'\n{yellow}Ingresa tu nombre de usuario: {reset}').strip().capitalize()

    while not (nombreUsuario.isalpha()): # Me aseguro que sólo tenga letras
        print('Error. Ingresa un nombre que no contenga números ni caracteres especiales.\n')
        nombreUsuario = input(f'{yellow}Ingresa tu nombre de usuario: {reset}').strip().capitalize()

    return nombreUsuario # Devuelvo el valor

# Imprimir Productos
def imprimir_productos():
    print(f'\n{green}Productos Disponibles:{reset}\n')
    for i in productos: 
        print(f'{i}') # Imprimo el valor

# Buscar Producto en la Lista
def buscar_producto(nombre):
    for i in productos: # Recorro la lista
        if i['nombre'] == nombre: # Pregunto si el nombre coincide
            return i # Devuelvo el valor
    return None # Si no lo encuentra, devuelve None

# Elegir Producto
def ingresar_producto():
    productoAComprar = input(f'\n{yellow}Ingresa el nombre del producto que quieres comprar: {reset}').strip().capitalize()

    while buscar_producto(productoAComprar) == None: # Me aseguro que el producto ingresado se encuentre en la lista
        print('Error. Ingresa el nombre de algún producto que se encuentre en la lista.\n')
        productoAComprar = input(f'{yellow}Ingresa el nombre del producto que quieres comprar: {reset}').strip().capitalize()

    return productoAComprar # Devuelvo el valor

# Elegir Cantidad
def ingresar_cantidad(producto):
    cantidadProductoAComprar = input(f'\n{yellow}Ingresa la cantidad del producto que quieres comprar: {reset}').strip().capitalize()

    while not (cantidadProductoAComprar.isnumeric()) or not (0 < int(cantidadProductoAComprar) <= buscar_producto(producto)['stock']): # Me aseguro que sea un número y que sea entre 0 y el stock disponible del producto
        print('Error. Ingresa un número mayor a 0 y menor o igual a la cantidad de stock del producto.\n')
        cantidadProductoAComprar = input(f'{yellow}Ingresa la cantidad del producto que quieres comprar: {reset}').strip().capitalize()

    buscar_producto(producto)['stock'] -= int(cantidadProductoAComprar) # Resto la CANTIDAD A COMPRAR al STOCK
    return cantidadProductoAComprar # Devuelvo el valor

# Crear Ticket
def crear_ticket(nombreUsuario, productoAComprar, cantidadProductoAComprar):
    ticket = {
        'cliente': nombreUsuario,
        'producto': productoAComprar,
        'cantidad': int(cantidadProductoAComprar),
        'precioTicket': buscar_producto(productoAComprar)['precio'] * int(cantidadProductoAComprar), # Precio x Cantidad
    }

    return ticket # Devuelvo el valor

# Seguir Comprando
def seguir_comprando():
    respuesta = input(f'\n{yellow}¿Quieres seguir comprando? ¿SI o NO? {reset}').strip().upper()
    
    while (respuesta != 'SI') and (respuesta != 'NO'): # Me aseguro que solo sea SI o NO
        print('Error. Ingresa SI (para seguir comprando) o NO (para finalizar la compra).\n')
        respuesta = input(f'{yellow}¿Quieres seguir comprando? ¿SI o NO? {reset}').strip().upper()

    return respuesta # Devuelvo el valor

# Imprimir Carrito
def imprimir_carrito(cantidadTickets, carrito, precioTotal):
    print(f'\n{yellow}Cantidad Tickets Generados:{reset} {cantidadTickets}') # Imprimo la cantidad de tickets
    print(f'\n{yellow}Tickets:{reset}\n')
    for i in carrito:
        print(f'{i}') # Imprimo cada ticket
    print(f'\n{yellow}Precio Promedio Tickets:{reset} ${round(precioTotal / cantidadTickets, 2)}') # Imprimo el precio promedio de los tickets
    print(f'\n{yellow}Precio Total:{reset} ${precioTotal}') # Imprimo el precio total