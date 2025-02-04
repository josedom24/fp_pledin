---
title: "Práctica (2 / 2): Servidor de correos"
---

## Gestión de correos desde un cliente

Ahora vamos a usar un cliente de correo para enviar y recibir correos usando nuestro servidor.

* Configura el buzón de los usuarios de tipo `Maildir`. Envía un correo a tu usuario y comprueba que el correo se ha guardado en el buzón `Maildir` del usuario del sistema correspondiente. Recuerda que ese tipo de buzón no se puede leer con la utilidad `mail`.
* Instala configura dovecot para ofrecer el protocolo IMAP. Configura dovecot de manera adecuada para ofrecer autentificación y cifrado.
    Para realizar el cifrado de la comunicación crea un certificado en LetsEncrypt para tu dominio `mail.tudominio.es`. Recuerda que para el ofrecer el cifrado tiene varias soluciones:
    * **IMAP con STARTTLS**: STARTTLS transforma una conexión insegura en una segura mediante el uso de SSL/TLS. Por lo tanto usando el mismo puerto 143/tcp tenemos cifrada la comunicación.
    * **IMAPS**: Versión segura del protocolo IMAP que usa el puerto 993/tcp.
    * Ofrecer las dos posibilidades.
    Elige una de las opciones anterior para realizar el cifrado. 
*  Configura de manera adecuada postfix para que podamos mandar un correo desde un cliente remoto. La conexión entre cliente y servidor debe estar autentificada con SASL usando dovecot y además debe estar cifrada. Para cifrar esta comunicación puedes usar dos opciones:
    * **ESMTP + STARTTLS**: Usando el puerto 567/tcp enviamos de forma segura el correo al servidor.
    * **SMTPS**: Utiliza un puerto no estándar  (465) para SMTPS (Simple Mail Transfer Protocol Secure). No es una extensión de smtp. Es muy parecido a HTTPS.
    Elige una de las opciones anterior para realizar el cifrado. Y
* Configura un cliente webmail (puedes usar docker) para el envío y recepción de correos. 
* Prueba de envío de correo. En esta [página](https://www.mail-tester.com/) tenemos una herramienta completa y fácil de usar a la que podemos enviar un correo para que verifique y puntúe el correo que enviamos. 

{% capture notice-text %}
## Entrega

1. Indica qué método has usado para recibir el correo de forma autentificada y cifrada. Detalla la configuración que has realizado. Muestra la configuración de un cliente de correo (evolution, thunderbird, ...) y muestra como puedes leer los correos enviado a tu usuario.
2.Indica que método has usado para enviar correo de forma autentificada y cifrada. Detalla la configuración que has realizado. Muestra la configuración de un cliente de correo (evolution, thunderbird, ...) y muestra como puedes enviar los correos.
3. Muestra el método de instalación del cliente webmail. Realiza una prueba de envío y recpción de correos con el webmail.
4. Captura la pantalla del envío de correo al página mail-tester mostrando la puntuación que has sacado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>