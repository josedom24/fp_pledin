---
title: "Práctica: Integridad, firmas y autenticación"
permalink: /seguridadgs/u02/firma.html
---


## firmas

https://www.gnupg.org/gph/es/manual/x75.html firmas del fingerprint de una clave pública para validarla

Autentificación de claves públicas https://cran.rstudio.com/web/packages/gpg/vignettes/intro.html

https://www.infotics.es/articulo/manual-de-creaci%C3%B3n-y-mantenimiento-de-clave-gpg/

## red de confianza

https://www.gnupg.org/gph/es/manual/x75.html

## Tarea 5: Correo seguro con evolution/thunderbird (2 puntos)

Ahora vamos a configurar nuestro cliente de correo electrónico para poder mandar correos cifrados, para ello:

{% capture notice-text %}
1. Configura el cliente de correo evolution con tu cuenta de correo habitual
2. Añade a la cuenta las opciones de seguridad para poder enviar correos firmados con tu clave privada o cifrar los mensajes para otros destinatarios
3. Envía y recibe varios mensajes con tus compañeros y comprueba el funcionamiento adecuado de GPG
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## integridad

apt secure
https://www.taringa.net/+linux/llaves-repositorios-y-secure-apt-debian_137kl8

# Autenticación

Estudio del protocolo ssh
https://www.hostinger.es/tutoriales/que-es-ssh
http://es.tldp.org/Tutoriales/doc-ssh-intro/introduccion_ssh-0.2.pdf