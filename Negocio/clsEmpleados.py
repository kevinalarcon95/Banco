class clsEmpleados:

    def __init__(self, nombreEmpleado, idEmpleado, sueldoEmpleado, añosTrabajados, vacaciones, cargoEmpleado):
        self.nombreEmpleado = nombreEmpleado
        self.idEmpleado = idEmpleado
        self.sueldoEmpleado =sueldoEmpleado
        self.añosTrabajados = añosTrabajados
        self.vacaciones = vacaciones
        self.cargaEmpleado = cargoEmpleado

    def get_nombreEmpleado(self):
        return self.nombreEmpleado

    def set_nombreEmpleado(self, nombreEmpleado):
        self.nombreEmpleado = nombreEmpleado

    def get_idEmpleado(self):
        return self.idEmpleado

    def set_idEmpleado(self, idEmpleado):
        self.idEmpleado = idEmpleado

    def get_sueldoEmpleado(self):
        return self.sueldoEmpleado

    def set_sueldoEmpleado(self, sueldoEmpleado):
        self.sueldoEmpleado = sueldoEmpleado

    def get_añosTrabajo(self):
        return self.añosTrabajados

    def set_añosTrabajos(self, añosTrabajados):
        self.añosTrabajados = añosTrabajados

    def get_vacaciones(self):
        return self.vacaciones

    def set_vacaciones(self, vacaciones):
        self.vacaciones

    def get_cargoEmpleado(self):
        return self.cargaEmpleado

    def set_cargoEmpleado(self, cargoEmpleado):
        self.cargaEmpleado = cargoEmpleado

    def mostrarInformacion(self):
        print('Nombre: ', self.nombreEmpleado, 'ID: ', self.idEmpleado)