---
title: Servidor de correo electrónico
---

En esta unidad vamos a introducir el servidor de correo electrónico. Vamos a instalar el servidor de correo `postfix` y vamos a configurar distintos tipos de clientes para gestionar nuestros correos. Vamos a estudiar los distintos protocolos de red que se utilizan: SMTP, POP e IMAP. Para finalizar vamos a estudiar aspectos un poco más avanzados: soluciones al problema del spam, antispam y antivirus, clientes virtuales en LDAP,...

## Indice

* [¿Cómo funciona el correo electrónico?](como_funciona_mail.html)
* [Instalación y configuración básica de postfix](postfix1.html)
* [Gestión del correo desde el servidor](postfix2.html)
  * [Caso 1: Envío local, entre usuarios del mismo servidor](postfix3.html)
  * [Caso 2: Envío de correo desde usuarios del servidor a correos de internet](postfix4.html)
    * [¿Qué tenemos que hacer para que nuestro correo "llegue a buen puerto"?](asegurar_envio_correo.html)
  * [Caso 3: Recibir correos desde internet a usuarios del servidor](postfix5.html)
    * [Alias y redirecciones](postfix6.html)
    * [Soluciones al problema del spam](postfix7.html)    
* Gestión del correo desde un cliente remoto
  * [Caso 4: Recepción de correo electrónico usando nuestro servidor de correos](postfix8.html)
  * [Caso 5: Envío de correo electrónico usando nuestro servidor de correos](postfix9.html)


<!--
## Práctica

* [Práctica servidor de correo](practica_correo_2020.html)

<!--
* [Práctica servidor de correo en servidores cloud](practica_correo.html)
* [Práctica servidor de correo en casa](practica_correo_casa.html)
-->