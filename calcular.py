import math
import argparse
argParser = argparse.ArgumentParser()

argParser.add_argument("-P", "--palabras", help="La cantidad de palabras posibles")
argParser.add_argument("-L", "--longitud", help="La longitud de la clave")
args = argParser.parse_args()

n = int(args.palabras) or 2048
r = int(args.longitud) or 12

combinaciones = math.comb(n, r)
combinaciones_formateadas = "{:,}".format(combinaciones)
print("Número total de combinaciones posibles:", combinaciones_formateadas)
