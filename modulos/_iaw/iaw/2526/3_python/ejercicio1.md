---
title: "Ejercicio 1: Introducción a aplicaciones web python django"
---

Siguiendo los apuntes sobre [Introducción a Django](django.html), vamos a hacer funcionar la siguiente aplicación, realizando los siguientes pasos.

1. Clona el repositorio de la aplicación [guestbook_django](https://github.com/josedom24/guestbook_django).
2. `guestbook_django` es una aplicación escrita en python django. Es una aplicación donde podemos dejar guardadas mensajes en un "libro de visita". Los mensajes se van a guardar en una base de datos SQLite.
3. Crea un entorno virtual donde vamos a instalar las librerías necesarias para que funcione nuestra aplicación (fichero `requirements.txt`).
4. Crea las migraciones del proyecto y ejecuta la migración para crear las tablas necesarias para la aplicación en la base de datos.
5. Ejecuta el servidor web de desarrollo y accede a la URL para acceder a la aplicación. Prueba a poner algún mensaje.
6. Mira los ficheros más importantes de los que te habla la teoría que has estudiado.
7. Crea un superusuario de la aplicación y accede a la zona de administración. Comprueba que puedes gestionar las tablas de la base de datos.