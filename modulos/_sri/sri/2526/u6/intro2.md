---
title: "Caso 3: Recibir correos desde internet a usuarios del servidor (desde el escenario de OpenStack)"
---

## Desde el aula

Vamos a tener un correo de la forma `usuario@tunombre.gonzalonazareno.org`. El servidor de correo lo vamos a instalar en el contenedor **horus**.

Tenemos que tener en cuenta los siguientes aspectos:

1. Si queremos recibir correos desde internet a nuestro servidor, todos nuestros dominios tienen que apuntar a nuestra ip pública `5.196.224.198` (IP de `macaco.gonzalonazareno.org`), sin embargo no hay que tocar el DNS de cdmon ya que tenemos un registro genérico que envía a `5.196.224.198` cualquier cosa de `.gonzalonazareno.org` que no tenga un registro tipo ADDRESS. Prueba a hacer un `dig loquesea.gonzalonazareno.org`. Esto se hace con el registro DNS:

		* IN CNAME macaco.gonzalonazareno.org.

	Por lo tanto cuando se recibe un correo en esa dirección pública, lo recibe el servidor de correo que tenemos en `macaco.gonzalonazareno.org`.

2. Tenemos que configurar el servidor de correos de `macaco.gonzalonazareno.org` para que haga relay con los correos cuyo destinos sean nuestros dominios, es decir el correo que vaya a `josedom.gonzalonazareno.org` lo tiene que enviar al servidor de correos de ese dominio, para ello:
    * Añadimos en la directiva `relay_domains`, del servidor de correos de `macaco.gonzalonazareno.org`, cada uno de los nombres de dominios a los que queremos reenviar los mensajes.
	* `macaco.gonzalonazareno.org` tiene como primer DNS a nuestro dns de la red local (**gorila**), por lo que puede preguntarle por nuestro registro MX, ya que tiene delegada todos nuestros subdominios.
    * Para que `macaco.gonzalonazareno.org` conozca la IP de nuestro servidor de correo tendremos que crear un registro MX en nuestro servidor DNS  para realizar la resolución.
	* En la vista externa el registro MX será `ra.tunombre.gonzalonazareno.org`. En las otras vistas, será `horus.tunombre.gonzalonazareno.org`.
	* El correo llegará a **ra** y para reenviarlo a **horus** tendrás que configurar un DNAT del puerto 25/TCP.

3. Con la configuración que tenemos en el servidor de correo de nuestra máquina debe ser suficiente para recibir el correo. Recuerda mandar un mensaje a un usuario que exista en el servidor.

## ¿Los correos que estamos recibiendo son legítimos?

Con la configuración que hemos explicado estaremos en disposición de que nuestro servidor de correo reciba correos de otros MTA. Pero, ¿podemos estar seguros de qué los correos recibidos no son spam?

Más adelante estudiaremos las distintas técnicas para luchar con el problema del **SPAM**. Algunas de ellas están configuradas en nuestro servidor de correos `macaco.gonzalonazareno.org`.