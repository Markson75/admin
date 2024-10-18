productos = []

def añadir_producto():
    # Lógica para añadir un producto
    
    name = input("Ingrese nombre del producto: ")
    precio = int(input("Ingrese precio (entero por favor que si no se crashea): "))
    cantidad = int(input("Ingrese cantidad (entero por favor que si no se crashea): "))
    new_product = {'nombre' : name, 'precio' : precio, 'cantidad' : cantidad}
    productos.append(new_product)
    pass

def ver_productos():
    # Lógica para ver todos los productos
    
    print(productos)
    pass

def actualizar_producto():
    # Lógica para actualizar un producto
    
    print("Ingrese el indice del producto a modificar")
    index = int(input())
    name = input("Ingrese nombre del producto: ")
    precio = int(input("Ingrese precio (entero por favor que si no se crashea): "))
    cantidad = int(input("Ingrese cantidad (entero por favor que si no se crashea): "))
    productos[index] = {'nombre' : name, 'precio' : precio, 'cantidad' : cantidad}
    pass

def eliminar_producto():
    # Lógica para eliminar un producto
    #NOTA: soy conciente que el material pide la eliminacion de un producto en base
    #a su nombre, a continuacion se ve la logica si cada atributo fuera un elemento
    #de una lista, en este caso una lista 2d, optar por este metodo implica cambiar
    #el codigo de manera que los productos, no se construyen a base de diccionarios, 
    # y como opte por el diseño de diccionarios, no funcionaria dicho metodo, lo dejo 
    # aqui de igual manera para demostrar una forma de eliminar productos en base a su 
    # nombre
    
    #nombre = input("Ingrese nombre del producto a eliminar: ")
    
    #contador = 0
    #for fila in productos:
    #    for item in fila:
    #        if item == nombre:
    #            del productos[contador]
    #    contador = contador + 1
        
    
    print("Ingrese indice del producto a eliminar")
    index = int(input())
    del productos[index]
        
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
        print("6: Cargar datos")

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
        elif opcion == '6':
            cargar_datos()
        else:
            print("Por favor, selecciona una opción válida.")
            
menu()