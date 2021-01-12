---
title: "Caso 3: Recibir correos desde internet a usuarios del servidor"
permalink: /serviciosgs/u06/postfix5.html
---

## Desde el aula

Vamos a tener un correo de la forma ``usuario@dominio_de_cada_alumno``, para nuestro ejemplos pongamos ``jose@josedom.gonzalonazareno.org``.

Tenemos que tener en cuenta los siguientes aspectos:

1. Si queremos recibir correos desde internet a nuestro servidor, todos nuestros dominios tienen que apuntar a nuestra ip pública `80.59.1.152`, sin embargo no hay que tocar el DNS de cdmon ya que tenemos un registro genérico que envía a `80.59.1.152` cualquier cosa de .gonzalonazareno.org que no tenga un registro tipo ADDRESS. Prueba a hacer un ``dig loquesea.gonzalonazareno.org``. Esto se hace con el registro DNS:

		* IN CNAME macaco.gonzalonazareno.org.

2. Cuando se recibe un correo en esa dirección pública, lo recibe el servidor de correo que tenemos en `babuino-smtp`. Esto lo hace el cortafuegos de `macaco` (regla DNAT).
3. Tenemos que configurar el servidor de correos de `babuino-smtp` para que haga relay con los correos cuyo destinos sean nuestros dominios, es decir el correo que vaya a ``josedom.gonzalonazareno.org`` lo tiene que enviar al servidor de correos de ese dominio, para ello:
    * Añadimos en la directiva ``relay_domains``, del servidor de correos de `babuino-smtp`, cada uno de los nombres de dominios a los que queremos reenviar los mensajes.
    * Para que `babuino-smtp` conozca la IP de nuestro servidor de correo tendremos que crear un registro MX en nuestro servidor DNS  para realizar la resolución.
4. Con la configuración que tenemos en el servidor de correo de nuestra máquina debe ser suficiente para recibir el correo. Recuerda mandar un mensaje a un usuario que exista en el servidor.

##  Desde tu servidor OVH

En este caso vamos a utilizar un nombre de dominio: `iesgnXX.es`. Tenemos que tener en cuenta los siguientes aspectos:

1. Configura el servidor postfix en tu servidor, teniendo en cuenta que en el fichero ``/etc/mailname`` este tu nombre de dominio.
2. Configura tu DNS para que el registro MX apunte a un nombre de ordenador que está definido como un registro A a tu dirección IP pública. Ejemplo:

		# dig mx iesgnXX.es
		; <<>> DiG 9.7.3 <<>> -t mx iesgnXX.es
		;; global options: +cmd
		;; Got answer:
		;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 9147
		;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 3, ADDITIONAL: 4		

		;; QUESTION SECTION:
		;iesgnXX.es.        IN    MX		

		;; ANSWER SECTION:
		iesgnXX.es.    900    IN    MX    10 tumaquina.iesgnXX.es.		

		;; ADDITIONAL SECTION:
		tumaquina.ieshnXX.es.    900    IN    A    XX.XX.XX.XX

3. Recuerda que el correo se guardará en el buzón del usuario, que tendrá que leerlo desde el servidor con la utilidad `mail`.
