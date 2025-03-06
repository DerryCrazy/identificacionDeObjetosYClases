class Coche:
    __velocidad =0
    __marcha=0
    __luces=False

    def __init__(self,luces = False):
        self.__luces=luces

    def acelerar(self):
        self.__velocidad+=10

    def frenar(self):
        self.__velocidad-=10

    def cambiarMarcha(self, marcha):
        self.__marcha=marcha

    def encenderLuces(self):
        self.__luces=True

    def __str__(self):
        return f"Velocidad: {self.__velocidad}, Marcha: {self.__marcha},Luces: {self.__luces}"

tsuru = Coche(True)
camaro = Coche()

print(tsuru)
tsuru.cambiarMarcha(2)

for i in range (1,9):
    tsuru.acelerar()

tsuru.cambiarMarcha(3)
tsuru.frenar()
print(f"{tsuru}")

print(camaro)

