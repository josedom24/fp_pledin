---
title: "Práctica: Servidor Web Nginx"
permalink: /serviciosgs/u03/practica_web_nginx.html
---

**(11 tareas - 10 puntos)(5 tareas obligatorias - 5 puntos)**
{: .notice--warning}
**Muestra al profesor: Tarea 4, Tarea 9**
{: .notice--warning}

{% capture notice-text %}
* **Tarea 1 (1 punto)(Obligatorio):** Crea un escenario Vagrant o utiliza una máquina del cloud con una red pública. Instala el servidor web nginx en la máquina. Modifica la página index.html que viene por defecto y accede a ella desde un navegador. Entrega una captura de pantalla accediendo a ella.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Virtual Hosting

Queremos que nuestro servidor web ofrezca dos sitios web, teniendo en cuenta lo siguiente:

1. Cada sitio web tendrá nombres distintos.
2. Cada sitio web compartirán la misma dirección IP y el mismo puerto (80).

Los dos sitios web tendrán las siguientes características:

* El nombre de dominio del primero será ``www.iesgn.org``, su directorio base será ``/srv/www/iesgn`` y contendrá una página llamada ``index.html``, donde sólo se verá una bienvenida a la página del Instituto Gonzalo Nazareno.
* En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será ``departamentos.iesgn.org``, y su directorio base será ``/srv/www/departamentos``. En este sitio sólo tendremos una página inicial ``index.html``, dando la bienvenida a la página de los departamentos del instituto.

{% capture notice-text %}
* **Tarea 2 (1 punto)(Obligatorio):** Configura la resolución estática en los clientes y muestra el acceso a cada una de las páginas.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Mapeo de URL

Cambia la configuración del sitio web ``www.iesgn.org`` para que se comporte de la siguiente forma:

{% capture notice-text %}
* **Tarea 3 (1 punto)(Obligatorio):** Cuando se entre a la dirección ``www.iesgn.org`` se redireccionará automáticamente a ``www.iesgn.org/principal``, donde se mostrará el mensaje de bienvenida. En el directorio **principal** no se permite ver la lista de los ficheros, no se permite que se siga los enlaces simbólicos y no se permite negociación de contenido. Muestra al profesor el funcionamiento.
* **Tarea 4 (1 punto)(Obligatorio):** Si accedes a la página ``www.iesgn.org/principal/documentos`` se visualizarán los documentos que hay en /srv/doc. Por lo tanto se permitirá el listado de fichero y el seguimiento de enlaces simbólicos siempre que sean a ficheros o directorios cuyo dueño sea el usuario. Muestra al profesor el funcionamiento.
* **Tarea 5 (1 punto):** En todo el host virtual se debe redefinir los mensajes de error de objeto no encontrado y no permitido. Para el ello se crearan dos ficheros html dentro del directorio error. Entrega las modificaciones necesarias en la configuración y una comprobación del buen funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Autentificación, Autorización, y Control de Acceso

{% capture notice-text %}
* **Tarea 6 (1 punto)(Obligatorio):** Añade al escenario Vagrant otra máquina conectada por una red interna al servidor. A la URL ``departamentos.iesgn.org/intranet`` sólo se debe tener acceso desde el cliente de la red local, y no se pueda acceder desde la anfitriona por la red pública. A la URL ``departamentos.iesgn.org/internet``, sin embargo, sólo se debe tener acceso desde la anfitriona por la red pública, y no desde la red local.
* **Tarea 7 (1 punto):** Autentificación básica. Limita el acceso a la URL ``departamentos.iesgn.org/secreto``. Comprueba las cabeceras de los mensajes HTTP que se intercambian entre el servidor y el cliente. ¿Cómo se manda la contraseña entre el cliente y el servidor?. Entrega una breve explicación del ejercicio.
* **Tarea 8 (1 punto):** Cómo hemos visto la autentificación básica no es segura, modifica la autentificación para que sea del tipo *digest*, y sólo sea accesible a los usuarios pertenecientes al grupo *directivos*. Comprueba las cabeceras de los mensajes HTTP que se intercambian entre el servidor y el cliente. ¿Cómo funciona esta autentificación?
* **Tarea 9 (1 punto):** Vamos a combinar el control de acceso (tarea 6) y la autentificación (tareas 7 y 8), y vamos a configurar el virtual host para que se comporte de la siguiente manera: el acceso a la URL ``departamentos.iesgn.org/secreto`` se hace forma directa desde la intranet, desde la red pública te pide la autentificación. Muestra el resultado al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## IPv6

{% capture notice-text %}
* **Tarea 10 (1 punto)**: Comprueba que el servidor web con la configuración por defecto está escuchando por el puerto 80 en ipv6. Configura la máquina para que tenga una ipv6 global. Activa el virtualhost por defecto y accede a la página principal utilizando la ipv6 global que tiene asignada.
* **Tarea 11 (1 punto)**: Configura la resolución estática para acceder a los virtualhost utilizando ipv6.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>