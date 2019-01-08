---
title: "Aumento de rendimiento en servidores web"
permalink: /serviciosgs/u06/aumento_rendimiento.html
---

## Memcached

[Memcached](http://memcached.org/) es un sistema distribuido de propósito general y que es muy usado en la actualidad por múltiples sitios web. Memcached es empleado para el almacenamiento en caché de datos u objetos en la memoria RAM, reduciendo así las necesidades de acceso a un origen de datos externo (como una base de datos o una API).

* [Manual de instalación de memcached](http://www.pontikis.net/blog/install-memcached-php-debian)
* [Como utilizar Memcached con WordPress](https://raiolanetworks.es/blog/como-utilizar-memcached-con-wordpress/)
* [Memcached para optimizar WordPress](https://raiolanetworks.es/blog/memcached/#memcached_para_optimizar_wordpress)

## Varnish

Varnish es un acelerador HTTP que funciona como un proxy inverso. Se sitúa por delante del servidor web, cacheando la respuesta de dicho servidor web en memoria. La próxima vez que un visitante visite la misma URL, la página será servida desde Varnish en lugar de desde el servidor web, ahorrando recursos en el backend y permitiendo más conexiones simultáneas.

* [Introducción a varnish](varnish.html)

Para seguir profundizando:

* [Presentación Madrid DevOps (Varnish: funcionamiento, configuración y uso)](http://www.youtube.com/watch?v=A5poVWqjJrs)
* [How to: Varnish listen port 80 with systemd](http://deshack.net/how-to-varnish-listen-port-80-systemd/)
* [http://kontsu.wordpress.com/2012/10/10/apache-2-performance-boost-with-varnish-yslow/](http://kontsu.wordpress.com/2012/10/10/apache-2-performance-boost-with-varnish-yslow/)
 * [Put Varnish on port 80](http://www.varnish-cache.org/docs/trunk/tutorial/putting_varnish_on_port_80.html)

