
#
#       programa que compara los nombres de unos archivos .jpg con los de una carpeta que esta en diferentes rutas
#       si son iguales copia automaticamente los jpg a la carpeta con su nombre
#

import os 
import shutil   # copiar,cortar, renombar archivo

# retorna una lista que contiene archivos y carpetas en una determinada ubicación == os.lisdir

certificados = os.listdir('c:/Users/EQUIPO-PC/Desktop/FOTOS');   # pdf a copiar 
directorio = os.listdir('c:/Users/EQUIPO-PC/Desktop/ESCANNER');     # carpeta destino con mismo nombre de certificados

contador = 0;


for i in range(26):
    for j in range(26) :
         if certificados[i].split(' ',1)[0].split('.jpg')[0] == " ".join(directorio[j].split(" ",1)):# 1 palabra del certificado == nombre completo de la carpeta
                 shutil.copy('c:/Users/EQUIPO-PC/Desktop/FOTOS/'+ certificados[i],'c:/Users/EQUIPO-PC/Desktop/ESCANNER/'+directorio[j]) 
                 contador+= 1;
                 print(certificados[i].split(' ',1)[0].split('.pdf')[0] + " == " + " ".join(directorio[j].split(" ",1)))
         if certificados[i].split('.jpg',)[0] == " ".join(directorio[j].split(" ",1)) and certificados[i].split('.jpg',)[0] != "KEINA RIVERA" and certificados[i].split('.jpg',)[0] != "KEYLA YEPEZ":# nombre completo del certificado == nombre completo de la carpeta
                 shutil.copy('c:/Users/EQUIPO-PC/Desktop/FOTOS/'+ certificados[i],'c:/Users/EQUIPO-PC/Desktop/ESCANNER/'+directorio[j]) 
                 contador+= 1;
                 print(certificados[i].split('.jpg',)[0] + " == " + " ".join(directorio[j].split(" ",1)))
         if certificados[i].split('.jpg',)[0].split(" ")[0] +" "+ certificados[i].split('.jpg',)[0].split(" ")[1]  == " ".join(directorio[j].split(" ",1)):# 1 y 2 palabra del certificado == nombre completo de la carpeta
                 shutil.copy('c:/Users/EQUIPO-PC/Desktop/FOTOS/'+ certificados[i],'c:/Users/EQUIPO-PC/Desktop/ESCANNER/'+directorio[j]) 
                 contador+= 1;
                 print(certificados[i].split('.jpg',)[0].split(" ")[0] +" "+ certificados[i].split('.jpg',)[0].split(" ")[1] + " == " + " ".join(directorio[j].split(" ",1)))        
            
print(contador);

 