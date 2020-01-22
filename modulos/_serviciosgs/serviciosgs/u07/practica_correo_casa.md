---
title: "Práctica: Servidor de correos en casa"
permalink: /serviciosgs/u07/practica_correo_casa.html
---
**(9 tareas - 10 puntos)**
{: .notice--warning}

Esta tarea consiste en instalar y configurar un servidor de correo similar al que hemos montado en clase pero utilizando los recursos que tengas en casa (router, ordenador,...)

## Pasos a realizar

* Configura adecuadamente el router de casa para que el puerto 25/tcp de tu equipo sea accesible desde Internet (eso se denomina DNAT o  forwarding)
* Date de alta en un servidor DNS dinámico como `dyndns.org`, `no-ip.com`, `duckdns`, etc. o usa el nombre de dominio propio.
* Si estás utilizando un servicio de DNS dinámico, asegurate que el nombre elegido está apuntando a la IP pública de tu router. Investiga si el servicio elegido te da la opción de automatizar la actualización la dirección IP.
* Si estas usando tu propio nombre de dominio, configura el DNS de tu proveedor para que la máquina a la que apunta el registro MX corresponda a tu IP pública. Quizás debas usar un servicio de DNS dinámico para tener un nombre que apunte a tu IP pública, y luego mediante un registro `CNAME` des de alta el nombre de tu servidor.
* Configura un cliente de correos para poder recibir correos (puedes usar una aplicación de escritorio o instalar un web mail).
* Comprueba que recibes correo desde gmail, hotmail, ...
* Envía desde tu equipo un correo electrónico a hotmail/gmail. Comprueba si llega bien, si lo mete en SPAM o si rebota los mensajes (mira en `/var/log/mail.log`), ya que no acepta correos de direcciones IP dinámicas.
* Configura un registro SPF en tu servidor DNS y vuelve a comprobar si el correo llega a su destinatario.
* Configura postfix para que envíe el correo electrónico a través de servidor SMTP relay (gmail, mailgun, sendgrid,...). Cuando funcione envía un correo a `josedom24@gmail.com`.

{% capture notice-text %}
**Ejericio: Documenta las configuraciones que vas realizando. Muestra comprobaciones (fichero log, capturas de pantalla,...) que comprueben el buen funcionamiento del servidor de correos.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

