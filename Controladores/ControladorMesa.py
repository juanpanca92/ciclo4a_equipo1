from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
class ControladorMesa():

    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self,infoMesa):
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self,id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self,id,infoMesa):
        MesaActual = Mesa(self.repositorioMesa.findById(id))
        MesaActual.id = infoMesa["Numero de la mesa"]
        MesaActual.cant_cedulas_inscritas = infoMesa["Cantidad de cedulas inscritas"]
        return self.repositorioMesa.save(MesaActual)

    def delete(self,id):
        print("Eliminando mesa con numero ",id)
        return self.repositorioMesa.delete(id)