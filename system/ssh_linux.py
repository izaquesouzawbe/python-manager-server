import paramiko

def executar_comando_ssh(hostname, username, password, comando):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(comando)
    resultado = stdout.read().decode('utf-8')

    print(resultado)

    client.close()

    return resultado

def transferir_arquivos_ssh(hostname, username, password, caminho_origem, caminho_destino):
    print(caminho_origem)
    print(caminho_destino)
    # Cria uma instância SSHClient
    client = paramiko.SSHClient()

    # Carrega as chaves do sistema (opcional, mas recomendado)
    client.load_system_host_keys()

    # Adiciona chaves do host automaticamente
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Conecta-se ao servidor SSH
    client.connect(hostname, username=username, password=password)

    sftp = client.open_sftp()

    # Realiza a transferência do arquivo
    sftp.put(caminho_origem, caminho_destino)
    # Fecha a conexão SFTP e SSH
    sftp.close()
    client.close()

    print("Arquivo transferido com sucesso.")