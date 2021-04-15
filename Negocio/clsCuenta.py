class clsCuenta:
    def __init__(self,numCuenta, tipoCuenta, montoInicial, minimoCuenta, porcentajeCuenta, saldoCuenta):
        self.numCuenta = numCuenta
        self.tipoCuenta = tipoCuenta
        self.montoInicial = montoInicial
        self.minimoCuenta = minimoCuenta
        self.porcentajeCuenta = porcentajeCuenta
        self.saldoCuenta = saldoCuenta

    def get_numCuenta(self):
        return self.numCuenta

    def set_numCuenta(self, numCuenta):
        self.numCuenta = numCuenta

    def get_tipoCuenta(self):
        return self.tipoCuenta

    def set_tipoCuenta(self, tipoCuenta):
        self.tipoCuenta = tipoCuenta

    def get_montoInicial(self):
        return self.montoInicial

    def set_montoInicial(self, montoInicial):
        self.montoInicial = montoInicial

    def get_minimoCuenta(self):
        return self.minimoCuenta

    def set_minimoCuenta(self, minimoCuenta):
        self.minimoCuenta = minimoCuenta

    def get_porcentajeCuenta(self):
        return self.porcentajeCuenta

    def set_porcentajeCuenta(self, porcentajeCuenta):
        self.porcentajeCuenta = porcentajeCuenta

    def get_saldoCuenta(self):
        return self.saldoCuenta

    def set_saldoCuenta(self, saldoCuenta):
        self.saldoCuenta = saldoCuenta

    def mostrarInformacion(self):
        print('Numero de Cuenta: ', self.numCuenta , 'Tipo Cuenta: ', self.tipoCuenta , 'Monto Inicial', self.montoInicial,
              'Minimo Cuenta: ' , self.minimoCuenta, 'Porcentaje Cuenta: ', self.porcentajeCuenta , 'Saldo Cuenta:',self.saldoCuenta)