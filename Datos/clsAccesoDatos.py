import os
import sys
import glob
import pickle
from shutil import rmtree
from os import remove
from Negocio.clsEmpleados import clsEmpleados
class clsAccesoDatos:
    def __init__(self, rutaAccesoDatos, nombreArchivo):
        self.rutaAccesoDatos = rutaAccesoDatos
        self.nombreArchivo = nombreArchivo

    def get_rutaAccesoDatos(self):
        return self.rutaAccesoDatos

    def set_rutaAccesoDatos(self,rutaAccesoDatos):
        self.rutaAccesoDatos = rutaAccesoDatos

    def get_nombreArchivo(self):
        return self.nombreArchivo

    def set_nombreArchivo(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo


    def crearDirectorio(self, empleado):

        try:
            if not os.path.exists(self.rutaAccesoDatos):
                os.mkdir(self.rutaAccesoDatos)
                archivo = open('self.rutaAccesoDatos + self.nombreArchivo','w')
                pickle.dump(self.empleado, archivo)
                archivo.close()
            else:
                print('Ya existe el directorio!')

        except OSError:
            print('Error el directorio!')

