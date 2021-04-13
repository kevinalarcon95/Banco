import os
import sys
import glob
from shutil import rmtree
from os import remove
class clsAccesoDatos:
    def __init__(self, rutaAccesoDatos):
        self.rutaAccesoDatos = rutaAccesoDatos

    def get_rutaAccesoDatos(self):
        return self.rutaAccesoDatos

    def set_rutaAccesoDatos(self,rutaAccesoDatos):
        self.rutaAccesoDatos = rutaAccesoDatos

    def crearDirectorio(self,rutaAccesoDatos):
        try:
            if not os.path.exists(rutaAccesoDatos):
                os.mkdir(ruta)
            else:
                print('Ya existe el directorio!')

        except OSError:
            print('Error!')