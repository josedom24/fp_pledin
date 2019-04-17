---
title: "Ejercicio: Zomato API"
permalink: /lmgs/u09/zomato.html
---

**Zomato** es una página web que nos permite buscar información sobre restaurantes en diferentes ciudades del mundo. Zomato dispone de una API REST que nos da la misma información, con lo que podemos hacer un programa que trabaje con la información ofrecida por el servicio web.

La página web de Zomato es [https://www.zomato.com](https://www.zomato.com) y la documentación de la API la puedes encontrar en: [https://developers.zomato.com](https://developers.zomato.com). Tienes que obter tu key para poder trabajar con la API.

## Ejercicio 1: Listar las categorías (categories)

* Entrega una captura de pantalla donde se vea en la página de la documentación de la API como has probado la petición para obtener la lista de categorías.
* Entrega la instrucción curl que se ha generado.
* Crea un programa en python que muestre la lista de categorías.

## Ejercicio 2: Listar información sobre la ciudad de Nueva York

La información de Nueva York que hay que listar es:

1. Las colecciones (callections)
2. Los tipos de cocinas (cuisines) 
3. Los tipos de locales (establishments)

* Busca en la página web esas informaciones en la ciudad de Nueva York.
* Entrega una captura de pantalla donde se vea en la página de la documentación de la API como has probado la petición para obtener cada una de las informaciones. Indica la instrucción curl que se ha generado.
* Crea un programa en python que muestre las informaciones en la ciudad de Nueva York.


## Ejercicio 3: Listar los restaurantes de la ciudad de Nueva York

* Busca en la página web los restaurantes en la ciudad de Nueva York.
* Entrega una captura de pantalla donde se vea en la página de la documentación de la API como has probado la petición para obtener los restaurantes de la ciudad de Nueva York. Indica la instrucción curl que se ha generado.
* Crea un programa en python que muestre los restaurantes en la ciudad de Nueva York. Tienes que tener en cuenta que hay muchos restaurantes en Nueva York, lo primero que tienes que hacer es mostrar el numero total. En cada petición te devuelven 20, cada vez que muestres 20 restaurantes tendrás que preguntar si quieres ver más o salir del programa.

## Ejercicio 4: Buscar restaurantes

Realiza un programa python basado en los ejercicios anteriores que vaya introduciendo las siguientes funcionalidades:

1. Posibilitar buscar restaurantes en otra ciudad.
2. Posibilidad de que la búsqueda anterior se pueda ordenar por un criterio.
3. Buscar restaurantes en la ciudad de Nueva York,introduciendo filtros de categoría, colecciones, tipos de cocina, tipos de locales y cadenas de texto.
4. Ofrecer información detallada de un restaurante seleccionado.
5. Ofrecer el menú del día de un restaurante seleccionado.
6. Posibilitar buscar restaurantes en alguna localización.
