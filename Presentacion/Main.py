import sys
from Negocio.clsEmpleados import clsEmpleados
from Negocio.clsClientes import clsClientes
from Negocio.clsCuenta import clsCuenta
from Negocio.clsBanco import clsBanco
from Datos.clsAccesoDatos import clsAccesoDatos


Clientes = { 25291907: { 'nombreCliente': 'Camilo Diaz', 'usuarioCliente': 'cdiaz',
                         'Cuentas': {
                                     12345: { 'tipoCuenta': 'ahorro', 'montoInicial': 1000000, 'minimoCuenta': 10000,
                                            'porcentajeCuenta': 10, 'saldoCuenta': 500000
                                              },
                                     99999: { 'tipoCuenta': 'corriente', 'montoInicial': 5000, 'minimoCuenta': 2000,
                                                        'porcentajeCuenta': 0, 'saldoCuenta': 3000000
                                              }
                                    }
                         },
            36316678: { 'nombreCliente': 'Sandra Cortes', 'usuarioCliente': 'sacortes',
                                     'Cuentas': {'numCuenta': 12345, 'tipoCuenta': 'corriente', 'montoInicial': 1000000, 'minimoCuenta': 10000,
                                     'porcentajeCuenta': 5, 'saldoCuenta': 1200000}
                                     }
            }

accesoDatos = clsAccesoDatos("C:/sistemaBancario/","empleados.txt")

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

def consignarDinero(nombreEmpleado):
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

            saldoConsignar = int(input('Digite la cantidad a consignar: '))

            for i in cliente.listaCuentas:
                saldo = i.get_saldoCuenta()
                saldo = saldoConsignar+saldo
                i.set_saldoCuenta(saldo)
                print('Consignacion exitosa! \n Saldo: ',i.get_saldoCuenta())

            generarRecibo(nombreEmpleado, cliente.nombreCliente,numCuenta,'Consignacion', saldoConsignar)
        else:
            print('\nATENCIÓN:\n\t¡No existen registros con ese numero cuenta!\n')

    else:
        print('\nATENCIÓN:\n\t¡No existe un cliente con ese ID!\n')

def retirarDinero():
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

            for i in cliente.listaCuentas:
                saldo = i.get_saldoCuenta()
                saldo = saldoRetirar - saldo
                i.set_saldoCuenta(saldo)
                print('Consignacion exitosa! \n Saldo: ', i.get_saldoCuenta())

            generarRecibo(nombreEmpleado, cliente.nombreCliente,numCuenta,'Consignacion', saldoConsignar)

        else:
            print('\nATENCIÓN:\n\t¡No existen registros con ese numero cuenta!\n')

    else:
        print('\nATENCIÓN:\n\t¡No existe un cliente con ese ID!\n')

def generarRecibo(nombreEmpleado, nombreCliente,numCuenta, transaccion, cantidad):
    banco = clsBanco('Bancolombia Popayan', 'Carrera 5 #3-23')
    recibo = banco.transaccion(nombreEmpleado,nombreCliente,numCuenta,transaccion,cantidad)
    nombreRecibo = input('Digita el nombre del recibo: ')
    archivo = clsAccesoDatos("C:/sistemaBancario/",nombreRecibo+".txt")
    print(recibo)
    archivo.escribirDatos(recibo)


def menuPrincipal():
    print(' -------------------------------------------------------------- \n' +
          ' |                   Sistema de Gestión Banco                  |\n' +
          ' | 1. Ingresar al sistema                                      |\n' +
          ' | 2. Salir.                                                   |\n' +
          ' --------------------------------------------------------------')

def ingresoAlSistema(nombreEmpleado):
    opc = 0
    while opc != 5:
        if opc == 1:
            consignarDinero(nombreEmpleado)
        if opc == 2:
            retirarDinero(nombreEmpleado)
        if opc == 3:
            extractoBancario()
        if opc == 4:
            gestionClientes()
        if opc == 5:
            sys.exit()

        print(' -------------------------------------------------------------- \n' +
              ' |                   Sistema de Gestión Banco                  |\n' +
              ' |                     Bienvenido '+nombreEmpleado+           '\t|\n' +
              ' | 1. Consignar dinero.                                        |\n' +
              ' | 2. Retirar dinero.                                          |\n' +
              ' | 3. Extracto bancario.                                       |\n' +
              ' | 4. Gestion de clientes.                                     |\n' +
              ' | 5. Salir.                                                   |\n' +
              ' --------------------------------------------------------------')
        opc = input('Digite una opción: ')
        try:
            opc = int(opc)
        except ValueError:
            print('\nATENCIÓN:\n\t¡Debe ingresar solo números enteros!\n')

listaEmpleados = listaEmpleados()

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
            ingresoAlSistema(i.get_nombreEmpleado())
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

