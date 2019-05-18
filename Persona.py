class Persona:

    def __init__(self, nombre, ingreso, tiempototal):
        self.nombre = nombre
        self.ingreso = int(ingreso)
        self.tiempototal = int(tiempototal)
        self.salida = int(ingreso) + int(tiempototal)

    def getTiempoIngreso(self):
        return self.ingreso

    def getTiempoFinal(self):
        return self.salida

    def compararHoraInicio(self,otro):
        return self.ingreso >= otro

    def __str__(self):
        return self.nombre

    def __eq__(self, other):
        return self.nombre == other.nombre
