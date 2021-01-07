---
title: ¿Cómo funciona el correo eléctronico?
permalink: /serviciosgs/u06/como_funciona_mail.html
---

## Direcciones de correo electrónico

Para enviar un correo necesitamos la dirección de correo de un usuario, la forma de esta dirección es:

    usuario@nombre_servicio_correo

Normalmente el nombre del servicio de correo es el nombre del dominio de la organización a la que pertenece el usuario.

Cuando envíamos un correo a esa dirección, de alguna manera tenemos que determinar la dirección IP del servidor de correo de la organización:

1. Si el nombre detrás de la @ está asociado a un **registro A** en un servidor DNS, ya sabríamos la dirección del servidor de correo.
2. Como hemos comentado, el nombre del servicio de correo es un nombre de dominio que no suele estar asociado a una dirección IP (y menos del servidor de correo). Por lo tanto, es necesario en el servidor dns un **registro MX** que indique el nombre del servidor de correo asociado al nombre de dominio.

## Conceptos:

* **MUA**: Un MUA (Mail User Agent, Agente de usuario de correo) es un programa que permite a un usuario, como mínimo, leer y escribir mensajes de correo electrónico. A un MUA se le denomina a menudo cliente de correo.
* **MTA**: Un programa MTA (Mail Transfer Agent, Agente de transferencia de correo) transfiere los mensajes de correo electrónico entre máquinas que usan el protocolo SMTP. Un mensaje puede pasar por varios MTA hasta llegar al destino final. A un MTA se le denomina a menudo servidor de correo.
* **MDA**: Los agentes MTA utilizan programas MDA (Mail Delivery Agent, Agente de entrega de correo) para entregar el correo electrónico al buzón de un usuario concreto. Esta entrega se puede hacer localmente en el servidor (la realizarán programas llamados LDA (Local Delivery Agent, Agente de entrega local)), o la pueden hacer de forma remota utilizando el protocolo POP3 o IMAP.
* **SMTP**: El protocolo para transferencia simple de correo (en inglés Simple Mail Transfer Protocol o SMTP) es un protocolo de red utilizado para el intercambio de mensajes de correo electrónico. Existe una mejora del protocolo llamada ESMTP (Enhanced Simple Mail Transfer Protocol).
* **POP3**: Mail Delivery Agent [Agente de Entrega de Correo]. Protocolo para recuperar correos electrónicos de un MDA. Su principal característica es que se descargan todos los correos.
* **IMAP**: Internet Message Access Protocol [Protocolo de Acceso a Mensajes de Internet]. Prótocolo para recuperar correos electrónicos de un MDA. En este caso, se sincroniza el estado de los correos entre el servidor y el cliente.

## ¿Cómo mandamos y recuperamos un correo electrónico?

![email](img/E-mail.svg.png)

1. Un usuario utiliza un **MUA** para enviar el correo electrónico a su servidor de correos (**MTA**). Este envío se hace usando el protocolo SMTP. El nombre del servidor tendrá que estar definido en un servidor DNS, y en un principio usamos el puerto 25/TCP. Está conexión no está ni autentificada (no hay que indicar usuario/contraseña), ni cifrada. Ya veremos en la actualidad vamos a usar el protocolo ESMTP, que utiliza otro puerto (587/TCP) y permite la autentificación y el cifrado de la comunicación.
2. El **MTA** recibe el correo desde el **MUA**:
    * Si la dirección del destinatario del correo es la misma que la que controla este servidor: el correo no se envía a ningún **MTA** y se le da al MDA para que lo guarde en el buzón del usuario destinatario.
    * Si la dirección del destinatario es distinta que la que controla este servidor, el correo se mandará al **MTA** correspondiente a la dirección del destinatario, esto se puede hacer de dos formas:
        * Si, por cualquier razón el **MTA** no puede enviar el correo directamente al **MTA** destino, puede tener configurado un servidor **MTA** intermediario (**relay**). Le mandará este correo al **MTA** intermediario que será el responsable de enviarlo al destinatario final.
        * Si el **MTA** no tiene configurado un servidor relay, tendrá que averiguar la dirección IP del servidor correspondiente al nombre de correo del destinatario, normalmente haciendo una consulta MX al sistema DNS. Si reciba varios servidores de correo le intentará mandar el correo al más prioritario (el que tiene el número más pequeño).
3. Cuando el correo llega al **MTA** destino, se pasa el correo al **MDA** que lo guardará en el buzón del usuario destinatario.
4. El usuario destinatario usará una **MUA** para conectarse al servidor **MDA** y recuperar el correo:
    * Puede usar el protocolo **POP3**, por lo que se conectará al servidor POP3. Está conexión está autentificada (tendrá que indicar usuario/contraseña) y puede estar cifrada. El protocolo POP3 suele usar el puerto 110/TCP. Con este protocolo lo que hacemos es descargar todos los correos desde nuestro buzón remoto a nuestro **MUA**.
    * Puede usar el protocolo **IMAP**, por lo que se conectará al servidor IMAP. Está conexión está autentificada (tendrá que indicar usuario/contraseña) y puede estar cifrada. El protocolo IMAP suele usar el puerto 143/TCP. Con este protocolo lo que hacemos es sincronizar el estado de los correos desde nuestro buzón remoto a nuestro **MUA**. De tal manera que podemos acceder desde distintos **MUA** y obtenemos el mismo estado de los correos en todos ellos. Es imprescindible si vamos a usar un **MUA** que sea una aplicación web.

