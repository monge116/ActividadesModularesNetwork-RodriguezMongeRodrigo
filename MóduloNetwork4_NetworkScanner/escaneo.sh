#!/bin/bash

# Escaneo de direcciones IP
equipos_activos=$(nmap -sn 192.168.1.0/24 | grep "Nmap scan report" | awk '{print $5}')

echo "Equipos Activos:"
echo "$equipos_activos"

# Escaneo de puertos TCP y UDP
resultado_puertos=$(nmap -p 0-65535 -sS -sU --open 192.168.1.0/24)

# Mostrar resultados de puertos con estado
echo -e "\nListado de Puertos TCP y UDP:"
echo "$resultado_puertos" | grep -E '^[0-9]+/' | awk '{print "Puerto "$1": "$2}'
