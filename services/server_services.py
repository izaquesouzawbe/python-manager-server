from flask import jsonify, request

from db.sqlite import *
from scripts.scripts_linux import *
from system.ssh_linux import executar_comando_ssh


def find_all_server_service():

    rows = find_all_sqlite("SELECT id, name, host, username FROM server", ())

    servers = []
    for row in rows:
        server = {
            "id": row[0],
            "name": row[1],
            "host": row[2],
            "username": row[3],
            "use": "-"
        }
        servers.append(server)

    return servers


def find_by_id_server_service(id):

    row = find_one_sqlite("SELECT id, name, host, username, password FROM server where id = ?", (id,))

    server = {
        "id": row[0],
        "name": row[1],
        "host": row[2],
        "username": row[3],
        "password": row[4]
    }

    return server


def save_server_service():
    data = request.get_json()

    if 'name' in data:

        if not data.get("id"):
            execute_sql_sqlite(
                'INSERT INTO server (name, host, username, password) VALUES (?, ?, ?, ?)',
                (data['name'], data['host'], data['username'], data['password'])
            )
            return {"message": "Servidor inserido com sucesso!"}, 201
        else:
            execute_sql_sqlite(
                'UPDATE server SET name=?, host=?, username=?, password=? WHERE id=?',
                (data['name'], data['host'], data['username'], data['password'], data["id"])
            )
            return {"message": "Servidor alterado com sucesso!"}, 201

    else:
        return {"error": "Nome é obrigatório"}, 400


def delete_server_service(id):

    execute_sql_sqlite('DELETE FROM server WHERE id = ?', (id,))
    return {"message": f"Servidor {id} foi apagado."}


def status_server_service(id):

    server = find_by_id_server_service(id)

    print(server)

    host = server["host"]
    username = server["username"]
    password = server["password"]

    result_ssh = executar_comando_ssh(host, username, password, comando_retorna_memoria + comando_retorna_uso_cpu)

    return {"result_ssh": result_ssh.replace('/n', '')}
