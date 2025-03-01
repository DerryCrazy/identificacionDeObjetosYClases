class Cliente:
    def __init__(self, nombre, correo, telefono, contrasena):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.contrasena = contrasena

    def registrar(self):
        pass

    def autenticar(self):
        pass

    def realizar_reserva(self, fecha_hora, num_comensales, mesa):
        pass

    def modificar_reserva(self, codigo_reserva, nuevos_datos):
        pass

    def cancelar_reserva(self, codigo_reserva):
        pass

    def ver_reservas(self):
        pass

    def recibir_notificacion(self, correo, mensaje):
        pass


class Mesa:
    def __init__(self, numero, capacidad, ubicacion):
        self.numero = numero
        self.capacidad = capacidad
        self.ubicacion = ubicacion

    def verificar_disponibilidad(self, fecha_hora):
        pass

    def obtener_mesas_disponibles(self, fecha_hora):
        pass


class Reserva:
    def __init__(self, codigo, fecha_hora, num_comensales, cliente, mesa):
        self.codigo = codigo
        self.fecha_hora = fecha_hora
        self.num_comensales = num_comensales
        self.cliente = cliente
        self.mesa = mesa

    def generar_codigo(self):
        pass

    def verificar_disponibilidad(self, fecha_hora, mesa):
        pass

    def crear(self):
        pass

    def modificar(self, nuevos_datos):
        pass

    def cancelar(self):
        pass

    def obtener_reporte_ocupacion(self, fecha):
        pass
