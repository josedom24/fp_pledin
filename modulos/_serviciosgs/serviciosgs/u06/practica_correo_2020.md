---
title: "Práctica: Servidor de correos"
permalink: /serviciosgs/u06/practica_correo_2020.html
---

Instala y configura de manera adecuada el servidor de correos en tu máquina de OVH, para tu dominio `iesgnXX.es`. El nombre del servidor de correo será `mail.iesgnXX.es` (Este es el nombre que deberá aparecer en el registro MX)

## Gestión de correos desde el servidor

* **Tarea 1**: Documenta una prueba de funcionamiento, donde envíes desde tu servidor local al exterior. Muestra el log donde se vea el envío. Muestra el correo que has recibido. Muestra el registro SPF.
* **Tarea 2**: Documenta una prueba de funcionamiento, donde envíes un correo desde el exterior (gmail, hotmail,...) a tu servidor local. Muestra el log donde se vea el envío. Muestra cómo has leído el correo. Muestra el registro MX de tu dominio.

## Uso de alias y redirecciones

* **Tarea 3 (No obligatoria)**: Uso de alias y redirecciones.

Vamos a comprobar como los procesos del servidor pueden mandar correos para informar sobre su estado. Por ejemplo cada vez que se ejecuta una tarea cron podemos enviar un correo informando del resultado. Normalmente estos correos se mandan al usuario `root` del servidor, para ello:

    $ crontab -e

E indico donde se envía el correo:

    MAILTO = root

Puedes poner alguna tarea en el cron para ver como se mandan correo.

Posteriormente usando alias y redirecciones podemos hacer llegar esos correos a nuestro correo personal.

Configura el `cron` para enviar correo al usuario `root`. Comprueba que están llegando esos correos al `root`. Crea un nuevo alias para que se manden a un usuario sin privilegios. Comprueban que llegan a ese usuario. Por último crea una redirección para enviar esos correo a tu correo personal (gmail,hotmail,...).

## Para asegurar el envío

* **Tarea 4 (No obligatoria)**: Configura de manera adecuada DKIM es tu sistema de correos. Comprueba el registro DKIM en la página https://mxtoolbox.com/dkim.aspx. Configura postfix para que firme los correos que envía. Manda un correo y comprueba la verificación de las firmas en ellos.

## Para luchar contra el SPAM

* **Tarea 5 (No obligatorio)**: Configura de manera adecuada Postfix para que tenga en cuenta el registro SPF de los correos que recibe. Muestra el log del correo para comprobar que se está haciendo el testeo del registro SPF.

* **Tarea 6 (No obligatoria)**: Configura un sistema antispam. Realiza comprobaciones para comprobarlo.

* **Tarea 7 (No obligatoria)**: Configura un sistema antivirus. Realiza comprobaciones para comprobarlo. 

## Gestión de correos desde un cliente

* **Tarea 8**: Configura el buzón de los usuarios de tipo `Maildir`. Envía un correo a tu usuario y comprueba que el correo se ha guardado en el buzón `Maildir` del usuario del sistema correspondiente. Recuerda que ese tipo de buzón no se puede leer con la utilidad `mail`.

* **Tarea 9**: Instala configura dovecot para ofrecer el protocolo IMAP. Configura dovecot de manera adecuada para ofrecer autentificación y cifrado.

    Para realizar el cifrado de la comunicación crea un certificado en LetsEncrypt para el dominio `mail.iesgnXX.es`. Recuerda que para el ofrecer el cifrado tiene varias soluciones:

    * **IMAP con STARTTLS**: STARTTLS transforma una conexión insegura en una segura mediante el uso de SSL/TLS. Por lo tanto usando el mismo puerto 143/tcp tenemos cifrada la comunicación.
    * **IMAPS**: Versión segura del protocolo IMAP que usa el puerto 993/tcp.
    * Ofrecer las dos posibilidades.

    Elige una de las opciones anterior para realizar el cifrado. Y muestra la configuración de un cliente de correo (evolution, thunderbird, ...) y muestra como puedes leer los correos enviado a tu usuario.

* **Tarea 10 (No obligatoria)**: Instala un webmail (roundcube, horde, rainloop) para gestionar el correo del equipo mediante una interfaz web. Muestra la configuración necesaria y cómo eres capaz de leer los correos que recibe tu usuario.

* **Tarea 11**: Configura de manera adecuada postfix para que podamos mandar un correo desde un cliente remoto. La conexión entre cliente y servidor debe estar autentificada con SASL usando dovecor y además debe estar cifrada. Para cifrar esta comunicación puedes usar dos opciones:

    * **ESMTP + STARTTLS**: Usando el puerto 567/tcp enviamos de forma segura el correo al servidor.
    * **SMTPS**: Utiliza un puerto no estándar  (465) para SMTPS (Simple Mail Transfer Protocol Secure). No es una extensión de smtp. Es muy parecido a HTTPS.

    Elige una de las opciones anterior para realizar el cifrado. Y muestra la configuración de un cliente de correo (evolution, thunderbird, ...) y muestra como puedes enviar los correos.

* **Tarea 12 (No obligatoria)**: Configura el cliente webmail para el envío de correo. Realiza una prueba de envío con el webmail.


## Comprobación final

* **Tarea 13 (No obligatoria)**: Prueba de envío de correo. En https://www.mail-tester.com/ tenemos una herramienta completa y fácil de usar a la que podemos enviar un correo para que verifique y puntúe el correo que enviamos. Captura la pantalla y muestra la puntuación que has sacado.
