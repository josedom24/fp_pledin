---
title: "Práctica: Instalación y configuración de un servidor de correos en el VPS"
---

## Ejercicio 1: Envío de correos desde usuarios del servidor a correos


Instala y configura de manera adecuada el servidor de correos en tu VPS. El nombre del servidor de correo será `nompre_vps.tudominio.algo` (este es el nombre que deberá aparecer en el registro MX).

El envío de correo se hará desde el servidor usando la herramienta `mail`. Debes tener en cuenta lo siguiente:

* Instala postfix en tu VPS.
* Configura el registro SPF en tu DNS para autorizar el envío de correos desde tu VPS.
* Configura de manera adecuada DKIM es tu sistema de correos. Comprueba el registro DKIM en la página [DKIM Record Lookup](https://mxtoolbox.com/dkim.aspx). 
* Configura de manera adecuada el registro DMARC. Muestra la configuración del registro que has realizado. Utiliza la página [DMARC Check Tool](https://mxtoolbox.com/dmarc.aspx?utm_term=&utm_campaign=Products+-+Email+Delivery&utm_source=adwords&utm_medium=ppc&hsa_acc=2278553980&hsa_cam=1331057180&hsa_grp=75858827199&hsa_ad=374948031324&hsa_src=g&hsa_tgt=dsa-795565777906&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQiAwbitBhDIARIsABfFYIKfywpY95Zchp8yG4J_qccCMLLvrhO114fTRcNFYU6jN-xoEQATP0waAjLOEALw_wcB) para verificar que el registro es correcto.
* No es necesario para el envío, pero sería bueno que configures el registro MX en tu servidor DNS. Recuerda que debes poner el nombre de tu VPS.
* Realiza un envío de correo desde tu servidor al exterior.

{% capture notice-text %}
## Entrega

1. Resultado de una consulta consulta con `dig` para mostrar la configuración de tu registro SPF, DKIM y DMARC.
2. Envía un correo desde tu servidor a la dirección de correo que te indica la página [Learn and Test DMARC](https://www.learndmarc.com/) y envía una captura de pantalla de la comprobación de que tu configuración SPF, DKIM y DMARC funcionan (**PASS**).
3. Muestra el log donde se demuestre el envío de correo. Una captura de pantalla donde se vea que el correo ha llegado. Y una comprobación en las cabeceras del correo que muestre que el receptor ha comprobado tus registros SPF, DKIM y DMARC.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejercicio 2: Recibir correos desde internet a usuarios del servidor

Para leer el correo en tu VPS usa la herramienta `mail`. Debes realizar las siguientes tareas:

* Si no configuraste el registro MX en el ejercicio anterior, ahora si lo tienes que hacer.
* Para solucionar el problema del SPAM, configura de manera adecuada tu servidor para que compruebe el SPF del emisor.
* Para solucionar el problema del SPAM, asegúrate que tu servidor comprueba el DKIM del emisor.
* Para solucionar el problema del SPAM, comprueba el registro DMAR del emisor.
* Envía un correo desde el exterior (gmail, hotmail,...) a tu servidor local. 

{% capture notice-text %}
## Entrega

1. Muestra el registro MX de tu dominio con una consulta con `dig`.
2. Muestra el log donde se vea la recepción del correo desde el exterior. Muestra cómo has leído el correo. 
3. Muestra el log del correo para comprobar que se está haciendo el testeo del SPF, DKIM y DMARC del correo que recibes.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Ejercicio 3: Gestión de correos desde un cliente

Ahora vamos a usar un cliente de correo para enviar y recibir correos usando nuestro servidor.

* Configura el buzón de los usuarios de tipo `Maildir`. Envía un correo a tu usuario y comprueba que el correo se ha guardado en el buzón `Maildir` del usuario del sistema correspondiente. Recuerda que ese tipo de buzón no se puede leer con la utilidad `mail`.
* Crea un nombre en tu DNS que vamos a usar para referenciar el servido de correos desde el cliente: `mail.tudominio.algo`.
* Instala configura dovecot para ofrecer el protocolo IMAP. Configura dovecot de manera adecuada para ofrecer autentificación y cifrado.
    Para realizar el cifrado de la comunicación crea un certificado en LetsEncrypt para tu dominio `mail.tudominio.es`. Recuerda que para el ofrecer el cifrado tiene varias soluciones:
    * **IMAP con STARTTLS**: STARTTLS transforma una conexión insegura en una segura mediante el uso de SSL/TLS. Por lo tanto usando el mismo puerto 143/tcp tenemos cifrada la comunicación.
    * **IMAPS**: Versión segura del protocolo IMAP que usa el puerto 993/tcp.
    * Ofrecer las dos posibilidades.
    Elige una de las opciones anterior para realizar el cifrado. 
*  Configura de manera adecuada postfix para que podamos mandar un correo desde un cliente remoto. La conexión entre cliente y servidor debe estar autentificada con SASL usando dovecot y además debe estar cifrada. Para cifrar esta comunicación puedes usar dos opciones:
    * **ESMTP + STARTTLS**: Usando el puerto 567/tcp enviamos de forma segura el correo al servidor.
    * **SMTPS**: Utiliza un puerto no estándar  (465) para SMTPS (Simple Mail Transfer Protocol Secure). No es una extensión de smtp. Es muy parecido a HTTPS.
    Elige una de las opciones anterior para realizar el cifrado. 
* Configura un cliente webmail (puedes usar docker) para el envío y recepción de correos. 
* Prueba de envío de correo. En esta [página](https://www.mail-tester.com/) tenemos una herramienta completa y fácil de usar a la que podemos enviar un correo para que verifique y puntúe el correo que enviamos. 
* **Optativo**: 
    * Configura un sistema antispam. 
    * Si tu VPS tiene más de 1Gb de RAM, instala un antivirus. (Aunque no es recomendable por el excesivo uso de memoria RAM).
    * Configura el envío seguro desde tu MTA con el certificado LetsEncrypt, para que además de cifrado se pueda verificar la identidad de nuestro servidor.

{% capture notice-text %}
## Entrega

1. Indica qué método has usado para recibir el correo de forma autentificada y cifrada. Detalla la configuración que has realizado. Muestra la configuración de un cliente de correo (evolution, thunderbird, ...) y muestra como puedes leer los correos enviado a tu usuario.
2. Indica que método has usado para enviar correo de forma autentificada y cifrada. Detalla la configuración que has realizado. Muestra la configuración de un cliente de correo (evolution, thunderbird, ...) y muestra como puedes enviar los correos.
3. Muestra el método de instalación del cliente webmail. Realiza una prueba de envío y recepción de correos con el webmail.
4. Captura la pantalla del envío de correo al página mail-tester mostrando la puntuación que has sacado.
5. Si has hecho la parte optativa: Usando el ejemplo de correo SPAM que hemos visto en clase, mándatelo y demuestra que tu servidor lo ha marcado como SPAM.
6. Si has hecho la parte optativa: Usando el ejemplo de correo con virus que hemos visto en clase, mándatelo y demuestra que tu servidor lo ha detectado.
7. Si has hecho la parte optativa, de usar el certificado LetsEncrypt para asegurar el envío de tu correo desde tu MTA, manda una prueba desde el receptor.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


