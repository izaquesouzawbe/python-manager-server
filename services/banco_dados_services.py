from flask import jsonify, request

from db.sqlite import *
from db.postgres import *


def consultar_banco_dados_service():

    rows = find_all_sqlite("SELECT id, descricao, nome, host, porta, usuario, senha FROM banco_dados")

    bancos_dados = []
    for row in rows:
        banco = {
            "id": row[0],
            "descricao": row[1],
            "nome": row[2],
            "host": row[3],
            "porta": row[4],
            "usuario": row[5],
            "senha": row[6]
        }
        bancos_dados.append(banco)

    return bancos_dados


def consultar_banco_dados_pelo_id_service(id):

    row = find_one_sqlite("SELECT id, descricao, nome, host, porta, usuario, senha FROM banco_dados where id = ?", (id,))

    banco = {
        "id": row[0],
        "descricao": row[1],
        "nome": row[2],
        "host": row[3],
        "porta": row[4],
        "usuario": row[5],
        "senha": row[6]
    }

    return banco


def inserir_banco_dados_service():
    data = request.get_json()

    if 'nome' in data:

        execute_sql_sqlite(
            'INSERT INTO banco_dados (descricao, nome, host, porta, usuario, senha) VALUES (?, ?, ?, ?, ?, ?)',
            (data['descricao'], data['nome'], data['host'], data['porta'], data['usuario'], data['senha'])
        )
        return jsonify({"message": "Banco de dados inserido com sucesso!"}), 201

    else:
        return jsonify({"error": "Nome é obrigatório"}), 400


def apagar_banco_dados_service(id):

    execute_sql_sqlite('DELETE FROM banco_dados WHERE id = ?', (id,))
    return {"message": f"Banco de dados {id} foi apagado."}


def obter_tabelas_banco_dados_service(id):
    banco = consultar_banco_dados_pelo_id_service(id)
    return obter_tabelas_banco_dados(banco)
