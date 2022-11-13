from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultados import ControladorResultados
miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()
miControladorPartido = ControladorPartido()
miControladorResultados = ControladorResultados()

###################################################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
######################################## CANDIDATOS ###########################################
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
######################################### MESAS ##########################################
@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)
#########################
@app.route("/candidatos/<string:id>/partidos/<string:id_partido>" ,methods=['PUT'])
def asignarPartidoACandidato(id,id_partido):
    json =miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)


####### PARTIDO ###################################################
@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)


################################# RESULTADOS ##################################################
@app.route("/resultados",methods=['GET'])#json con informacion de idresultados,candidato y mesa
def getResultados():
    json=miControladorResultados.index()
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])#json con los json del voto
def getResultado(id):
    json=miControladorResultados.show(id)
    return jsonify(json)
@app.route("/resultados/mesas/<string:id_mesa>/candidatos/<string:id_candidato>",methods=['POST'])
def crearResultado(id_mesa,id_candidato):
    data = request.get_json()
    json=miControladorResultados.create(data,id_mesa,id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>/mesas/<string:id_mesa>/candidatos/<string:id_candidato>",methods=['PUT'])
def modificarResultado(id_resultado,id_mesa,id_candidato):
    data = request.get_json()
    json=miControladorResultados.update(id_resultado,data,id_mesa,id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    json=miControladorResultados.delete(id_resultado)
    return jsonify(json)

############################LISTAR resultado de los CANDIDATOS###############################################

@app.route("/resultados/candidatos/<string:id_candidato>",methods=['GET'])#json con json de los votos de este candidato
def resultadosCandidato(id_candidato):
    json = miControladorResultados.listarResultadosCandidatos(id_candidato)
    return jsonify(json)


########## votacion mas alta ###############

@app.route("/resultados/candidato_ganador",methods=['GET'])#json con el id del candidato ganandor y sus votos
def getVotosMayores():
    json=miControladorResultados.ganadorElecciones()
    return jsonify(json)

@app.route("/resultados/consolidadomesas",methods=['GET'])#json con el id de la mesa y sus votos
def getTotalVotosMesas():
    json=miControladorResultados.listaConsolidadosMesas()
    return jsonify(json)
@app.route("/resultados/TodosLosResultados",methods=['GET'])#json nombre, apellidos del candidato partido y sus votos en todas las mesas
def getTodosLosResultados():
    json=miControladorResultados.listaDelTutorControlador()
    return jsonify(json)
@app.route("/resultados/consolidadoMesas2",methods=['GET'])#json con idmesa, doc(candidato) y mesa y su total de votos
def getConsolidado2():
    json=miControladorResultados.elConsolidador2()
    return jsonify(json)
@app.route("/resultados/votosPartido",methods=['GET'])
def getVotosPartido():
    json=miControladorResultados.elPuntoC()
    return jsonify(json)

@app.route("/resultados/ListadoPartidosOrdenadosVotos",methods=['GET'])
def getListadoPartidosOrdenadosPorVotos():
    json=miControladorResultados.listarpartidosOrdenadosPorVotos()
    return jsonify(json)
@app.route("/resultados/porcentajeParticipacion",methods=['GET'])
def getPorcentajeParticipacion():
    json=miControladorResultados.listarPorcentajeParticipacion()
    return jsonify(json)
@app.route("/resultados/listarporcentajepartidos",methods=['GET'])
def porcentajePartidosCongreso():
    json=miControladorResultados.listarPorcentualPartidos()
    return jsonify(json)

##########listar resultados en la mesa indicada #########
@app.route("/resultados/listaVotosCandidatosMesa/<string:id_mesa>",methods=['GET'])#YYY
def listaVotosCandidatosMesas(id_mesa):
    json=miControladorResultados.listaVotocCandidatosMesa(id_mesa)
    return jsonify(json)

#############################     mfdc3     ####################################################
#############################continuar trabajando, esta copia está en el repositorio ###########
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])