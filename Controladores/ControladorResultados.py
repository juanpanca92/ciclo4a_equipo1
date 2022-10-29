from Modelos.Resultados import Resultados
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioMesas = RepositorioMesa()
        self.repositorioCandidatos = RepositorioCandidato()

    def index(self):
        return self.repositorioResultados.findAll()

"""
Asignacion Mesa y Candidato a Resultados
"""

def create(self, infoResultados, id_Mesa, id_Candidato):
    nuevoResultado = Resultados(infoResultados)
    laMesa = Mesa(self.repositorioMesa.findById(id_Mesa))
    elCandidato = Candidato(self.repositorioCandidato.findById(id_Candidato))
    nuevoResultado.Mesa = laMesa
    nuevoResultado.Candidato = elCandidato
    return self.repositorioResultados.save(nuevoResultado)

def show(self, id):
    elResultado = Resultados(self.repositorioResultados.findById(id))
    return elResultado.__dict__

"""
Modificación de Resultados (Mesa y Candidato)
"""

def update(self, id, infoResultados, id_mesa, id_candidato):
    elResultado = Resultados(self.repositorioResultados.findById(id))
    elResultado.id_mesa = infoResultados["id_mesa"]
    elResultado.id_candidato = infoResultados["id_candidato"]
    laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
    elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
    elResultado.Mesa = laMesa
    elResultado.Candidato = elCandidato
    return self.repositorioResultados.save(elResultado)

def delete(self, id):
    return self.repositorioResultado.delete(id)

"Obtener todos los Votos de un Candidato"

def listarVotosDeCandidato(self, id_candidato):
    return self.repositorioResultados.getListadoVotosCandidato(id_candidato)

"Obtener cantidad de votos por Candidato"

def sumarVotosPorCandidato(self, id_candidato):
    return self.repositorioResultados.sumarVotosporCandidato(id_candidato)

