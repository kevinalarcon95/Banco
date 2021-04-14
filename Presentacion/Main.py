import sys
from Negocio.clsEmpleados import clsEmpleados
from Negocio.clsClientes import clsClientes
from Datos.clsAccesoDatos import clsAccesoDatos
Empleados = { 1111: {'nombreEmpleado': 'Sandra Casas', 'idEmpleado': 1061782345, 'sueldo': 15000000, 'añosTrabajados': 3,
                    'vacaciones': 2, 'cargoEmpleado': 'asesor'},
              1112: {'nombreEmpleado': 'Cristian Rojas', 'idEmpleado': 1060345677, 'sueldo': 21000000,'añosTrabajados': 6,
                    'vacaciones': 2, 'cargoEmpleado': 'cajero'},
              1113: {'nombreEmpleado': 'Monica Paz', 'idEmpleado': 1061456790, 'sueldo': 21000000,'añosTrabajados': 5,
                    'vacaciones': 2, 'cargoEmpleado': 'cajero'}
              }

Clientes = { 25291907: { 'nombreCliente': 'Camilo Diaz', 'usuarioCliente': 'cdiaz',
                         'Cuentas': {'numCuenta': 12345, 'tipoCuenta': 'ahorro', 'montoInicial': 1000000, 'minimoCuenta': 10000,
                         'porcentajeCuenta': 10, 'saldoCuenta': 500000}
                         }
            }

def consignarDinero():
    idCliente = input('Digite el ID del cliente: ')
    confirmar = False
    infoCliente = Clientes.get(idCliente)
    if infoCliente != None:
        print(infoCliente)
        return infoCliente
    else:
        print('\nATENCIÓN:\n\t¡No existe un cliente con ese ID!\n')
        print(infoCliente)


def menuPrincipal():
    print(' -------------------------------------------------------------- \n' +
          ' |                   Sistema de Gestión Banco                  |\n' +
          ' | 1. Ingresar al sistema                                      |\n' +
          ' | 2. Salir.                                                   |\n' +
          ' --------------------------------------------------------------')

def ingresoAlSistema():
    opc = 0
    while opc != 5:
        if opc == 1:
            consignarDinero()
        if opc == 2:
            retirarDinero()
        if opc == 3:
            extractoBancario()
        if opc == 4:
            gestionClientes()
        if opc == 5:
            sys.exit()

        print(' -------------------------------------------------------------- \n' +
              ' |                   Sistema de Gestión Banco                  |\n' +
              ' |                     Bienvenido             |\n' +
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


opc = 0
while opc != 2:
    if opc == 1:
        ingresoAlSistema()
    if opc == 2:
        sys.exit()
    menuPrincipal()
    opc = input('Digite una opción: ')
    try:
        opc = int(opc)
    except ValueError:
        print('\nATENCIÓN:\n\t¡Debe ingresar solo números enteros!\n')

