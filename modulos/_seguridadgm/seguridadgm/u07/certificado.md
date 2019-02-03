---
title: "Certificados digitales"
permalink: /seguridadgm/u07/certificado.html
---

## Instalación del certificado

### Ejercicio 1

Una vez que hayas obtenido tu certificado, explica brevemente como se instala en tu navegador favorito. Muestra una captura de pantalla donde se vea las preferencias del navegador donde se ve instalado tu certificado. ¿Cómo puedes hacer una copia de tu certificado?, ¿Como vas a realizar la copia de seguridad de tu certificado?. Razona la respuesta.

Investiga como exportar la clave pública de tu certificado.

### Ejercicio 2

Instala en tu ordenador el software [autofirma](https://firmaelectronica.gob.es/Home/Descargas.html) y desde la página de VALIDe valida tu certificado. Muestra capturas de pantalla donde se comprueba la validación.

## Firma electrónica

### Ejercicio 3

Utilizando la página VALDe y el programa autofirma, firma un documento con tu certificado y envíalo por correo a un compañero.

Tu debes recibir otro documento firmado por un compañero y utilizando las herramientas anteriores debes visualizar la firma (**Visualizar Firma**) y (**Verificar Firma**). ¿Puedes verificar la firma aunque no tengas la clave pública de tu compañero?, ¿Es necesario estar conectado a internet para hacer la validación de la firma?. Razona tus respuestas.

### Ejercicio 4

Entre dos compañeros, firmar los dos un documento, verificar la firma para comprobar que está firmado por los dos.

## Autentificación

### Ejercicio 5

Utilizando tu certificado accede a alguna página de la administración pública )cita médica, becas, puntos del carnet,...). Entrega capturas de pantalla donde se demuestre el acceso a ellas.


## HTTPS / SSL

### Ejercicio 6

Indica una captura de pantalla donde se vean la lista de las claves públicas de las Autoridades de Certificación que hay instalado en tu servidor.

### Ejercicio 7

En el administrador de certificados de tu navegador, borra todos los certificados que tienes guardado en la pestaña **Servidores** (estos certificados no pudiste certificar que eran válidos y añadiste una excepción en el navegador, aceptado los certificados aunque no lo pudieras verificar).

Aceede a `dit.gonzalonazareno.org`, ¿por qué te sale una pantalla de **Su conexión no es segura**?, ¿podemos saber quien es la AC que ha firmado el certificado de esta página?, ¿qué ocurre si pulsamos la opción **Añadir excepción...**?. Añade una excepción y comprueba quién ha firmado el certificado (con una captura de pantalla). Razona tu respuesta.

### Ejercicio 8

Para poder verficar el certificado de `dit.gonzalonazareno.org` necesitamos instalar en nuestro navegador el certificado digital de la AC que es el IES Gonzalo Nazareno. Puede descargar su certificado en esta [página](https://dit.gonzalonazareno.org/gestiona/documentacion/ca).

Descárgalo e instálalo en tu navegador indicando la opción **Confiar en esta CA para identificar sitios web**.

Vuelve acceder a la página y comprueba que ya puedes navegar de forma segura (observar el "candadito" verde). Entrega capturas de pantallas donde se comprueba que estamos navegando con seguridad.