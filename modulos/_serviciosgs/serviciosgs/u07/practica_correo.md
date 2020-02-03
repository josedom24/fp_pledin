---
title: "Práctica: Servidor de correos en los servidores cloud"
permalink: /serviciosgs/u07/practica_correo.html
---

**(10 tareas - 25 puntos)(5 tareas obligatorias - 8 puntos)**
{: .notice--warning}

Esta tarea consiste en instalar y configurar un servidor de correo similar al de cualquier organización, capaz de enviar y recibir directamente correo, almacenar los usuarios en LDAP, filtrar el correo en busca de virus o spam y servirlo a sus usuarios a través de los protocolos POP, IMAP y configurar un Webmail.

* El servidor de correos se va a instalar en **croqueta** (debian)
* Los servidores que necesites para realizar la práctica serán los del cloud: **salmorejo** (servidor web) y **croqueta** (servidor dns y ldap).

## Pasos a realizar 

Vamos a realizar un sistema de correo para el dominio `tudominio.gonzalonazareno.org`, cuyo servidor DNS lo administras en tu propio servidor DNS. Tienes que comunicar el nombre de dominio al profesor para configurar el servidor de correos del departamento. Instala postfix y comprueba que recibe correo directamente desde un equipo de Internet (hotmail, gmail, etc.). Configura tu servidor de correos para que use a `babuino-smtp` como relay y comprueba que puedes enviar correos.

{% capture notice-text %}
* **Tarea 1 (1 puntos)(Obligatorio)**: Documenta en redmine una prueba de funcionamiento, donde envíes desde tu servidor local al exterior. Muestra el log donde se vea el envío. Muestra el correo que has recibido.
* **Tarea 2 (1 puntos)(Obligatorio)**: Documenta en redmine una prueba de funcionamiento, donde envíes un correo desde el exterior (gmail, hotmail,...) a tu servidor local. Muestra el log donde se vea el envío. Muestra cómo has leído el correo.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

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

## Tarea adicional: Configuración de usuarios virtuales con LDAP

Instala un esquema adecuado para usuarios de postfix en LDAP y crea un script que reciba un nombre de usuario y añade un nuevo registro al LDAP:

1. El dn debes ajustarlo a la base a la de tu directorio
2. Cada entrada incluye un objectClass y atributos adecuados para postfix
3. El atributo mail es del tipo usuario@dominio
4. El buzón de cada usuario está en formato Maildir
5. El atributo userPassword es un hash SSHA del uid del usuario

{% capture notice-text %}
* **Tarea 8 (4 puntos)**: Documenta en redmine la configuración realizada. Y realiza una prueba de funcionamiento al profesor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea adicional: Configuración de seguridad para SMTP, POP e IMAP

En el servidor de clase, configura postfix para que las conexiones al servidor SMTP, POP e IMAP sean seguras (SSL). 

{% capture notice-text %}
* **Tarea 9 (2 puntos)**: Documenta en redmine la configuración realizada para que nuestro servidor SMTP sea seguro. Indica alguna prueba de funcionamiento .
* **Tarea 10 (3 puntos)**: Documenta en redmine la configuración realizada para que nuestro servidor POP o IMAP sea seguro. Indica alguna prueba de funcionamiento.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
