from flask import jsonify, request
from db.sqlite import *
import os
from services.server_services import find_by_id_server_service
from system.cmd_windows import executar_comando_windows
from system.ssh_linux import transferir_arquivos_ssh, executar_comando_ssh


def consultar_deploy_pelo_id(id):
    row = find_one_sqlite(
        "select id_servidor, comando_origem, caminho_origem, caminho_destino, comando_destino from deploy where id = ?",
        (id,)
    )

    deploy = {
        "servidor": find_by_id_server_service(2),
        "comando_origem": row[1],
        "caminho_origem": row[2],
        "caminho_destino": row[3],
        "comando_destino": row[4]
    }

    return deploy


def get_deploy_service():
    rows = find_all_sqlite("SELECT id, nome FROM deploy")

    deploys = []
    for row in rows:
        deploy = {
            "id": row[0],
            "nome": row[1]
        }
        deploys.append(deploy)

    return deploys


def post_deploy_service():
    data = request.get_json()

    if 'nome' in data:

        execute_sql_sqlite(
            'INSERT INTO deploy (nome, id_servidor, comando_origem, caminho_origem, caminho_destino, comando_destino) '
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (data['nome'], data['id_servidor'], data['comando_origem'], data['caminho_origem'], data['caminho_destino'],
             data['comando_destino'])
        )
        return jsonify({"message": "Banco de dados inserido com sucesso!"}), 201

    else:
        return jsonify({"error": "Nome é obrigatório"}), 400


def delete_deploy_service(id):
    execute_sql_sqlite('DELETE FROM deploy WHERE id = ?', (id,))
    return {"message": f"Banco de dados {id} foi apagado."}


def execute_deploy_by_id_service(id):
    deploy = consultar_deploy_pelo_id(id)
    servidor = deploy["servidor"]

    if deploy["comando_origem"]:
        executar_comando_windows(os.path.normpath(deploy["comando_origem"]))

    transferir_arquivos_ssh(servidor["host"], servidor["usuario"], servidor["senha"],
                            os.path.normpath(deploy["caminho_origem"]), os.path.normpath(deploy["caminho_destino"]))

    if deploy["comando_destino"]:
        executar_comando_ssh(servidor["host"], servidor["usuario"], servidor["senha"], deploy["comando_destino"])