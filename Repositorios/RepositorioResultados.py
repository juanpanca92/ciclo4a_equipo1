from bson import ObjectId
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultado
class RepositorioResultados(InterfaceRepositorio[Resultado]):
    pass

    def getListadoResultadosPorCandidato(self,id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def getListadoResultadosPorMesa(self,id_mesa):
        theQuery = {"mesa.$id":ObjectId(id_mesa)}
        return self.query(theQuery)

    def getMayorVotacionPorCandidato(self):
        query1={
                "$group":{
                        "_id":"$candidato",
                        "total_votos ":{
                            "$count":{}
                        }

                    }
                }
        pipeline= [query1]
        return self.queryAggregation(pipeline)


