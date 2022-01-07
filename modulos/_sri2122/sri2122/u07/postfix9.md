---
title: "Caso 4: Envío de correo electrónico usando nuestro servidor de correos"
---

## Protocolo SMTP

En primer lugar hay que tener en cuenta que para el envío de correos entre MTA se utiliza el puerto 25/tcp.

Sin embargo si vamos a usar un cliente de correos para el envío de correos, este cliente, en la actualidad no usa el puerto 25/tcp para conectarse al servidor. Tenemos dos opciones:

* **ESMTP + STARTTLS**: esmtp (Enhanced Simple Mail Transfer Protocol): En este caso se usa el puerto 587/tcp. Este protocolo tiene nuevas extensiones: como smtp-auth y STARTTLS (STARTTLS transforma una conexión insegura en una segura mediante el uso de SSL/TLS).

	El puerto 587/tcp se conoce como puerto de submission o presentación. Al abrir este puero postfix esta funcionando de MSA (mail submission agent) que recibe mensajes de correo electrónico desde un Mail User Agent (MUA) y coopera con un Mail Transport Agent (MTA) para entregar el correo.

	Tenemos que conseguir que la comunicación que se establece desde el cliente con el servidor sea autentificada para ella usamos **SASL** (Simple Authentication and Security Layer) que es un framework para autenticación y autorización en protocolos de Internet. Para realizar la autenticación vamos a usar **dovecot** (que ya tiene un mecanismo de autenticación).

	Ademmás tenemos que conseguir que la comunicación sea cifrada, para ello vamos a usar **STARTTLS** que nos permite que utilizando el mismo puerto (587/tcp) la conexión este cifrada.

* **SMTPS**: Simple Mail Transfer Protocol Secure: Con este protocolo conseguimos el cifrado de la comunicación entre el cliente y el servidor. Utiliza un puerto no estándar 465/tcp. No es una extensión de smtp. Es muy parecido a HTTPS.

Como comentábamos en el apartado anterior nosotros vamos a usar un certificado firmado por LetsEncrypt para cifrar la comunicación.

## Enlaces interesantes

Os dejo dos entradas que os pueden ayudar para la configuración de estos dos últimos apartados:

* [ISP Mail Tutorial for Debian 10 (Buster)](https://123qwe.com/tutorial-debian-10/)
* [How to secure Postfix using Let’s Encrypt](https://upcloud.com/community/tutorials/secure-postfix-using-lets-encrypt/)