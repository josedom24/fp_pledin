---
title: "Antispam y antivirus en nuestro servidor de correos"
permalink: /serviciosgs/u06/postfix10.html
---

En este apartado vamos a realizar una introducción a la configuración de nuestro servidor de correos postfix para que sea capaz de determinar si los correos que le llegan tienen algun virus o son spam. Para ello vamos a utilizar tres programas:

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


Os voy a dejar los pasos para realizar la instalación, este manual nace de mi experiencia, si veis algún cambio o hay algo incorrecto, por favor decírmelo. Empezamos con la instalación (vamos a instalar los todos los paquetes necesarios)::

	apt-get install amavisd-new spamassassin clamav clamav-daemon

Instalamos descompresores y utilidades::

	apt-get install unrar-free zoo unzip bzip2 libnet-ph-perl libnet-snpp-perl libnet-telnet-perl nomarch lzop

## amavisd

En el fichero ``/etc/amavis/conf.d/15-content_filter_mode`` descomentamos las siguientes líneas si vamos a activar el antivirus::

	@bypass_virus_checks_maps = (
   		\%bypass_virus_checks, \@bypass_virus_checks_acl, \$bypass_virus_checks_re);

Y las siguientes si vamos a activar el antispam::

	@bypass_spam_checks_maps = (
   		\%bypass_spam_checks, \@bypass_spam_checks_acl, \$bypass_spam_checks_re);


En el fichero ``etc/amavis/conf.d/20-debian_defaults``, configuramos que hacer con los correos sospechosos, la configuración que viene por defecto es correcta pero podemos hacer algunos cambios, por ejemplo podemos dejar pasar el spam, aunque lo marquemos::

	$final_spam_destiny = D_PASS;

Por último::

	adduser clamav amavis
	systemctl restart amavis

Para que amavis pueda comunicar con postfix, añadimos a la configuración las siguientes líneas::

	postconf -e 'content_filter = amavis:[127.0.0.1]:10024'
	postconf -e 'receive_override_options = no_address_mappings'

Añadimos las siguientes líneas al fichero ``/etc/postfix/master.cf``::

	amavis unix - - - - 2 smtp
	        -o smtp_data_done_timeout=1200
	        -o smtp_send_xforward_command=yes	

	127.0.0.1:10025 inet n - - - - smtpd
	        -o content_filter=
	        -o local_recipient_maps=
	        -o relay_recipient_maps=
	        -o smtpd_restriction_classes=
	        -o smtpd_client_restrictions=
	        -o smtpd_helo_restrictions=
	        -o smtpd_sender_restrictions=
	        -o smtpd_recipient_restrictions=permit_mynetworks,reject
	        -o mynetworks=127.0.0.0/8
	        -o strict_rfc821_envelopes=yes
	        -o receive_override_options=no_unknown_recipient_checks,no_header_body_checks
	        -o smtpd_bind_address=127.0.0.1

Y podemos ver los puertos por los que se está escuchando::

	tcp        0      0 127.0.0.1:10024         0.0.0.0:*               LISTEN      18955/amavisd-new (
	tcp        0      0 127.0.0.1:10025         0.0.0.0:*               LISTEN      19134/master    
	tcp        0      0 127.0.0.1:783           0.0.0.0:*               LISTEN      16089/spamassassin.
	tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      19134/master    


## clamav

Actualizamos el antivirus::

	freshclam
	systemctl restart clamav-daemon

## spamassassin

Lo activamos en el fichero ``/etc/default/spamassassin``::

	ENABLED=1

El fichero de configuración es ``/etc/spamassassin/local.cf``

Para más información puedes leer los siguientes artículos:

* [howtoforge - Integrating amavisd-new Into Postfix For Spam- And Virus-Scanning](https://www.howtoforge.com/amavisd_postfix_debian_ubuntu_p2)
* [Correo SPAM](http://spamassassin.apache.org/gtube/gtube.txt)
* [Como probar la efectividad y eficiencia del programa antivirus instalado](https://norfipc.com/virus/probar-antivirus.html)
* [Los test de spamassassin](https://spamassassin.apache.org/old/tests_3_3_x.html)
