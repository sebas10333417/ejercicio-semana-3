# Ejercicio semanal 3
Datos = []
continuar = True
while continuar:

    print("-------------------------- ")
    print("--- Bienvenido al menu --- ")
    print("-------------------------- ")
    texto_menu = int(input("""
    1. Añadir productos
    2. Consultar productos
    3. Actualizar precios
    4. Eliminar productos
    5. Calcular el valor total del inventario
    Escribe la opcion ->
    """))

    if texto_menu == 1:
        print("Ingresa los siguientes datos: ")
        usuario_id = int(input("Por favor ingrese el ID del producto -> :"))
        Datos.append(usuario_id)
        usuario = input("Ingresa el producto que desea registrar -> :")
        Datos.append(usuario)
        usuario1 = int(input("Ingresa el precio del producto -> :"))
        Datos.append(usuario1)
        usuario2 = int(input("Ingresa la cantidad disponible -> :"))
        Datos.append(usuario2)

        Datos.append([usuario_id, usuario, usuario1, usuario2])

        consultar = Datos
        

        print(consultar)

        


        
        #[usuario_id] = {"Nombre" : usuario, "Precio" : usuario1, "Cantidad" :usuario2}

        

    #     print([usuario_id])
    
    # elif texto_menu == 2:
    #      print("Producto a consultar: ")
    #      usuario3 = input("Ingresa el ID del producto que quieres consultar -> :")
    #      if usuario3 in:
    #          print("El producto se encuentra registrado -> ")
    #      else:
    #          print("El ID no se encuentra registrado: ")