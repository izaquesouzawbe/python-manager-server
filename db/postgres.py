import psycopg2


def get_params(banco):
    db_params = {
        'dbname': banco["nome"],
        'user': banco["usuario"],
        'password': banco["senha"],
        'host': banco["host"],
        'port': banco["porta"]
    }

    return db_params

def obter_conexao_banco_dados(banco):
    connection = psycopg2.connect(**get_params(banco))
    return connection


def testar_conexao_banco_dados(banco):
    connection = None
    try:
        connection = obter_conexao_banco_dados(banco)
        print("Conexão bem-sucedida!")
        return True
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return False
    finally:
        if connection:
            connection.close()


def obter_tabelas_banco_dados(banco):
    print(banco)
    connection = obter_conexao_banco_dados(banco)
    cursor = connection.cursor()

    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    rows = cursor.fetchall()

    cursor.close()

    tabelas = []
    for row in rows:
        tabela = {
            "nome": row[0]
        }
        tabelas.append(tabela)

    print(tabelas)

    return tabelas