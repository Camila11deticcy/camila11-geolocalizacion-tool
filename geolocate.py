#!/usr/bin/env python3
import requests
import sys

def geolocate(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error obteniendo datos")
        return
    
    data = response.json()
    print("\n--- Información de IP ---")
    print(f"IP: {data.get('ip', 'N/A')}")
    print(f"Ciudad: {data.get('city', 'N/A')}")
    print(f"Región: {data.get('region', 'N/A')}")
    print(f"País: {data.get('country', 'N/A')}")
    print(f"Ubicación (lat,long): {data.get('loc', 'N/A')}")
    print(f"Proveedor (ISP): {data.get('org', 'N/A')}")
    print(f"Zona Horaria: {data.get('timezone', 'N/A')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python geolocate.py <IP>")
        sys.exit(1)

    geolocate(sys.argv[1])
