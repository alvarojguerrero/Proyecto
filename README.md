# Proyecto

## El juego de la Vida

En el año 1970, el matemático inglés John Horton Conway creó un juego matemático de simulación que consistía en un universo cuadriculado donde es posible determinar un estado inicial y luego hacerlo correr para observar su evolución. Lo llamó _El Juego de la Vida_ y es en realidad un autómata celular, un modelo matemático para un sistema dinámico que va evolucionando en pasos discretos.

## Desarrollo del Juego

El juego de la vida se despliega sobre un tablero cuadriculado o rejilla que en principio se presupone infinito. Cada casilla del tablero contendra una celular que puede estar viva (color verde) o muerta (color gris). De esta forma cada celula en el tablero estará rodeada a su vez por otras 8 celulas. 

**Este es un juego de cero jugadores, lo que significa que no es necesaria la interacción mas que por la configuración o disposicion inicial del tablero**

El juego se desarrolla por iteraciones: en cada iteracion se examinan todas las casillas del tablero y se calcula cual será su estado en el siguiente iteracion dadas las siguentes reglas: 

### Reglas

+ Si una celula está viva y el número de celulas vivas adyacentes es menor que 2, la célula muere por aislamiento.

+ Si una celula está viva y el número de células vivas que la rodean es mayor que 3, la célula muere por superpoblación.

+ Una celula muerta que tenga 3 (y sólo 3) células vivas adyacentes revive en la siguiente iteracion.
