---
title: "Caso 3: Recibir correos desde internet a usuarios del servidor"
---

En este caso vamos a configurar nuestro **VPS como servidor de correo receptor**, de forma que pueda **recibir correos desde Internet** dirigidos a los usuarios locales del sistema, utilizando **nuestro nombre de dominio**.

Para que esto sea posible, debemos tener en cuenta varios aspectos fundamentales.

## Configuración del servidor de correo

En primer lugar, debemos configurar **Postfix** en nuestro servidor. Es importante que en el fichero `/etc/mailname` aparezca **nuestro nombre de dominio**, ya que será el dominio que identifique al servidor de correo.

Además, el servidor debe tener configurado un **nombre de host completo (FQDN)**, normalmente el mismo que utilizaremos en el registro MX, por ejemplo:

```
mail.tudominio.org
```

Postfix debe estar escuchando en el **puerto 25/tcp**, y el firewall del VPS debe permitir conexiones entrantes a dicho puerto para que otros servidores de correo puedan conectarse.

## Configuración del DNS

Para que otros servidores de correo sepan a qué máquina deben enviar los mensajes destinados a nuestro dominio, es necesario configurar correctamente el **registro MX** en el DNS.

El registro MX debe apuntar a un **nombre de máquina**, que a su vez debe tener un **registro A** asociado a la dirección IP pública del VPS.

Ejemplo:

```

# dig mx tudominio.org

; <<>> DiG 9.7.3 <<>> -t mx tudominio.org
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 9147
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 3, ADDITIONAL: 4

;; QUESTION SECTION:
;tudominio.org.        IN    MX

;; ANSWER SECTION:
tudominio.org.    900    IN    MX    10 mail.tudominio.org.

;; ADDITIONAL SECTION:
mail.tudominio.org.    900    IN    A    XX.XX.XX.XX

```

En este ejemplo, los correos enviados a `@tudominio.org` serán entregados al servidor `mail.tudominio.org`, cuya dirección IP pública es `XX.XX.XX.XX`.

## Recepción del correo

Una vez configurado el servidor y el DNS, nuestro VPS estará en disposición de **recibir correos desde otros MTAs de Internet**. Los mensajes recibidos se almacenarán en el **buzón local del usuario destinatario**.

Cada usuario podrá leer su correo directamente en el servidor utilizando la utilidad `mail`, tal y como se ha visto en los casos anteriores.

## ¿Los correos que recibimos son legítimos?

Con la configuración descrita hasta ahora, nuestro servidor de correo **acepta correos entrantes**, pero **no distingue todavía si los mensajes son legítimos o spam**.

Es decir:
* cualquier servidor puede intentar enviar correo a nuestro dominio,
* no se comprueba aún la autenticidad del emisor,
* ni se aplican políticas antispam o de validación.

En el siguiente apartado, **Soluciones al problema del spam**, veremos cómo configurar nuestro servidor de correo para comprobar si los correos recibidos son válidos y legítimos. Para ello, se analizarán los mecanismos **SPF, DKIM y DMARC del emisor**, permitiendo decidir si un mensaje debe aceptarse, marcarse como spam o rechazarse.

## Alias y redirecciones

### Alias

Cuando se define un alias para un determinado usuario se redirige el correo que llegue a otro usuario de la misma máquina. Los alias de correo se utilizan principalmente para gestionar el correo de las "cuentas de administración" y se definen en el fichero `/etc/aliases`, que tiene el siguiente aspecto:

	# /etc/aliases
	mailer-daemon: postmaster
	postmaster: root
	nobody: root
	hostmaster: root
	usenet: root
	news: root
	webmaster: root
	www: root
	ftp: root
	abuse: root
	noc: root
	security: root
	www-data: root
	logcheck: root
	root: alberto, jose, raul

En este caso el correo que llega a los usuarios `postmaster`, `webmaster`, etc. se redirige a la cuenta de `root`, que a su vez se redirige a los usuarios reales `alberto`, `jose` y `raul`, que son los administradores del equipo.

Cada vez que se modifica el fichero `/etc/aliases` hay que ejecutar la instrucción `newaliases` para que los cambios tengan efecto.

### Redirecciones

Una redirección se utiliza para enviar el correo que llegue a un usuario a una cuenta de correo exterior. Para usuarios reales las redirecciones se definen en el fichero `~/.forward` y el formato de este fichero es simplemente un listado de cuentas de correo a las que se quiere redirigir el correo.