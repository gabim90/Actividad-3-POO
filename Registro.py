class Registro:
    __temperatura= 0.0
    __humedad= 0.0
    __presion= 0.0

    def __init__(self,temp,hum,pres):
        self.__humedad=hum
        self.__presion=pres
        self.__temperatura=temp

    def get_humedad (self):
        return self.__humedad
    
    def get_temperatura (self):
        return self.__temperatura
    
    def get_presion (self):
        return self.__presion
    
    def mostrar_datos(self):
        print (self.__temperatura)
        print (self.__humedad)
        print (self.__presion)