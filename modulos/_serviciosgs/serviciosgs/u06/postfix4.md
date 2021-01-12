---
title: "Caso 2: Envío de correo desde usuarios del servidor a correos de internet"
permalink: /serviciosgs/u06/postfix4.html
---

## Desde el aula

En el caso de la configuración de nuestra red del instituto, sólo puede enviar correo el servidor de correo de `babuino-smtp`. Por lo tanto tenemos que configurar nuestro servidor para que utilice a `babuino-smtp` como relay para enviar nuestros correos, para ello, modificamos la siguiente directiva en el fichero de configuración:

	ralayhost = babuino-smtp.gonzalonazareno.org

## Desde tu servidor OVH

¿Qué necesitamos para que desde nuestro servidor OVH podamos mandar correos al exterior?:

* Con la configuración básica del servidor, seríamos capaces de enviar el correo (no necesitamos un relay).
* Quizás no sea necesario para el envío de correos, pero estaría muy bien que ya tengamos configurado en nuestro DNS el registro MX apuntando a nuestra máquina.
* El servidor de correo al que mandamos el correo confía en que el correo que le ha llegado proviene de un servidor de correo legítimo de nuestro dominio.

Para contestar a esta pregunta tenemos que considerar varias cosas:

* Es posible que si mandamos el correo desde un servidor que utilice una ip dinámica, seguramente gmail /hotmail/yahoo lo rechaza, por estar en una lista de bloqueo, al intentar enviar un correo nos salen registro de este tipo:
 un correo nos salen registro de este tipo:

	![postfix6](img/postfix4.jpg)

* Para solucionar este problema (es decir, para que el servidor de destine confíe en nuetro servidor) tenemos varias soluciones: [Soluciones al problema del spam](postfix7.html).

En nuestro caso cómo mínimo vamos a usar un registro SPF:

* **Sender Policy Framework (SPF)**: Esta técnica consiste en publicar una serie de datos en un registro TXT del servidor DNS que haga que el servidor de correo donde llega el correo confíe en que el correo no es spam. Para más información lee el artículo: [Sender Policy Framework (SPF)](https://github.com/josedom24/serviciosgs_doc/raw/master/correo/doc/SPF.pdf)
