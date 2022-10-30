from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados

from bson import ObjectId

class RepositorioResultados(InterfaceRepositorio[Resultados]):

    def getListadoResultadosCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def sumaVotosporCandidato(self,id_candidato):
        query1 = {
          "$match": {"candidato.$id": ObjectId(id_candidato)}
        }
        query2 = {
          "$group": {
            "_id": "$candidato",
            "suma": {
              "$sum": "$conteo_final"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)