import subprocess


def executar_comando_windows(comando):
    output = subprocess.check_output(comando, shell=True, text=True)
    print(output)
    return output
