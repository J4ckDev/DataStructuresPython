# Listas

Una lista es una estructura de datos que está conformada por un conjunto de elementos que pueden ser de cualquier tipo de dato o de un tipo de dato específico. Cada elemento de la lista está identificado por un índice que indica su posición en la lista. El primer elemento de la lista tiene como índice el valor 0, el segundo el valor 1 y así sucesivamente.  
Para acceder a un elemento de la lista es utilizado el índice del elemento. En el caso de Python para acceder a un elemento de la lista se utiliza el nombre de la lista seguido de corchetes que contienen el índice del elemento. Ej. lista[índice].

## Funciones

En el caso de Python, estas son las funciones más utilizadas para trabajar con listas:

- **sort()**: Ordena los elementos de la lista de menor a mayor.
- **reverse()**: Invierte el orden de los elementos de la lista.
- **append(nuevo_elemento)**: Agrega un nuevo elemento al final de la lista.
- **extend(array_o_string)**: Agrega los elementos de una lista a otra lista.
- **insert(índice, elemento)**: Agrega un elemento en una posición específica de la lista.
- **remove(elemento)**: Elimina un elemento de la lista.
- **clear()**: Elimina todos los elementos de la lista.
- **__contains__(elemento)**: Devuelve True si el elemento se encuentra en la lista.
- **index(elemento)**: Devuelve el índice del elemento en la lista si existe, sino retorna un error.
- **count(elemento)**: Devuelve la cantidad de veces que se repite el elemento en la lista.
- **pop(índice)**: Elimina el elemento de la lista que se encuentra en la posición indicada por el índice y lo retorna.

## Lista anidada (Nested List)
Una lista aniada es una lista que tiene como elementos a otras listas. Para acceder a los elementos de una lista anidada se utiliza el índice de la lista y el índice del elemento de la lista anidada. En el caso de Python se utiliza el nombre de la lista seguido de corchetes que contienen el índice de la lista anidada y el índice del elemento de la lista anidada. Ej. lista[índice_lista_anidada][índice_elemento_lista_anidada].

# Tuplas

Una tupla funciona de la misma forma que una lista, con la diferencia que es inmutable, es decir, no se puede modificar una vez creada. Para crear una tupla se utiliza paréntesis en lugar de corchetes. Ej. tupla = (1, 2, 3, 4, 5).

## Funciones
En el caso de Python las tuplas solo tienen las siguientes funciones:

- **count(elemento)**: Devuelve la cantidad de veces que se repite el elemento en la tupla.
- **index(elemento)**: Devuelve el índice del elemento en la tupla si existe, sino retorna un error.
- **__contains__(elemento)**: Devuelve True si el elemento se encuentra en la tupla.

## Objetos mutables en una tupla
Aunque una tupla es inmutable, los objetos que contiene pueden ser mutables. Por ejemplo, una tupla puede contener una lista y esta lista puede ser modificada. Ej. tupla = (1, 2, 3, [4, 5, 6]). En este caso la tupla no puede ser modificada, pero la lista que contiene si puede ser modificada.