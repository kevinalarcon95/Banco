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


    def cargarDatos(self):
       lineas = list()
       datos = list()
       archivo = open(self.rutaAccesoDatos+self.nombreArchivo, "r")
       for linea in archivo:
        lineas.append(linea.strip('\n'))

       archivo.close()
       return lineas




