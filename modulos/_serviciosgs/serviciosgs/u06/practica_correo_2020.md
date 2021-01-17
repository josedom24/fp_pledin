---
title: "Práctica: Servidor de correos"
permalink: /serviciosgs/u06/practica_correo_2020.html
---

## Nivel 1: Envío de correo desde el servidor

Instala y configura de manera adecuada el servidor de correos en tu máquina de OVH, para tu dominio `iesgnXX.es`. El nombre del servidor de correo será `mail.iesgnXX.es` (Este es el nombre que deberá aparecer en el registro MX)

* **Tarea 1**: Documenta una prueba de funcionamiento, donde envíes desde tu servidor local al exterior. Muestra el log donde se vea el envío. Muestra el correo que has recibido.
* **Tarea 2**: Documenta una prueba de funcionamiento, donde envíes un correo desde el exterior (gmail, hotmail,...) a tu servidor local. Muestra el log donde se vea el envío. Muestra cómo has leído el correo. Muestra los registros que has tenido que crear en el DNS (MX, SPF).





Instala y configura un servidor dovecot POP e IMAP en tu equipo. Configura adecuadamente un cliente de correo (evolution, outlook, thunderbird, ...) para que reciba el correo a través de POP o IMAP. El cliente debe estar configurado en una máquina cliente. Nombra en tu servidor DNS al servidor smtp, pop e imap.

{% capture notice-text %}
* **Tarea 3 (2 puntos)(Obligatorio)**: Documenta en redmine una prueba de funcionamiento, donde envíes desde tu cliente de correos al exterior. ¿Cómo se llama el servidor para enviar el correo? (Muestra la configuración).
* **Tarea 4 (2 puntos)(Obligatorio)**: Documenta en redmine una prueba de funcionamiento, donde recibas un correo desde el exterior (gmail, hotmail,...) y lo leas en tu cliente de correo. Utiliza el protocolo POP. ¿Cómo se llama el servidor para enviar el correo? (Muestra la configuración). Muestra una prueba de funcionamiento de cómo funciona el protocolo POP.
* **Tarea 5 (2 puntos)(Obligatorio)**: Documenta en redmine una prueba de funcionamiento, donde recibas un correo desde el exterior (gmail, hotmail,...) y lo leas  en tu cliente de correo. Utiliza el protocolo IMAP. ¿Cómo se llama el servidor para enviar el correo? (Muestra la configuración). Muestra una prueba de funcionamiento de cómo funciona el protocolo IMAP.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

Instala un webmail (roundcube, horde, ...) para gestionar el correo del equipo mediante una interfaz web. Instala y configura correctamente un sistema de filtrado de virus y spam utilizando amavis, clamav y spamassasin .

{% capture notice-text %}
* **Tarea 6 (3 puntos)**: Muestra al profesor el envío y recepción de correos utilizando el webmail.
* **Tarea 7 (5 puntos)**: Muestra al profesor el funcionamiento del sistema de filtrado de virus y spam.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Pasos a realizar en casa 

* Configura adecuadamente el router de casa para que el puerto 25/tcp de tu equipo sea accesible desde Internet (eso se denomina DNAT o  forwarding)
* Date de alta en un servidor DNS dinámico como `dyndns.org`, `no-ip.com`, etc. o usa el nombre de dominio propio.
* Configura el DNS  de tu * Configura el DNS de tu proveedor para que la máquina a la que apunta el registro MX corresponda a tu IP pública. Si vas a utilizar un servicio gratuito como `dyndns.org`, `no-ip.com`, simplemente debes configurarlo para que apunte a tu ip. Instala postfix en tu máquina y comprueba que recibe correo directamente desde un equipo de Internet (hotmail, gmail, etc.)
* Prueba a enviar desde tu equipo un correo electrónico a `jose@gonzalonazareno.org`, que no lo rechazará aunque venga de una dirección IP dinámica. Prueba a enviar desde tu equipo un correo electrónico a hotmail/gmail. Comprueba si llega bien, si lo mete en SPAM o si rebota los mensajes (mira en `/var/log/mail.log`), ya que no acepta correos de direcciones IP dinámicas.
* Configura postfix para que envíe el correo electrónico a través de servidor SMTP relay (gmail, mailgun, sendgrid,...). Cuando funcione envía un correo a `josedom24@gmail.com`

{% capture notice-text %}
* **Tarea 8 (2 puntos)**: Envía el correo a `jose@gonzalonazareno.org`
* **Tarea 9 (3 puntos)**: Responde al correo que yo te voy a mandar desde esa dirección.
* **Tarea 10 (4 puntos)**: ¿Te rebota el correo enviado al exterior por qué estas usando ip dinámica? Independientemente de la respuesta, muestra el log donde se vea el envío de ese correo y documenta la configuración del relay. Finalmente envía un correo a `josedom24@gmail.com`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea adicional: Configuración de usuarios virtuales con LDAP

Instala un esquema adecuado para usuarios de postfix en LDAP y crea un script que reciba un nombre de usuario y añade un nuevo registro al LDAP:

1. El dn debes ajustarlo a la base a la de tu directorio
2. Cada entrada incluye un objectClass y atributos adecuados para postfix
3. El atributo mail es del tipo usuario@dominio
4. El buzón de cada usuario está en formato Maildir
5. El atributo userPassword es un hash SSHA del uid del usuario

{% capture notice-text %}
* **Tarea 11 (5 puntos)**: Documenta en redmine la configuración realizada. Y realiza una prueba de funcionamiento al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea adicional: Configuración de seguridad para SMTP, POP e IMAP

En el servidor de clase, configura postfix para que las conexiones al servidor SMTP, POP e IMAP sean seguras (SSL). 

{% capture notice-text %}
* **Tarea 12 (2 puntos)**: Documenta en redmine la configuración realizada para que nuestro servidor SMTP sea seguro. Indica alguna prueba de funcionamiento .
* **Tarea 13 (3 puntos)**: Documenta en redmine la configuración realizada para que nuestro servidor POP o IMAP sea seguro. Indica alguna prueba de funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
