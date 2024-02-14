#!/bin/bash

# Especifica el rango de IP de tu red (ajusta según tu red)
red="192.168.1.0/24"

# Realiza un escaneo de todos los hosts activos en la red y guarda los resultados en un archivo
nmap -sn $red -oG resultados.txt

# Crea un archivo HTML con la estructura básica y un título
echo -e "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>Hosts Activos</title>\n<style>\nbody { text-align: center; }\np { margin: 10px; }\nh1 { margin-top: 20px; }\n</style>\n</head>\n<body>\n<h1>HOSTS ACTIVOS</h1>" > hosts_activos.html

# Extrae las direcciones IP activas del archivo de resultados y las agrega al archivo HTML
awk '/Up$/{print "<p>" $2 "</p>"}' resultados.txt >> hosts_activos.html

# Cierra la estructura del archivo HTML
echo "</body>\n</html>" >> hosts_activos.html

# Abre el archivo HTML en el navegador predeterminado
xdg-open hosts_activos.html
