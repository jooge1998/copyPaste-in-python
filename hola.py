
#
#       programa que compara los nombres de un archivo pdf con los de una carpeta que esta en diferentes rutas
#       si son iguales copia automaticamente los pdf a la carpeta con su nombre
#

import os 
import shutil   # copiar,cortar, renombar archivo

# retorna una lista que contiene archivos y carpetas en una determinada ubicación == os.lisdir

certificados = os.listdir('c:/Users/EQUIPO-PC/Desktop/Nueva/CERTIFICADOS');   # pdf a copiar 
directorio = os.listdir('c:/Users/EQUIPO-PC/Desktop/ESCANNER');     # carpeta destino con mismo nombre de certificados


contador = 0;

for i in range(25):
    for j in range(26) :    
        if certificados[i].split(' ',1)[1].split('.pdf')[0] == directorio[j].split(" ",1)[0]: # apartir de la 2 palabra del certifico == 1 palabra de la carpeta
          
         #copia de la ruta certificados a la carptera escaner 
         shutil.copy('c:/Users/EQUIPO-PC/Desktop/Nueva/CERTIFICADOS/'+ certificados[i],'c:/Users/EQUIPO-PC/Desktop/ESCANNER/'+directorio[j])    
         contador+= 1;
         print(certificados[i].split(' ',1)[1].split('.pdf')[0] + " == " + directorio[j].split(" ",1)[0])
         
        else:
            if certificados[i].split(' ',1)[1].split('.pdf')[0] == " ".join(directorio[j].split(" ",1)): # apartir de la 2 palabra del certifico == nombre completo de la carpeta
                 #shutil.copy('c:/Users/EQUIPO-PC/Desktop/Nueva/CERTIFICADOS/'+ certificados[i],'c:/Users/EQUIPO-PC/Desktop/ESCANNER/'+directorio[j]) 
                 contador+= 1;
                 print(certificados[i].split(' ',1)[1].split('.pdf')[0] + " == " + " ".join(directorio[j].split(" ",1)))

            if certificados[i].split(' ',1)[0].split('.pdf')[0] == " ".join(directorio[j].split(" ",1)):# 1 palabra del certificado == nombre completo de la carpeta
                # shutil.copy('c:/Users/EQUIPO-PC/Desktop/Nueva/CERTIFICADOS/'+ certificados[i],'c:/Users/EQUIPO-PC/Desktop/ESCANNER/'+directorio[j]) 
                 contador+= 1;
                 print(certificados[i].split(' ',1)[0].split('.pdf')[0] + " == " + " ".join(directorio[j].split(" ",1)))

            if "".join(certificados[i].split('.pdf')) == directorio[j]:     # NOMBRE COMPLETO CERTIFICADO == NOMBRE COMPLETO CARPETA

                # shutil.copy('c:/Users/EQUIPO-PC/Desktop/Nueva/CERTIFICADOS/'+ certificados[i],'c:/Users/EQUIPO-PC/Desktop/ESCANNER/'+directorio[j]) 
                 contador+= 1;
                 print(" ".join(certificados[i].split('.pdf')) + " == " + directorio[j])     # imprime el nombre de los pdf con los nombres de las carpetas a pasar
             
                 
print(contador) # imprime el numero de archivo copias

