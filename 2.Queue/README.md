# Colas (Queue)
La cola es una estructura de datos que se caracteriza por ser una secuencia de elementos en la que la operación de inserción push se realiza por un extremo y la operación de extracción pop por el otro. También se le llama estructura FIFO (del inglés First In First Out), debido a que el primer elemento en entrar será también el primero en salir. Un ejemplo de cola es la cola de una taquilla, en la cual el primero en llegar será el primero en ser atendido como se observa a continuación:

> **|3ra Persona|, |2da Persona|, |1ra Persona| -> Taquilla -> |1ra Persona es atendida|**  
> **|3ra Persona|, |2da Persona| -> Taquilla -> |2da Persona es atendida|**  
> **|3ra Persona| -> Taquilla -> |3ra Persona es atendida|**  
> **Nadie queda en la cola -> Taquilla -> Nadie se puede atender**  

## Operaciones de una cola
Las operaciones básicas que se pueden realizar en una cola son las siguientes:

- **Encolar (enqueue):** Agrega un elemento al final de la cola.
- **Desencolar (dequeue):** Elimina el elemento que llegó primero a la cola.
- **Número de elementos (size):** Devuelve el número de elementos que contiene la cola.

## Recorriendo una cola (Traversing a Queue)
Para recorrer una cola se debe tener en cuenta que la cola es una estructura de datos lineal, por lo que se puede recorrer de la misma forma que una lista enlazada o un arreglo.