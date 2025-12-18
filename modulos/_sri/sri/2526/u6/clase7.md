---
title: Soluciones al problema del spam
---

Para reducir el correo no deseado y los intentos de suplantación de identidad, los servidores de correo modernos aplican distintos mecanismos de validación. En este curso nos centraremos principalmente en **SPF, DKIM y DMARC**, que permiten verificar la legitimidad del servidor y del dominio emisor.

Existen además otras técnicas complementarias, que se nombran brevemente al final de este apartado.


## SPF

Una de las primeras comprobaciones que puede realizar un servidor de correo al recibir un mensaje es verificar el **registro SPF** del dominio emisor. De este modo se comprueba si la dirección IP desde la que se envía el correo está autorizada a enviar mensajes en nombre de dicho dominio.

### Configuración de la comprobación SPF en Postfix

Para que Postfix realice la verificación SPF de los correos recibidos, instalamos el siguiente paquete:

```
apt install postfix-policyd-spf-python
```

A continuación, añadimos el servicio de comprobación SPF en el fichero `/etc/postfix/master.cf`:

```
policyd-spf  unix  -       n       n       -       0       spawn user=policyd-spf argv=/usr/bin/policyd-spf
```

Este servicio se ejecutará a través de un **socket UNIX** y será utilizado por Postfix para evaluar el registro SPF del dominio emisor.

Después, indicamos en `/etc/postfix/main.cf` que se utilice este servicio dentro de las restricciones del destinatario:

```

policyd-spf_time_limit = 3600
smtpd_recipient_restrictions =
...
check_policy_service unix:private/policyd-spf
```

### Comprobación del funcionamiento de SPF

Al recibir un correo desde otro servidor, podemos comprobar en los logs que se ha realizado la validación SPF:

```
postfix/smtpd[28324]: connect from X.red-X-X-X.staticip.rima-tde.net[X.X.X.X]
policyd-spf[28329]: prepend Received-SPF: Pass (mailfrom)
postfix/smtpd[28324]: disconnect from X.red-X-X-X.staticip.rima-tde.net[X.X.X.X]
```

En este caso, el resultado **Pass** indica que el servidor emisor está autorizado según el registro SPF del dominio.


## DKIM

Además de SPF, los correos recibidos pueden incluir una **firma DKIM**, que permite verificar que el mensaje no ha sido modificado durante el transporte y que está asociado a un dominio concreto.

En nuestro servidor ya tenemos configurado **OpenDKIM** con el modo de funcionamiento:

```
Mode sv
```

Esto permite que el servidor:
* firme los correos salientes (*signing*)
* verifique las firmas DKIM de los correos entrantes (*verification*)

La verificación DKIM no implica por sí misma el rechazo del correo, sino que proporciona información adicional que podrá ser utilizada por otros mecanismos como DMARC.


## DMARC

**DMARC** permite al propietario de un dominio definir una **política** que indica qué debe hacer el servidor receptor cuando un mensaje no supera las comprobaciones de SPF y/o DKIM.

Para que **Postfix en Debian verifique políticas DMARC de los correos entrantes** necesitas usar un **milter especializado** como **OpenDMARC**, que es la implementación estándar para comprobar DMARC contra los resultados de SPF y DKIM. A continuación te explico **cómo configurarlo y comprobarlo** de forma que funcione con Postfix.

### Instalar el verificador DMARC

Postfix por sí mismo **no verifica DMARC**. Debemos instalar el paquete **OpenDMARC**, disponible en los repositorios de Debian:

```bash
sudo apt update
sudo apt install opendmarc
```

Esto instalará el servicio que puede **leer los encabezados SPF y DKIM** producidos por los demás milters y aplicar la política DMARC. 

### Configurar OpenDMARC

Edita el fichero de configuración de OpenDMARC (`/etc/opendmarc.conf`) para ajustar algunos parámetros:

Ejemplo mínimo de configuración:

```
AuthservID mail.midominio.org
Socket local:/var/spool/postfix/opendmarc/opendmarc.sock
PidFile /var/run/opendmarc/opendmarc.pid
RejectFailures false
Syslog true
```

* **AuthservID**: nombre con el que OpenDMARC identifica tu servidor.
* **Socket**: ruta al socket donde Postfix se conectará al servicio.
* **RejectFailures**: si se pone a `true`, OpenDMARC puede rechazar correos que *fallan* DMARC; si está en `false`, solo marca el resultado para que tú decidas qué hacer.

Crea también el directorio para el socket de Postfix y ajusta permisos si es necesario:

```bash
sudo mkdir -p /var/spool/postfix/opendmarc
sudo chown opendmarc:opendmarc /var/spool/postfix/opendmarc
```

### Integrar OpenDMARC con Postfix

En el fichero principal de Postfix (`/etc/postfix/main.cf`), hay que agregar **OpenDMARC como milter**:

```
smtpd_milters = unix:/var/spool/postfix/opendmarc/opendmarc.sock
non_smtpd_milters = $smtpd_milters
milter_default_action = accept
milter_protocol = 2
```

Esto indica a Postfix que utilice **el milter de OpenDMARC** durante la recepción de correos. ([blog.cyberfront.org][2])

Después de configurar ambos:

```bash
sudo systemctl restart opendmarc
sudo systemctl restart postfix
```


### Cómo comprobar que la verificación DMARC funciona

Tenemos que ver las cabeceras de correo. Cuando Postfix recibe correo, OpenDMARC añadirá cabeceras DMARC en el mensaje entregado al buzón o a tu servidor IMAP/POP. Por ejemplo:

```
Authentication-Results: mail.midominio.org;
    dmarc=pass (p=quarantine dis=none) header.from=example.org
```

Este tipo de cabecera indica que:

* se aplicó la política DMARC,
* y el resultado de la verificación. 

### Notas importantes

* **OpenDMARC depende de SPF y DKIM**: no puede verificar DMARC a menos que ya se estén evaluando SPF y DKIM, porque DMARC *combina* esos resultados para tomar una decisión.
* **El rechazo automático de correos fallidos (RejectFailures)** no se recomienda sin pruebas, pues puede bloquear correos legítimos mal configurados. Es mejor empezar con `false` y revisar logs o cabeceras.
* El servicio también puede generar **informes DMARC** (opcional) si lo conectas a una base de datos o scripts de reporte (avanzado, no obligatorio).


## Otras técnicas complementarias

Además de SPF, DKIM y DMARC, existen otros mecanismos que ayudan a reducir el spam:

### SMTPd restrictions

Postfix permite definir **restricciones SMTP** que se aplican durante la comunicación SMTP y permiten controlar quién puede enviar correos al servidor y en qué condiciones. Algunas de las directivas más habituales son:

- `smtpd_helo_restrictions`
- `smtpd_client_restrictions`
- `smtpd_relay_restrictions`
- `smtpd_recipient_restrictions`

En este curso no se profundiza en su configuración, pero es importante conocer su existencia.

### Listas grises (Greylisting)

Las **listas grises** (*greylisting*) consisten en rechazar temporalmente el primer intento de entrega de un correo procedente de un servidor desconocido. Los servidores legítimos volverán a intentar la entrega pasado un tiempo, mientras que muchos servidores de spam no lo hacen.

Esta técnica permite reducir el spam sin analizar el contenido del mensaje, aunque introduce un pequeño retraso en la entrega de correos legítimos.

{% capture notice-text %}
## Práctica 1/2

Ejercicio 2: Recibir correos


{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>