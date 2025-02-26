---
title: "Práctica (2 / 2): Servidores Web, Base de Datos y DNS en nuestros escenario de OpenStack"
---

## Servidor DNS

1. Será necesario realizar consultas desde el exterior (ya que vamos a hacer una delegación del subdominio). Por lo tanto tienes que realizar las siguientes tareas:
    * Determina la regla DNAT en `luffy` para que podamos hacer consultas DNS desde el exterior. Prueba a hacer una consulta desde tu anfitrión usando la IP flotante de `luffy`.
    * Crea una tercera vista para cuando se realizan consultas desde el exterior.
2. Indica al profesor el nombre de tu dominio para que pueda realizar la delegación en el servidor DNS principal `dns.gonzalonazareno.org`. Ahora prueba, desde tu anfitrión a resolver tus nombres pero preguntando al DNS de nuestra red (`172.22.0.1`).
3. Queremos que el servidor DNS que has configurado también pueda resolver los nombres de los DNS de los compañeros. Para ello lo vamos a configurar como **servidor DNS forward/caché**, de tal manera que las consultas la realizará sobre nuestro servidor `172.22.0.1`. Para configurar el servidor como forwarder hay que modificar el parámetro en el fichero `named.conf.options`.

## Servidor Web

En `zoro` vamos a instalar un servidor web apache. Configura el servidor para que sea capaz de ejecutar código php. Investiga las reglas DNAT de cortafuegos que tienes que configurar en `luffy` para, cuando accedemos a la IP flotante/pública se acceda al servidor web. Instala un CMS WordPress que debe ser accesible con el nombre `www.tu_nombre.gonzalonazareno.org`.

## Servidor de base de datos

En `sanji` vamos a instalar un servidor de base de datos mariadb (`bd.tu_nombre.gonzalonazareno.org`). A este servidor de base de datos se debe permitir el acceso desde todas las máquinas del escenario.

{% capture notice-text %}
## Entrega

1. Entrega la definición de la nueva vista.
2. Entrega el resultado de las siguientes consultas desde la máquina anfitriona, preguntando a nuestro servidor DNS `172.22.0.1`:
    * El servidor DNS con autoridad sobre la zona del dominio `tu_nombre.gonzalonazareno.org`.
    * La dirección IP de `luffy`.
    * Una resolución de www.
3. Realiza una consulta a tu DNS preguntando por el nombre de un dns de un compañero, para comprobar si se está comportando como DNS fordward/caché.
4. Entrega el contenido del fichero de configuración de Wordpress (`wp-config.php`) para comprobar el nombre de la base de datos que has configurado.
5. Entrega una captura de pantalla accediendo a `www.tunombre.gonzalonazareno.org` donde se vea el Wordpress.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
