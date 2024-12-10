# -*- coding: utf-8 -*-
"""
Ejercicio "fundir dos listas en una".

@author: Angel Gil
"""

def fundicion(agenda1,agenda2):
    agenda={} # Creamos el diccionario donde fundiremos las dos agendas.
    
    # Recorremos los nombres de nuestra primera agenda.
    for nombre in agenda1:
         
        if nombre in agenda2: # El punto delicado es cuando ambas agendas
                              # contienen un mismo nombre, vamos despacio:
            
            tuplas=[] # Para cada nombre, creamos una lista de tuplas de la
                      # forma (campo,entrada) que mas tarde convertiremos en
                      # diccionario mediante el comando dict().
            for campo in agenda1[nombre]:
                campoyentrada = [campo,agenda1[nombre][campo]]
                # 'campoyentrada' contiene la siguiente tupla a añadir.
                
                if campo in agenda2[nombre]:
                    # Si el campo (del mismo nombre) se encuentra en agenda2
                    # creamos una lista auxiliar que nos ayudara a actualizar
                    # la entrada de 'campoyentrada' cuando sea necesario.
                    if type(agenda1[nombre][campo]) == list:
                        apaño = agenda1[nombre][campo]
                    else: # Independientemente de que el campo solo contuviera
                          # una entrada, queremos una lista en la que añadir
                          # datos o no, dependiendo de agenda2.
                        apaño = [ agenda1[nombre][campo] ]
                    
                    # Si hay datos nuevos, atualizamos apaño para insertarlo
                    # posteriormente en la segunda componente de campoyentrada.
                    if type(agenda2[nombre][campo]) == list:
                        for i in range(len(agenda2[nombre][campo])):
                            if agenda2[nombre][campo][i] not in apaño:
                                apaño.append(agenda2[nombre][campo][i])
                                campoyentrada[1] = apaño
                    else:
                        if agenda2[nombre][campo] not in apaño: 
                            apaño.append(agenda2[nombre][campo])
                            campoyentrada[1] = apaño
                    # En cualquier caso, 'campoyentrada' contiene la union
                    # de ambos campos, aportemos informacion adicional con
                    # agenda2 o no.
                    
                # Si el campo no se encuentra en agenda2, 'campoyentrada' ya
                # contenia la siguiente tupla a añadir, luego tampoco es
                # necesario añadir un 'else'.
                tuplas.append((campoyentrada))

            # 'Tuplas' contiene en cada tupla un campo de agenda1 referente al
            # nombre 'nombre' junto a los datos de dicho campo donde agenda2
            # contenga informacion adicional. Tan solo queda añadir los campos
            # (referentes al nombre 'nombre') de agenda2 que no aparezcan en
            # agenda1.
            for campo in agenda2[nombre]:
                if campo not in agenda1[nombre]:
                    tuplas.append((campo,agenda2[nombre][campo]))
                        
            # 'Tuplas' ya contiene todos los campos del nombre junto a sus
            # datos, queda añadirlo en agenda transformandolo en diccionario.
            agenda[nombre] = dict(tuplas)
            
        else: # Si el nombre se encuentra solo en agenda1, basta con añadirlo
              # tal cual a agenda desde agenda1.
            agenda[nombre] = agenda1[nombre]
            
        # Solo falta meter los nombres de agenda2 que no aparezcan en agenda1.
        for nombre in agenda2:
            if nombre not in agenda1:
                agenda[nombre] = agenda2[nombre]
           
        return agenda # ¡Voila!
            
        