import json
"""
Actividad 6 clase Hotel
"""

class Hotel:

    def __init__(self, data):
        self.nombre = data.get('nombre')
        self.ubicacion = data.get('ubicacion')
        self.habitaciones = data.get('habitaciones', {})

    def mostrar_info(self):
        return json.dumps({
            'nombre': self.nombre,
            'ubicacion': self.ubicacion,
            'habitaciones': self.habitaciones
        }, indent=4)

    def modificar_info(self, nombre=None, ubicacion=None, habitaciones=None):
        if nombre:
            self.nombre = nombre
        if ubicacion:
            self.ubicacion = ubicacion
        if habitaciones is not None:
            self.habitaciones = habitaciones

    def reservar_habitacion(self, numero_habitacion):
        if self.habitaciones.get(str(numero_habitacion), None):
            self.habitaciones[str(numero_habitacion)] = False
            return f"Habitación {numero_habitacion} reservada con éxito."
        else:
            return "Habitación no disponible."

    def cancelar_reserva(self, numero_habitacion):
        if not self.habitaciones.get(str(numero_habitacion), True):
            self.habitaciones[str(numero_habitacion)] = True
            return f"Reserva de la habitación {numero_habitacion} cancelada."
        else:
            return "La habitación no estaba reservada."
