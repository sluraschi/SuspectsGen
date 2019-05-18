#!/usr/bin/python3

import sys
import Persona
import GeneradorSospechosos


def generar_personas(nombrea_archivo):
    archivo = open(nombrea_archivo, 'r')
    lista_personas = []
    lineas = archivo.read().splitlines()

    for elemento in lineas:
        linea1 = elemento.split(",")
        personaAux = Persona.Persona(linea1[0],linea1[1],linea1[2])
        lista_personas.append(personaAux)

    archivo.close()
    return lista_personas


def generar_archivo_salida(lista_de_listas):
    ## ver que pasa con lista de listas vacia
    with open('sospechosos.txt', 'w') as f:
        for lista in lista_de_listas:
            for elemento in lista:
                f.write(elemento.nombre + "," + str(elemento.tiempototal)),
                f.write('\n')
            f.write('\n')


def main(argv):
    lista_personas = generar_personas(argv)
    generador_sospechosos = GeneradorSospechosos.GeneradorSospechosos(lista_personas)
    lista_sospechosos = generador_sospechosos.encontrar_sospechosos()
    generar_archivo_salida(lista_sospechosos)


if __name__ == "__main__":
    main(sys.argv[1])
