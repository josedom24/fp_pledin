---
title: "Resumen: Servidor de correos"
---
## Instalación postfix

* `apt install postfix`
* Tipo de servidor: Internet Site (vamos a recibir y enviar correo directamente)
* Mailname: **DOMINIO**
* Fichero de configuración: `/etc/postfix/main.cf`

## Caso 1: Envío local, entre usuarios del mismo servidor

* Instalamos el cliente de correos `mail`:
    ```
    sudo apt install bsd-mailx
    ```

* Envío de correo
    ```
    usuario1@maquina:~$ mail usuario2@localhost
    ```
* Leer correo
    ```
    usuario2@maquina:~$ mail
    ```
* Como vemos el buzón del usuario está en `/var/mail/usuario2`. Los correos leídos se guardan en `~/mbox`.
* Podemos comprobar el log para comprobar que se ha mandado el mensaje:
    ```
    sudo journalctl -fu postfix@-
    ```

## Caso 2: Envío de correo desde usuarios del servidor a correos de internet

### Desde el aula

* En el fichero de configuración: `relayhost = mail.gonzalonazareno.org`

### Desde tu servidor VPS

* Con la configuración básica del servidor, seríamos capaces de enviar el correo (no necesitamos un relay).
* Quizás no sea necesario para el envío de correos, pero estaría muy bien que ya tengamos configurado en nuestro DNS el registro **MX** apuntando a nuestra máquina.
* Necesitamos implementar varias técnicas (**SPF, DKIM, DMARK**) para asegurar que el servidor de correo al que mandamos nuestro correo confíe en nuestro servidor de correos y en nuestro correo.
* Necesitamos que nuestra IP esté "limpia", es posible que si mandamos el correo desde un servidor que utilice una ip dinámica, seguramente gmail /hotmail / yahoo lo rechaza, por estar en una lista de bloqueo.
* [¿Qué tenemos que hacer para que nuestro correo “llegue a buen puerto”?](https://github.com/josedom24/curso_correo_electronico_ies/blob/main/modulo3/asegurar_envio_correo.md)

## Caso 3: Recibir correos desde internet a usuarios del servidor

### Desde el aula

* Vamos a tener un correo de la forma usuario@dominio_de_cada_alumno, por ejemplo `jose@josedom.gonzalonazareno.org`.
* Servidor de correos en **samji**.
* Tenemos que tener en cuenta los siguientes aspectos:
    1. Si queremos recibir correos desde internet a nuestro servidor, todos nuestros dominios tienen que apuntar a nuestra ip pública `5.196.224.198` (IP de `macaco.gonzalonazareno.org`), esto se consigue con el registro en nuestro DNS de cdmon:
    ```
    * IN CNAME macaco.gonzalonazareno.org.
    ```
    **El correo llega a macaco.**
    2. Tengo que configurar **macaco** para que reenvie el correo a vuestro servidor de correo:
        * Yo como administrador de **macaco** añado vuestro correo en el parámetro `relay_domains` del servidor de correos de macaco.
        **macaco** tiene configurado como primer DNS a **gorila**, por lo que puede preguntarle por nuestro registro MX, ya que tiene delegada todos nuestros subdominios. 
        * Por lo tanto tenemos que crear un registro **MX** en nuestro servidor DNS para realizar la resolución. 
        * En la vista externa el registro MX será `luffy.loquesea.gonzalonazareno.org`. En las otras vistas, será `samji.loquesea.gonzalonazareno.org`.
	    * El correo llegará a **luffy** y para reenviarlo a **samji** tendrás que configurar un DNAT del puerto 25/TCP.
    3. Con la configuración que tenemos en el servidor de correo de nuestra máquina debe ser suficiente para recibir el correo. Recuerda mandar un mensaje a un usuario que exista en el servidor.

### Desde tu VPS

* Asegúrate que al configurar tu servidor de correo pusiste como nombre del sistema de correo tu **dominio**, para asegurarte en el fichero `/etc/mailname` debe estar tu dominio.
* Configura tu DNS para que el registro MX apunte a un nombre de ordenador que está definido como un registro A a tu dirección IP pública. 
* Recuerda que el correo se guardará en el buzón del usuario, que tendrá que leerlo desde el servidor con la utilidad mail.
* ¿Los correos que estamos recibiendo son legítimos? ¿No son SPAM? Para evitar que el correo sea SPAM tendremos que comprobar el registro SPF, DKIM y DMARC del emisor. [Soluciones al problema del spam](https://github.com/josedom24/curso_correo_electronico_ies/blob/main/modulo3/spam.md).

## Caso 4: Recepción de correo electrónico usando nuestro servidor de correos

* Protocolo para recibir correos:
    * **POP3**: Mail Delivery Agent [Agente de Entrega de Correo]. Protocolo para recuperar correos electrónicos de un MDA. Su principal característica es que se descargan todos los correos.
    * **IMAP**: Internet Message Access Protocol [Protocolo de Acceso a Mensajes de Internet]. Protocolo para recuperar correos electrónicos de un MDA. En este caso, se sincroniza el estado de los correos entre el servidor y el cliente.
* **Vamos a trabajar con IMAP**.
* La comunicación con estos protocolos es autentificada y debería ser cifrada.
* Tipos de buzones:
    * **Buzón mbox**: Todos los mensajes están en un fichero, es el tipo de buzón que hemos utilizado hasta ahora, y puede ser válido para el protocolo POP3 donde se descargan todos los correos desde el servidor.
    * **Buzón maildir**: Los mensajes se guardan en una carpeta. Es imprescindible para que funcione el protocolo IMAP.
* Configuración buzón Maildir:
    Añadimos y modificamos las siguientes directivas de configuración en el fichero de configuración:

    ```
    home_mailbox = Maildir/
    mailbox_command =
    ```
    Después de reiniciar el servicio los correos se guardarán en un directorio `Maildir` que se creara en el directorio home de cada usuario.
* Protocolo IMAP: La comunicación es autentificada y sería muy conveniente que fuera cifrada. Para cifrar la comunicación tenemos dos opciones:
    * **IMAP con STARTTLS**: STARTTLS transforma una conexión insegura en una segura mediante el uso de SSL/TLS. Por lo tanto usando el mismo puerto 143/tcp tenemos cifrada la comunicación.
    * **IMAPS**: Versión segura del protocolo IMAP que usa el puerto 993/tcp.
* Vamos a usar el programa **dovecot** como servidor IMAP. (`apt-get install dovecot-imapd`).
* Ya podríamos configurar nuestro cliente de correos para recibir correo utilizando el protocolo imap, para ello creamos un nombre en el servidor DNS, por ejemplo, `imap.josedom.gonzalonazareno.org`.
* Para cifrar la comunicación, nosotros vamos a usar un certificado firmado por LetsEncypt.
* En este caso también puedes instalar un **cliente web de correos** para leer los correos del servidor. Hay muchas: round cube, horde, rainloop, SquirrelMail, ...

## Caso 5: Envío de correo electrónico usando nuestro servidor de correos

* Hay que modificar en el fichero de configuración, el parámetro `mynetworks` (En donde se indican las IPs desde las que pueden enviarse mensajes). 
* Si los clientes de correo van a estar en internet (no en una red específica) tenemos que configurar este parámetro con el valor `0.0.0.0/0` (a esta configuración se le llama **abrir el relay**) y en en esta circunstancia cualquier cliente de correo podría usar nuestro servidor para enviar correo.
* Si abrimos el relay (`mynetworks = 0.0.0.0/0`) es totalmente necesario que la conexión entre el cliente y el servidor **sea autentificada y estar cifrada**. Para ello tenemos dos opciones:
    * **ESMTP + STARTTLS**: esmtp (Enhanced Simple Mail Transfer Protocol): En este caso se usa el puerto **587/tcp**. Este protocolo tiene nuevas extensiones: como smtp-auth y STARTTLS (STARTTLS transforma una conexión insegura en una segura mediante el uso de SSL/TLS).
        * El puerto **587/tcp** se conoce como **puerto de submission o presentación**. Al abrir este puero postfix esta funcionando de **MSA (mail submission agent)** que recibe mensajes de correo electrónico desde un Mail User Agent (MUA) y coopera con un Mail Transport Agent (MTA) para entregar el correo.
        * Para autentificar la conexión usamos **SASL (Simple Authentication and Security Layer)** que es un framework para autenticación y autorización en protocolos de Internet. Para realizar la autenticación vamos a **usar dovecot** (que ya tiene un mecanismo de autenticación).
        * Para cifrar la comunicación, vamos a usar **STARTTLS** que nos permite que utilizando el mismo puerto (587/tcp) la conexión este cifrada.
    * **SMTPS**: Simple Mail Transfer Protocol Secure: Con este protocolo conseguimos el cifrado de la comunicación entre el cliente y el servidor. Utiliza un puerto no estándar **465/tcp**. No es una extensión de smtp. Es muy parecido a HTTPS.
* Enlaces:
    * [ISP Mail Tutorial for Debian 10 (Buster)](https://123qwe.com/tutorial-debian-10/)
    * [How to secure Postfix using Let’s Encrypt](https://upcloud.com/community/tutorials/secure-postfix-using-lets-encrypt/)

## Postfix y el cifrado de correos con TLS

* [Postfix y el cifrado de correos con TLS](https://github.com/josedom24/curso_correo_electronico_ies/blob/main/modulo4/tls.md)


