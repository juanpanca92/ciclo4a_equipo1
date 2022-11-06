from Modelos.Resultados import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioResultados.findAll()
    def create(self,infoResultados,id_mesa,id_candidato):
        nuevoResultado = Resultado(infoResultados)
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato= Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa=laMesa
        nuevoResultado.candidato=elCandidato
        return self.repositorioResultados.save(nuevoResultado)
    def show(self,id):
        losResultados = Resultado(self.repositorioResultados.findById(id))
        return losResultados.__dict__
    def update(self,id,infoResultados,id_mesa,id_candidato):
        elResultado=Resultado(self.repositorioResultados.findById(id))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultados.save(elResultado)
    def delete(self,id):
        return self.repositorioResultados.delete(id)
    def listarResultadosCandidatos(self,id_candidato):
        return self.repositorioResultados.getListadoResultadosPorCandidato(id_candidato)
    def listarResultadosPorMesa(self,id_mesa):
        return self.repositorioResultados.getListadoResultadosPorMesa(id_mesa)
    def ganadorElecciones(self):
        return self.repositorioResultados.getVotacionMasAlta()

    def listaConsolidadosMesas(self):
        return self.repositorioResultados.consolidadoMesas()