---
title: "Práctica (3 / 3): Instalación/migración de aplicaciones web PHP"
---

## Configuración de HTTPS en el VPS

Vamos a configurar el protocolo HTTPS para el acceso a nuestras aplicaciones, para ello tienes que tener en cuenta los siguiente.

1. Vamos a utilizar el servicio [letsencrypt](https://letsencrypt.org) para solicitar los certificados de nuestras páginas.
2. Comprueba que el navegador tiene el certificado de Let's Encrypt.
3. Solicita un certificado en Let's Encrypt. Tienes dos opciones:
    * Solicitar dos certificados para los nombres que tienes: `www.tudominio.algo` y `cloud.tudominio.algo`.
    * Solicitar un certificado wildcard `*.tudominio.algo` que te sirve para todos tus nombres.
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
