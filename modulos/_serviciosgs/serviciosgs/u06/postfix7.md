---
title: "Soluciones al problema del spam"
permalink: /serviciosgs/u06/postfix7.html
---

## SMTPd restrintions

Con las restricciones postfix podemos limitar el uso de nuestro servidor como cliente para enviar correos y como servidor a la hora de recibir correos. 

Tenemos varias directivas que nos permiten restringuir tanto el envío como la recepción de correos:

* `smtpd_helo_restrictions`: Podemos configurar nuestro servidor de correos para que filtre a los clientes que intentan usarlo por medio de algún parámetro del protocolo: HELO, MAIL FROM, RCPT TO,..., 
* `smtpd_client_restrictions`: Podemos filtrar los dominios de envíos, campo MAIL FROM.
* `smtpd_relay_restrictions`: Podemos filtrar quien tiene permiso para utilziar nuestro servidor como relay.
* `smtpd_recipient_restrictions`: Podemos filtrar los clientes desde los que nos llegan correos. Por ejemplo, podemos hacer una búsqueda en las listas de cloqueo de SPAM (RBL).

Para más información:

* [SMTPd restrictions, SPF, DKIM and greylisting ](https://workaround.org/ispmail/wheezy/smtpd-restrictions-spf-dkim-and-greylisting)
* [Postfix restrictions](https://wiki.centos.org/HowTos/postfix_restrictions)


## SPF

Podríamos hacer que nuestro servidor de correos hiiciera la comprobación del registro SPF del dominio origen del correo.

Para realizar la configuración debemos modificar postfix para que haga la verificación de SPF de los correos recibidos, para lo que instalamos el paquete `postfix-policyd-spf-python` y añadimos la siguiente línea a `/etc/postfix/master.cf`:

    policyd-spf  unix  -       n       n       -       0       spawn     user=policyd-spf argv=/usr/bin/policyd-spf

Se ejecutará un proceso en un socket UNIX para realizar el análisis de SPF, le decimos a postfix que acepte los correos que se validen con SPF realizando la siguiente modificación en /`etc/postfix/main.cf`:
	
    policyd-spf_time_limit = 3600
    smtpd_recipient_restrictions =
    ...
        check_policy_service unix:private/policyd-spf

Probamos a enviar un correo desde otro origen con destino a nuestra máquina y comprobaremos que se realiza la comprobación de spf:

    postfix/smtpd[28324]: connect from X.red-X-X-X.staticip.rima-tde.net[X.X.X.X]
    policyd-spf[28329]: prepend Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=X.X.X.X; helo=X.gonzalonazareno.org; envelope-from=redmine@gonzalonazareno.org; receiver= 
    postfix/smtpd[28324]: E6ECD143: client=X.red-X-X-X.staticip.rima-tde.net[X.X.X.X]
    postfix/cleanup[28330]: E6ECD143: message-id=
    postfix/smtpd[28324]: disconnect from X.red-X-X-X.staticip.rima-tde.net[X.X.X.X] ehlo=1 mail=1 rcpt=1 data=1 quit=1 commands=5
    postfix/qmgr[28052]: E6ECD143: from=, size=3432, nrcpt=1 (queue active)
    postfix/local[28331]: E6ECD143: to=, relay=local, delay=1.9, delays=1.8/0.03/0/0, dsn=2.0.0, status=sent (delivered to maildir)
    postfix/qmgr[28052]: E6ECD143: removed


## DKIM

Podemos configurar nuestro postfix, para que verifique el registro DKIM y valide la firma que trae el correo.

Este apartado hay que terminarlo.

## Antivirus y antispam

En este apartado vamos a realizar una introducción a la configuración de nuestro servidor de correos postfix para que sea capaz de determinar si los correos que le llegan tienen algún virus o son spam. Para ello vamos a utilizar tres programas:

* [amavisd](https://www.ijs.si/software/amavisd/): Es una interfaz entre el servidor de correos y el antivirus y antispam.
* [ClamAV](https://www.clamav.net/): Un antivirus.
* [SpamAssassin](http://spamassassin.apache.org/): Un software para detectar el spam.

Es esquema de funcionamiento es el siguiente::

                                         [SpamAssassin]
	                                            ^
	                                            |
	Email --> [(Port 25) Postfix] --> [(10024) amavisd-new] --> [(10025) Postfix] --> Mailbox
	                                            |
	                                            v
	                                         [ClamAV]

Para seguir investigando:

* [howtoforge - Integrating amavisd-new Into Postfix For Spam- And Virus-Scanning](https://www.howtoforge.com/amavisd_postfix_debian_ubuntu_p2)
* [Correo SPAM](http://spamassassin.apache.org/gtube/gtube.txt)
* [Como probar la efectividad y eficiencia del programa antivirus instalado](https://norfipc.com/virus/probar-antivirus.html)
* [Los test de spamassassin](https://spamassassin.apache.org/old/tests_3_3_x.html)
