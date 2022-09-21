

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
    
    

  def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.coordenada_X - self.coordenada_X, p.coordenada_Y - self.coordenada_Y) )


