import unittest
from hotel import Hotel
from customer import Customer
from reservation import Reservation


class TestHotelReserva(unittest.TestCase):

    def setUp(self):
        self.datos_cliente = {
            "id_cliente": 1,
            "nombre": "Angel Lun",
            "correo": "angellm@email.com"
        }

        self.datos_hotel = {
            "nombre": "Sheratonn",
            "ubicacion": "CDMX",
            "habitaciones": {
                "20": True,
                "21": True
            }
        }

        self.datos_reserva = {
            "cliente": self.datos_cliente,
            "hotel": self.datos_hotel,
            "numero_habitacion": 20
        }

        self.cliente = Customer(self.datos_cliente)
        self.hotel = Hotel(self.datos_hotel)
        self.reserva = Reservation(self.datos_reserva)

    def test_reservar_habitacion(self):
        """Probar la reserva de una habitación."""
        resultado = self.hotel.reservar_habitacion(20)
        self.assertEqual(resultado, "Habitación 20 reservada con éxito.")
        self.assertFalse(self.hotel.habitaciones["20"])

    def test_reservar_habitacion_no_disponible(self):
        """Probar la reserva de una habitación no disponible."""
        self.hotel.reservar_habitacion(20)
        resultado = self.hotel.reservar_habitacion(20)
        self.assertEqual(resultado, "Habitación no disponible.")

    def test_cancelar_reserva(self):
        """Probar la cancelación de una reserva."""
        self.hotel.reservar_habitacion(20)
        resultado = self.hotel.cancelar_reserva(20)
        self.assertEqual(resultado, "Reserva de la habitación 20 cancelada.")
        self.assertTrue(self.hotel.habitaciones["20"])

    def test_cancelar_reserva_no_reservada(self):
        """Probar la cancelación de una habitación que no estaba reservada."""
        resultado = self.hotel.cancelar_reserva(20)
        self.assertEqual(resultado, "La habitación no estaba reservada.")

    def test_modificar_info_cliente(self):
        """Probar la modificación de los datos del cliente."""
        self.cliente.modificar_info(nombre="nombre cambiado")
        self.assertEqual(self.cliente.nombre, "nombre cambiado")
        self.cliente.modificar_info(correo="nombrecambiado@email.com")
        self.assertEqual(self.cliente.correo, "nombrecambiado@email.com")

    def test_modificar_info_hotel(self):
        """Probar la modificación de los datos del hotel."""
        self.hotel.modificar_info(nombre="Fiesta INN")
        self.assertEqual(self.hotel.nombre, "Fiesta INN")
        self.hotel.modificar_info(ubicacion="Toluca")
        self.assertEqual(self.hotel.ubicacion, "Toluca")

    def test_crear_reserva(self):
        """Probar la creación de una reserva."""
        resultado = self.reserva.crear_reserva()
        self.assertEqual(resultado, "Habitación 20 reservada con éxito.")

    def test_cancelar_reserva_metodo(self):
        """Probar la cancelación de una reserva a través de la clase Reserva."""
        self.reserva.crear_reserva()
        resultado = self.reserva.cancelar_reserva()
        self.assertEqual(resultado, "Reserva de la habitación 20 cancelada.")


if __name__ == "__main__":
    unittest.main()
