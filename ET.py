productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
}

# ---------------------------------------------------------------------------------

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
}

# ---------------------------------------------------------------------------------

def stock_marca(marca):
    total_st = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total_st += stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {total_st}")
    
# ---------------------------------------------------------------------------------

def bus_pre(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return

    resultado = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultado.append(f"{marca}---{modelo}")

    if resultado:
        print("Los notebooks entre los precios consultados son:", sorted(resultado))
    else:
        print("No hay notebooks en ese rango de precios.")

# ---------------------------------------------------------------------------------

def actualizar_precio(marca, p):
    for marca, datos in productos.items():  
        if marca in stock:
            stock[marca][0] = p
            return True
        else:
            return False
            
# ---------------------------------------------------------------------------------        

def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1- Stock marca")
        print("2- Búsqueda por precio")
        print("3- Actualizar precio")
        print("4- Salir")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == "2":
            p_min = input("Ingrese precio mínimo: ")
            p_max = input("Ingrese precio máximo: ")
            bus_pre(p_min, p_max)

        elif opcion == "3":
            while True:
                marca = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("Debe ingresar un precio válido!!")
                    continue

                if actualizar_precio(marca, nuevo_precio):
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                seguir = input("Desea actualizar otro precio (s/n)?: ")
                if seguir.lower() != "s":
                    break

        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida!!")

menu()

        

        