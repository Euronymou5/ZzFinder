# ZzFinder
# By: Euronymou5

import requests
from colorama import Fore
import os
import argparse
import sys

class colores:
    rojo = Fore.RED
    verde = Fore.GREEN
    azul = Fore.BLUE
    cyan = Fore.CYAN
    amarillo = Fore.YELLOW
    magenta = Fore.MAGENTA

logo = f"""
{colores.cyan}███████╗███████╗███████╗{colores.amarillo}██╗███╗   ██╗██████╗ {colores.magenta}███████╗██████╗     
{colores.cyan}╚══███╔╝╚══███╔╝██╔════╝{colores.amarillo}██║████╗  ██║██╔══██╗{colores.magenta}██╔════╝██╔══██╗    
{colores.cyan}  ███╔╝   ███╔╝ █████╗  {colores.amarillo}██║██╔██╗ ██║██║  ██║{colores.magenta}█████╗  ██████╔╝    
{colores.cyan} ███╔╝   ███╔╝  ██╔══╝  {colores.amarillo}██║██║╚██╗██║██║  ██║{colores.magenta}██╔══╝  ██╔══██╗    
{colores.cyan}███████╗███████╗██║     {colores.amarillo}██║██║ ╚████║██████╔╝{colores.magenta}███████╗██║  ██║    
{colores.cyan}╚══════╝╚══════╝╚═╝     {colores.amarillo}╚═╝╚═╝  ╚═══╝╚═════╝ {colores.magenta}╚══════╝╚═╝  ╚═╝    
"""

parser = argparse.ArgumentParser()
parser.add_argument("-wordlist", "-w", type=str, help="Introduce el directorio en el que se encuentre la wordlist que deseas utilizar.")
parser.add_argument('-dominio', '-d', required=True, help="Ingresa el dominio de la pagina web.")
args = parser.parse_args()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

lista_codigos_accesibles = [200, 201, 204, 205, 300, 301, 302, 304] # Lista de los codigos de respuesta que se consideran accesibles

def online(ver):
    try:
        res = requests.head(ver)
        if res.status_code in lista_codigos_accesibles:
            return True
        else:
            print(f'\n{colores.rojo}[!] Error al acceder a {ver}. Codigo de estado: {res.status_code}')
            return False
    except requests.ConnectionError:
        print(f'\n{colores.rojo}[!] Error: Ocurrio un error de conexion a: {ver}')
        return False

def checker():
    clear()
    print(logo)

    if args.wordlist:
        if not os.path.exists(args.wordlist):
            print(f'\n{colores.rojo}[!] Error: Wordlist no encontrada.')
            sys.exit(1)
            
    # Abrir wordlist y leer las lineas.
    with open(args.wordlist) as f:
        lineas = f.readlines()
        for linea in lineas:
           subs = linea.strip()
            
           # Busqueda de los subdominios
           try:
                response = requests.head(f'http://{subs}.{args.dominio}')
                if response.status_code in lista_codigos_accesibles: # Revisa el el codigo de respuesta de la pagina esta en la lista de codigos "accesibles"
                   print(f'\n{colores.verde}[ ✔ ] Subdominio encontrado: http://{subs}.{args.dominio}. Codigo de respuesta: {response.status_code}')
           except requests.ConnectionError: 
                print(f'\n{colores.rojo}[ ❌ ] Subdominio no accesible: http://{subs}.{args.dominio}')
                continue

    
print(logo)
if args.dominio:
    pass
# Checker para ver si la pagina es accesible.
ver = f"http://{args.dominio}" # Junta el http junto con el dominio para poder verificar que se tiene acceso a este.
if online(ver):
    checker()
else:
    print(f'{colores.rojo}[!] Error: El dominio ingresado no es accesible.')