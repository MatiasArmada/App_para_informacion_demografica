class Provincia(object):
    __nombre= None
    __capital= None
    __cantidad_hab= None
    __cantidad_dep= None

    def __init__(self,nombre, capital, cantidad_hab, cantidad_dep):
        self.__nombre = self.__nombre= self.requerido(nombre, 'Nombre es un valor requerido')
        self.__capital = self.requerido(capital, 'Capital es un valor requerido')
        self.__cantidad_hab= self.requerido(cantidad_hab, 'Cantidad de Habitantes es un valor requerido')
        self.__cantidad_dep= self.requerido(cantidad_dep, 'Cantidad de Departamentos es un valor requerido')

    def get_nombre(self):
        return self.__nombre
    
    def get_capital(self):
        return self.__capital
    
    def get_cantidad_hab(self):
        return self.__cantidad_hab
    
    def get_cantidad_dep(self):
        return self.__cantidad_dep

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre= str(self.__nombre),
                capital= str(self.__capital),
                cantidad_hab= int(self.__cantidad_hab),
                cantidad_dep= int(self.__cantidad_dep)
                )
            )
        return d