---
title: "Práctica : Instalación de un servidor LEMP en nuestra VPS"
---

## Instalación ( 1 punto)

1. Instala un servidor web nginx
2. Instala un servidor de base de datos MariaDB. Ejecuta el programa necesario para asegurar el servicio, ya que lo vamos a tener corriendo en el entorno de producción.
3. Instala un servidor de aplicaciones PHP-FPM.

## VirtualHosting (1 punto)

4. Crea un virtualhost al que vamos acceder con el nombre `www.tudominio.algo` Recuerda que tendrás que crear un registro CNAME en la zona DNS.
5. Cuando se acceda al virtualhost por defecto `default` nos tiene que redirigir al virtualhost que hemos creado en el punto anterior.

## Mapeo de URL (2 puntos)

6. Cuando se acceda a `www.tudominio.algo` se nos redigirá a la página `www.tudominio.algo/principal`. En el directorio principal no se permite ver la lista de los ficheros, no se permite que se siga los enlaces simbólicos y no se permite negociación de contenido. 
7. En la página `www.tudominio.algo/principal` se debe mostrar una página web estática (utiliza alguna plantilla para que tenga hoja de estilo o la página estática que has generado en IAW). En esta página debe aparecer tu nombre, y una lista de enlaces a las aplicaciones que vamos a ir desplegando posteriormente.
8. Si accedes a la página `www.tudominio.algo/principal/documentos` se visualizarán los documentos que hay en `/srv/doc`. Por lo tanto se permitirá el listado de fichero y el seguimiento de enlaces simbólicos.
9. En todo el host virtual se debe redefinir los mensajes de error de objeto no encontrado y no permitido. Para el ello se crearan dos ficheros html dentro del directorio `error`.

## Autentificación (1 puntos)

10. Autentificación básica. Limita el acceso a la URL `www.tudominio.algo/secreto`.

## PHP (2 puntos)

11. Configura el nuevo virtualhost, para que pueda ejecutar PHP. Determina que configuración tiene por defecto php-fpm (socket unix o socket TCP) para configurar nginx de forma adecuada.
12. Crea un fichero `info.php` que demuestre que está funcionando el servidor LEMP.

## Ansible (3 puntos)

13. Realiza la configuración básica de nginx creando una receta ansible. Utilizando como base la receta ansible que utilizaste para el [ejercicio 6](doc/ejercicio_proxy/ejercicio_proxy.zip), modifícala para añadir las siguientes funcionalidades:

* Instalación de los servicios. (Cada servicio se instalará y configurará en un rol diferenciado)
* Como hace la receta original, creará virtualhost que tengas definido en una lista. Estos virtual host estarán configurados para ejecutar PHP.
* La receta debe poder desactivar los virtualhost que tengas definido en una lista.
* Como la receta tiene que ser lo más general posible, si quieres hacer algo más de la práctica, añade las tareas a un rol llamado `practica`.

{% capture notice-text %}
Explica de forma precisa el proceso que has realizado encad auno de los puntos. Entrega pruebas de funcionamiento donde se pueda verificar el correcto funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

