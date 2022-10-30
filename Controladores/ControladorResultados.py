from Modelos.Resultados import Resultados
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioResultados.findAll()

    """
    Asignacion Mesa y Candidato a Resultados
    """

    def create (self, infoResultados, id_mesa, id_candidato):
        nuevoResultado = Resultados(infoResultados)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultados.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__

    """
    Modificación de Resultados (Mesa y Candidato)
    """

    def update(self, id, infoResultados, id_mesa, id_candidato):
        elResultado = Resultados(self.repositorioResultados.findById(id))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultados.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener todos los Votos de un Candidato"

    def listarResultadosCandidato(self, id_candidato):
        return self.repositorioResultados.getListadoResultadosCandidato(id_candidato)

    "Obtener cantidad de votos por Candidato"

    def sumarVotosPorCandidato(self, id_candidato):
        return self.repositorioResultados.sumaVotosporCandidato(id_candidato)

