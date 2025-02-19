---
title: "Práctica: Implantación de aplicaciones web Python en docker"
---

Queremos desplegar en docker la aplicación escrita en python django: **Django Publicaciones** [django_publicaciones](https://github.com/josedom24/django_publicaciones). Si quieres puedes hacer un fork para modificar los ficheros del repositorio.

Tienes que tener en cuenta los siguientes aspectos:

* La aplicación debe guardar los datos en una base de datos mariadb persistente.
* La aplicación se podrá configurar para indicar los parámetros de conexión a la base de datos: usuario, contraseña, host y base de datos.
* Durante la construcción de la imagen se deberá clonar tu fork del repositorio para copiarlo al contenedor durante su construcción.
* La aplicación deberá tener creado un usuario administrador para el acceso.

{% capture notice-text %}
1. Crea una imagen docker para poder desplegar un contenedor con la aplicación. La imagen la puedes hacer desde una imagen base o desde la imagen oficial de python.
2. Utiliza Compose para desplegar los contenedores necesarios. Configura los volúmenes que creas necesarios para que la aplicación sea persistente.
3. Una vez probada en el entorno de desarrollo, despliega la aplicación en tu VPS usando Compose y configurando el nginx como proxy inverso para acceder por nombre a la aplicación `https://djangodocker.tudominio.algo`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
