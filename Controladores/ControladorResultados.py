from Modelos.Resultados import Resultados
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultados():

    def __init__(self):
        self.repositorioResultados = RepositorioResultados()

    def index(self):
        return self.repositorioResultados.findAll()

    def create(self,infoResultados):
        nuevosResultados = Resultados(infoResultados)
        return self.repositorioResultados.save(nuevosResultados)

    def show(self,id):
        losResultados = Resultados(self.repositorioResultados.findById(id))
        return losResultados.__dict__

    def update(self,id,infoResultados):
        ResultadosActual = Resultados(self.repositorioResultados.findById(id))
        ResultadosActual.id = infoResultados["Numero del resultado"]
        ResultadosActual.numero_mesa = infoResultados["Numero de la mesa"]
        ResultadosActual.numero_candidato = infoResultados["Numero del candidato"]
        return self.repositorioResultados.save(ResultadosActual)

    def delete(self,id):
        print("Eliminando resultado con numero ",id)
        return self.repositorioResultados.delete(id)