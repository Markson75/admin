productos = []

def añadir_producto():
    # Lógica para añadir un producto
    
    name = input("Ingrese nombre del producto: ")
    precio = input("Ingrese precio: ")
    if precio.isdecimal():
        precio = int(precio)
    else:
        print("Ingrese un valor adecuado")
        añadir_producto()

    cantidad = input("Ingrese cantidad: ")
    
    if cantidad.isdecimal():
        cantidad = int(cantidad)
    else:
        print("Ingrese un valor adecuado")
        añadir_producto()
    new_product = {'nombre' : name, 'precio' : precio, 'cantidad' : cantidad}
    productos.append(new_product)
    pass

def ver_productos():
    # Lógica para ver todos los productos
    
    print(productos)
    pass

def actualizar_producto():
    # Lógica para actualizar un producto
    
    size = len(productos) - 1
    print(f"Ingrese el indice del producto a modificar (0 a {size})")
    index = input()
    if index.isdecimal():
        index = int(index)
    else:
        print("Ingrese un valor adecuado")
        actualizar_producto()
    
    if index < 0 or index > size:
        print("Ingrese un valor de indice valido")
        actualizar_producto()
        
        
    name = input("Ingrese nombre del producto: ")
    
    precio = input("Ingrese precio: ")
    if precio.isdecimal():
        precio = int(precio)
    else:
        print("Ingrese un valor adecuado")
        actualizar_producto()
    
    cantidad = input("Ingrese cantidad: ")
    if cantidad.isdecimal():
        cantidad = int(cantidad)
    else:
        print("Ingrese un valor adecuado")
        actualizar_producto()
    
    
    productos[index] = {'nombre' : name, 'precio' : precio, 'cantidad' : cantidad}
    pass

def eliminar_producto():
    # Lógica para eliminar un producto
    
    print("Ingrese nombre del producto a eliminar")
    value = input()
    
    contador = 0
    for index in productos:
        if index['nombre'] == value:
            del productos[contador]
            print("Producto eliminado")
        contador = contador + 1
    
    pass

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    contador = 1
    for index in productos:
        post = f'Producto {contador} {index}'
        archivo = open("data.txt", 'a')
        archivo.write(f'{post} \n' )
        contador += 1
    archivo.close()
    print("Fin")
    exit()
    pass

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    
    print("Resultados hasta ahora")
    archivo = open("data.txt", "r")
    print(archivo.read())
    archivo.close
    pass

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
            
cargar_datos()
menu()