class Vehicle:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
class Car(Vehicle): 
    def __init__(self, speed, cilindrada, color, ruedas):
        Vehicle.__init__(self,color,ruedas)
        self.speed = speed
        self.cilindrada = cilindrada
class Bicycle(Vehicle): 
    def __init__(self, type, color, ruedas):
        Vehicle.__init__(self,color,ruedas)
        self.type = type
class Camioneta(Car):
    def __init__(self, carga, color, ruedas,speed, cilindrada):
        Car.__init__(self,color,ruedas,speed, cilindrada)
        self.carga = carga
class Motorcycle(Bicycle):
    def __init__(self, carga, color, ruedas,type,cilindrada):
        Bicycle.__init__(self,color,ruedas,type, cilindrada)
        self.carga= carga
        self.cilindrada=cilindrada