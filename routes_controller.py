from services.banco_dados_services import *
from services.deploy_service import *
from services.server_services import *

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# SERVER
@app.route('/find_all_server', methods=['GET'])
def route_find_all_server():
    return jsonify(find_all_server_service())


@app.route('/find_by_id_server/<int:id>', methods=['GET'])
def route_find_by_id_server(id):
    return jsonify(find_by_id_server_service(id))


@app.route('/save_server', methods=['POST'])
def route_save_server():
    return jsonify(save_server_service())


@app.route('/delete_server/<int:id>', methods=['DELETE'])
def route_delete_server(id):
    return jsonify(delete_server_service(id))


@app.route('/status_server/<int:id>', methods=['GET'])
def route_status_server(id):
    return jsonify(status_server_service(id))


# BANCO DE DADOS
@app.route('/consultar_banco_dados', methods=['GET'])
def rota_consultar_banco_dados():
    return jsonify(consultar_banco_dados_service())


@app.route('/inserir_banco_dados', methods=['POST'])
def rota_inserir_banco_dados():
    return inserir_banco_dados_service()


@app.route('/apagar_banco_dados/<int:id>', methods=['DELETE'])
def rota_apagar_banco_dados(id):
    return jsonify(apagar_banco_dados_service(id))


@app.route('/testar_conexao_banco_dados/<int:id>', methods=['GET'])
def rota_testar_conexao_banco_dados(id):
    return testar_conexao_banco_dados(id)


@app.route('/obter_tabelas_banco_dados/<int:id>', methods=['GET'])
def rota_obter_tabelas_banco_dados(id):
    return jsonify(obter_tabelas_banco_dados_service(id))


# DEPLOY
@app.route('/execute_deploy_by_id/<int:id>', methods=['GET'])
def rota_execute_deploy_by_id(id):
    return execute_deploy_by_id_service(id)


@app.route('/get_deploy', methods=['GET'])
def rota_get_deploy():
    return jsonify(get_deploy_service())


@app.route('/post_deploy', methods=['POST'])
def rota_post_deploy():
    return post_deploy_service()


@app.route('/delete_deploy/<int:id>', methods=['DELETE'])
def rota_delete_deploy(id):
    return jsonify(delete_deploy_service(id))

# PROCESSOS
# CONFIGURACOES
