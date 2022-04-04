import psutil
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

memoriatexto=psutil.virtual_memory()
valorram=f"Memória total:{convert_size(memoriatexto[0])}, Memória Usada: ${convert_size(memoriatexto[3])}"
print(valorram)

import json

valor = {
    "total":memoriatexto[0],
    "usada":memoriatexto[3]
}
print(valor)


#total/usada