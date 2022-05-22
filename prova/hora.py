class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def __repr__(self):
        return str(self.hora) + ':' + str(self.minuto) + ':' + str(self.segundo)

h = Horario(15,23,50)
print(h)

