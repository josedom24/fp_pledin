---
title: "Clase 4: Introducción a proxy inverso"
---

## ¿Qué vas a aprender en esta clase?

* Vamos a aprender el concepto de proxy inverso.
* Vamos a montar un escenario usando opentofu y ansible.
* Vamos a configurar Apache2 y nginx como proxy inverso.
* Vamos a configurar el proxy inverso para que sea capaz de resolver las redirecciones.

## ¿Qué tienes que hacer?

1. Vamos a a usar el **escenario2** del repositorio [opentofu-libvirt](https://github.com/josedom24/opentofu-libvirt/tree/main) para montar el siguiente escenario:

	* Una máquina `proxy` que esta conectada al exterior por una red NAT y a una red interna muy aislada (dirección `10.0.0.1`).
    * Una máquina `backend` que tendrá un servidor web interno, conectada a la red interna muy aislada (dirección `10.0.0.2`). También está conectado a la red NAT, pero sólo para poder configurarla con la receta ansible. 

2. Tenemos a nuestra disposición un playbook de ansible que va a instalar un servidor web apache2 en la máquina `backend` y puede crear una lista de virtualhost. Para configurar los virtualhost tienes que modificar la lista de diccionarios llamada `virtualhosts` que encuentras en el fichero `gruops_vars/all`.

    Configura esa variable para crear dos virtualhosts:

    * Uno en el fichero `vhost1.conf` que se acceda con el nombre `interno.example1.org`, cuyo DocumentRoot sea `/var/www/example1`.
    * Otro en el fichero `vhost2.conf` que se acceda con el nombre `interno.example2.org`, cuyo DocumentRoot sea `/var/www/example2`.
    
    Además tienes que ir indicar n el inventario la dirección IP del servidor `backend`.

    Crea el escenario y ejecuta el playbook de ansible para configurar el `backend` (recuerda que tienes que poner en el inventario la ip del servidor `backend`).
3. Instala un servidor web apache2 en la máquina `proxy`. Vamos a configurar el proxy para acceder a las páginas del `backend`: A la primera página con la URL `www.app1.org` y a la segunda página con la URL `www.app2.org`. Recuerda que debes añadir en la resolución estática del `proxy` los nombres con los que se accede internamente a las práginas web. Cuidado con la directiva `ProxyPreserveHost On`, en este ejercicio el nombre de los host virtuales del `backend` son distintos a los que usamos accediendo al proxy inverso.
4. Realiza la configuración para que las redirecciones funcionen: al acceder a `http://www.app1.org/directorio` se debe realizar una redirección al directorio `nuevodirectorio`. 
5. Modifica la configuración del proxy para acceder a las páginas web con las siguientes URL: `www.servidor.org/app1` y `www.servidor.org/app2`. Debe seguir funcionando las redirecciones.
6. Desisntala apache2 e instala nginx en el `proxy`.
7. Configura nginx como proxy inverso para acceder a las páginas del `backend`: A la primera página con la URL `www.app1.org` y a la segunda página con la URL `www.app2.org`.
8. Modifica la configuración del proxy para acceder a las páginas web con las siguientes URL: `www.servidor.org/app1` y `www.servidor.org/app2`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Con apache2, pantallazos donde se compruebe el acceso a las dos páginas web: `www.app1.org` y `www.app2.org`.
2. Quita la directiva `ProxyPassReverse` y comprueba que no se sigue la redirección. Realiza una petición HEAD con `curl` a `http://www.app1.org/directorio`. ¿Qué cabecera tienes que comprobar para asegurar que la redirección no funciona?
3. Con apache2, pantallazos donde se compruebe el acceso a las dos páginas web: `www.servidor.org/app1` y `www.servidor.org/app2`.
4. Con nginx, pantallazos donde se compruebe el acceso a las dos páginas web: `www.app1.org` y `www.app2.org`.
5. Con nginx, pantallazos donde se compruebe el acceso a las dos páginas web: `www.servidor.org/app1` y `www.servidor.org/app2`.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


