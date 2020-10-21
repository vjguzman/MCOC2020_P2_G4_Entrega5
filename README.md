# MCOC2020 P2-G4 Entrega5

- ¿Cual fue su diseño inicial? ¿Cuanto pesaba? ¿Como eran los factores de utilización y las deformaciones?
Para comenzar con el diseño del puente tubular de acero, y sus dimensiones por cada nodo dado en las instrucciones de la Entrega N°5, se comenzó por dar algunas medidas generales en torno al puente:
  * Las geometría de las barras: R = 20*cm ; t = 200*mm.
  * El inicio y el fin del puente (Puntos de apoyo de este), dándole un inicio en el punto 7 y su fin en el punto 28 (Viceversa). Donde en ambos puntos mencionados, existe una restricción completa, en los 3 ejes x,y,z. 
  * Las medidas de las barras, donde se tuvo que optimizar cual era la mejor distancia, para obtener la menor cantidad de cortes de barras (Que hace más fácil su trabajo físico), en este caso, para la mayor parte de las barras fue de 6 metros, mientras que la última barra (Amplificada según el eje Y=2) le dimos una medida de 4 metros, todo esto debido a la distancia de 230 metros totales por los cuales debía pasar nuestro puente. 

Para observar de mejor manera el puente a diseñar en un comienzo, es que se observa la siguiente imagen: 

![alt text](https://github.com/vjguzman/MCOC2020_P2_G4_Entrega5/blob/main/Informe/reticulado.jpeg)

A su vez, se puede analizar el peso de la estructura, y el cumplimiento de este bajo las condiciones mencionadas más arriba (Diferentes combinaciones, ante cargas vivas y muertas): 

![alt text](https://github.com/vjguzman/MCOC2020_P2_G4_Entrega5/blob/main/Informe/comprobar%20si%20cumple.jpeg)

Al observar estas, podemos notar un gran peso inicial antes de la optimización que se le realizaría al puente, con un valor cercano a los 43.227.000 Kg, lo que a simple vista puede parecer una gran magnitud, sin embargo, pensando en que es un puente echo de acero, y que debe cruzar una longitud de 230 metros, se ajusta a los requerimientos, no obstante, siempre es mejorable y optimizable para su peso final, tema que veremos en el siguiente anexo. Además de esto, podemos analizar las combinaciones que se realizaron para ver el cumplimiento de la estructura ante las fuerzas que se le aplican, que tal como se observa en la imagen, cumple ante ambas combinaciones. 

Finalmente, podemos observar la deformación máxima que siente la estructura. Para entender el contexto de estos, se tomaron en consideración en un comienzo el total de nodos de la estructura los cuales eran 113, sin embargo, es fácil notar que las deformaciones importantes deben existir en el punto donde se provocan las cargas vivas y muertas respectivamente, que serán los nodos del tablero, que en este caso son 75. Es por esto, que en la imagen que sigue, se observa únicamente la deformación máxima que siente la estructura, además del nodo donde se encuentra: 

![alt text](https://github.com/vjguzman/MCOC2020_P2_G4_Entrega5/blob/main/Informe/deformacion%20maxima.jpeg)

A partir de ella, es visible notar que las distancias que se moverá en los tres ejes el nodo adjunto. En este caso, el nodo N°59 es el que tiene esta propiedad de ser el de máxima deformación. En el eje que más se mueve, es el eje Y, con un valor de 0,59 metros, que si bien es una gran cantidad, es una cota superior a nuestro problema, que obviamente será cada vez más acotado según se disminuya el peso de la estructura, con lo que disminuirá las cargas a las que estará sujeta la estructura. Como también es visible tanto en el eje x e z, se obtienen deformaciones considerables con valores no menores a 0,26 metros. 

A su vez, y como comentario general en esta entrega, se baso el diseño del reticulado, a lo realizado a lo largo de este proyecto, es decir, la estructura general con la que se trabajó en la entrega N°4. Esto es debido a que se intentó darle una forma distinta al reticulado, sin embargo, a lo largo de los intentos, no daba un resultado debido a que no se tenían una misma cantidad de incógnitas y ecuaciones, con lo que o no había resultado o bien existían infinitas soluciones.

Finalmente, los factores de utilización para el primer modelo, es el que sigue, para ambas combinaciones de carga:

![alt text](https://github.com/vjguzman/MCOC2020_P2_G4_Entrega5/blob/main/Informe/Fu_Caso1.png)
![alt text](https://github.com/vjguzman/MCOC2020_P2_G4_Entrega5/blob/main/Informe/Fu_Caso2.png)

- Para cada cambio informe qué cambios hizo y porqué, y como cambia el peso y los factores de utilización. 

Luego de analizar los datos se logró optimizar el trabajo bajando el peso en casi un 80%, para ello se modificó el radio y el espesor de las barras siempre manteniendo las demás propiedades de las barras siempre tratando de  cumplir los requerimientos de nuestro sistema.

Los cambios realizados fueron los siguientes:
![alt text](https://github.com/vjguzman/MCOC2020_P2_G4_Entrega5/blob/main/Informe/propiedades.jpeg)
donde se ve claramente que los radios de las barras fueron cambiados, para lograr el menor peso posible.
