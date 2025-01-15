---
title: Servidores Web, Base de Datos y DNS en nuestros escenario de OpenStack
---



2. Será necesario realizar consultas desde el exterior (ya que vamos a hacer una delegación del subdominio). 3. 
4. 



{% capture notice-text %}
## Entrega

1. Entrega la configuración DNS de cada máquina.
2. Entrega la definición de las vistas y de las zonas.
3. Entrega el resultado de las siguientes consultas desde una máquina interna a nuestra red y otro externo:
    * El servidor DNS con autoridad sobre la zona del dominio `tu_nombre.gonzalonazareno.org`.
    * La dirección IP de `luffy`.
    * Una resolución de www.
    * Una resolución de bd.
    * Un resolución inversa de IP fija en cada una de las redes. (Esta consulta sólo funcionará desde una máquina interna).
4. Realiza una consulta a tu DNS preguntando por el nombre de un dns de un compañero, para comprobar si se está comportando como DNS fordward/caché.
5. Desde `luffy` entrega la salida de `ping hela` y `ssh loki` para comprobar que funcionan los nombres cortos en la resolución.
6. Entrega el contenido del fichero de configuración de Wordpress (`wp-config.php`) para comprobar el nombre de la base de datos que has configurado.
7. Entrega una captura de pantalla accediendo a `www.tunombre.gonzalonazareno.org` donde se vea el Wordpress.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
