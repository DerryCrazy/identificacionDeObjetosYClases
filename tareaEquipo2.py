# Clase para manejar todo lo relacionado con las prendas en el inventario
class Prenda:
    def __init__(self, codigo, descripcion, talla, color, precio_renta, precio_venta, estado="disponible"):
        # Inicializamos los atributos privados (nadie toca esto sin permiso xd)
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__talla = talla
        self.__color = color
        self.__precio_renta = precio_renta
        self.__precio_venta = precio_venta
        self.__estado = estado

    # Getters para acceder a los atributos (porque privacidad es prioridad )
    def get_codigo(self):
        return self.__codigo

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        # Si queremos cambiar la descripción de la prenda (por ejemplo, "Vestido corto" a "Vestido elegante")
        self.__descripcion = descripcion

    def get_estado(self):#Nomas lo agarras jejej 
        return self.__estado

    def set_estado(self, estado):
        # Cambiamos el estado (disponible, rentada, vendida... ¡qué emoción!)
        self.__estado = estado

    # Método mágico para mostrar los detalles de una prenda como texto (es como la carta de presentación de esta clase)
    def __str__(self):
        return f"Prenda {self.__codigo}: {self.__descripcion} - Estado: {self.__estado}"


# Clase para representar a los clientes
class Cliente:
    def __init__(self, nombre, identificacion):
        # Guardamos el nombre y la identificación 
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__transacciones = []  # Lista para llevar el registro de transacciones

    def agregar_transaccion(self, transaccion):
        # Agregamos cada transacción al historial del cliente, T OBSERVOOOoOO
        self.__transacciones.append(transaccion)

    def get_transacciones(self):
        # Recupera las transacciones para consultarlas más tarde (chismosos del sistema, esto es para ustedes xd)
        return self.__transacciones

    def __str__(self):
        # Representamos al cliente con su nombre e ID
        return f"Cliente {self.__nombre} (ID: {self.__identificacion})"


# Clase para gestionar a los empleados 
class Empleado:
    def __init__(self, nombre, rol, horario):
        # Atributos básicos de los empleados 
        self.__nombre = nombre
        self.__rol = rol
        self.__horario = horario

    def __str__(self):
        # Para mostrar info del empleado de forma cool
        return f"Empleado {self.__nombre} - Rol: {self.__rol} - Horario: {self.__horario}"


# Sistema central para gestionar todo el caos
class Sistema:
    def __init__(self):
        # Listas para guardar prendas, clientes y empleados
        self.prendas = []
        self.clientes = []
        self.empleados = []

    def registrar_prenda(self, prenda):
        # Añadimos una nueva prenda al inventario 
        self.prendas.append(prenda)

    def registrar_cliente(self, cliente):
        # Añadimos un nuevo cliente al sistema
        self.clientes.append(cliente)

    def registrar_empleado(self, empleado):
        # Añadimos un nuevo empleado 
        self.empleados.append(empleado)

    def mostrar_inventario(self):
        # Mostramos todas las prendas disponibles 
        disponibles = [prenda for prenda in self.prendas if prenda.get_estado() == "disponible"]
        if disponibles:
            print("\nInventario Disponible:")
            for prenda in disponibles:
                print(prenda)
        else:
            print("\nNo hay prendas disponibles.")  # Ups, se acabó el inventario

    def realizar_renta(self, cliente, prenda_codigo):
        try:
            # Buscamos la prenda en el inventario por su código
            prenda = next(p for p in self.prendas if p.get_codigo() == prenda_codigo)
            if prenda.get_estado() != "disponible":
                # Si la prenda no está disponible, lanzamos un error
                raise Exception(f"La prenda {prenda_codigo} no está disponible para renta.")
            prenda.set_estado("rentada")  # Actualizamos el estado de la prenda
            cliente.agregar_transaccion(f"Renta: {prenda.get_descripcion()}")
            print(f"¡Renta completada! {prenda.get_descripcion()} ha sido rentada.")
        except StopIteration:
            # Si el código no existe, lanzamos un aviso
            print(f"La prenda con código {prenda_codigo} no existe.")
        except Exception as e:
            # Cualquier otro error que surja, lo mostramos aquí
            print(f"Error: {e}")

    def realizar_venta(self, cliente, prenda_codigo):
        try:
            # Misma lógica que la renta, pero esta vez para venta
            prenda = next(p for p in self.prendas if p.get_codigo() == prenda_codigo)
            if prenda.get_estado() != "disponible":
                raise Exception(f"La prenda {prenda_codigo} no está disponible para venta.")
            prenda.set_estado("vendida")
            cliente.agregar_transaccion(f"Venta: {prenda.get_descripcion()}")
            print(f"¡Venta completada! {prenda.get_descripcion()} ha sido vendida.")
        except StopIteration:
            print(f"La prenda con código {prenda_codigo} no existe.")
        except Exception as e:
            print(f"Error: {e}")

    def mostrar_historial_cliente(self, cliente):
        # Mostramos el historial de transacciones del cliente
        print(f"\nHistorial de transacciones para {cliente}:")
        transacciones = cliente.get_transacciones()
        if transacciones:
            for transaccion in transacciones:
                print(f"- {transaccion}")
        else:
            print("No hay transacciones registradas.")  # Cliente nuevo o tímido 😉


# Bloque de pruebas para ver si el sistema funciona 
sistema = Sistema()

# Agregamos prendas al inventario
prenda1 = Prenda("001", "Vestido Rojo", "M", "Rojo", 50.0, 200.0)
prenda2 = Prenda("002", "Traje Azul", "L", "Azul", 70.0, 300.0)
sistema.registrar_prenda(prenda1)
sistema.registrar_prenda(prenda2)

# Registramos un cliente
cliente1 = Cliente("Ana Pérez", "C123")
sistema.registrar_cliente(cliente1)

# Registramos un empleado
empleado1 = Empleado("Carlos Gómez", "Vendedor", "09:00 - 17:00")
sistema.registrar_empleado(empleado1)

# Mostramos el inventario inicial
sistema.mostrar_inventario()

# Realizamos una renta y una venta
sistema.realizar_renta(cliente1, "001")
sistema.realizar_venta(cliente1, "002")

# Mostramos el historial del cliente
sistema.mostrar_historial_cliente(cliente1)

def menu():
    # Función principal para mostrar el menú de opciones.
    sistema = Sistema()  # Instancia del sistema para manejar datos.

    while True:  # Ciclo para mantener el menú activo hasta que el usuario decida salir.
        print("\n--- Menú de Gestión ---")
        print("1. Registrar Prenda")
        print("2. Registrar Cliente")
        print("3. Registrar Empleado")
        print("4. Mostrar Inventario")
        print("5. Realizar Renta")
        print("6. Realizar Venta")
        print("7. Mostrar Historial de Cliente")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")  # Solicita al usuario una elección.

        if opcion == "1":  # Opción para registrar prendas.
            codigo = input("Código de la prenda: ")
            descripcion = input("Descripción: ")
            talla = input("Talla: ")
            color = input("Color: ")
            precio_renta = float(input("Precio de renta: "))
            precio_venta = float(input("Precio de venta: "))
            prenda = Prenda(codigo, descripcion, talla, color, precio_renta, precio_venta)
            sistema.registrar_prenda(prenda)
            print("Prenda registrada.")

        elif opcion == "2":  # Opción para registrar clientes.
            nombre = input("Nombre del cliente: ")
            identificacion = input("Identificación del cliente: ")
            cliente = Cliente(nombre, identificacion)
            sistema.registrar_cliente(cliente)
            print("Cliente registrado.")

        elif opcion == "3":  # Opción para registrar empleados.
            nombre = input("Nombre del empleado: ")
            rol = input("Rol (vendedor/administrador): ")
            horario = input("Horario de trabajo: ")
            empleado = Empleado(nombre, rol, horario)
            sistema.registrar_empleado(empleado)
            print("Empleado registrado.")

        elif opcion == "4":  # Muestra el inventario actual.
            sistema.mostrar_inventario()

        elif opcion == "5":  # Realiza una renta.
            identificacion_cliente = input("Identificación del cliente: ")
            cliente = next((c for c in sistema.clientes if c.__str__().find(identificacion_cliente) != -1), None)
            if not cliente:
                print("Cliente no encontrado.")
                continue
            prenda_codigo = input("Código de la prenda a rentar: ")
            sistema.realizar_renta(cliente, prenda_codigo)

        elif opcion == "6":  # Realiza una venta.
            identificacion_cliente = input("Identificación del cliente: ")
            cliente = next((c for c in sistema.clientes if c.__str__().find(identificacion_cliente) != -1), None)
            if not cliente:
                print("Cliente no encontrado.")
                continue
            prenda_codigo = input("Código de la prenda a vender: ")
            sistema.realizar_venta(cliente, prenda_codigo)

        elif opcion == "7":  # Muestra el historial de un cliente.
            identificacion_cliente = input("Identificación del cliente: ")
            cliente = next((c for c in sistema.clientes if c.__str__().find(identificacion_cliente) != -1), None)
            if cliente:
                sistema.mostrar_historial_cliente(cliente)
            else:
                print("Cliente no encontrado.")

        elif opcion == "8":  # Sale del programa.
            print("Gracias por usar el sistema.")
            break

        else:  # Manejo de opciones inválidas.
            print("Opción inválida. Intenta nuevamente.")

menu() #mandamos llamar al menu pa q jale todo el show jeje BOORRARA datos anteriores
