#!/bin/bash

echo "Instalando Camila11 GeoIP Tool..."

# Crear carpeta si no existe
mkdir -p $PREFIX/bin

# Descargar el script directamente al bin
curl -s https://raw.githubusercontent.com/Camila11deticcy/camila11-geolocalizacion-tool/main/geolocate.py -o $PREFIX/bin/camila-geo

# Dar permisos
chmod +x $PREFIX/bin/camila-geo

echo "Instalación completa!"
echo "Usa el comando: camila-geo <IP>"
