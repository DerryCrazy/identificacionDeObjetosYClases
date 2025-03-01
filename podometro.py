from multipledispatch import dispatch

class Podometro: #Nombre del archivo debe ser en minusculas 
    __pasos = 0 #Atributo privado
    #def __init__(self): #constructor que inicializa podometro en 0 "vacio"
     #   self.__pasos = 0

    def __init__(self,pasos=0): #Python permite aregar valores por defecto, si no se recibe nada dara el 0 en cuestion
        self.__pasos=pasos

    @dispatch()
    def contar(self): #metodo sin parametros
        self.__pasos +=1
    @dispatch()
    def contar(self, pasos): #metodo con parametros el metodo se reemplaza por el mas actual implementando un valor default
        self.__pasos += pasos


    def getPasos(self): #Lee cuantos pasos tiene el podometro
        return self.__pasos

pod1 = Podometro(5) #se crea el objeto de la clase Podometro  pasando un 5 de parametro
print(pod1.getPasos()) 
pod1.contar()
pod1.contar(3)
print(pod1.getPasos())

#pip install multipledispatch dentro de la carpeta donde esta el proyecto

#pod2 = Podometro(10)
#print(pod2.getPasos())

#pod3 = Podometro() #se crea el objeto sin pasar parametros
#print(pod3.getPasos())