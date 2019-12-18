---
title: "Práctica: Ejecución de scripts PHP y Python. Rendimiento"
permalink: /serviciosgs/u06/practica.html
---

(9 tareas - 20 puntos)(8 tareas obligatorias - 15 puntos)
{: .notice--warning}
    
## Ejecución de scripts PHP

Vamos a comparar el rendimiento de distintas configuraciones de servidores web sirviendo páginas dinámicas programadas con PHP, en concreto vamos a servir un CMS Wordpress.

Las configuraciones que vamos a realizar son las siguientes:
	
* Módulo php5-apache2
* PHP-FPM (socket unix) + apache2
* PHP-FPM (socket TCP) + apache2
* PHP-FPM (socket unix) + nginx 
* PHP-FPM (socket TCP) + nginx 

{% capture notice-text %}
### Apache2

* **Tarea 1 (1 punto)**: Documenta la instalación del módulo php de apache2. Muestra wordpress funcionando con el módulo php de apache2. Realiza una comprobación de que, efectivamente, se está usando el módulo php.
* **Tarea 2 (1 punto)**: Documenta la instalación y configuración de FPM-PHP y apache2 (escuchando en un socket UNIX) con el módulo de multiprocesamiento event. Muestra wordpress funcionando con FPM-PHP. Realiza una comprobación de que, efectivamente, se está usando FPM-PHP.
* **Tarea 3 (1 punto)**: Cambia la configuración anterior para que PHP-FPM escuche en un socket CP.
    
### nginx

* **Tarea 4 (1 punto)**: Documenta la instalación y configuración de PHP-FPM y nginx (escuchando en un socket UNIX) con el módulo de multiprocesamiento event. Muestra wordpress funcionando con PHP-FPM. Realiza una comprobación de que, efectivamente, se está usando PHP-FPM.
* **Tarea 5 (1 punto)**: Cambia la configuración anterior para que PHP-FPM escuche en un socket TCP.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Rendimiento

Después de hacer varias pruebas de rendimiento con un número variable de peticiones concurrentes (1, 10, 25, 50, 75, 100, 250, 500, 1000). Los resultados obtenidos son los siguientes:

![php](img/php1.png)

Podemos determinar que la opción que nos ofrece más rendimiento es nginx + fpm_php (socket unix).

A partir de esa configuración vamos a intentar aumentar el rendimiento de nuestro servidor.


## Aumento de rendimiento en la ejecución de scripts PHP

{% capture notice-text %}

* **Tarea 7 (2 puntos)**: Añade a la configuración **ganadora del punto anterior** memcached. Documenta la instalación y configuración memcached. Recuerda que para que Wordpress utilice memcached le tenemos que instalar un plugin. Muestra las estadísticas de memcached después de acceder varias veces a wordpress para comprobar que esa funcionando.
* **Tarea 8 (3 puntos)**: Configura un proxy inverso - caché Varnish escuchando en el puerto 80 y que se comunica con el servidor web por el puerto 8080. Entrega y muestra una comprobación de que varnish está funcionando con la nueva configuración.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Rendimiento

Veamos las tres opciones que hemos configurado y veamos los resultados después del estudio de rendimiento:

![php](img/php2.png)

Podemos observar como el uso de varnishd aumenta muy significativamente el rendimiento de nuestro servidor.

