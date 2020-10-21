# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:01:18 2020

@author: TOSHIBA 2IN1
"""

from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
import math
from numpy import loadtxt
import numpy as np

def caso_L():
    
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa
    
    #Parametros
    L = 15.0  *m
    F = 100*KN
    qL = ((400*kg)/(m**2))
    B = 2.0 *m
    h = 3.5*m
    
    posibles_apoyos = loadtxt("coordenadas_apoyos.txt")

    importantes = []
    for i in range(7,29):
       importantes.append(list(posibles_apoyos[i]))
    
    x = []
    z = []
    for i in importantes:
        x.append(i[0])
        z.append(i[1])
    
    #p = lagrange(x,z) #Ecuacion de la recta
    
    dist_x = []
    for i in range(len(x)-1):
        d = np.abs(x[i] - x[i+1])
        dist_x.append(d)
    
    nodos_x = []
    
    for i in range(len(dist_x)):
        d = dist_x[i]
        if d > 6:
            cant = d/6
            dec,ent = math.modf(cant)
            for i in range(int(ent)):
                nodos_x.append(6.0)

            L = d - ent*6
            nodos_x.append(L)
 
        else:
            nodos_x.append(d)
 
    '''
    # Con Barras tomando si el largo es > 6 cree la cantidad de barras de 6 m de largo y una con el sobrante.
 
    ret = Reticulado()
    i = 10.0
 
    ret.agregar_nodo(10.0, 0, 100.0)
    ret.agregar_nodo(10.0, 2, 100.0)
     
    for j in range(len(nodos_x)):
        ret.agregar_nodo(i+nodos_x[j], 0, 100.0) 
        ret.agregar_nodo(i+nodos_x[j], 2, 100.0) 
    
    ret.agregar_nodo(230, 0, 100.0)
    ret.agregar_nodo(230, 2, 100.0)
 
    print(ret)
    '''
    
    # Con BARRAS DE 6 m c/u
    i = 10*m
    delta = 6*m
    ret = Reticulado()

    for j in range(37):
        ret.agregar_nodo(i + delta*j , 0, 100.0)
        ret.agregar_nodo(i + delta*j, 2, 100.0)

    ret.agregar_nodo(230.0, 0, 100.0)
    ret.agregar_nodo(230.0, 2, 100.0)

    nodos = np.arange(0, ret.Nnodos, 1)

    par = []
    impar = []

    for n in nodos:
        if n%2 == 0:
            par.append(n)
        else:
            impar.append(n)

    ret.agregar_nodo(10, 1, 150.0)
    ret.agregar_nodo(i+19*delta, 1, 150.0)
    ret.agregar_nodo(230.0, 1, 150.0)

    #, R, t, E, ρ, σy
    R = 8*cm
    t = 5*mm
    props = [R, t, 200*GPa, 7850*kg/m**3, 360*MPa]

    print(par)
    print(impar)

    for i in range(int(38/2)):
        a = par[2*i]
        b = impar[2*i+1]
        ret.agregar_barra(Barra(a, b, *props))  

    for i in range(int(38/2)):
        a = par[2*i+1]
        b = impar[2*i]
        ret.agregar_barra(Barra(a, b, *props))  

    for i in range(0,75):
        ret.agregar_barra(Barra(i, i+1, *props))  

    for i in range (0,36):
        p=i*2+1
        ret.agregar_barra(Barra(p, p+2, *props))
 
    for i in range(0,36):
        p = 2*i
        ret.agregar_barra(Barra(p, p+2, *props))
 
    
    ret.agregar_barra(Barra(0, 76, *props))
    ret.agregar_barra(Barra(76, 1, *props))
    
    ret.agregar_barra(Barra(38, 77, *props))
    ret.agregar_barra(Barra(39, 77, *props))
    
    ret.agregar_barra(Barra(78, 74, *props))
    ret.agregar_barra(Barra(78, 75, *props))
    
    ret.agregar_barra(Barra(76, 77, *props))
    ret.agregar_barra(Barra(77, 78, *props))
    
    #restricciones
    
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
     
    ret.agregar_restriccion(1, 0, 0)
    ret.agregar_restriccion(1, 1, 0)
    ret.agregar_restriccion(1, 2, 0)
    
    ret.agregar_restriccion(74, 0, 0)
    ret.agregar_restriccion(74, 1, 0)
    ret.agregar_restriccion(74, 2, 0)
        
    ret.agregar_restriccion(75, 0, 0)
    ret.agregar_restriccion(75, 1, 0)
    ret.agregar_restriccion(75, 2, 0)

    

    # Carga viva
    # nodos 0 y 1
   
    qL_A1 = -qL*(3*m**2)
     
    ret.agregar_fuerza(0, 2, qL_A1)
    ret.agregar_fuerza(1, 2, qL_A1)
    
    # nodos 2 al 71
    qL_A2 = -qL*(6*m**2)
    
    for i in range(2,72):
        ret.agregar_fuerza(i, 2, qL_A2)
        
    # nodos 72 y 73
    qL_A3 = -qL*(5*m**2)
    
    ret.agregar_fuerza(72, 2, qL_A3)
    ret.agregar_fuerza(73, 2, qL_A3)
    
    #nodos 74 y 75
    qL_A4 = -qL*(2*m**2)
    
    ret.agregar_fuerza(74, 2, qL_A4)
    ret.agregar_fuerza(75, 2, qL_A4)
    
    return ret
    
    

