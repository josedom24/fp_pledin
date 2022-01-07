---
title: "Caso 4: Recepción de correo electrónico usando nuestro servidor de correos"
---

## Protocolos para recibir el correo

Si utilizamos un cliente de correo (MUA) externo para leer el correo guardado en el servidor de correos podemos usar dos protocolos de comunicación:

* **POP3**: Mail Delivery Agent [Agente de Entrega de Correo]. Protocolo para recuperar correos electrónicos de un MDA. Su principal característica es que se descargan todos los correos.
* **IMAP**: Internet Message Access Protocol [Protocolo de Acceso a Mensajes de Internet]. Prótocolo para recuperar correos electrónicos de un MDA. En este caso, se sincroniza el estado de los correos entre el servidor y el cliente.

En nuestro caso **vamos a trabajar con IMAP** que es el protocolo que actualmente se utiliza para poder leer nuestro correo desde distintos clientes de correos al no descargar todos los correos del buzón.

La comunicación con estos protocolos es autentificada y debería ser cifrada. 

## Tipos de buzones

Los buzones son los espacios usados por el servidor de correo para guardar los correos de un usuarios, hasta que este lo lee. Tenemos dos tipos:

* [Buzón mbox](https://es.wikipedia.org/wiki/Mbox): Todos los mensajes están en un fichero, es el tipo de buzón que hemos utilizado hasta ahora, y puede ser válido para el protocolo POP3 donde se descargan todos los correos desde el servidor.
* [Buzón maildir](https://es.wikipedia.org/wiki/Maildir): Los mensajes se guardan en una carpeta. Es imprescindible para que funcione el protocolo IMAP.

### Configurando un buzón Maildir

Lo primero que vamos a hacer es configurar postfix para que guarde los correos en un buzón del tipo *Maildir*, para ello añadimos y modificamos las siguientes directivas de configuración en el fichero de configuración:
	
	home_mailbox = Maildir/
	mailbox_command =

Después de reiniciar el servicio los correos se guardarán en un directorio `Maildir` que se creara en el directorio home de cada usuario.

**Desde este momento no podrás leer los correos con la herramienta `mail` podrías usar otro cliente para leer los correos desde la línea de comandos del servidor, por ejemplo `mutt`.**

## Protocolo IMAP

Internet Message Access Protocol, o su acrónimo IMAP, es un protocolo de red de acceso a mensajes electrónicos almacenados en un servidor. Mediante IMAP se puede tener acceso al correo electrónico desde cualquier equipo que tenga una conexión a Internet. IMAP tiene varias ventajas sobre POP, que es el otro protocolo empleado para obtener correo desde un servidor. Por ejemplo, es posible especificar en IMAP carpetas del lado servidor. Por otro lado, es más complejo que POP ya que permite visualizar los mensajes de manera remota y no descargando los mensajes como lo hace POP.

El protocolo imap utiliza el puerto 143/tcp. La comunicación es autentificada y sería muy conveniente que fuera cifrada. Para cifrar la comunicación tenemos dos opciones:

* **IMAP con STARTTLS**: STARTTLS transforma una conexión insegura en una segura mediante el uso de SSL/TLS. Por lo tanto usando el mismo puerto 143/tcp tenemos cifrada la comunicación.
* **IMAPS**: Versión segura del protocolo IMAP que usa el puerto 993/tcp.

Nosotros vamos a usar el programa `dovecot` como servidor IMAP:

    apt-get install dovecot-imapd

Ya podríamos configurar nuestro cliente de correos para recibir correo utilizando el protocolo imap, para ello tendríamos creado un nombre en el servidor DNS, por ejemplo, ``imap.josedom.gonzalonazareno.org``.

Para cifrar la comunicación, nosotros vamos a usar un certificado firmado por LetsEncypt.

En este caso también puedes instalar un cliente web de correos para leer los correos del servidor. Hay muchas: round cube, horde, rainloop, SquirrelMail, ...