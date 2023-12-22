# Pilas (Stacks)

Una pila o stack es una estructura de datos que permite almacenar y recuperar datos, este consiste en apilar datos uno encima de otro, y solo se puede acceder al dato que se encuentra en la cima de la pila, es decir, el último dato que se ingresó. Este comportamiento se conoce como LIFO (Last In First Out) o FILO (First In Last Out). Un ejemplo es la pila más usada que es el historial de navegación de la pestaña del navegador, si por ejemplo abrimos 4 páginas, el historial tendría las 3 primeras páginas visitadas en la pila y la última estaría en pantalla, si usamos el botón regresar se vería de la siguiente forma:

> **1ra Página -> 2da Página -> 3ra Página -> Botón de regresar -> 3ra Página en pantalla**  
> **1ra Página -> 2da Página -> Botón de regresar -> 2da Página en pantalla**  
> **1ra Página -> Botón de regresar -> 1ra Página en pantalla**  
> **La acción anterior deja a la pila vacía -> botón de regresar queda bloqueado y la 1ra Página sigue en pantalla** 

## Operaciones de una pila
Las operaciones básicas que se pueden realizar en una pila son las siguientes:

- **Apilar (push):** Agrega un elemento a la pila.
- **Desapilar (pop):** Elimina el elemento que se encuentra en la cima de la pila.
- **Número de elementos (size):** Devuelve el número de elementos que contiene la pila.

## Recorriendo una pila (Traversing a Stack)
Para recorrer una pila se debe tener en cuenta que el último elemento que fue agregado es el primero que se debe mostrar, por lo que se debe recorrer la pila como si fuera un arreglo, pero iniciando con el último elemento.