# Listas enlazadas (Linked List)

Este tipo de estructura de datos está conformada por nodos que contienen como información un dato almacenado y la referencia al siguiente nodo en la lista. Esta lista está conformada por un nodo de inicio y un nodo final que es identificado por el valor null en la referencia del siguiente nodo. Un ejemplo a continuación:

> **|nodo 1|-> |nodo 2|-> |nodo 3|-> null**  
> En este caso el nodo inicial es el nodo 1 y el nodo final el nodo 3 por su referencia null para un siguiente nodo.

## Nodo
Un nodo es el contenedor que contiene los datos y cuando estos nodos son unidos con otros, es formada la lista enlazada. Un nodo está conformado por las siguientes partes:  

1. **Datos:** La primera parte de este nodo son los datos que pueden ser un número, un carácter, una cadena de caracteres, un número flotante o cualquier tipo de dato.

2. **Referencia:** Al momento de tener un grupo de nodos unidos, esta referencia indica cuál es el siguiente nodo en la lista. Si su valor es null, indica que no hay más nodos en la lista.

## Recorriendo una lista enlazada (Traversing a Linked List)
Esto consiste en recorrer la lista enlazada para obtener los datos que tiene guardados en cada nodo y mostrarlos de una forma más amigable.

## Borrando un nodo de la lista enlazada
Para borrar un nodo existen 3 posibilidades de eliminación:  

1. **Nodo inicial:** En este caso el siguiente nodo referenciado será el nuevo nodo de inicio. Ejemplos:  

    > **|nodo 1|-> null**  
    > **empty**  
    > Al eliminar el nodo 1, la lista queda vacía.
    >
    > **|nodo 1|-> |nodo 2|-> |nodo 3|-> null**  
    > **|nodo 2|-> |nodo 3|-> null**  
    > Al eliminar el nodo 1, el nodo 2 sería el nuevo nodo inicial.

2. **Nodo intermedio:** En este caso es realizado un salto de tal forma que la referencia del nodo anterior al que se va a eliminar, tenga como referencia la del siguiente nodo del nodo a eliminar. Ejemplo:  

    > **|nodo 1|-> |nodo 2|-> |nodo 3|-> |nodo 4|-> |nodo 5|-> null**  
    > **|nodo 1|-> |nodo 2|-> |nodo 4|-> |nodo 5|-> null**  
    > Al eliminar el nodo 3, el nodo 2 tendrá como referencia al nodo 4.

3. **Nodo final:** En este caso el nodo anterior tendrá como referencia un null en lugar de tener el nodo final. Ejemplos:

    > **|nodo 1|-> null**  
    > **empty**  
    > Al eliminar el nodo 1, la lista queda vacía.
    >
    > **|nodo 1|-> |nodo 2|-> |nodo 3|-> null**  
    > **|nodo 1|-> |nodo 2|-> null**  
    > Al eliminar el nodo 3, el nodo 2 sería el nuevo nodo final.
