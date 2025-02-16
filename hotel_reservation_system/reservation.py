from customer import Customer
from hotel import Hotel

"""
Actividad 6 clase Reservation
"""
class Reservation:
    def __init__(self, data):
        self.customer = Customer(data['cliente'])
        self.hotel = Hotel(data['hotel'])
        self.numero_habitacion = data['numero_habitacion']

    def crear_reserva(self):
        return self.hotel.reservar_habitacion(self.numero_habitacion)

    def cancelar_reserva(self):
        return self.hotel.cancelar_reserva(self.numero_habitacion)
