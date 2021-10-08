from modulo_provincia import Provincia
from ObjectEncoder import ObjectEncoder
from modulo_ManejadorProvincias import ManejadorProvincias

class RepositorioProvincias(object):
    __conn=None
    __manejador=None
    
    def __init__(self, conn):
        self.__conn= conn
        diccionario= self.__conn.leerJSONArchivo()
        self.__manejador= self.__conn.decodificarDiccionario(diccionario)
    
    def to_values(self, provincia):
        return provincia.get_nombre(), provincia.get_capital(), provincia.get_cantidad_hab(), provincia.get_cantidad_dep()
    
    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()
    
    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia
    
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())