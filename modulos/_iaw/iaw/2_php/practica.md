---
title: "Práctica: Instalación/migración de aplicaciones web PHP"
---

## Descripción

### Escenario

Crea un escenario con vagrant o kvm con las siguientes características:

* Dos máquinas virtuales que se llamen `servidor_web_tunombre` y `servidor_bd_tunombre`.
* La máquina `servidor_web_tunombre` estará conectada una red pública.
* Las dos máquinas están conectadas entre si por una red muy aislada.

## Tarea 1: Instalación de un CMS PHP en mi servidor local

* Selecciona un CMS escrito en PHP para desplegarlo en nuestra infraestructura. No se puede elegir ni WordPress (que lo hemos visto en un vídeo, ni NextCloud que lo instalaremos a continuación).
* Configura en la máquina `servidor_web_tunombre` un servidor web apache2 que ejecute PHP, con un VirtualHost, para que el CMS sea accesible desde la dirección: `www.nombrealumno.org`.
* Configura en la máquina `servidor_bd_tunombre` una base de datos. Crea un usuario con privilegios sobre la base de datos donde se van a guardar los datos del CMS. Configura la base de datos para que permita conexión desde la otra máquina.
* Descarga el CMS seleccionado y realiza la instalación.
* Realiza una configuración mínima de la aplicación (cambia la plantilla, crea algún contenido, ...)
* Instala un módulo para añadir alguna funcionalidad al CMS.

{% capture notice-text %}
## Entrega

1. Entrega la configuración del virtualhost.
2. La configuración de resolución estática.
3. Una captura de pantalla donde se vea el acceso a la aplicación.
4. Indica que plugin has instalado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Instalación de un CMS NextCloud

* Instala el CMS PHP NextCloud en otro host virtual con el que accedemos con el nombre `cloud.nombrealumno.org`.

{% capture notice-text %}
## Entrega

1. Una captura de pantalla donde se vea el acceso a la aplicación.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Tarea 3: Migración a tu VPS

* Configura en tu VPS un servidor LEMP.
* Configura registros DNS en tu servidor DNS de tipo **CNAME** para que el nombre `www` y `cloud` apunten al nombre de vuestro servidor.
* Realiza la migración de tus aplicaciones web a tu VPS. La primera aplicación debe ser accesible desde la URL `www.tudominio.algo/portal`, y el NextCloud con la URL `cloud.tudominio.algo`.
* Al acceder a `www.tudominio.algo` se debe hacer una redirección a `www.tudominio.algo/portal`.
*  Instala en un ordenador el cliente de NextCloud y realiza la configuración adecuada para acceder a "tu nube".


{% capture notice-text %}
## Entrega

1. Documenta de la forma más precisa posible cada uno de los pasos que has dado para migrar una de las dos aplicaciones.
2. Las URL de acceso a las aplicaciones.
3. Capturas de pantalla donde se demuestre que esta funcionando el cliente de NextCloud.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Configuración de HTTPS en el VPS"

Vamos a configurar el protocolo HTTPS para el acceso a nuestras aplicaciones, para ello tienes que tener en cuenta los siguiente.

1. Vamos a utilizar el servicio [letsencrypt](https://letsencrypt.org) para solicitar los certificados de nuestras páginas.
2. Comprueba que el navegador tiene el certificado de Let's Encrypt.
3. Solicita un certificado en Let's Encrypt. Tienes dos opciones:
    * Solicitar dos certificados para los nombres que tienes: `www.tudominio.algo` y `cloud.tudominio.algo`.
    * Solicitar un certificado wildcard `*.tudominio.algo` que te sirve para todos tus nombres. (Esta opción te dará más puntos).
4. Utiliza dos ficheros de configuración de nginx, para cada virtualhost: uno para la configuración del virtualhost HTTP y otro para la configuración del virtualhost HTTPS.
5. Realiza una redirección o una reescritura para que cuando accedas a HTTP te redirija al sitio HTTPS.
6. Comprueba que se ha creado una tarea cron que renueva el certificado cada 3 meses.
7. Comprueba que las páginas son accesibles por HTTPS y visualiza los detalles del certificado que has creado.
8. Modifica la configuración del cliente de NextCloud para comprobar que sigue en funcionamiento con HTTPS.


{% capture notice-text %}
## Entrega

1. Captura de pantalla para comprobar que el navegador tiene el certificado de Let's Encrypt.
2. ¿Qué opción has elegido? ¿Qué pruebas realiza Let's Encrypt para asegurar que somos los administrados del sitio web al elegir esa opción? 
3. Entrega la configuración de nginx (los dos ficheros de cada virtualhost) para que funcione HTTPS y la redirección.
4. Entrega la configuración del cron donde se ve que se hará la renovación cada 3 meses.
5. Captura de pantalla accediendo a las dos páginas con https. Captura de pantalla con los detalles del certificado.
6. Captura de pantalla donde se vea el cliente de NextCloud conectado por https.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
