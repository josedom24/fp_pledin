---
title: "Práctica: Servidor Web Nginx"
permalink: /serviciosgs/u03/practica_web_nginx.html
---

{% capture notice-text %}
* **Tarea 1 (1 punto)(Obligatorio):** Crea una máquina del cloud con una red pública. Añade la clave pública del profesor a la máquina. Instala el servidor web nginx en la máquina. Modifica la página index.html que viene por defecto y accede a ella desde un navegador. 

* Entrega la ip flotante de la máquina para que el profesor pueda acceder a ella.
* Entrega una captura de pantalla accediendo a ella.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Virtual Hosting

Queremos que nuestro servidor web ofrezca dos sitios web, teniendo en cuenta lo siguiente:

1. Cada sitio web tendrá nombres distintos.
2. Cada sitio web compartirán la misma dirección IP y el mismo puerto (80).

Los dos sitios web tendrán las siguientes características:

* El nombre de dominio del primero será ``www.iesgn.org``, su directorio base será ``/srv/www/iesgn`` y contendrá una página llamada ``index.html``, donde sólo se verá una bienvenida a la página del Instituto Gonzalo Nazareno.
* En el segundo sitio vamos a crear una página donde se pondrán noticias por parte de los departamento, el nombre de este sitio será ``departamentos.iesgn.org``, y su directorio base será ``/srv/www/departamentos``. En este sitio sólo tendremos una página inicial ``index.html``, dando la bienvenida a la página de los departamentos del instituto.

{% capture notice-text %}
* **Tarea 2 (2 punto)(Obligatorio):** Configura la resolución estática en los clientes y muestra el acceso a cada una de las páginas.
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
* **Tarea 6 (1 punto)(Obligatorio):** Añade al escenario otra máquina conectada por una red interna al servidor. A la URL ``departamentos.iesgn.org/intranet`` sólo se debe tener acceso desde el cliente de la red local, y no se pueda acceder desde la anfitriona por la red pública. A la URL ``departamentos.iesgn.org/internet``, sin embargo, sólo se debe tener acceso desde la anfitriona por la red pública, y no desde la red local.
* **Tarea 7 (1 punto):** Autentificación básica. Limita el acceso a la URL ``departamentos.iesgn.org/secreto``. Comprueba las cabeceras de los mensajes HTTP que se intercambian entre el servidor y el cliente. 
* **Tarea 8 (2 punto):** Vamos a combinar el control de acceso (tarea 6) y la autentificación (tarea 7), y vamos a configurar el virtual host para que se comporte de la siguiente manera: el acceso a la URL ``departamentos.iesgn.org/secreto`` se hace forma directa desde la intranet, desde la red pública te pide la autentificación. Muestra el resultado al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

