import json, requests, time
from pathlib import Path

print("PullReceita 2018 - Versão 1.0 ")
print("Autor: Lucas Teles\n")
cnpj = open("cnpj.txt", "r")
cnpj = (cnpj.read()).split(',')
arq = open(str(Path.home()) +'/desktop/lista.txt', 'a+')
for c in cnpj:
    response = requests.get("http://receitaws.com.br/v1/cnpj/" + c)
    if response.status_code == 504:
        print("INVALIDO ", c)
        text = ("INVALIDO ", c, "\n")
    else:
        data = json.loads(response.content)
        if data["status"] == "ERROR":
            print("INVALIDO ", c)
            text = ("INVALIDO ", c, "\n")
        else:
            print (data["situacao"], " " , data["cnpj"])
            text = (data["situacao"], " " , data["cnpj"], "\n")
    arq.writelines(text)
    time.sleep(20)
arq.close()
cnpj.close()