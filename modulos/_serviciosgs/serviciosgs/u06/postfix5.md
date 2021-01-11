---
title: "Caso 3: Envío de correos desde internet a usuarios del servidor"
permalink: /serviciosgs/u06/postfix5.html
---

## Desde el aula

Vamos a tener un correo de la forma ``usuario@dominio_de_cada_alumno``, para nuestro ejemplos pongamos ``jose@josedom.gonzalonazareno.org``.

Tenemos que tener en cuenta los siguientes aspectos:

1. Si queremos recibir correos desde internet a nuestro servidor, todos nuestros de dominios tienen que apuntar a nuestra ip pública `80.59.1.152`, sin embargo no hay que tocar el DNS de cdmon ya que tenemos un registro genérico que envía a `80.59.1.152` cualquier cosa de .gonzalonazareno.org que no tenga un registro tipo ADDRESS. Prueba a hacer un ``dig loquesea.gonzalonazareno.org``.
2. Cuando se recibe un correo en esa dirección pública, lo recibe el servidor de correo que tenemos en `babuino-smtp`. Esto lo hace el cortafuegos de `macaco` (regla DNAT).
3. Tenemos que configurar el servidor de correos de `babuino-smtp` para que haga relay con los correos cuyo destinos sean nuestros dominios, es decir el correo que vaya a ``josedom.gonzalonazareno.org`` lo tiene que enviar al servidor de correos de ese dominio, para ello:
    * Añadimos en la directiva ``relay_domains``, del servidor de correos de `babuino-smtp`, cada uno de los nombres de dominios a los que queremos reenviar los mensajes.
    * Para que conozca la IP de nuestro servidor de correo tendremos que crear un registro MX en nuestro servidor DNS  para realizar la resolución.
4. Con la configuración que tenemos en el servidor de correo de nuestra máquina debe ser suficiente para recibir el correo. Recuerda mandar un mensaje a un usuario que exista en el servidor.

## Desde casa

### Usando un nombre de dominio

En este caso vamos a utilizar un nombre de dominio, en mi caso he usado ``josedomingo.org``. Tenemos que tener en cuenta los siguientes aspectos:

1. Configura el servidor postfix en tu ordenador, teniendo en cuenta que en el fichero ``/etc/mailname`` este tu nombre de dominio.
2. Configura tu DNS para que el registro MX apunte a un nombre de ordenador que está definido como un registro A a tu dirección IP pública (si es dinámica y por cualquier motivo te cambia tendrás que actualizar el registro). Ejemplo:

		; <<>> DiG 9.7.3 <<>> -t mx josedomingo.org
		;; global options: +cmd
		;; Got answer:
		;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 9147
		;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 3, ADDITIONAL: 4		

		;; QUESTION SECTION:
		;josedomingo.org.        IN    MX		

		;; ANSWER SECTION:
		josedomingo.org.    900    IN    MX    10 mail2.josedomingo.org.		

		;; AUTHORITY SECTION:
		josedomingo.org.    21600    IN    NS    ns1.cdmon.net.
		josedomingo.org.    21600    IN    NS    ns3.cdmon.net.
		josedomingo.org.    21600    IN    NS    ns2.cdmon.net.		

		;; ADDITIONAL SECTION:
		mail2.josedomingo.org.    900    IN    A    46.234.130.137

3. En tu router haz DNAT para redirigir las peticiones por el puerto 25 al ordenador local que tiene instalado el servidor de correos.

### Usando un nombre de máquina

En el caso de que utilices un servicio gratuito como no-ip o dyndns, estarás reservando un nombre de máquina y no de dominio, por ejemplo ``avatar.dyndns.com``, en este caso no tiene sentido configurar el registro MX:

1. En este caso el nombre de máquina (``avatar.dyndns.com``) por ejemplo, apuntará a tu dirección IP pública.
2. En tu router haz DNAT para redirigir las peticiones por el puerto 25 al ordenador local que tiene instalado el servidor de correos.