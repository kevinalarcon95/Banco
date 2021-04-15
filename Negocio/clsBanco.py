class clsBanco:
    def __init__(self, sucursalBanco, direccionBanco):
        self.sucursalBanco = sucursalBanco
        self.direccionBanco = direccionBanco

    def get_sucursalBanco(self):
        return self.sucursalBanco

    def set_sucursalBanco(self, sucursalBanco):
        self.sucursalBanco = sucursalBanco

    def get_direccionBanco(self):
        return self.direccionBanco

    def set_direccionBanco(self, direccionBanco):
        self.direccionBanco = direccionBanco

    def transaccion(self, nombreEmpleado, nombrecliente, numCuenta, transaccion, cantidadTransaccion):
        return "Banco: "+ self.sucursalBanco + "\tDireccion: "+ self.direccionBanco + "\nEmpleado: " + nombrecliente + "\tCliente: " + nombrecliente + "\nNumero de Cuenta: " + str(numCuenta) + "\tTransaccion: " + transaccion + "\nCantidad: " + str(cantidadTransaccion)