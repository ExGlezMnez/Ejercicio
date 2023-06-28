class Producto:
    def __init__(self, num_parte, nombre, precio):
        self.num_parte = num_parte
        self.nombre = nombre
        self.precio = precio
    def mostrar_informacion(self):
        return f"Numero de patente : {self.num_parte}\nMarca del auto :  {self.nombre}\nPrecio del auto : ${self.precio}"
def grabar_producto():
    while True:
        num_parte = input("Ingresa el numero de patente ")
        if validar_numero_parte(num_parte):
            break
        else:
            print("Error, intente de nuevo.")
    nombre = input("Ingrese el nombre del auto (Min. 6 caracteres): ")
    while len(nombre) < 6:
        print("Error, debe tener al menos 6 caracteres.")
        nombre = input("Ingrese el nombre del producto (Min. 6 caracteres): ")
    while True:
        precio = float(input("Ingresa el precio del auto (mayor a 5 millones): "))
        if precio > 5000000:
            break
        else:
            print("Erro, debe ser mayor a 5 millones")
    producto = Producto(num_parte, nombre, precio)
    productos.append(producto)
    print("Grabado sin problemas")
def buscar_producto():
    num_parte = input("Ingresa la patente que quiere buscar: ")
    encontrado = False
    for producto in productos:
        if producto.num_parte == num_parte:
            encontrado = True
            if producto.precio >= 5000000:
                print(producto.mostrar_informacion())
            else:
                print("Producto sin ingresar")
    if not encontrado:
        print("No encontrado")
def imprimir_reporte():
    print("REPORTE GENERAL")
    for producto in productos:
        print(f"{producto.mostrar_informacion()}")
def validar_numero_parte(num_parte):
    return len(num_parte) >= 1
productos = []
while True:
    print("(----)AUTOMOTORA AUTO SEGURO(----)")
    print("1) Grabar")
    print("2) Buscar")
    print("3) Imprimir Certificado")
    print("4) Salir")
    opcion = input("Pon opcion que usaras : ")
    if opcion == "1":
        grabar_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        imprimir_reporte()
    elif opcion == "4":
        print("Hasta la proxima")
        print("Autor: Felipe Martinez")
        print("Ver. 4.0")
        break
    else:
        print("Error, intenta nuevamente")