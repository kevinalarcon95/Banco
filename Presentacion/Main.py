import sys
from Negocio.clsEmpleados import clsEmpleados
from Negocio.clsClientes import clsClientes
from Datos.clsAccesoDatos import clsAccesoDatos

accesoDatos = clsAccesoDatos("C:/sistemaBancario/","empleados.txt")

def listaEmpleados():
    listaEmpleados = accesoDatos.cargarDatos()
    listaEmpleados2 = list()
    datos = list()
    for i in listaEmpleados:
        datos.append(i.split(','))
        print(datos)

    for j in datos:
        empleado = clsEmpleados(j[0],j[1],j[2],j[3],j[4],j[5])



listaEmpleados()

