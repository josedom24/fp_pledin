# Caso 2: Envío de correo desde usuarios del servidor a correos de internet (desde el escenario de OpenStack)

## Desde el aula

Para que un equipo envíe correos al exterior, es necesario que se cumplan varios puntos:

* Disponer de una **IP pública** asociada al VPS.
* Tener configurado un **nombre de host completo (FQDN)** para el servidor (por ejemplo, `mail.midominio.com`).
* Verificar que el **puerto 25/tcp** no está bloqueado por el proveedor del VPS.

En nuestro caso vamos a enviar correos desde la máquina **horus**, que no tiene una IP pública, además, por seguridad, en nuestra red sólo puede enviar correo el servidor de correo de `macaco.gonzalonazareno.org`. Por lo tanto tenemos que configurar nuestro servidor para que utilice este servidor como relay para enviar nuestros correos, para que sea más sencillo hemos creado un alias llamado `mail.gonzalonazareno.org`. Para ello, modificamos la siguiente directiva en el fichero de configuración del servidor Postfix que hemos instalado en **horus**:

	relayhost = mail.gonzalonazareno.org


Incluso cumpliendo los requisitos anteriores, es posible que los servidores de destino no acepten nuestros correos como válidos. Para ello, es necesario implementar una serie de mecanismos que permiten **verificar la legitimidad del correo**. Los correos que mandamos deben cumplir las siguientes estándares:

* **SPF**: autoriza qué servidores pueden enviar correo en nombre de un dominio.
* **DKIM**: garantiza la integridad del mensaje mediante firma criptográfica.
* **DMARC**: indica al servidor receptor qué hacer si SPF o DKIM fallan (rechazar, marcar como spam, etc.).

Pero, como en realidad el servidor que manda el correo al exterior es `macaco.gonzalonazareno.org`, el administrador de ese servidor ya los ha configurado de manera adecuada.


### Envío de un correo de prueba

Desde el servidor cliente podemos enviar un correo utilizando la utilidad `mail`:

```
debian@maquina:~$ mail josedom24@josedomingo.org
Subject: Hola
Que tal
Cc: 
```

El correo no se enviará directamente al destinatario final, sino que será entregado al servidor relay, que lo procesará y enviará según su configuración.

### Comprobación del log

Podemos verificar el funcionamiento revisando el log de Postfix en el servidor cliente:

```
debian@maquina:~$ sudo journalctl -u postfix
...
...

```

Como se observa, el correo ha sido reenviado correctamente al servidor relay de la red local.

## Envío de correo desde otros servidores de nuestra red local

En una red local es habitual disponer de **un único servidor de correo saliente** (en nuestro caso `horus.tunombre.gonzalonazareno.org`), encargado de enviar los correos hacia el exterior. Por motivos de **seguridad y control**, el puerto **25/tcp** suele estar abierto únicamente en este servidor, evitando que el resto de máquinas de la red envíen correo directamente a Internet.

En este escenario, los servidores de la red que necesitan enviar correos (por ejemplo, para notificaciones del sistema, tareas programadas o aplicaciones) no actúan como servidores de correo completos. En su lugar, utilizan un **servidor relay** al que reenvían todo el correo saliente.

### Configuración como *Satellite system*

Para ello, instalamos Postfix en los servidores clientes configurándolo en modo **Satellite system**. En este modo, Postfix **no recibe correo desde la red** y únicamente se encarga de reenviar los mensajes al servidor de correo central.

Durante la instalación de Postfix seleccionamos la opción *Satellite system* e indicamos como **relayhost** el servidor de correo de la red local.

### Ejemplo de configuración

En nuestra red local el servidor de correo se llama `horus.tunombre.gonzalonazareno.org`. En el servidor cliente, el parámetro `relayhost` quedará configurado de la siguiente forma en el fichero `/etc/postfix/main.cf`:

```

relayhost = horus.tunombre.gonzalonazareno.org
```

De este modo, cualquier correo enviado desde el servidor será reenviado automáticamente al servidor relay, que será el encargado de realizar la entrega final.