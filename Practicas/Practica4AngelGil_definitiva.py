# -*- coding: utf-8 -*-
"""
Práctica 4 - Metro.

@author: Ángel Gil

----------------------------------------------------------------------------------------------
En esta práctica haremos uso de clases para representar la red de metro de Madrid.

La práctica se divide en tres partes:
    - Creación de la clase Line
    - Creación de la clase Metro
    - Actualización de ambas clases para poder cerrar/abrir estaciones o secciones de línea.

----------------------------------------------------------------------------------------------

   Código para cargar la red de metro:
   ----------------------------------
   Mi_metro = Metro()
   Mi_metro.load_metro(fichero.txt)
       Donde el fichero debe estar preparado convenientemente siguiendo el PDF de la práctica
       en nuestro caso el fichero es 'metro_costes_capada.txt'
   ----------------------------------
   Una vez cargado el metro en la variable tipo Metro llamada Mi_metro, podemos llamar
   a los métodos definidos para ambas clases durante la práctica.
"""
                
###   Creamos dos clases de tipo excepción para incorporar más tarde.

class LineException(Exception):
    pass

class MetroException(Exception):
    pass

###   Parte 1 - Clase 'Line'   ###

class Line(object):
    """
    Representa las líneas de una red de metro. 
    
    Una línea de metro viene definida por una lista de nombres de estaciones y los tiempos del
    trayecto entre estaciones.
    
    Actualizacion Parte 3:
        - state: lista de booleanos asociados a cada estación. Si la estación i-ésima está 
                 cerrada, entonces state[i] == False; True si está abierta.
            
        - tramo: será una lista vacía si no hay sección cerrada en la línea. Si hay una sección 
                 cortada, contendrá el índice del principio y el final del corte. (Quizás
                 hubiera sido más cómodo meter directamente los nombres en lugar de los índices)
    """
    def __init__(self, estaciones, tiempos):
        self.s:list = estaciones
        self.t:list = tiempos
        self.state = []
        self.tramo = []
        
    def __str__(self)->str:
        """
        Metodo al que llama print(x), donde x es de clase Line
        
        Actualizada a Parte 3: Tiene en cuenta cierre de secciones y estaciones.
        """
        total = ''
        # Primero comprobamos si hay cierre de seccion.
        if len(self.tramo) > 0:
            
            # Escribimos las estaciones hasta el corte.
            for i in range(0,self.tramo[0]):
                
                # Comprobamos el estado de la estacion.
                if self.state[i]:
                    total = total + f'{self.s[i]} --> '
                else:
                    total = total + f'{self.s[i]} (cerrada) --> '
                    
            # Escribimos el corte.
            total = total + f'{self.s[self.tramo[0]]} (CORTE) -/- (CORTE) '
            
            # Escribimos las estaciones que quedan tras el corte.
            for i in range(self.tramo[1],len(self.state)):
                if self.state[i] and i != len(self.state)-1:
                    total = total + f'{self.s[i]} --> '
                elif i != len(self.state)-1:
                    total = total + f'{self.s[i]} (cerrada) --> '
                elif i == len(self.state)-1 and self.state[i]:
                    total = total + f'{self.s[i]}'
                else:
                    total = total + f'{self.s[i]} (cerrada)'
        
        # Si no hay corte procedemos directamente, comprobando el estado de las estaciones.
        else:
            for i in self.s:
                if i != self.s[len(self.s)-1] and self.state[self.s.index(i)]:
                    total = total + f'{i} --> '
                elif i != self.s[len(self.s)-1]:
                    total = total + f'{i} (cerrada) --> '
                elif i == self.s[len(self.s)-1] and self.state[self.s.index(i)]:
                    total = total + f'{i}'
                else:
                    total = total + f'{i} (cerrada)'
        return total
        
    def contains_station(self,e):
        """
        De vuelve True si la estacion e pertenece a la linea y False en caso contrario.
        
        No actualizada a parte 3:
            Supongo que una estación pertenece a la linea, esté cerrada o no.
        """
        if e in self.s:
            return True
        else:
            return False
        
    def previous_e(self,e):
        """
        Devuelve la estacion anterior a 'e' en la linea
        
        Actualizada a parte 3: Aporta informacion si la estacion se encuentra cerrada
                               o esta dentro de un corte de seccion.
        """
        try:
            # Comprobamos que no haya errores de entrada.
            if e not in self.s:
                raise LineException(str(e)+' no se encuentra en la linea dada.')
            i = self.s.index(e)
            if i == 0:
                raise LineException(str(e)+' es la primera parada de la linea')
                
            # Vemos si hay seccion cerrada.
            if len(self.tramo) > 0:
                
                # Vemos si se encuentra dentro del corte de la linea.
                if self.s[i-1] > self.tramo[0] and self.s[i-1] < self.tramo[1]:
                    ant = self.s[i-1] + ', aunque se encuentra dentro de una seccion cortada.'
                    
                # Si no esta dentro, comprobamos si esta cerrada o abierta.
                elif self.state[i-1]:
                    ant = self.s[i-1]
                else:
                    ant = self.s[i-1] + ', aunque se encuentra cerrada.'
            
            # Si no hay seccion cerrada, solo comprobamos el estado de la estacion.
            else:
                if self.state[i-1]:
                    ant = self.s[i-1]
                else:
                    ant = self.s[i-1] + ', aunque se encuentra cerrada.'
            return ant
        
        except LineException as k:
            print(k)

    def next_e(self,e):
        """
        Devuelve la siguiente estacion a 'e' en la linea
        
        Actualizada a parte 3: Aporta informacion si la estacion se encuentra cerrada
                               o esta dentro de un corte de seccion.
        """
        try:
            # Comprobamos que no haya errores de entrada.
            if e not in self.s:
                raise LineException(str(e)+' no se encuentra en la linea dada.')
            i = self.s.index(e)
            if i == len(self.s) - 1:
                raise LineException(str(e)+' es la ultima parada de la linea')
                
            # Vemos si hay seccion cerrada.
            if len(self.tramo) > 0:
                
                # Vemos si se encuentra dentro del corte de la linea.
                if self.s[i+1] > self.tramo[0] and self.s[i+1] < self.tramo[1]:
                    sig = self.s[i+1] + ', aunque se encuentra dentro de una seccion cortada.'
                    
                # Si no esta dentro, comprobamos si esta cerrada o abierta.
                elif self.state[i+1]:
                    sig = self.s[i+1]
                else:
                    sig = self.s[i+1] + ', aunque se encuentra cerrada.'
            
            # Si no hay seccion cerrada, solo comprobamos el estado de la estacion.
            else:
                if self.state[i+1]:
                    sig = self.s[i+1]
                else:
                    sig = self.s[i+1] + ', aunque se encuentra cerrada.'
            return sig

        except LineException as k:
            print(k)


    def cost_origin2destination(self,start, finish):
        """
        Calcula el tiempo estimado en ir de la estacion start a finish sin salir de la linea.
        
        Actualizado a Parte 3:
            - Si la estacion de partida o de destino estan cerrada devolvemos 'None'
            - Si hay cierre de seccion, solo calculamos la distancia en caso que ambas se 
              encuentren a un mismo lado del corte.
        """
        try:
            # Comprobamos que no haya errores de entrada.
            if not (start in self.s and finish in self.s):
                raise LineException('Alguna de estas estaciones no se encuentra en la linea dada.')
                
            a,b = self.s.index(start),self.s.index(finish)
            # No podemos salir de o llegar a una estacion cerrada.
            if not self.state[a] or not self.state[b]:
                return None
            
            # Intercambiamos indices si es necesario.
            if a > b:
                x_temp = b
                b = a
                a = x_temp

            # Iniciamos los calculos.
            suma = 0
            
            # Comprobamos si hay un tramo cortado.
            if len(self.tramo) > 0:
                
                t1,t2 = self.tramo[0],self.tramo[1]
                # Si ambas estaciones estan antes o despues del corte, podemos viajar.
                if a <= t1 and b <= t1:
                    for i in range(a,b):
                        suma = suma + self.t[i]
                elif a >= t2 and b >= t2:
                    for i in range(a,b):
                        suma = suma + self.t[i]
                        
                # Si se encuentran en extremos opuestos del corte o dentro de el no podemos viajar.
                else:
                    return None
                
            # No hay problemas.
            else:
                    for i in range(a,b):
                        suma = suma + self.t[i]
                        
            # Si no hemos devuelto 'None' es que todo fue bien, devolvemos 'suma'.
            return suma
        
        except LineException as k:
            print(k)

###   Parte 2 - Clase 'Metro'   ###

class Metro(object):
    """
    Representa la red de metro.
    
    Los objetos de la clase Metro almacenan la información de las líneas que forman la red 
    junto con los transbordos entre líneas.
    
    Actualizacion Parte 3:
        Nuevos metodos y adaptacion de los ya existentes.
        -close_station/open_station: permiten cerrar y abrir estaciones desde una linea concreta.
                                     La estacion sigue siendo transitable y podremos bajarnos en
                                     ella desde las otras lineas que la contengan.
                                    
        -close_section/open_section: permiten cerrar y abrir una seccion por linea. La seccion
                                     cerrada dejará de ser transitable sin incluir los extremos.
    """
    def __init__(self):
        self.vals = {}
        self.tbd  = {}
        
    def __str__(self)->str:
        """
        Metodo al que llama print(x), donde x es de clase Metro. 
        
        Actualizada a Parte 3: Tiene en cuenta cierre de secciones y estaciones.
        """
        # Sacamos por pantalla cada linea de metro dejando espacios de por medio.
        for key in self.vals.keys():
            print(key,self.vals[key],sep='\n',end='\n\n')
            
        # No funcionaba si no ponia un return. Esta fue la solucion mas facil que se me ocurrio.
        # Aunque un poco cutre ciertamente.
        return ''

    def add_line(self,line_name,line):
        """
        Añade la linea de tipo Line con nombre 'line_name'a la red de metro.
        
        No actualizamos en Parte 3 (no es necesario).
        """
        try:
            # Comprobamos que no haya errores de entrada. 
            if line_name in self.vals.keys():
                raise MetroException
            
            # Añadimos la linea a la red
            self.vals[line_name]=line
            
            # Llamamos al metodo que actualiza los transbordos posibles.
            self.add_connections(line_name,line)
            
        except MetroException:
            print('Esta linea ya se encontraba en la red de metro')

    def add_connections(self,line_name, line):
        """
        Añade los transbordos de la linea 'line' con nombre 'line_name' a la red de metro.
        
        No actualizamos en Parte 3 (no es necesario).
        """
        # Recorremos las estaciones de la linea.
        for i in line.s:
            
            # Si ya se ha creado la entrada de la estacion 'i' es que ya habia al menos dos
            # lineas que la contengan. Añadimos la nueva linea a la lista de transbordos.
            if i in self.tbd.keys():
                self.tbd[i].append(line_name)
                
            # Si no se ha creado, buscamos en el resto de lineas de la red si existe alguna
            # que tambien contenga la estacion 'i'.
            else:
                for j in self.vals.keys():
                    
                    # Si se da el caso, creamos la entrada 'i' con las lineas que la contienen.
                    if i in self.vals[j].s and j != line_name:
                       self.tbd[i] = [j,line_name]

    def load_metro(self,file_name):
        """
        Crea la red de metro desde el fichero 'file_name'.
        
        Actualizacion Parte 3: Añadimos a la linea la lista de estados de las estaciones. Al 
                               principio todas estaran abiertas, por lo que sera una lista de
                              'True' con longitud el numero de estaciones que tenga la linea.
        """
        # Abrimos el fichero y almacenamos las lineas en una lista.
        f = open(file_name,'r')
        contenido = f.readlines()
        
        # Evaluamos las lineas contenidas en el fichero
        for i in range(len(contenido)):
            
            # Si ocupa una posicion par se trata de un nombre de linea
            if i % 2 == 0:
                nombre_linea = contenido[i].rstrip() # Nos deshacemos de posibles espacios invisibles
                
            # Si ocupa una posicion impar se trata del contenido de la linea con el nombre de 'i-1'
            else:
                
                # Almacenamos ahora el recorrido de la linea en otra lista.
                # La informacion de la linea viene dada entre '->'.
                recorrido = contenido[i].split('->')
                estaciones, tiempos, estados = [],[],[]
                
                # Si ocupa posicion par se trata de una estacion. Si es impar es el tiempo de la
                # estacion j-1 a la j+1
                for j in range(len(recorrido)):
                    
                    # Si ocupa posicion par se trata de una estacion.
                    if j % 2 == 0:
                        estaciones.append(recorrido[j].strip('\n'))
                        estados.append(True)
                    
                    # Si es impar representa el tiempo que tardamos en ir de la estacion 'j-1' a la 'j+1'
                    else:
                        tiempos.append(int(recorrido[j]))
                
                # Una vez completado la secuencia (par, impar) añadimos la nueva linea a la red.
                linea = Line(estaciones,tiempos)
                linea.state = estados
                self.add_line(nombre_linea, linea)
                
        print(self) # Se puede comentar, lo puse para comprobar que todo iba bien.
                    
    def get_connections(self,e, line_name):
        """
        Devuelve los transbordos que podemos hacer desde estacion 'e' de la linea 'line_name' a 
        otras lineas
        
        Actualizado a Parte 3:
            - Si la estacion se encuentra cerrada desde la linea, lanza una excepcion
            - Si hay un cierre de seccion que afecte a la estacion, lanza una excepcion
            - Si la estacion (o una seccion que la incluya) esta cerrada desde otra linea 
              no sera posible hacer el transbordo a esa linea
        """
        try:
            # Comprobamos que no haya errores de datos de entrada
            if line_name not in self.vals.keys():
                raise MetroException('Esta linea no se encontraba en la red de metro')
            elif e not in self.vals[line_name].s:
                raise MetroException('La estacion no pertenece a la linea dada')
            elif not self.vals[line_name].state[self.vals[line_name].s.index(e)]:
                raise MetroException('La estacion se encuentra cerrada desde esta linea')
                
            # Vemos si hay un cierre de seccion en la linea    
            elif len(self.vals[line_name].tramo) > 0:
                cnt = []
                
                # La parada no puede estar dentro del cierre de seccion
                if self.vals[line_name].tramo[0] < self.vals[line_name].s.index(e) and self.vals[line_name].s.index(e) < self.vals[line_name].tramo[1]:
                    raise MetroException('Hay un cierre de seccion en la linea que incluye a la parada dada')
                    
                else:
                    if e in self.tbd.keys():
                        
                        # Miramos las demas lineas que incluyan a la parada
                        for lin in self.tbd[e]:
                            if lin != line_name:
                                
                                # Puede haber cierre de seccion en esas lineas
                                if len(self.vals[lin].tramo) > 0:
                                    # La estacion debe encontrarse fuera del cierre
                                    if self.vals[lin].tramo[0] > self.vals[lin].s.index(e) or self.vals[lin].s.index(e) > self.vals[lin].tramo[1]:
                                        # Ademas debe estar abierta desde esa linea
                                        if self.vals[lin].state[self.vals[lin].s.index(e)]:
                                            cnt.append(lin)
                                
                                # Si no lo hay y la estacion esta abierta desde esa linea, la incorporamos a 'cnt'        
                                elif self.vals[lin].state[self.vals[lin].s.index(e)]:
                                    cnt.append(lin)
            else:
                cnt = []
                if e in self.tbd.keys():
                    
                    # Miramos las demas lineas que incluyan a la parada
                    for lin in self.tbd[e]:
                        if lin != line_name:
                            
                            # Puede haber cierre de seccion en esas lineas
                            if len(self.vals[lin].tramo) > 0:
                                # La estacion debe encontrarse fuera del cierre
                                if self.vals[lin].tramo[0] > self.vals[lin].s.index(e) or self.vals[lin].s.index(e) > self.vals[lin].tramo[1]:
                                    # Ademas debe estar abierta desde esa linea
                                        if self.vals[lin].state[self.vals[lin].s.index(e)]:
                                            cnt.append(lin)
                                    
                            # Si no lo hay y la estacion esta abierta desde esa linea, la incorporamos a 'cnt'
                            elif self.vals[lin].state[self.vals[lin].s.index(e)]:
                                cnt.append(lin)
            return cnt
        except MetroException as k:
            print(k)

    def cost_origin2destination_transfer(self,start, finish):
        """
        Calcula el tiempo estimado en ir de la estacion start a finish haciendo como maximo
        un transbordo.
        
        Actualizado a Parte 3:
            - Si la estacion de partida o de destino estan cerrada devolvemos 'None'
            - Ahora tenemos en cuenta los cierres tanto de estacion como de seccion
        """
        # inicializamos el coste de transbordo con una cota superior a cualquier trayecto.
        # Conveniente tambien para la comparacion entre rutas, almacenara el trayecto mas corto.
        cost_min = 99999
        
        
        for key in self.vals.keys():
            if start in self.vals[key].s:
                # La estacion tiene que estar abierta desde la linea
                if self.vals[key].state[self.vals[key].s.index(start)]:
                    
                    # La estacion de llegada tambien se encuentra en la linea
                    if finish in self.vals[key].s:
                        # Tambien tiene que estar abierta
                        if self.vals[key].state[self.vals[key].s.index(finish)]:
                            
                            cost = self.vals[key].cost_origin2destination(start,finish)
                            # Actualizamos si tardamos menos tiempo que con la mejor ruta anterior
                            if cost < cost_min:
                                cost_min = cost
                    
                    # La estacion de llegada no se encuentra en la linea
                    else:
                        # Recorremos la linea mirando los transbordos de sus estaciones
                        for e in self.vals[key].s:
                            if self.vals[key].state[self.vals[key].s.index(e)]:
                                for lin in self.get_connections(e,key):
                                    
                                    # La estacion de llegada se encuentra en alguno de los transbordos posibles
                                    if finish in self.vals[lin].s:
                                        # Tambien tiene que estar abierta
                                        if self.vals[lin].state[self.vals[lin].s.index(finish)]:
                                            
                                            # Vamos de la estacion de partida a la estacion del transbordo
                                            trozo1 = self.vals[key].cost_origin2destination(start,e)
                                            # Del transbordo vamos a la estacion de llegada
                                            trozo2 = self.vals[lin].cost_origin2destination(e,finish)
                                            # El coste sera el de esos dos trayectos mas el tiempo del
                                            # transbordo (solo si ambos trayectos son posibles
                                            if trozo1 != None and trozo2 != None:
                                                cost = trozo1 + 300 + trozo2
                                                # Actualizamos si tardamos menos tiempo que con la mejor ruta anterior
                                                if cost < cost_min:
                                                    cost_min = cost
                                                    
        # Si no hemos encontrado una ruta, no devolvemos nada
        if cost_min >= 99999:
            return None
        
        # Si al menos hemos encontrado una ruta, devolvemos el tiempo de la mas rapida
        else:
            return cost_min

    def close_station(self,line_name, e):
        """
        Cierra la estacion 'e' para la linea 'line_name'
        
        Si ya estaba cerrada no hace nada
        """
        try:
            # Comprobamos que no haya errores de entrada.
            if line_name not in self.vals.keys():
                raise MetroException
            if e not in self.vals[line_name].s:
                raise LineException
            
            # Cambiamos el estado de la estacion 'e' a False
            pos = self.vals[line_name].s.index(e)
            self.vals[line_name].state[pos] = False
            
        except MetroException:
            print('Esta línea no se encuentra en la red de metro')
        except LineException:
            print('Esta estación no pertenece a la línea dada')
            
    def open_station(self,line_name, e):
        """
        Abre la estacion 'e' para la linea 'line_name'
        
        Si ya estaba abierta no hace nada
        """
        try:
            # Comprobamos que no haya errores de entrada.
            if line_name not in self.vals.keys():
                raise MetroException
            if e not in self.vals[line_name].s:
                raise LineException
            
            # Cambiamos el estado de la estacion 'e' a True
            pos = self.vals[line_name].s.index(e)
            self.vals[line_name].state[pos] = True
            
        except MetroException:
            print('Esta linea no se encuentra en la red de metro')
        except LineException:
            print('Esta estacion no pertenece a la linea dada')
            
    def close_section(self,line_name, start, finish):
        """
        Cierra la linea 'line_name' desde 'start' hasta 'finish'
        
        El cierre no incluye a los extremos; las estaciones intermedias son intransitables.
        Solo se puede cerrar una seccion por linea. Para actualizar la seccion cerrada habria
        que abrir la seccion y volver a cerrarla con el nuevo intervalo
        """
        try:
            # Comprobamos que no haya errores de entrada.
            if line_name not in self.vals.keys():
                raise MetroException
            if start not in self.vals[line_name].s or finish not in self.vals[line_name].s:
                raise LineException
                
            # Añadimos a la lista los indices ordenados de los extremos de la seccion cerrada
            # Solo si es vacia (es decir, no hay ya una seccion cerrada)
            if self.vals[line_name].tramo == []:
                st,fi = self.vals[line_name].s.index(start),self.vals[line_name].s.index(finish)
                if st < fi:
                    self.vals[line_name].tramo = [st,fi]
                else:
                    self.vals[line_name].tramo = [fi,st]
            
        except MetroException:
            print('Esta linea no se encuentra en la red de metro')
        except LineException:
            print('Alguna de las estaciones no pertenece a la linea dada')
            
    def open_section(self,line_name):
        """
        Abre la seccion cerrada de 'line_name'
        
        Si no habia ninguna seccion cerrada no hace nada
        """
        try:
            # Comprobamos que no haya errores de entrada.
            if line_name not in self.vals.keys():
                raise MetroException
                
            # Dejamos vacia la lista de la seccion cerrada
            self.vals[line_name].tramo = []
            
        except MetroException:
            print('Esta linea no se encuentra en la red de metro')