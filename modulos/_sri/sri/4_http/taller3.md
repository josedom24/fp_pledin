---
title: "Taller 3: Introducción a proxy inverso"
---

## ¿Qué vas a aprender en este taller?

* Vamos a aprender el concepto de proxy inverso.
* Vamos a montar un escenario usando Vagrant y Ansible.
* Vamos a configurar Apache2 y nginx como proxy inverso.
* Vamos a configurar el proxy inverso para que sea capaz de resolver las redirecciones.

## ¿Qué tienes que hacer?

1. Vamos a usar los ficheros del directorio `taller3` del repositorio [taller_http](https://github.com/josedom24/taller_http) donde encontrarás un escenario vagrant para configurar el siguiente escenario:

	* Una máquina `proxy` conectada al exterior y a una red interna.
    * Una máquina `servidorweb` conectada a la red interna (suponemos que no vamos a usar la red de mantenimiento para acceder a ella).

2. Tenemos a nuestra disposición un playbook de ansible que va a instalar un servidor web apache2 en la máquina `servidorweb` y puede crear una lista de virtualhost. Para configurar los virtualhost tienes que modificar la lista de diccionarios llamada `virtualhosts` que encuentras en el fichero `grups_vars/all`.

    Configura esa variable para crear dos virtualhosts:

    * Uno en el fichero `vhost1.conf` que se acceda con el nombre `interno.example1.org`, cuyo DocumentRoot sea `/var/www/example1`.
    * Otro en el fichero `vhost2.conf` que se acceda con el nombre `interno.example2.org`, cuyo DocumentRoot sea `/var/www/example2`.
    
    Ejecuta el playbook de ansible para configurar el `servidorweb`.
3. Instala un servidor web apache2 en la máquina `proxy`. Vamos a configurar el proxy para acceder a las páginas del `servidorweb`: A la primera página con la URL `www.app1.org` y a la segunda página con la URL `www.app2.org`. Realiza la configuración para que las redirecciones funcionen: al acceder a `http://www.app1.org/directorio` se debe realizar una redirección al directorio `nuevodirectorio`. 
4. Modifica la configuración del proxy para acceder a las páginas web con las siguientes URL: `www.servidor.org/app1` y `www.servidor.org/app2`. Debe seguir funcionando las redirecciones.
5. Desisntala apache2 e instala nginx.
6. Configura nginx como proxy inverso para acceder a las páginas del `servidorweb`: A la primera página con la URL `www.app1.org` y a la segunda página con la URL `www.app2.org`.
7. Modifica la configuración del proxy para acceder a las páginas web con las siguientes URL: `www.servidor.org/app1` y `www.servidor.org/app2`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Con apache2, pantallazos donde se compruebe el acceso a las dos páginas web: `www.app1.org` y `www.app2.org`.
2. Quita la directiva `ProxyPassReverse` y comprueba que no se sigue la redirección. Realiza una petición HEAD con `curl` a `http://www.app1.org/directorio`. ¿Qué cabecera tienes que comprobar para asegurar que la redirección no funciona?
3. Con apache2, pantallazos donde se compruebe el acceso a las dos páginas web: `www.servidor.org/app1` y `www.servidor.org/app2`.
4. Con nginx, pantallazos donde se compruebe el acceso a las dos páginas web: `www.app1.org` y `www.app2.org`.
5. Con nginx, pantallazos donde se compruebe el acceso a las dos páginas web: `www.servidor.org/app1` y `www.servidor.org/app2`.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

