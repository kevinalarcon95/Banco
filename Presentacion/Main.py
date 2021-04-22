"""
Taller Final - Sistema de Gestión Bancario

Presentado por:
    Kevin Fernando Alarcón Camayo  <kfalarcon@unicauca.edu.co>
    Carlos Enrique Hoyos Joiro     <joiroce@unicauca.edu.co>

"""
import sys
from Negocio.clsEmpleados import clsEmpleados
from Negocio.clsClientes import clsClientes
from Negocio.clsCuenta import clsCuenta
from Negocio.clsBanco import clsBanco
from Datos.clsAccesoDatos import clsAccesoDatos
from datetime import datetime

#Diccionario de Clientes
Clientes = { 25291907: {'nombreCliente': 'Camilo Diaz', 'usuarioCliente': 'cdiaz',
                         'Cuentas': {
                                     12345: { 'tipoCuenta': 'ahorro', 'montoInicial': 1000000, 'minimoCuenta': 10000,
                                            'porcentajeCuenta': 10, 'saldoCuenta': 500000
                                              },
                                     99999: { 'tipoCuenta': 'corriente', 'montoInicial': 5000, 'minimoCuenta': 2000,
                                                        'porcentajeCuenta': 0, 'saldoCuenta': 3000000
                                              }
                                    }
                         },
             36316678: {'nombreCliente': 'Sandra Cortes', 'usuarioCliente': 'sacortes',
                        'Cuentas': {54321:{ 'tipoCuenta': 'corriente', 'montoInicial': 1000000, 'minimoCuenta': 10000,
                                     'porcentajeCuenta': 5, 'saldoCuenta': 1200000
                                            }
                                     }
                        },
             76543219: {'nombreCliente': 'Carlos Rodriguez', 'usuarioCliente': 'caRodriguez',
                        'Cuentas': {89082:{ 'tipoCuenta': 'corriente', 'montoInicial': 1000000, 'minimoCuenta': 10000,
                                     'porcentajeCuenta': 5, 'saldoCuenta': 1200000
                                            }
                                     }
                        }
            }

accesoDatos = clsAccesoDatos("C:/sistemaBancario/","empleados.txt")
fecha = datetime.now()

def listaEmpleados():
    listaEmpleados = accesoDatos.cargarDatos()
    listaEmpleados2 = list()
    datos = list()
    for i in listaEmpleados:
        datos.append(i.split(','))

    for j in datos:
        nombreEmpleado = j[0]
        idEmpleado = j[1]
        sueldoEmpleado = j[2]
        añosTrabajados = j[3]
        vacaciones = j[4]
        cargoEmpleado = j[5]
        empleado = clsEmpleados(nombreEmpleado,idEmpleado,sueldoEmpleado,añosTrabajados,vacaciones,cargoEmpleado)
        listaEmpleados2.append(empleado)

    return listaEmpleados2

listaEmpleados = listaEmpleados()

def consignarDinero(nombreEmpleado, idEmpleado):
    iDCliente = int(input('Digite el ID del cliente: '))
    infoCliente = Clientes.get(iDCliente)
    if infoCliente != None:
        numCuenta = int(input('Digite el numero de cuenta: '))
        infoCuenta = infoCliente.get('Cuentas')
        cuentas = infoCuenta.get(numCuenta)
        if cuentas != None:
            print('\nSaldo de la Cuenta: ', cuentas['saldoCuenta'])
            numCuenta = numCuenta
            tipoCuenta = cuentas['tipoCuenta']
            montoInicial = cuentas['montoInicial']
            minimoCuenta = cuentas['minimoCuenta']
            porcentaje = cuentas['porcentajeCuenta']
            saldoCuenta = cuentas['saldoCuenta']
            cliente = clsClientes(infoCliente['nombreCliente'], infoCliente['usuarioCliente'], iDCliente)
            cliente.add_Cuenta(numCuenta, tipoCuenta, montoInicial, minimoCuenta, porcentaje, saldoCuenta)
            cliente.mostrarInformacion()

            saldoConsignar = int(input('Digite la cantidad a consignar: '))

            for i in cliente.listaCuentas:
                saldo = i.get_saldoCuenta()
                saldo = saldoConsignar+saldo
                cuentas['saldoCuenta'] = saldo
                i.set_saldoCuenta(saldo)
                print('Consignacion exitosa! \n Saldo: ',i.get_saldoCuenta())
                fecha = datetime.now()

            for empleado in listaEmpleados:
                if idEmpleado == empleado.get_idEmpleado():
                    empleado.listaClientes.append((cliente.get_idCliente(),numCuenta))

            generarRecibo(fecha,nombreEmpleado, cliente.nombreCliente,numCuenta,'Consignacion', saldoConsignar)
        else:
            print('\nATENCIÓN:\n\t¡No existen registros con ese numero cuenta!\n')

    else:
        print('\nATENCIÓN:\n\t¡No existe un cliente con ese ID!\n')

def retirarDinero(nombreEmpleado, idEmpleado):
    iDCliente = int(input('Digite el ID del cliente: '))
    infoCliente = Clientes.get(iDCliente)
    if infoCliente != None:
        numCuenta = int(input('Digite el numero de cuenta: '))
        infoCuenta = infoCliente.get('Cuentas')
        cuentas = infoCuenta.get(numCuenta)
        if cuentas != None:
            print('Saldo de la Cuenta: ', cuentas['saldoCuenta'])
            numCuenta = numCuenta
            tipoCuenta = cuentas['tipoCuenta']
            montoInicial = cuentas['montoInicial']
            minimoCuenta = cuentas['minimoCuenta']
            porcentaje = cuentas['porcentajeCuenta']
            saldoCuenta = cuentas['saldoCuenta']
            cliente = clsClientes(infoCliente['nombreCliente'], infoCliente['usuarioCliente'], iDCliente)
            cliente.add_Cuenta(numCuenta, tipoCuenta, montoInicial, minimoCuenta, porcentaje, saldoCuenta)

            cliente.mostrarInformacion()

            saldoRetirar = int(input('Digite la cantidad a retirar: '))
            if saldoRetirar < 0 or saldoRetirar>saldoCuenta:
                print('Operacion invalida!...No puedes retirar un monto mayor a tu saldo.')
            else:
                for i in cliente.listaCuentas:
                    saldo = i.get_saldoCuenta()
                    saldo = saldo - saldoRetirar
                    cuentas['saldoCuenta'] = saldo
                    i.set_saldoCuenta(saldo)
                    print('\nINFORMACIÓN:\nSaldo: ', i.get_saldoCuenta(),'\nConsignacion exitosa!')
                    fecha = datetime.now()
            generarRecibo(fecha,nombreEmpleado, cliente.nombreCliente,numCuenta,'Retirar', saldoRetirar)

        else:
            print('\nATENCIÓN:\n\t¡No existen registros con ese numero cuenta!\n')

    else:
        print('\nATENCIÓN:\n\t¡No existe un cliente con ese ID!\n')

def generarRecibo(fecha,nombreEmpleado, nombreCliente,numCuenta, transaccion, cantidad):
    banco = clsBanco('Bancolombia Popayan', 'Carrera 5 #3-23')
    recibo = banco.transaccion(nombreEmpleado,nombreCliente,numCuenta,transaccion,cantidad)
    #nombreRecibo = input('Digita el nombre del recibo: ')
    archivo = clsAccesoDatos("C:/sistemaBancario/",str(fecha.year)+"-"+str(fecha.month)+"-"+str(fecha.day)+"-"+
                             str(fecha.hour)+"-"+str(fecha.minute)+"-"+str(numCuenta)+".txt")
    archivo.escribirDatos(recibo)
    extractoBancario(fecha,recibo,numCuenta)
    print('\nINFORMACIÓN:\n\tRecibo generado!\n\n' + recibo + '\n')

def extractoBancario(fecha,recibo,numCuenta):
    archivo = clsAccesoDatos("C:/sistemaBancario/",'extractoBancario_'+ str(numCuenta) +".txt")
    archivo.escribirDatos('Fecha de transaccion: ' + str(fecha) +'\n' + recibo+'\n\n')

def mostrarExtractoBancario():
    numCuenta = int(input('Digite el numero de cuenta: '))
    archivo = clsAccesoDatos("C:/sistemaBancario/", 'extractoBancario_' + str(numCuenta) + ".txt")
    archivo.leerArchivo()

def informeEmpleado(idEmpleado):
    atendioClientes = False
    for empleado in listaEmpleados:
        if len(empleado.listaClientes) != 0:
            atendioClientes = True
            empleadoPos = empleado
    if atendioClientes:
        archivo = clsAccesoDatos("C:/sistemaBancario/", 'informeEmpleado_' + str(idEmpleado) + ".txt")
        archivo.escribirDatos('\nFecha de atención: ' + str(fecha) + '\n Cliente: ' + str(empleadoPos.get_listaClientes()))
        archivo.leerArchivo()
    else:
        print('\nINFORMACIÓN:\n\tNo has atendido clientes!')

def menuPrincipal():
    print(' -------------------------------------------------------------- \n' +
          ' |                   Sistema de Gestión Banco                  |\n' +
          ' | 1. Ingresar al sistema                                      |\n' +
          ' | 2. Salir.                                                   |\n' +
          ' --------------------------------------------------------------')

def ingresoAlSistema(nombreEmpleado,idEmpleado):
    opc = 0
    while opc != 5:
        if opc == 1:
            consignarDinero(nombreEmpleado,idEmpleado)
        if opc == 2:
            retirarDinero(nombreEmpleado,idEmpleado)
        if opc == 3:
            mostrarExtractoBancario()
        if opc == 4:
            informeEmpleado(idEmpleado)
        if opc == 5:
            sys.exit()

        print(' -------------------------------------------------------------- \n' +
              ' |                   Sistema de Gestión Banco                  |\n' +
              ' |                   Bienvenido '+nombreEmpleado+'\t               |\n' +
              ' | 1. Consignar dinero del cliente.                            |\n' +
              ' | 2. Retirar dinero del cliente.                              |\n' +
              ' | 3. Extracto bancario del cliente.                           |\n' +
              ' | 4. Informe del empleado.                                    |\n' +
              ' | 5. Salir.                                                   |\n' +
              ' --------------------------------------------------------------')
        opc = input('Digite una opción: ')
        try:
            opc = int(opc)
        except ValueError:
            print('\nATENCIÓN:\n\t¡Debe ingresar solo números enteros!\n')



opc = 0
while opc != 2:
    if opc == 1:
        existeEmpleado = False
        idEmpleado = input('Digite su ID para ingresar al sistema: ')
        for i in listaEmpleados:
            if idEmpleado in i.get_idEmpleado():
                existeEmpleado = True
                empleadoPos = i

        if existeEmpleado:
            ingresoAlSistema(empleadoPos.get_nombreEmpleado(), empleadoPos.get_idEmpleado())
        else:
            print('\nATENCIÓN:\n\t¡No existe un empleado con ese ID!\n')
    if opc == 2:
        sys.exit()
    menuPrincipal()
    opc = input('Digite una opción: ')
    try:
        opc = int(opc)
    except ValueError:
        print('\nATENCIÓN:\n\t¡Debe ingresar solo números enteros!\n')

