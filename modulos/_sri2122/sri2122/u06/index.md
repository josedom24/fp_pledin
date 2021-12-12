---
title: Protocolo HTTP (II)
---

## Gestión de peticiones y rendimiento en servidores Web

Los servidores web pueden ser configurado para manejar las peticiones de diferente forma, desde el punto de vista en que son creados y manejados los subprocesos necesarios que atienden a cada cliente conectado a este. En esta unidad vamos a explicar los MPM (Módulos de multiprocesamiento) que nos permiten configurar el servidor Web para gestionar las peticiones que llegan al servidor.

* [Gestión de peticiones en los servidores web](peticiones.html)
* [Haciendo pruebas de rendimiento con ab](ab.html)
* [Comparativa de servidores web sirviendo páginas estáticas](estatica.html)
* [Comparativa de servidores web sirviendo páginas dinámicas](dinamica.html)

¿Podemos aumentar el rendimiento de los servidores que ejecutan PHP? Vamos a ver tres posibilidades:

## Balanceo de carga con HAProxy

Un *Balanceador de Carga* es un dispositivo de hardware o software que se pone al frente de un conjunto de servidores que atienden una aplicación y, tal como su nombre lo indica, asigna o balancea las solicitudes que llegan de los clientes a los servidores usando algún algoritmo.

Podríamos configurar o nginx o apache2 para balanceaar la carga, pero vamos a usar un proframa específico de balanceo de carga como es [HAProxy](http://www.haproxy.org/).

Al balancear la carga entre más de un servidor aumentaremos el rendimiento.

* [Presentación: Introducción a HAProxy](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/haproxy.pdf)
* [Ejemplo: Introducción a HAProxy](haproxy.html)
* [Vídeo: Introducción a HAProxy](https://youtu.be/eRgWCUcvzoA)

## memcached

[Memcached](http://memcached.org) es un sistema distribuido de propósito general y que es muy usado en la actualidad por múltiples sitios web. Memcached es empleado para el almacenamiento en caché de datos u objetos en la memoria RAM, reduciendo así las necesidades de acceso a un origen de datos externo (como una base de datos o una API).

* [Optimizar WordPress con Memcached](https://www.rjcardenas.com/optimizar-wordpress-con-memcached/)


## Varnish

Podríamos configurar nginx o apache2 como proxy inverso con cache, pero vamos a usar una herramienta especicalidad que funciona como proxy inverso cache, como es [Varnish](https://varnish-cache.org/).

Varnish es un acelerador HTTP que funciona como un proxy inverso. Se sitúa por delante del servidor web, cacheando la respuesta de dicho servidor web en memoria. La próxima vez que un visitante visite la misma URL, la página será servida desde Varnish en lugar de desde el servidor web, ahorrando recursos en el backend y permitiendo más conexiones simultáneas.

* [Introducción a varnish](varnish.html)
* [Presentación Madrid DevOps (Varnish: funcionamiento, configuración y uso)](https://www.youtube.com/watch?v=A5poVWqjJrs)

## Práctica

* [Práctica: Aumento de rendimiento en servidores web](practica.html)