from http.server import HTTPServer, BaseHTTPRequestHandler

import base64
import os
import psutil
import math

#import datetime
#now = datetime.datetime.now()
#data = f"{now.year}/{now.month}/{now.day} {now.hour}:{now.minute} and {now.second}s"
print()


#funcao retorna a variavel do valor da ram antes era pego usando sistema de arquivos
def pega_saida_saida_ram():
    """""
    os.system("free -h > saida.txt")
    print("Iniciando")
    #executando comando no term e saida para arquivo
    os.system("free -h > saida.txt")
    

    #abrindo texto de arquivo
    texto = open("saida.txt","r")

    #transferindo texto para outra variavel para poder fecar o texto1
    texto2 = str(texto.read())

    #fechando texto1
    texto.close()
    print(texto2)
    """""
    #puxa um array com informacoes da ram em bytes
    memoriatexto=psutil.virtual_memory()
    #valorram=f"Memória total:{convert_size(memoriatexto[0])}, Memória Usada: ${convert_size(memoriatexto[3])}"
    valorjson = {
    "total":memoriatexto[0],
    "usada":memoriatexto[3]
    }
    #valorram=f"{memoriatexto[0])} | {memoriatexto[3])}"
    return str(valorjson)



print('Começando')
def codificar(dados):
    encoded = base64.b64encode(dados.encode('utf-8'))
    #desencoded = base64.b64decode(encoded)

    return encoded

#print(codificar("dados.txt"))

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path == "/admin"):
            msg=codificar(pega_saida_saida_ram())#+self.date_time_string()
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            #self.wfile.write(self.date_time_string().encode()) #msg
            self.wfile.write(msg)
        else:
            """
            self.close_connection()
            data = self.date_time_string()
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            #self.path
            self.wfile.write(data.encode())
            """
            #self.end_headers()
            self.send_error(404)
def main():
    PORT = 8500
    #localhost
    server = HTTPServer(('',PORT),echoHandler)
    print("server roando na porta ",PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
