---
title: "Instalación y configuración básica de postfix"
---

**Postfix** es un agente de transferencia de correo (*Mail Transfer Agent*, MTA) de código abierto que permite enviar y recibir correos electrónicos mediante SMTP en sistemas Unix y Linux. Destaca por su seguridad, buen rendimiento y facilidad de configuración, siendo una alternativa moderna a MTAs clásicos como Sendmail.

## Instalación de postfix

    apt install postfix


* Tipo de servidor: Internet Site (vamos a recibir y enviar correo directamente)
* Mailname: **DOMINIO**

## Directivas de configuración

Revisemos las directivas a tener en cuenta en nuestra configuración (`/etc/postfix/main.cf`):

* `mydestination`: Observa que en la directiva `mydestination` se indican los dominios que serán propios del servidor de correo, es decir, el correo enviado a estos dominios está dirigido a usuarios del propio servidor. Si el usuario existe, el mensaje será almacenado, sino el servidor devolverá un mensaje de error. Por defecto aparece entre otros: DOMINIO, HOSTNAME, localhost
* `relay_domains`: Con la directiva `relay_domains` indicamos los dominios que serán reenviados. Por lo tanto se permitirán el envío de correos a usuarios de estos dominios.
* `mynetworks`: Con `mynetworks` se indican las IPs desde las que pueden enviarse mensajes. Por defecto: `127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128`
* `myorigin`: Por último, con `myorigin` se indica el dominio con el que el servidor enviará correo, el cual está configurado en `/etc/mailname`. 