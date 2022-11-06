from bson import ObjectId
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultado
from operator import itemgetter
import json
class RepositorioResultados(InterfaceRepositorio[Resultado]):
    pass
    def getListadoResultadosPorCandidato(self,id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    def getListadoResultadosPorMesa(self,id_mesa):
        theQuery = {"mesa.$id":ObjectId(id_mesa)}
        return self.query(theQuery)
    def getVotacionMasAlta(self):
        query1={
                "$group":{
                        "_id":"$candidato",
                        "total_votos ":{
                            "$count":{}
                        }
                    }
                }
        pipeline = [query1]
        json = self.queryAggregation(pipeline)

        maximo = 0
        candidatos = []
        for i in json:
            t = (i["total_votos "])
            if t > maximo:
                maximo = t
        print(maximo)
        for i in json:
            if (i["total_votos "]) == maximo:
                candidatos.append(i)
        print(candidatos)

        return candidatos

    def consolidadoMesas(self):
        query ={
                "$group":{
                        "_id":"$mesa",
                        "total_votos ":{
                            "$count":{}
                        }
                    }
                }
        pipeline =[query]
        lista = self.queryAggregation(pipeline)
        print(lista)
        ordenados = sorted(lista, key=lambda votos: votos['total_votos '])
        print(ordenados)
        return ordenados


