host = "local"
user = "root"
passwd = "1234"

#comando_a_executar = "kill $(ps aux | grep \"java -jar crypto.scheduled-0.0.1-SNAPSHOT.jar\" | grep -v grep | awk '{print $2}')"
#comando_a_executar = "nohup java -jar crypto.scheduled-0.0.1-SNAPSHOT.jar &"
#comando_a_executar = "sudo apt-get install tomcat9"
#comando_a_executar = "top -bn 1 | grep '%Cpu' | awk '{print $2 + $4}'"

comando_retorna_uso_cpu = "top -b -n 1 | grep '%Cpu' | awk '{print \" - Cpu: \" $2 + $4 + $6 \"%/\" 100 \"%\"}';"
comando_retorna_memoria = "free -h | grep Mem | awk  '{print \"Mem: \" $3\"/\"$2}';"
