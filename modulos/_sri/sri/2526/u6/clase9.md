---
title: "Caso 5: Envío de correo electrónico usando nuestro servidor de correos"
---

## Protocolo SMTP

El protocolo **SMTP** es el encargado del envío de correo electrónico. Es importante distinguir entre el envío de correos **entre servidores de correo (MTA ↔ MTA)** y el envío de correos **desde clientes de correo (MUA)** hacia el servidor.

* El envío entre servidores de correo se realiza utilizando el **puerto 25/tcp**.
* El envío desde clientes de correo debe realizarse mediante servicios específicos de **presentación o submission**, que permiten autenticación y cifrado.

## Configuración de Postfix

En la configuración de Postfix existe la directiva:

```
mynetworks
```

Con `mynetworks` se indican las direcciones IP o redes **de confianza** desde las que se permite enviar correos **sin autenticación**. Por defecto, solo se permite el envío desde el propio servidor:

```
127.0.0.0/8
[::1]/128
```

Esta directiva **no debe utilizarse para permitir el envío de correos desde clientes externos en Internet**. Esta configuración convierte el servidor en un **open relay**, permitiendo que cualquier equipo de Internet utilice el servidor para enviar correos, lo que provocaría su inclusión en listas negras.

El control del envío desde clientes debe realizarse mediante **autenticación SMTP (SMTP AUTH)** y no mediante direcciones IP.

## Autenticación y cifrado de la conexión para el envío del correo

Cuando un usuario envía correos desde un cliente de correo, este **no debe conectarse al puerto 25/tcp**, ya que dicho puerto está pensado para la comunicación entre MTAs y no garantiza autenticación ni cifrado.

Para el envío desde clientes se utilizan los siguientes mecanismos:

### ESMTP + STARTTLS (Submission)

**ESMTP** (*Enhanced Simple Mail Transfer Protocol*) es una extensión de SMTP que permite el uso de autenticación y cifrado.

* Utiliza el **puerto 587/tcp**
* Se conoce como **puerto de submission**
* Postfix actúa como **MSA (Mail Submission Agent)**

Mediante STARTTLS, una conexión inicialmente no cifrada se convierte en una conexión segura usando SSL/TLS.

Para autenticar a los usuarios se utiliza **SASL (Simple Authentication and Security Layer)**, que proporciona un marco de autenticación. En nuestro caso, utilizaremos **Dovecot** como proveedor de autenticación, reutilizando los usuarios del sistema.

### SMTPS

**SMTPS (Simple Mail Transfer Protocol Secure)** establece una conexión cifrada desde el inicio utilizando el puerto **465/tcp**. No es una extensión de SMTP, sino un servicio independiente, similar al funcionamiento de HTTPS.

Aunque no es el método recomendado actualmente, muchos clientes de correo siguen soportándolo por compatibilidad.

## Cifrado de la comunicación

Para cifrar la comunicación entre el cliente y el servidor utilizaremos un **certificado digital**, que en nuestro caso estará firmado por **Let’s Encrypt**. El certificado deberá coincidir con el nombre del servidor de correo configurado.

## Cifrado del correo entre servidores (SMTP)

El envío de correo entre servidores de correo se realiza mediante el protocolo **SMTP**, utilizando el **puerto 25/tcp**. Un MTA puede actuar de dos formas:

* Como **servidor (smtpd)**, cuando otros MTAs se conectan a él para entregarle correos.
* Como **cliente (smtp)**, cuando se conecta a otros MTAs para enviar correos.

### TLS en SMTP entre MTAs

Por defecto, Postfix está configurado para **ofrecer TLS de forma oportunista** cuando recibe conexiones SMTP. Esto significa que:

* Si el servidor remoto soporta TLS, la comunicación se cifra.
* Si no lo soporta, el correo se envía sin cifrar.

Este comportamiento se controla mediante el parámetro:

```
smtpd_tls_security_level = may
```

Con esta configuración, el cifrado es opcional y se prioriza la compatibilidad con otros servidores de correo. Aunque se utiliza TLS, **no se puede garantizar que todos los correos viajen cifrados en todos los saltos**, ya que depende de la configuración de los servidores intermedios.

Por defecto, Postfix utiliza un **certificado autofirmado**, lo que permite cifrar la comunicación, pero no garantiza la identidad del servidor. Para mejorar la confianza, se recomienda utilizar un certificado firmado por una autoridad de certificación, como **Let’s Encrypt**.