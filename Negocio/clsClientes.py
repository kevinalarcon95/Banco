from Negocio.clsCuenta import clsCuenta
class clsClientes:

    def __init__(self,nombreCliente, usuarioCliente, idCliente):
        self.nombreCliente = nombreCliente
        self.usuarioCliente = usuarioCliente
        self.idCliente = idCliente
        self.listaCuentas = list()

    def get_nombreCliente(self):
        return self.nombreCliente

    def set_nombreCliente(self,nombreCliente):
        self.nombreCliente = nombreCliente

    def get_usuarioCliente(self):
        return self.usuarioCliente

    def set_usuarioCliente(self, usuarioCliente):
        self.usuarioCliente = usuarioCliente

    def get_idCliente(self):
        return self.idCliente

    def set_idCliente(self, idCliente):
        self.idCliente = idCliente

    def add_Cuenta(self, numCuenta, tipoCuenta, montoInicial, minimoCuenta, porcentajeCuenta, saldoCuenta):
        self.listaCuentas.append((clsCuenta(numCuenta, tipoCuenta, montoInicial, minimoCuenta, porcentajeCuenta, saldoCuenta)))

    def listarCuentas(self):
        if(len(self.listaCuentas) == 0):
            print('\nINFORMACIÓN:\n\t¡No existen cuentas registrados aún!\n')
        else:
            for clsCuenta in self.listaCuentas:
                clsCuenta.mostrarInformacion()
