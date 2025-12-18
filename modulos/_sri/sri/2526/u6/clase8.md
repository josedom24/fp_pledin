---
title: "Caso 4: Recepción de correo electrónico usando nuestro servidor de correos"
---

## Protocolos para recibir el correo

Si utilizamos un cliente de correo (MUA) externo para leer el correo almacenado en nuestro servidor de correos, podemos usar dos protocolos:

* **POP3**: *Post Office Protocol*. Protocolo que permite descargar los correos electrónicos almacenados en el servidor al cliente. Una vez descargados, normalmente se eliminan del servidor.
* **IMAP**: *Internet Message Access Protocol*. Protocolo que permite acceder a los correos electrónicos almacenados en el servidor, manteniendo sincronizado el estado de los mensajes entre el servidor y uno o varios clientes.

En nuestro caso **vamos a trabajar con IMAP**, ya que es el protocolo que se utiliza actualmente cuando se accede al correo desde distintos clientes sin descargar los mensajes del servidor.

La comunicación mediante estos protocolos es **autenticada** y es muy recomendable que esté **cifrada**.

## Tipos de buzones

Los buzones son los espacios que utiliza el servidor de correo para almacenar los mensajes de los usuarios hasta que estos los leen. Existen dos formatos principales:

* **Buzón mbox**: todos los mensajes se almacenan en un único fichero. Es el formato que hemos utilizado hasta ahora y puede ser válido para escenarios sencillos o para el uso con POP3.
* **Buzón Maildir**: los mensajes se almacenan como ficheros individuales dentro de un directorio. Es el formato **recomendado** cuando se utiliza IMAP, ya que evita problemas de bloqueo y permite el acceso concurrente.

### Configuración de un buzón Maildir

Para utilizar IMAP es recomendable que los correos se almacenen en formato *Maildir*. Para ello configuramos Postfix modificando o añadiendo las siguientes directivas en su fichero de configuración:

```

home_mailbox = Maildir/
mailbox_command =

```

De este modo, los correos se guardarán en un directorio llamado `Maildir` que se creará en el directorio `home` de cada usuario.

**A partir de este momento no podremos leer los correos con la herramienta `mail`**, que está pensada para buzones del tipo *mbox*. Para leer el correo desde la línea de comandos del servidor podemos utilizar otros clientes como `mutt`.

## Protocolo IMAP

**Internet Message Access Protocol (IMAP)** es un protocolo de red que permite acceder a los correos electrónicos almacenados en un servidor desde cualquier equipo con conexión a Internet. A diferencia de POP3, IMAP permite trabajar con los mensajes de forma remota, manteniendo su estado sincronizado entre el servidor y los clientes.

IMAP ofrece, entre otras ventajas:
* Acceso al correo desde múltiples dispositivos.
* Gestión de carpetas en el servidor.
* Sincronización del estado de los mensajes (leído, no leído, borrado).

El protocolo IMAP utiliza el puerto **143/tcp**. La comunicación es autenticada y es muy recomendable que esté cifrada. Para cifrar la comunicación existen dos opciones:

* **IMAP con STARTTLS**: utiliza el puerto 143/tcp y establece una conexión cifrada mediante TLS.
* **IMAPS**: versión segura de IMAP que utiliza directamente el puerto **993/tcp**.

## Servidor IMAP: Dovecot

Para proporcionar acceso IMAP a los buzones de los usuarios utilizaremos el servidor **Dovecot**. En este caso, Postfix se encarga de recibir y entregar los correos, mientras que Dovecot permite a los usuarios acceder a sus buzones mediante IMAP.

Instalamos el servidor IMAP:

```

apt-get install dovecot-imapd

```

Una vez instalado y configurado Dovecot, ya podríamos configurar un cliente de correo para recibir mensajes utilizando IMAP. Para ello, normalmente se define un nombre en el DNS del servidor, por ejemplo:

```
imap.tudominio.org
```

## Cifrado de la comunicación

Para cifrar la comunicación IMAP utilizaremos un certificado digital. En este caso, podemos emplear un certificado firmado por **Let’s Encrypt**, que deberá coincidir con el nombre del servidor IMAP configurado.

## Acceso mediante webmail

Además de utilizar clientes de correo tradicionales, también es posible acceder al correo mediante un **cliente web**. Existen múltiples soluciones, como por ejemplo:

* Roundcube
* Horde
* RainLoop
* SquirrelMail

Estas aplicaciones permiten acceder al correo desde un navegador web utilizando IMAP como protocolo de acceso.

{% capture notice-text %}
## Práctica 2/2




{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>