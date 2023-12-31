import os
import sys

#Ejecuta el comando ffmpeg
def ejecutar_ffmpeg(comando):
    os.system(comando)

#main
if __name__=="__main__":
    ruta_salida = ""
    escala = "15"

    #Comprobar que se introdujo al menos el primer parámetro.
    if(len(sys.argv)<2):
        print("Debes especificar al menos la ruta en la que se encuentran los ficheros.")
        exit(1)

    #Comprobar que los parámetros introducidos son válidos.
    if(not os.path.exists(sys.argv[1])):
        print("Debes introducir la ruta en la que se encuentran los ficheros a convertir.")
        exit(1)

    if(len(sys.argv)>2):
        ruta_salida = sys.argv[2]
        if(not os.path.exists(ruta_salida)):
            print("Asegurate de que el directorio de salida introducido es válido")
            exit(1)
    else:
        ruta_salida = sys.argv[1]
    if(len(sys.argv)>3):
        try:
            if(int(sys.argv[3])>31 or int(sys.argv[3])<2):
                print("El valor debe ser entre 2 y 31")
                exit(1)
            escala = sys.argv[3]
        except ValueError:
            print("Debes introducir un valor entre 2 y 31")
            exit(1)
    try:
        #Se leen los ficheros en el directorio introducido y se escriben los comandos para transformar cada archivo.
        procesos = list()
        ficheros_entrada = os.listdir(sys.argv[1])
        entrada = sys.argv[1] + "/"
        comandos = ["ffmpeg -i " '"'+entrada+fichero+'"'+" -codec:v mpeg2video -qscale:v "+escala+' "'+ruta_salida+"/"+fichero[:fichero.index('.')]+".mpeg"+'"' for fichero in (ficheros_entrada)]
        for c in comandos:
            ejecutar_ffmpeg(c)
            
            
    except FileNotFoundError:
        print("Asegurate de que la ruta que has introducido existe.")
        exit(1)

