lista = {}
continuar = True
while continuar:
    print("----------------")
    print("----------------")
    lista_text = int(input("""
    1. Añadir producto
    2. Consultar producto
    3. Actualizar precio
    4. eliminar producto
    5. calcular el valor total del inventario
    6. Salir
    Por favor ingresa la opcion deseada: \n """))
    print("----------------")
    print("----------------")

    if lista_text == 1:
        id = input("Por favor ingresa el ID del producto ->")
        producto = input("Por favor ingresa el nombre del producto -> ")
        valor = int(input("Por favor ingresa el precio del producto ->"))
        unidades = int(input("Por favor ingresa la cantidad del producto ->"))

        lista[id] = {
        "nombre" : producto,
        "precio" : valor,
        "cantidad" : unidades}

        for i, n in lista.items():
            print (i , n )


    elif lista_text == 2:
        consultar = input("Ingresa el ID del producto a consultar -> ")
        
        info_producto = lista.get(consultar)
        print(f"{consultar} {info_producto}")
    