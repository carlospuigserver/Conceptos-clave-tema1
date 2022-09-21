import math

math.sqrt(9)


#Crea una clase llamada Punto con sus coordenadas X e Y.
class Punto:
    def __init__(self, coordx, coordy):
      self.coordx = coordy
      self.coordx = coordy

#Método string para que al imprimir por pantalla un punto aparezca en formato (X,Y)

def __str__(self):
        return  "({}, {})".format(self.coordx, self.coordy)


#Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.

def cuadrante(self):
  
  
  
  if self.coordenada_X != 0 and self.coordenada_Y == 0:
    print("{} está en el eje X".format(self))
  
  elif self.coordenada_X == 0 and self.coordenada_Y != 0:
    print("{} se sitúa sobre el eje Y".format(self))
  
  elif self.coordx>0 and self.coordy>0:
    print("{} está en el primer cuadrante".format(self))
  
  elif self.coordx>0 and self.coordy<0:
    print("{} está en el cuarto cuadrante".format(self))
  
  elif self.coordx<0 and self.coordy<0:
    print("{} está en el tercer cuadrante".format(self))
  
  elif self.coordx<0 and self.coordy>0:
    print("{} está en el segundo cuadrante".format(self))
  
  else: 
    print("{} está en el origen".format(self))


#Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.

def vector (self,t):
  print("El vector entre {} y {} es ({}, {})".format(self,t, t.coordx - self.coordx, p.coordy - self.coordy)

        
        
        


  
  

        
  