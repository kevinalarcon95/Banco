class clsCasaInversionista:
    def __init__(self, nombre, clave, porcentajeRetorno, montos, plazos, nivelRiesgo):
        self.nombre = nombre
        self.clave = clave
        self.porcentajeRetorno = porcentajeRetorno
        self.montos = montos
        self.plazos = plazos
        self.nivelRiesgo = nivelRiesgo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_clave(self):
        return self.clave

    def set_clave(self, clave):
        self.clave = clave

    def get_porcentajeRetorno(self):
        return self.porcentajeRetorno

    def set_porcentajeRetorno(self,porcentajeRetorno):
        self.porcentajeRetorno = porcentajeRetorno

    def get_montos(self):
        return self.montos

    def set_montos(self, montos):
        self.montos = montos

    def get_plazos(self):
        return self.plazos

    def set_plazos(self, plazos):
        self.plazos

    def get_nivelRiesgo(self):
        return self.nivelRiesgo

    def set_nivelRiesgo(self, nivelRiesgo):
        self.nivelRiesgo = nivelRiesgo