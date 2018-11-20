---
title: "Práctica: Configuración de servidores GNU/Linux"
permalink: /serviciosgs/u04/practica_linux_server.html
---    

**(13 tareas - 20 puntos)(6 tareas obligatorias - 7 puntos)**
{: .notice--warning}

{% capture notice-text %}
**Objetivo**

El objetivo de esta práctica es montar una infraestructura de servicios que se mantenga en el tiempo y que nos sirva para montar servicios y aplicaciones en los distintos módulos durante el curso. Esta práctica la tenéis que realizar en la infraestructura de máquinas que hemos creado en el cloud para todas los módulos. En cualquier momento del curso los servicios que instalemos en esta práctica deben estar funcionando de manera adecuada.

* Servidor1: rajoy (Debian)
* Servidor2: aznar (Ubuntu)
* Servidor3: zapatero (CentOs)
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

{% capture notice-text %}
Ejemplo de nombres, suponiendo que mi nombre de dominio va a ser ``josedom.gonzalonazareno.org``:

Los nombres de los equipos van a ser:

* ``aznar.josedom.gonzalonazareno.org``
* ``rajoy.josedom.gonzalonazareno.org``
* ``zapatero.josedom.gonzalonazareno.org``

Vamos a instalar los siguientes servicios:

* El servidor DNS va a estar instalado en ``rajoy.josedom.gonzalonazareno.org``
* El servidor web va a estar instalado en ``zapatero.josedom.gonzalonazareno.org``, y vamos a tener dos páginas webs:
       
    * ``www.josedom.gonzalonazareno.org``
    * ``informatica.josedom.gonzalonazareno.org``

* El servidor de base de datos va a estar instalado en ``aznar.josedom.gonzalonazareno.org``
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Servidor DNS

Vamos a instalar un servidor dns que nos permita gestionar la resolución directa e inversa de nuestros nombres. Cada alumno va a poseer un servidor dns con autoridad sobre un subdominio de nuestro dominio principal *gonzalonazareno.org*, que se llamará ``tu_nombre.gonzalonazareno.org``.

Indica al profesor el nombre de tu dominio para que pueda realizar la delegación en el servidor DNS principal *papion*.
{: .notice--warning}

### Instalación del servidor DNS

El servidor DNS se va a instalar en el servidor1 (rajoy). Y en un primer momento se configurará de la siguiente manera:

* El servidor DNS se llama ``rajoy.tu_nombre.gonzalonazareno.org`` y va a ser el servidor con autoridad para la zona ``tu_nombre.gonzalonazareno.org``.
* El servidor debe resolver el nombre de los tres servidores.
* Se debe configurar las zonas de resolución inversa.

{% capture notice-text %}
* Debes determinar si la resolución directa se hace con dirección ip fijas o flotantes del cloud depediendo del servicio que se este prestando.
* Debes considerar la posibilidad de hacer dos zonas de resolución inversa para resolver ip fijas o flotantes del cloud.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

{% capture notice-text %}
* **Tarea 1 (1 puntos):** Comprueba que los servidores tienen configurados el nuevo nombre de dominio de forma adecuada después de volver a reiniciar el servidor (o tomar una nueva configuración DHCP). Para que el servidor tenga el FQDN debes terner configurado de forma correcta el parámetro `domain` en el fichero ``/etc/resolv.conf``, además debemos evitar que este fichero se sobreescriba con los datos que manda el servidor DHCP de OpenStack. Documenta la configuración que has tenido que modificar y muestra el contenido del fichero ``/etc/resolv.conf`` y la salida del comando ``hostname -f`` después de un reincio..
* **Tarea 2 (2 puntos)(Obligatorio):** Entrega el resultado de las siguientes consultas :

    * El servidor DNS con autoridad sobre la zona del dominio ``tu_nombre.gonzalonazareno.org``
    * La dirección IP de los tres servidores
    * Un resolución inversa de IP fija, y otra resolución inversa de IP flotante.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Nos gustaría poder dar de alta nuevos nombres en el servidor DNS. Para ello vas a crear un scipt en python que nos permita añadir o borrar registros en las zonas de nuestro servidor.

El script se debe llamar ``gestionDNS.py`` y recibe cutro parámetros:

* ``-a`` o ``-b``: Si recibe ``-a`` añadirá un nuevo nombre, si recibe ``-b`` borrará el nombre que ha recibido.
* ``-dir`` o ``-alias``, si recibe ``-dir`` va a crear un registro tipo A, si recibe ``-alias`` va a crear un registro CNAME
* El nombre de la máquina para añadir o borrar
* El nombre del alias o la dirección ip: Si has usuado la opción ``-dir`` recibirá una ip y si has usuado ``-alias`` recibirá el nombre de la máquina a la que le vamos a hacer el alias. Si has utilizado -b no teendrá este parámetro.

**Ejemplos**

Crear el registro -> smtp    A    192.168.4.1

    gestionDNS.py -a -dir smtp 192.168.4.1

Crear el registro -> correo      CNAME    smtp	

    gestionDNS.py -a -alias correo smtp

Borrar el último registro

    gestionDNS.py -b correo



Todos los registros creados o borrados pertenecen a las zonas ``tu_nombre.gonzalonazareno.org``. Se debe modificar la zona inversa en los casos necesarios. El script debe reiniciar el servidor bind9.

{% capture notice-text %}
* **Tarea 3 (3 puntos):** Entrega el repositorio github donde has desarrollado el script y realiza un ejemplo al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Servidor Web

En nuestro servidor3 (zapatero) vamos a instalar un servidor Web apache2 con las siguientes características.

{% capture notice-text %}
* **Tarea 4 (1 punto)(Obligatorio):** Nuestro servidor va  a tener dos hosts virtuales: ``www.tu_nombre.gonzalonazareno.org`` y ``informatica.tu_nombre.gonzalonazareno.org``. Explica los pasos fundamentales para realizar los dos virtual hosts.
* **Tarea 5 (1 punto):** Comenta los cambios en el servidor DNS para de dar de alta los dos nuevos nombres.
* **Tarea 6 (1 punto)(Obligatorio):** La página ``www.tu_nombre.gonzalonazareno.org`` va a ser la página principal, busca una plantilla html, modifícala un poco y desplégala en el primer virtual host. 
* **Tarea 7 (1 punto)(Obligatorio):** Por seguridad, en la página ``www.tu_nombre.gonzalonazareno.org``, no se permite que se sigan enlaces simbólicos, no se permite negociación de contenidos, no se permite visualizar la lista de ficheros y no se permite usar ficheros .htaccess. Entrega la modificaciones en la configuración necesarias.
* **Tarea 8 (1 punto)(Obligatorio):** La página ``informatica.tu_nombre.gonzalonazareno.org`` es una página relacionada con el mundo de la informática, busca una plantilla html, modificarla un poco y desplegala en el primer virtual host. La página se guardará en  un directorio llamado `plataforma`. Por lo tanto si accedemos a ``informatica.tu_nombre.gonzalonazareno.org`` se deberá redirigir automáticamente a ``informatica.tu_nombre.gonzalonazareno.org/plataforma``. 
* **Tarea 9 (2 puntos):** Para llevar una estadística de visitas y accesos instala la aplicación **awstats** en el servidor. Configura el cron para que la estadistíca se vaya actualizando. Debes realizar dos estadísticas, una para cada host virtual.
* **Tarea 10 (1 punto):** **GoAccess** es otro analizador de logs, configura esta herramienta para obtener las estadísticas de tus sitios virtuales.
* **Tarea 11 (3 puntos):** En el directorio ``/srv/isos`` tenemos una colección de imágenes isos, queremos acceder a ella en la dirección ``informatica.tu_nombre.gonzalonazareno.org/isos``. Esta dirección debe ser sólo accesible desde la intranet, si accedemos desde fuera tenemos que autentificarnos (digest) con un usuario.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Servidor de Base de Datos

En nuestro servidor2 (aznar) vamos a instalar un servidor de base de datos mysql.

{% capture notice-text %}
* **Tarea 12 (1 punto)(Obligatorio):** Configura el servidor para que sea accesible por los equipos de la red local. Muestra al profesor una conexión a la base de datos desde el servidor3 (zapatero).
* **Tarea 13 (2 puntos):** Instala en el servidor3 (zapatero) la aplicación phpmyadmin que nos permite gestionar las bases de datos de nuestro servidor. Esta aplicación sólo será accesible desde la URL ``www.tu_nombre.gonzalonazareno.org/basededatos``. Muestra el acceso al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>