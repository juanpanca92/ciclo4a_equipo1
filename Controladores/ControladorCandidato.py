from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self,id,infoCandidato):
        candidatoActual=Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.numero = infoCandidato["Numero"]
        candidatoActual.resolucion = infoCandidato["Resolucion"]
        candidatoActual.cedula = infoCandidato["Cedula"]
        candidatoActual.nombre=infoCandidato["Nombre"]
        candidatoActual.apellido = infoCandidato["Apellido"]
        candidatoActual.partido = infoCandidato["Partido"]
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self,id):
        return self.repositorioCandidato.delete(id)

    """
    Relación partido y candidato
    """
    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)