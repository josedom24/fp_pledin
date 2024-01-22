---
title: "Práctica: Servidor de correos"
---

Instala y configura de manera adecuada el servidor de correos en tu VPS. El nombre del servidor de correo será `mail.tudominio.es` (este es el nombre que deberá aparecer en el registro MX).

## Gestión de correos desde el servidor

El envío y recepción se hará desde el servidor usando la herramienta `mail`.

* **Tarea 1**: Configura el registro SPF en tu DNS para autorizar el envío de correos desde tu VPS. Muestra la configuración del registro SPF. 

* **Tarea 2**: Configura de manera adecuada DKIM es tu sistema de correos. Comprueba el registro DKIM en la página [DKIM Record Lookup](https://mxtoolbox.com/dkim.aspx). Configura postfix para que firme los correos que envía. 

* **Tarea 3**: Configura de manera adecuada el registro DMARC. Muestra la configuración del registro que has realizado. Utiliza la página [DMARC Check Tool](https://mxtoolbox.com/dmarc.aspx?utm_term=&utm_campaign=Products+-+Email+Delivery&utm_source=adwords&utm_medium=ppc&hsa_acc=2278553980&hsa_cam=1331057180&hsa_grp=75858827199&hsa_ad=374948031324&hsa_src=g&hsa_tgt=dsa-795565777906&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQiAwbitBhDIARIsABfFYIKfywpY95Zchp8yG4J_qccCMLLvrhO114fTRcNFYU6jN-xoEQATP0waAjLOEALw_wcB) para verificar que el registro es correcto.

* **Tarea 5**: Documenta una prueba de funcionamiento, donde envíes desde tu servidor local al exterior. Muestra el log donde se vea el envío. Muestra el correo que has recibido. Muestra que el receptor ha comprobado tus registros SPF, DKIM y DMARC.
* **Tarea 6**: Documenta una prueba de funcionamiento, donde envíes un correo desde el exterior (gmail, hotmail,...) a tu servidor local. Muestra el log donde se vea el envío. Muestra cómo has leído el correo. Muestra el registro MX de tu dominio.

## Para luchar contra el SPAM

* **Tarea 7 (No obligatorio)**: Configura de manera adecuada Postfix para que tenga en cuenta el registro SPF de los correos que recibes. Muestra el log del correo para comprobar que se está haciendo el testeo del registro SPF.

* **Tarea 8 (No obligatoria)**: Configura un sistema antispam. Realiza comprobaciones para comprobarlo.

* **Tarea 9 (No obligatoria)**: Configura un sistema antivirus. Realiza comprobaciones para comprobarlo. 

## Gestión de correos desde un cliente

* **Tarea 10**: Configura el buzón de los usuarios de tipo `Maildir`. Envía un correo a tu usuario y comprueba que el correo se ha guardado en el buzón `Maildir` del usuario del sistema correspondiente. Recuerda que ese tipo de buzón no se puede leer con la utilidad `mail`.

* **Tarea 11**: Instala configura dovecot para ofrecer el protocolo IMAP. Configura dovecot de manera adecuada para ofrecer autentificación y cifrado.

    Para realizar el cifrado de la comunicación crea un certificado en LetsEncrypt para tu dominio `mail.tudominio.es`. Recuerda que para el ofrecer el cifrado tiene varias soluciones:

    * **IMAP con STARTTLS**: STARTTLS transforma una conexión insegura en una segura mediante el uso de SSL/TLS. Por lo tanto usando el mismo puerto 143/tcp tenemos cifrada la comunicación.
    * **IMAPS**: Versión segura del protocolo IMAP que usa el puerto 993/tcp.
    * Ofrecer las dos posibilidades.

    Elige una de las opciones anterior para realizar el cifrado. Y muestra la configuración de un cliente de correo (evolution, thunderbird, ...) y muestra como puedes leer los correos enviado a tu usuario.

* **Tarea 12 (No obligatoria)**: Instala un webmail (roundcube, horde, rainloop) para gestionar el correo del equipo mediante una interfaz web. Muestra la configuración necesaria y cómo eres capaz de leer los correos que recibe tu usuario.

* **Tarea 13**: Configura de manera adecuada postfix para que podamos mandar un correo desde un cliente remoto. La conexión entre cliente y servidor debe estar autentificada con SASL usando dovecor y además debe estar cifrada. Para cifrar esta comunicación puedes usar dos opciones:

    * **ESMTP + STARTTLS**: Usando el puerto 567/tcp enviamos de forma segura el correo al servidor.
    * **SMTPS**: Utiliza un puerto no estándar  (465) para SMTPS (Simple Mail Transfer Protocol Secure). No es una extensión de smtp. Es muy parecido a HTTPS.

    Elige una de las opciones anterior para realizar el cifrado. Y muestra la configuración de un cliente de correo (evolution, thunderbird, ...) y muestra como puedes enviar los correos.

* **Tarea 14 (No obligatoria)**: Configura el cliente webmail para el envío de correo. Realiza una prueba de envío con el webmail.


## Comprobación final

* **Tarea 15**: Prueba de envío de correo. En esta [página](https://www.mail-tester.com/) tenemos una herramienta completa y fácil de usar a la que podemos enviar un correo para que verifique y puntúe el correo que enviamos. Captura la pantalla y muestra la puntuación que has sacado.
