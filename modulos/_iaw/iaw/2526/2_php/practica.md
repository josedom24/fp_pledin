---
title: "Práctica: Instalación/migración de aplicaciones web PHP"
---

## Escenario

Crea un escenario con dos máquinas virtuales: en una pondremos un servidor web y en otra un servidor de base de datos. Elige la configuración de red que quieras, donde el servidor web sea accesible desde el exterior y pueda acceder al servidor de base de datos.

## Instalación de un CMS PHP en mi servidor local

* Selecciona un CMS escrito en PHP para desplegarlo en nuestra infraestructura. No se puede elegir ni WordPress (que lo hemos visto en un vídeo, ni NextCloud que lo instalaremos a continuación).
* Configura en una de las máquinas, un servidor web apache2 que ejecute PHP, con un VirtualHost, para que el CMS sea accesible desde la dirección: `www.nombrealumno.org`.
* Configura en la otra máquina una base de datos. Crea un usuario con privilegios sobre la base de datos donde se van a guardar los datos del CMS. Configura la base de datos para que permita conexión desde la otra máquina por la red muy aislada, es decir la máquina servidor web se conecta a la máquina servidor de base de datos usando su ip que tiene configurada en la red privada muy aislada (**No uses una ip usa un nombre**).
* Descarga el CMS seleccionado y realiza la instalación.
* Realiza una configuración mínima de la aplicación (cambia la plantilla, crea algún contenido, ...)

{% capture notice-text %}
## Entrega

1. Entrega la configuración del virtualhost.
2. Del contenido del fichero de configuración del CMS el fragmento donde se ve las credenciales de acceso a la base de datos.
3. Una captura de pantalla donde se vea el acceso a la aplicación.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Instalación de un CMS NextCloud

* Instala el CMS PHP NextCloud en otro host virtual con el que accedemos con el nombre `cloud.nombrealumno.org`.

{% capture notice-text %}
## Entrega

1. Una captura de pantalla donde se vea el acceso a la aplicación.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Migración a tu VPS

* Configura en tu VPS un servidor LEMP.
* Configura registros DNS en tu servidor DNS de tipo **CNAME** para que el nombre `www` y `cloud` apunten al nombre de vuestro servidor.
* Realiza la migración de tus aplicaciones web a tu VPS. La primera aplicación debe ser accesible desde la URL `www.tudominio.algo`, y el NextCloud con la URL `cloud.tudominio.algo`.
* Instala en un ordenador el cliente de NextCloud y realiza la configuración adecuada para acceder a "tu nube".


{% capture notice-text %}
## Entrega

1. Entrega la configuración del virtualhost para servir el primer CMS.
2. Del contenido del fichero de configuración del primer CMS, el fragmento donde se ve las credenciales de acceso a la base de datos.
3. Las URL de acceso a las aplicaciones.
4. Capturas de pantalla donde se demuestre que esta funcionando el cliente de NextCloud.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Configuración de HTTPS en el VPS

Vamos a configurar el protocolo HTTPS para el acceso a nuestras aplicaciones, para ello tienes que tener en cuenta los siguiente.

1. Vamos a utilizar el servicio [letsencrypt](https://letsencrypt.org) para solicitar los certificados de nuestras páginas.
2. Comprueba que el navegador tiene el certificado de Let's Encrypt.
3. Solicita un certificado en Let's Encrypt. Tienes dos opciones:
    * Solicitar dos certificados para los nombres que tienes: `www.tudominio.algo` y `cloud.tudominio.algo`.
    * Solicitar un certificado wildcard `*.tudominio.algo` que te sirve para todos tus nombres.
4. Realiza una redirección o una reescritura para que cuando accedas a HTTP te redirija al sitio HTTPS.
5. Comprueba que se ha creado una tarea cron que renueva el certificado cada 3 meses.
6. Comprueba que las páginas son accesibles por HTTPS y visualiza los detalles del certificado que has creado.
7. Modifica la configuración del cliente de NextCloud para comprobar que sigue en funcionamiento con HTTPS.


{% capture notice-text %}
## Entrega

1. Captura de pantalla para comprobar que el navegador tiene el certificado de Let's Encrypt.
2. Entrega la configuración del virtualhost de nginx para el acceso por HTTPS al primer CMS.
3. Entrega la configuración del cron donde se ve que se hará la renovación cada 3 meses.
4. Captura de pantalla accediendo a las dos páginas con https. Captura de pantalla con los detalles del certificado.
5. Captura de pantalla donde se vea el cliente de NextCloud conectado por https.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
