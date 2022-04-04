from http.server import HTTPServer, BaseHTTPRequestHandler

import base64
import os

#pip const q pega o endereço atual

import socket
"""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
PEIP = s.getsockname()[0]
s.close
"""
hostname = socket.gethostname()
PEIP = socket.gethostbyname(hostname)

#import datetime
#now = datetime.datetime.now()
#data = f"{now.year}/{now.month}/{now.day} {now.hour}:{now.minute} and {now.second}s"
#print()

def pega_saida_saida_ram():
    
    #print("Iniciando")
    #executando comando no term e saida para arquivo
    os.system("vmstat -s > saida.txt")
    

    #abrindo texto de arquivo
    texto = open("saida.txt","r")

    #transferindo texto para outra variavel para poder fecar o texto1
    texto2 = str(texto.read())

    #fechando texto1
    texto.close()

    textot = texto2[:texto2.find('free swap')+9]
    textot = textot.split("\n")
    arr=[]
    for i in textot:
        i=i.lstrip()
        i= int(int(i[:i.find(' ')]) / 1000)
        arr.append(i)
    txtn = arr
    #print(txtn)
    #textofinal = (f" Ram Total : {txtn[0]}Mb | Ram Usada : {txtn[1]}Mb | Swap Total : {txtn[7]}Mb | Swap Usada : {txtn[8]}Mb")
    textofinal = (f"{txtn[0]}|{txtn[1]}|{txtn[7]}|{txtn[8]}")
    return textofinal



print('Carregando Recusos...')
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
    print(f"Servidor Carregado!\nIP:{PEIP}\nPorta:{PORT}")
    server.serve_forever()

if __name__ == '__main__':
    main()
