from multipledispatch import dispatch

class Podometro:
    __pasos = 0

    def __init__(self, pasos=0):  # Constructor con valor por defecto
        self.__pasos = pasos

    @dispatch()  # Método sin parámetros
    def contar(self):
        self.__pasos += 1

    @dispatch(int)  # Método con un parámetro de tipo entero
    def contar(self, pasos):
        self.__pasos += pasos

    def getPasos(self):  # Devuelve los pasos registrados
        return self.__pasos
    
    #Metodos adicionales 04/03/2025
    def calcularDistancia(self,pasos=0,unidad='m'):
        #Distancia en metros
        if pasos ==0:
            return self.getPasos() * 0.7
        else:
            return pasos * 0.7 
            
    def distanciaPasos(self, distancia=0, unidad='m'):
    # Convierte la distancia según la unidad especificada
        _distancia = self.__convertidorDistancia(distancia, unidad)
    # Utiliza la distancia convertida en el cálculo
        return round(_distancia / 0.7)

    
    def __convertidorDistancia(self,distancia=0,unidad='m'):
        match unidad:
            case 'cm':
                return distancia/1000
            case 'm':
                return distancia
            case 'km':
                return distancia*1000
            case _:
                return distancia    
            
    def saltar(self):
        self.contar(2)


# Pruebas
pod1 = Podometro(5) #se crea el objeto de la clase Podometro  pasando un 5 de parametro
print(pod1.getPasos()) 
pod1.contar()
pod1.contar(3)
print(pod1)
pod1.saltar()
print(pod1.getPasos()) 
print("Distancias")
print(f"5,000 pasos equivalen a {pod1.calcularDistancia(5000)} metros")
print(f"Distancia actual: {pod1.calcularDistancia():.2f}")
print(f"1km equivale a: {pod1.distanciaPasos(7.7,'m'):.2f}")


#pip install multipledispatch dentro de la carpeta donde esta el proyecto

#pod2 = Podometro(10)
#print(pod2.getPasos())

#pod3 = Podometro() #se crea el objeto sin pasar parametros
#print(pod3.getPasos())