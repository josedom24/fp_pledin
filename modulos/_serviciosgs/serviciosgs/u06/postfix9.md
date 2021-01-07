---
title: "Caso 5: Recepción de correo electrónico usando nuestro servidor de correos"
permalink: /serviciosgs/u06/postfix9.html
---

En este caso vamos a utilizar el [protocolo pop3](https://es.wikipedia.org/wiki/Post_Office_Protocol/) y el [protocolo imap](https://es.wikipedia.org/wiki/Internet_Message_Access_Protocol) para obtener los correos electrónicos que hemos recibio en nuestro servidor. 

Ante de ellos tenemos que estudiar los ditintos tipos de buzones donde un servidor de correos puede guardar los mensajes: 

* [Buzón mbox](https://es.wikipedia.org/wiki/Mbox): Todos los mensjaes están en un fichero, es el tipo de buzón que hemos utilizado hasta ahora.
* [Buzón maildir](https://es.wikipedia.org/wiki/Maildir): Los mensajes se guardan en una carpeta. Es imprescindible para que funcione el protocolo imap.

**Configurando un bozón Maildir**

Lo primero que vamos a hacer es configurar postfix para que guarde los correos en un buzón del tipo Maildir, para ello añadimos y modificamos las siguientes directivas de configuración en el fichero de configuración:
	
	home_mailbox = Maildir/
	mailbox_command =

Después de reinicar el servicio los correos se guardarán en un directorio Maildir que se creara en el directorio home de cada usuario.

## Prorocolo pop3

En informática se utiliza el Post Office Protocol (POP3, Protocolo de la oficina de correo) en clientes locales de correo para obtener los mensajes de correo electrónico almacenados en un servidor remoto.

En nuestro caso el servidor pop3 que vamos a instalar se llama dovecot-pop3, para instalarlo, simplemente:

    apt-get install dovecot-pop3d

La configuración que tenemos que realizar es la siguiente: cambiamos en ``/etc/dovecot/conf.d/10-auth.conf``:

    #disable_plaintext_auth = yes    ->    disable_plaintext_auth = no

Para que este habilitada la autentificación con contraseña en claro.

Cambiamos en el fichero ``/etc/dovecot/conf.d/10-mail.conf``, donde se encuentra el buzón:

    #mail_location = mbox:~/mail:INBOX=/var/mail/%u
    mail_location = maildir:~/Maildir

**Configuración del cliente de correo**

Es la hora de configurar un cliente de coreo desde nuestro cliente, en este ejemplo vamos a ver la configuración en evolution. Además tenemos que tener creados en el DNS de nuestro servidor los nombres ``pop3.josedom.gonzalonazareno.org``.

## Protocolo imap

Internet Message Access Protocol, o su acrónimo IMAP, es un protocolo de red de acceso a mensajes electrónicos almacenados en un servidor. Mediante IMAP se puede tener acceso al correo electrónico desde cualquier equipo que tenga una conexión a Internet. IMAP tiene varias ventajas sobre POP, que es el otro protocolo empleado para obtener correo desde un servidor. Por ejemplo, es posible especificar en IMAP carpetas del lado servidor. Por otro lado, es más complejo que POP ya que permite visualizar los mensajes de manera remota y no descargando los mensajes como lo hace POP.

Para instalar el servidor IMAP ejecutamos la siguiente instrucción:

    apt-get install dovecot-imapd

Ya podríamos configurar nuestro cliente de correos para recibir correo utilizando el protocolo imap, para ello tendríamos creado un nombre en el servidor DNS, por ejemplo, ``imap.josedom.gonzalonazreno.org``.

Podrías hacer la prueba de ver la diferencia entre los dos protocolos: si usas pop3 los correos se borran del servidor (hay que configurar algunos clientes para que funcionen de esta forma) y cómo sin embargo al usar el servidor imap los correos no se borran del servidor.
{: .notice--warning}

En este caso también puedes instalar un cliente web de correos para leer los correos del servidor. Hay muchas: squirrelmail, round cube, horde, ...