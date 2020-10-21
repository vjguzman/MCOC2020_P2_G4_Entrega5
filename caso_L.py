# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:01:18 2020

@author: TOSHIBA 2IN1
"""

from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from numpy import loadtxt
import numpy as np
import math

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
    qL = ((400*kg)/(m**2))

    posibles_apoyos = loadtxt("coordenadas_apoyos.txt")

    importantes = []
    for i in range(7,29):
        importantes.append(list(posibles_apoyos[i]))

    x = []
    z = []
    for i in importantes:
        x.append(i[0])
        z.append(i[1])

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


    # Con BARRAS DE 6 m c/u
    i = 10*m
    delta = 6*m
    h = 5.0

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

    # especie de arco
    for a in range(19):
        if a == 0:
            h = 115.0
        else:
            h = 115.0 + a*0.5
        ret.agregar_nodo(a + delta*a, 1, h)

    for a in range(19,37):
        h = 124 - (a-19)*0.5
        if h <= 230:
            ret.agregar_nodo(a + delta*a, 1, h)

    '''
    fig = plt.figure()
    fig.set_size_inches([12, 10], forward=True)
    ax = fig.add_subplot(111, projection='3d')
    graficar_nodos(ret, fig, opciones={})
    plt.show()
    '''

    #, R, t, E, ρ, σy
    R = 20*cm
    t = 10*mm

    props1 = [R, t, 200*GPa, 7500*kg/m**3, 420*MPa]
    props2 = [R*2, t*3, 200*GPa, 7500*kg/m**3, 420*MPa]
    props3 = [R*3, t*4, 200*GPa, 7500*kg/m**3, 420*MPa]

    for i in range(int(38/2)):
        a = par[2*i]
        b = impar[2*i+1]
        ret.agregar_barra(Barra(a, b, *props3))  

    for i in range(int(38/2)):
        a = par[2*i+1]
        b = impar[2*i]
        ret.agregar_barra(Barra(a, b, *props2))  

    for i in range(0,75):
        ret.agregar_barra(Barra(i, i+1, *props3))  

    for i in range (0,36):
        p=i*2+1
        ret.agregar_barra(Barra(p, p+2, *props2))

    for i in range(0,36):
        p = 2*i
        ret.agregar_barra(Barra(p, p+2, *props2))


    arc = np.arange(76,113,1)

    for i in range(len(arc)):
        n1 = 2*i
        n2 = 2*i+1

        ret.agregar_barra(Barra(n1, arc[i], *props1))
        ret.agregar_barra(Barra(arc[i], n2, *props1))
    
    #restricciones
    
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
     
    ret.agregar_restriccion(1, 0, 0)
    ret.agregar_restriccion(1, 1, 0)
    ret.agregar_restriccion(1, 2, 0)
    
    ret.agregar_restriccion(38, 0, 0)
    ret.agregar_restriccion(38, 1, 0)
    ret.agregar_restriccion(38, 2, 0)
        
    ret.agregar_restriccion(39, 0, 0)
    ret.agregar_restriccion(39, 1, 0)
    ret.agregar_restriccion(39, 2, 0)

    ret.agregar_restriccion(74, 0, 0)
    ret.agregar_restriccion(74, 1, 0)
    ret.agregar_restriccion(74, 2, 0)
        
    ret.agregar_restriccion(75, 0, 0)
    ret.agregar_restriccion(75, 1, 0)
    ret.agregar_restriccion(75, 2, 0)

    for i in arc:
        ret.agregar_restriccion(i, 0, 0)
        ret.agregar_restriccion(i, 1, 0)
        ret.agregar_restriccion(i, 2, 0)

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
    
