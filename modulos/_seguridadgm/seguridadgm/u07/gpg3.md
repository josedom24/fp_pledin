---
title: "Integridad, firmas y autenticación"
permalink: /seguridadgm/u07/gpg3.html
---

## Firmas digitales

### Ejercicio 1

Verifica que el documento [`importante.pdf`](importante.pdf) ha sido firmado por mí, para ello puedes obtener la firma del documente en el fichero [`importante.pdf.asc`](importante.pdf.asc). ¿Necesitas alguna otra cosa para verificar la firma?. ¿Podemos asegurar que el documento no ha sido manipulado?. Razona la respuesta.

### Ejercicio 2

Envíame por correo electrónico un documento (fichero plano cuyo contenido sea tu nombre completo) que esté encriptado y firmado por tí. Envíame toda la información que necesito para desencriptar y verificar el documento recibido.

### Ejercicio 3

Sería muy recomendable poder escribir correos electrónicos cifrados y firmados directamente desde nuestro gestor de correo electrónico. Siguiendo este [tutorial](https://www.redeszone.net/2017/01/21/aprende-usar-cifrado-pgp-gmail-outlook-la-extension-mailvelope-firefox-chrome/) envía un correo cifrado y firmado a un compañero. Recibe de un compañero otro correo cifrado y firmado y verifica la firma y desencripta el correo.

**Nota: Se valorará más ejercicio si no generáis nuevas claves en la extensión. Es muy recomendable importar las claves que ya poseéis.**

## Integridad

Vamos a descargarnos la ISO de debian, y posteriormente vamos a comprobar su integridad.

Puedes encontrar la ISO en la dirección: [https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/).

1. Para validar el contenido de la imagen CD, solo asegúrese de usar la herramienta apropiada para sumas de verificación. Para cada versión publicada existen archivos de suma de comprobación con algoritmos fuertes (SHA256 y SHA512); debería usar las herramientas `sha256sum` o `sha512sum` para trabajar con ellos. 
2. Verifica que el contenido del hash que has utilizado no ha sido manipulado, usando la firma digital que encontrarás en el repositorio. Puedes encontrar una guía para realizarlo en este artículo: [How to verify an authenticity of downloaded Debian ISO images ](https://linuxconfig.org/how-to-verify-an-authenticity-of-downloaded-debian-iso-images)