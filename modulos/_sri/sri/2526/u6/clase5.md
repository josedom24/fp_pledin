---
title: "Caso 2b: Envío de correo a través de un servidor relay en la red local"
---

En una red local es habitual disponer de **un único servidor de correo saliente**, encargado de enviar los correos hacia el exterior. Por motivos de **seguridad y control**, el puerto **25/tcp** suele estar abierto únicamente en este servidor, evitando que el resto de máquinas de la red envíen correo directamente a Internet.

En este escenario, los servidores de la red que necesitan enviar correos (por ejemplo, para notificaciones del sistema, tareas programadas o aplicaciones) no actúan como servidores de correo completos. En su lugar, utilizan un **servidor relay** al que reenvían todo el correo saliente.

### Configuración como *Satellite system*

Para ello, instalamos Postfix en los servidores clientes configurándolo en modo **Satellite system**. En este modo, Postfix **no recibe correo desde la red** y únicamente se encarga de reenviar los mensajes al servidor de correo central.

Durante la instalación de Postfix seleccionamos la opción *Satellite system* e indicamos como **relayhost** el servidor de correo de la red local.

### Ejemplo de configuración

En nuestra red local el servidor de correo se llama `mail.gonzalonazareno.org`. En el servidor cliente, el parámetro `relayhost` quedará configurado de la siguiente forma en el fichero `/etc/postfix/main.cf`:

```

relayhost = mail.gonzalonazareno.org
```

De este modo, cualquier correo enviado desde el servidor será reenviado automáticamente al servidor relay, que será el encargado de realizar la entrega final.

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


