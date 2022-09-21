#Crea una clase llamada Punto con sus coordenadas X e Y.

class Punto:
    def __init__(self, coord_X, coord_Y):
      self.coord_X = coord_X
      self.coord_Y = coord_Y

#Método string para que al imprimir por pantalla un punto aparezca en formato (X,Y)

def __str__(self):
        return  "({}, {})".format(self.coord_X, self.coord_Y)


