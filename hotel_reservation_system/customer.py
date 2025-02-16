"""
Actividad 6 clase customer
"""
import json


class Customer:

    def __init__(self, data):
        self.id_cliente = data.get('id_cliente')
        self.nombre = data.get('nombre')
        self.correo = data.get('correo')

    def mostrar_info(self):
        return json.dumps({
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'correo': self.correo
        }, indent=4)

    def modificar_info(self, nombre=None, correo=None):
        if nombre:
            self.nombre = nombre
        if correo:
            self.correo = correo
