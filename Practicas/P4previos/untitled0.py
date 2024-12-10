# -*- coding: utf-8 -*-
"""
Práctica 4 - Metro.

@author: Ángel Gil


"""
                

class LineException(Exception):
    pass

class MetroException(Exception):
    pass

###   Parte 1 - Clase 'Line'   ###

class Line(object):
    """
    """
    def __init__(self, estaciones, tiempos):
        self.s:list = estaciones
        self.t:list = tiempos
        self.state = []
        self.tramo = []
        
    def __str__(self)->str:
        total = ''
        if len(self.tramo) > 0:
            for i in range(0,self.tramo[0]):
                if self.state[i]:
                    total = total + f'{self.s[i]} --> '
                else:
                    total = total + f'{self.s[i]} (cerrada) --> '
            total = total + f'{self.s[self.tramo[0]]} (CORTE) -/- (CORTE) '
            for i in range(self.tramo[1],len(self.state)):
                if self.state[i] and i != len(self.state)-1:
                    total = total + f'{self.s[i]} --> '
                elif i != len(self.state)-1:
                    total = total + f'{self.s[i]} (cerrada) --> '
                elif i == len(self.state)-1 and self.state[i]:
                    total = total + f'{self.s[i]}'
                else:
                    total = total + f'{self.s[i]} (cerrada)'
                    
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
        if e in self.s:
            return True
        else:
            return False
        
    def previous_e(self,e):
        try:
            if e not in self.s:
                raise LineException(str(e)+' no se encuentra en la linea dada.')
            i = self.s.index(e)
            if i == 0:
                raise LineException(str(e)+' es la primera parada de la linea')
            return self.s[i-1]
        except LineException as k:
            print(k)
        except:
            return None
            
    def next_e(self,e):
        try:
            if e not in self.s:
                raise LineException(str(e)+' no se encuentra en la linea dada.')
            i = self.s.index(e)
            if i == len(self.s) - 1:
                raise LineException(str(e)+' es la ultima parada de la linea')
            return self.s[i+1]
        except LineException as k:
            print(k)
        except:
            return None

    def cost_origin2destination(self,start, finish):
        try:
            if not (start in self.s and finish in self.s):
                raise LineException('Alguna de estas estaciones no se encuentra en la linea dada.')
            a,b = self.s.index(start),self.s.index(finish)
            suma = 0
            if len(self.tramo) > 0:
                t1,t2 = self.tramo[0],self.tramo[1]
                if a < t1 and b < t1:
                    for i in range(self.s.index(start),b):
                        suma = suma + self.t[i]
                elif a > t2 and b > t2:
                    for i in range(a,b):
                        suma = suma + self.t[i]
                else:
                    suma = 99999
            else:
                    for i in range(a,b):
                        suma = suma + self.t[i]
            return suma
        except LineException as k:
            print(k)

###   Parte 2 - Clase 'Metro'   ###

class Metro(object):
    """
    """
    def __init__(self):
        self.vals = {}
        self.tbd  = {}
        
    def __str__(self)->str:
        for key in self.vals.keys():
            print(key,self.vals[key],sep='\n',end='\n\n')
        return ''

    def add_line(self,line_name,line):
        try:
            if line_name in self.vals.keys():
                raise MetroException
            self.vals[line_name]=line
            self.add_connections(line_name,line)
            
        except MetroException:
            print('Esta linea ya se encontraba en la red de metro')

    def add_connections(self,line_name, line):
        for i in line.s:
            if i in self.tbd.keys():
                self.tbd[i].append(line_name)
            else:
                for j in self.vals.keys():
                    if i in self.vals[j].s and j != line_name:
                       self.tbd[i] = [j,line_name]
            
    def load_metro(self,file_name):
        f = open(file_name,'r')
        contenido = f.readlines()
        for i in range(len(contenido)):
            if i % 2 == 0:
                nombre_linea = contenido[i].rstrip()
            else:
                recorrido = contenido[i].split('->')
                estaciones, tiempos, estados = [],[],[]
                for j in range(len(recorrido)):
                    if j % 2 == 0:
                        estaciones.append(recorrido[j].strip('\n'))
                        estados.append(True)
                    else:
                        tiempos.append(int(recorrido[j]))
                linea = Line(estaciones,tiempos)
                linea.state = estados
                self.add_line(nombre_linea, linea)
        print(self) # Se puede comentar, lo puse para comprobar que todo iba bien.
                    
    def get_connections(self,e, line_name):
        try:
            if line_name not in self.vals.keys():
                raise MetroException('Esta linea no se encontraba en la red de metro')
            elif e not in self.vals[line_name].s:
                raise MetroException('La estacion no pertenece a la linea dada')
            elif not self.vals[line_name].state[self.vals[line_name].s.index(e)]:
                raise MetroException('La estacion se encuentra cerrada desde esta linea')
            elif len(self.vals[line_name].tramo) > 0:
                if self.vals[line_name].tramo[0] < self.vals[line_name].s.index(e) and self.vals[line_name].s.index(e) < self.vals[line_name].tramo[1]:
                    raise MetroException('Hay un cierre de seccion en la linea que incluye a la parada dada')
                    
                else:
                    cnt = []
                    if e in self.tbd.keys():
                        for lin in self.tbd[e]:
                            if lin != line_name:
                                if len(self.vals[lin].tramo) > 0:
                                    if self.vals[lin].tramo[0] > self.vals[lin].s.index(e) or self.vals[lin].s.index(e) > self.vals[lin].tramo[1]:
                                        cnt.append(lin)
                                elif self.vals[lin].state[self.vals[lin].s.index(e)]:
                                    cnt.append(lin)
            else:
                cnt = []
                if e in self.tbd.keys():
                    for lin in self.tbd[e]:
                        if lin != line_name:
                            if len(self.vals[lin].tramo) > 0:
                                if self.vals[lin].tramo[0] > self.vals[lin].s.index(e) or self.vals[lin].s.index(e) > self.vals[lin].tramo[1]:
                                    cnt.append(lin)
                            elif self.vals[lin].state[self.vals[lin].s.index(e)]:
                                cnt.append(lin)
            return cnt
        except MetroException as k:
            print(k)

    def cost_origin2destination_transfer(self,start, finish):
        cost_min = 99999
        for key in self.vals.keys():
            if start in self.vals[key].s:
                if self.vals[key].state[self.vals[key].s.index(start)]:
                    if finish in self.vals[key].s:
                        if self.vals[key].state[self.vals[key].s.index(finish)]:
                            cost = self.vals[key].cost_origin2destination(start,finish)
                            print(cost)
                            if cost < cost_min:
                                cost_min = cost
                    else:
                        for e in self.vals[key].s:
                            if self.vals[key].state[self.vals[key].s.index(e)]:
                                for lin in self.get_connections(e,key):
                                    if finish in self.vals[lin].s: 
                                        if self.vals[lin].state[self.vals[lin].s.index(finish)]:
                                            cost = self.vals[key].cost_origin2destination(start,e) + \
                                                300 + self.vals[lin].cost_origin2destination(e,finish)
                                            print(cost)
                                            if cost < cost_min:
                                                cost_min = cost
        if cost_min >= 99999:
            return None
        else:
            return cost_min

    def close_station(self,line_name, e):
        try:
            if line_name not in self.vals.keys():
                raise MetroException
            if e not in self.vals[line_name].s:
                raise LineException
            pos = self.vals[line_name].s.index(e)
            self.vals[line_name].state[pos] = False
            
        except MetroException:
            print('Esta línea no se encuentra en la red de metro')
        except LineException:
            print('Esta estación no pertenece a la línea dada')
            
    def open_station(self,line_name, e):
        try:
            if line_name not in self.vals.keys():
                raise MetroException
            if e not in self.vals[line_name].s:
                raise LineException
            pos = self.vals[line_name].s.index(e)
            self.vals[line_name].state[pos] = True
            
        except MetroException:
            print('Esta linea no se encuentra en la red de metro')
        except LineException:
            print('Esta estacion no pertenece a la linea dada')
            
    def close_section(self,line_name, start, finish):
        try:
            if line_name not in self.vals.keys():
                raise MetroException
            if start not in self.vals[line_name].s or finish not in self.vals[line_name].s:
                raise LineException
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
        try:
            if line_name not in self.vals.keys():
                raise MetroException
            self.vals[line_name].tramo = []
            
        except MetroException:
            print('Esta linea no se encuentra en la red de metro')
    