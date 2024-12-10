# -*- coding: utf-8 -*-
"""
MezclaAgendasBien

@author: Angel Gil
"""

def unir_agendas(ag1,ag2):
# Une dos agendas cuyas entradas son a su vez directorios
    for nombre in ag2.keys():
        meter_ags(ag1,nombre,ag2[nombre])
    return ag1

def meter_ags(agenda,nombre,entrada):
# Mete en la agenda en el nombre indicado
# que podría estar o no ya en ella
# el diccionario entrada que se pasa como entrada
# respetando la especificación del problema
    if nombre not in agenda.keys():
        agenda[nombre] = entrada
    else:
        agenda[nombre] = añadir_datos(agenda,nombre,entrada)
    return agenda

def añadir_datos(agenda,nombre,entrada):
# hace lo indicado para meter_ags en el caso
# en el que el nombre ya aparecía en agenda
# (lo que asumiremos que es cierto)
    for campo in entrada.keys():
        if campo not in agenda[nombre].keys():
            agenda[nombre][campo]=entrada[campo]
        else:
            agenda[nombre][campo]=juntar(agenda,nombre,entrada,campo)
    return agenda[nombre]
    
def juntar(agenda,nombre,entrada,campo):
# mete en agenda en el nombre indicado y dentro
# de él en el campo indicado el valor asociado
# a campo en el diccionario entrada
# partiendose de que tanto entrada como
# la correspondiente a nombre en agenda
# contienen el campo campo
    if type(entrada[campo]) == list:
        if type(agenda[nombre][campo]) == list:
            for i in entrada[campo]:
                if i not in agenda[nombre][campo]:
                    agenda[nombre][campo].append(i)
        else:
            if agenda[nombre][campo] not in entrada[campo]:
                entrada[campo].append(agenda[nombre][campo])
            agenda[nombre][campo] = entrada[campo]
    else:
        if type(agenda[nombre][campo]) == list:
            if entrada[campo] not in agenda[nombre][campo]:
                agenda[nombre][campo].append(entrada[campo])
        else:
            if entrada[campo] != agenda[nombre][campo]:
                agenda[nombre][campo]=[ agenda[nombre][campo],entrada[campo] ]
    return agenda[nombre][campo]
   