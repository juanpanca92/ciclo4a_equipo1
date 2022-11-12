import operator
from bson import ObjectId
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultado
from operator import itemgetter
import json
class RepositorioResultados(InterfaceRepositorio[Resultado]):
    pass

    def partidosOrdenadosPorVotos(self):#puntoC
        listadoGeneral=self.findAll()
        diccPartidos = {}
        listaPartidos = []
        for diccionario in listadoGeneral:
            candidato = diccionario.get('candidato')
            partido = candidato.get('partido')
            idPartido = partido.get('_id')
            nombPartido = partido.get('nombre')
            if idPartido in listaPartidos:
                diccPartidos[nombPartido] = diccPartidos[nombPartido] + 1
            else:
                listaPartidos.append(idPartido)
                diccPartidos[nombPartido] = 1
        Ordenado = dict(sorted(diccPartidos.items(), key=operator.itemgetter(1), reverse=True))

        enOrden=[]
        for i in Ordenado:
            part=[]
            a=Ordenado.get(i)
            Stra= str(a)
            part.append("Partido : "+i)
            part.append("Votos   : "+Stra)
            print(part)
            enOrden.append(part)
        return Ordenado

    def getPorcentajeParticipacion(self):
        listadoGeneral = self.findAll()
        diccPartidos = {}
        listaPartidos = []
        for diccionario in listadoGeneral:
            candidato = diccionario.get('candidato')
            partido = candidato.get('partido')
            idPartido = partido.get('_id')
            nombPartido = partido.get('nombre')
            if idPartido in listaPartidos:
                diccPartidos[nombPartido] = diccPartidos[nombPartido] + 1
            else:
                listaPartidos.append(idPartido)
                diccPartidos[nombPartido] = 1
        Ordenado = dict(sorted(diccPartidos.items(), key=lambda item: item[1], reverse=True))
        print(Ordenado)
        # sacar los porcentajes de cada partido |
        def porcentajevotos(total, votos):
            result = (votos / total) * 100
            b = round(result, 2)
            return b
        total = 0  # acumulador de todos los votos
        a = Ordenado.values()
        listado=[]
        for i in a:
            total += i
        for i in (Ordenado):
            x = (porcentajevotos(total, Ordenado[i]))
            y=str(x)
            partido=("Partido "+ i+ " : "+ y+ "%")  # Porcentaje de cada partido
            strPartido=str(partido)
            listado.append(strPartido)
        return listado

    def distribucionPorcentualPartidos(self):
        query1 = {
            "$group": {
                "_id": "$candidato",
                "Total_votos": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query1]
        lista = self.queryAggregation(pipeline)
        ordenado = sorted(lista, key=lambda votos: votos['Total_votos'], reverse=True)
        diccPartidos = {}
        listaPartidos = []
        for candidatoConTodo in ordenado[0:15]:
            candidato = candidatoConTodo.get("doc")
            elemDelCandidato = candidato.get("candidato")
            partidoDelCandidato = elemDelCandidato.get("partido")
            idPartido = partidoDelCandidato.get('_id')
            nombrePartido = partidoDelCandidato.get("nombre")
            if idPartido in listaPartidos:
                diccPartidos[nombrePartido] = diccPartidos[nombrePartido] + 1
            else:
                listaPartidos.append(idPartido)
                diccPartidos[nombrePartido] = 1
        for i in diccPartidos:
            diccPartidos[i] = round(diccPartidos[i] / 15 * 100, 1)
        Ordenado = sorted(diccPartidos.items(), key=operator.itemgetter(1), reverse=True)

        return Ordenado
    def getListadoResultadosPorCandidato(self,id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def getVotacionMasAlta(self):
        query1={
            "$group": {
                "_id": "$candidato",
                "Total_votos": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query1]
        lista = self.queryAggregation(pipeline)

        maximo = 0
        candidatos = []
        for candidatoConTodo in lista:
            t = candidatoConTodo["Total_votos"]
            print(t)
            if t > maximo:
               maximo = t
        for candidatoConTodo in lista:
            votos = candidatoConTodo["Total_votos"]
            if votos == maximo:
                resultado = []
                candidato = candidatoConTodo.get("doc")
                elem = candidato.get("candidato")
                nombre = elem.get("nombre")
                apellido = elem.get("apellido")
                nombrecompleto = nombre + " " + apellido
                resultado.append(nombrecompleto)
                resultado.append(votos)
                candidatos.append(resultado)
        print (candidatos)
        return candidatos
    def consolidadoMesas(self):#punto b
        query ={"$group":{"_id":"$mesa","total_votos ":{"$count":{}},"doc":{"$first":"$$ROOT"}}}
        pipeline =[query]
        lista = self.queryAggregation(pipeline)
        ordenados = sorted(lista, key=lambda votos: votos['total_votos '])
        lista_mesas = []
        for dicc in ordenados:
            lista = []
            votos = dicc.get("total_votos ")
            StrVotos = str(votos)
            doc = dicc.get("doc")
            mesa = doc.get("mesa")
            num_mesa = mesa.get("num_mesa")
            lista.append("Mesa  : " + num_mesa)
            lista.append("Votos : " + StrVotos)
            lista_mesas.append(lista)
        return lista_mesas
    def VotosCandidatoPartido(self):#punto A1
        query1 = {"$group":{"_id":"$candidato","suma":{"$sum":1},"doc":{"$first":"$$ROOT"}}}
        query2 = {"$sort":{"suma":1}}
        pipeline = [query1,query2]
        lista = self.queryAggregation(pipeline)
        listadoGeneral = sorted(lista, key=lambda votos: votos['suma'],reverse=True)#manipular listadoGeneral
        print("listadoGeneral =",listadoGeneral)
        listadoVotos=["Punto a listado de todos los candidatos con info, ordenados por votacion"]
        for candidatoConTodo in listadoGeneral:
            resultado=[]
            votosCandidato = candidatoConTodo.get("suma")  # obtener los votos
            votosStr= str(votosCandidato)
            candidato = candidatoConTodo.get("doc")  # desde aqui obtener elnombre del partido
            elemDelCandidato = candidato.get("candidato")
            nombreCandidato = elemDelCandidato.get("nombre")
            apellidoCandidato = elemDelCandidato.get("apellido")
            partidoDelCandidato = elemDelCandidato.get("partido")
            nombrePartido = partidoDelCandidato.get("nombre")
            resultado.append("Nombres   : "+nombreCandidato)
            resultado.append("Apellidos : "+apellidoCandidato)
            resultado.append("Votos     : "+votosStr)
            resultado.append("Partido   : "+nombrePartido)
            listadoVotos.append(resultado)
        return listadoVotos





    ######################################################################################################################
    """Listado de lo votos obtenidos por todos los candidatos con el nombre del partido politico ordenados de mayor a menor"""
    def consolidadoMesas2(self):
        query ={"$group":{"_id":"$mesa","total_votos ":{"$count":{}},"doc":{"$first":"$$ROOT"}}}
        pipeline =[query]
        lista = self.queryAggregation(pipeline)
        ordenados = sorted(lista, key=lambda votos: votos['total_votos '],reverse=True)
        return ordenados

    def listadoVotosCandidatoPartidosxMesa(self, id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
            "$group": {
                "_id": "$candidato",
                "Total_votos": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query1, query2]
        lista = self.queryAggregation(pipeline)
        ordenado = sorted(lista, key=lambda votos: votos['Total_votos'], reverse=True)
        listadoVotos = []
        for candidatoConTodo in lista:
            resultado = []
            votosCandidato = candidatoConTodo.get("Total_votos")  # obtener los votos
            StrvotosCandidato = str(votosCandidato)
            candidato = candidatoConTodo.get("doc")  # desde aqui obtener elnombre del partido
            elemDelCandidato = candidato.get("candidato")
            nombreCandidato = elemDelCandidato.get("nombre")
            apellidoCandidato = elemDelCandidato.get("apellido")
            nombreCompleto = nombreCandidato + " " + apellidoCandidato
            numeroDelCandidato = elemDelCandidato.get("numero")
            partidoDelCandidato = elemDelCandidato.get("partido")
            nombrePartido = partidoDelCandidato.get("nombre")
            resultado.append("Num Candidato    :"+numeroDelCandidato)
            resultado.append("Nombre Candidato :"+nombreCompleto)
            resultado.append("Votos            :"+StrvotosCandidato)
            resultado.append("Partido          :"+nombrePartido)
            listadoVotos.append(resultado)
        return listadoVotos