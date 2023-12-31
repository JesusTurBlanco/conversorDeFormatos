#Conversor de formatos de vídeo a mpeg

Este script sirve para cambiar el formato de todos los vídeos ubicados en una carpeta a otro compatible con un reproductor de dvd.

Para poder usarlo es necesario descargar e instalar ffmpeg, para ello puede seguir las siguientes instrucciones:
```
1-Descargue la versión correspondiente de ffmpeg en el siguiente enlace: https://www.gyan.dev/ffmpeg/builds/
Recomiendo la versión full.
2-Extraiga el archivo 7z en la carpeta que usted desee (Si no lo ha instalado, es recomendable instalar 7zip)
3-Acceda a la carpeta bin, dónde se encuentran los ejecutables y copie su ruta.
4-En la variable de entorno y usuario path, añada la ruta copiada anteriormente.
```

Una vez instalado ffmpeg puede usar el script de la siguiente forma:
```
py .\convert_avi_to_mpeg.py "Directorio de entrada" "Directorio de salida" 13
```
El script puede tomar hasta 3 parámetros, siendo obligatorio solo el primero, en el que debe especificar la ruta de la carpeta dónde están los vídeos que desea convertir a formato mpeg.

El segundo parámetro es opcional. Indica la carpeta dónde se depositarán los vídeos ya convertidos a formato mpeg. En caso de no especificarse usará la misma que se especifica en el primer parámetro.

El tercer parámetro es también opcional, indica la calidad que se desea para la conversión. Deberá introducir un número entre 2 y 31. Siendo 2 la máxima calidad y 31 la mínima. En caso de no introducir ninguno se supondrá que la calidad es 15.

#Recomendaciones:
En caso de que el directorio de entrada o el de salida contengan espacios, asegúrese de que al introducir la ruta del directorio como parámetro, esta vaya entrecomillada.

Evite usar la máxima calidad de conversión, pues el tamaño aumenta considerablemente.