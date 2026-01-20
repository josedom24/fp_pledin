---
title: "Caso 1:  Envío local, entre usuarios del mismo servidor"
---

En este primer caso, vamos a usar el servidor de correo para el envío de correos entre usuarios de la máquina, disponiendo de correo interno. 

## Envío de correos

Para el envío de correo vamos a usar la utilidad `mail` (se encuentra en el paquete `bsd-mailx`). Y para enviar un correo desde el usuario `debian` al usuario `usuario`:


Instalamos el cliente de correos mail:

```
sudo apt install bsd-mailx
```

Ahora enviamos el correo:

```
debian@maquina:~$ mail usuario@localhost
Subject: Hola
Esto es una prueba
Cc: 
```

**Recuerda que para terminar de escribir el cuerpo del mensaje hay que ponerse en una nueva línea e introducir CTRL+D.**

Para leer el correo el usuario `usuario` ejecuta la instrucción `mail`:

```
usuario@maquina:~$ mail
Mail version 8.1.2 01/15/2001.  Type ? for help.
"/var/mail/usuario": 1 message 1 new
>N  1 debian@midominio  Wed Dec 17 19:01   18/534   Hola
& 1
```

Introducimos el número de correo para leerlo.

Como vemos el buzón del usuario está en `/var/mail/usuario`. Los correos leídos se guardan en `~/mbox`.


Podemos comprobar el log del servidor de correo:

```
sudo journalctl -u postifx
...
Dec 17 19:01:21 glpi postfix/pickup[12220]: 8568C6A46B: uid=1000 from=<debian>
Dec 17 19:01:21 glpi postfix/cleanup[12368]: 8568C6A46B: message-id=<20251217190121.8568C6A46B@glpi>
Dec 17 19:01:21 glpi postfix/qmgr[12221]: 8568C6A46B: from=<debian@josedomingo.org>, size=389, nrcpt=1 (queue active)
Dec 17 19:01:21 glpi postfix/local[12370]: 8568C6A46B: to=<usuario@localhost>, relay=local, delay=0.02, delays=0.01/0.01/0/0, dsn=2.0.0, status=sent (delivered to mailbox)
Dec 17 19:01:21 glpi postfix/qmgr[12221]: 8568C6A46B: removed
```


{% capture notice-text %}
## Ejercicio 1 taller 1

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>





