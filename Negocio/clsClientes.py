class Clientes:

    def __init__(self,nombreCliente, usuarioCliente, idCliente):
        self.nombreCliente = nombreCliente
        self.usuarioCliente = usuarioCliente
        self.idCliente = idCliente

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