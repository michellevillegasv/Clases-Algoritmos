class Seccion:
    def __init__(self,number):
        self.number=number
class Redactor(Seccion):
    def __init__(self, name, ID, number):
        Seccion.__init__(self,number)
        self.name = name
        self.ID = ID
class Jefe(Redactor):
    def __init__(self, name, ID, number, redactores):
        super().__init__(name, ID, number)
        self.redactores = redactores
class Article:
    def __init__(self, title, summary, cuerpo,image, fecha_publicacion, fecha_creacion, redactor):
        self.title = title
        self.summary = summary
        self.cuerpo = cuerpo
        self.image = image
        self.fecha_publicacion = fecha_publicacion
        self.fecha_creacion = fecha_creacion
        self.redactor = redactor
class Comercial(Seccion):
    def __init__(self, number,name, ID, title, cuerpo):
        super().__init__(number)
        self.name =name
        self.ID=ID
        self.title = title
        self.cuerpo= cuerpo
class Clasificado()


        