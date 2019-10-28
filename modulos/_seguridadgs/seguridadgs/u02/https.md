---
title: "Práctica: Certificados digitales. HTTPS"
permalink: /seguridadgs/u02/https.html
---

## Certificado digital de persona física

### Tarea 1: Instalación del certificado

{% capture notice-text %}
1. Una vez que hayas obtenido tu certificado, explica brevemente como se instala en tu navegador favorito. 
2. Muestra una captura de pantalla donde se vea las preferencias del navegador donde se ve instalado tu certificado. 
3. ¿Cómo puedes hacer una copia de tu certificado?, ¿Como vas a realizar la copia de seguridad de tu certificado?. Razona la respuesta.
4. Investiga como exportar la clave pública de tu certificado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Tarea 2: Validación del certificado

{% capture notice-text %}
1. Instala en tu ordenador el software [autofirma](https://firmaelectronica.gob.es/Home/Descargas.html) y desde la página de VALIDe valida tu certificado. Muestra capturas de pantalla donde se comprueba la validación.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Tarea 3: Firma electrónica

{% capture notice-text %}
1. Utilizando la página VALIDe y el programa autofirma, firma un documento con tu certificado y envíalo por correo a un compañero.
2. Tu debes recibir otro documento firmado por un compañero y utilizando las herramientas anteriores debes visualizar la firma (**Visualizar Firma**) y (**Verificar Firma**). ¿Puedes verificar la firma aunque no tengas la clave pública de tu compañero?, ¿Es necesario estar conectado a internet para hacer la validación de la firma?. Razona tus respuestas.
3. Entre dos compañeros, firmar los dos un documento, verificar la firma para comprobar que está firmado por los dos.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

### Tarea 4: Autentificación

{% capture notice-text %}
1. Utilizando tu certificado accede a alguna página de la administración pública )cita médica, becas, puntos del carnet,...). Entrega capturas de pantalla donde se demuestre el acceso a ellas.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## HTTPS / SSL

{% capture notice-text %}
Antes de hacer esta práctica vamos a crear una página web (puedes usar una página estática o instalar una aplicación web) en un servidor web apache2 que se acceda con el nombre `tunombre.iesgn.org`.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

### Certificado autofirmado

Esta práctica la vamos a realizar con un compañero. En un primer momento un alumno creará una **Autoridad Certficadora** y firmará un certificado para la página del otro alumno. Posteriormente se volverá a realizar la práctica con los roles cambiados.

El alumno que hace de Autoridad Certificadora deberá entregar una documentación donde explique los siguientes puntos:

{% capture notice-text %}
1. Crear su autoridad certificadora (generar el certificado digital de la CA).
2. Debe recibir el fichero CSR (Solicitud de Firmar un Certificado) de su compañero, debe firmarlo y enviar el certificado generado a su compañero.
3. ¿Qué otra información debe aportar a tu compañero para que éste configure de forma adecuada su servidor web con el certificado generado?
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

El alumno que hace de administrador del servidor web, debe entregar una documentación que describa los siguientes puntos:

{% capture notice-text %}
1. Crea una clave privada RSA de 4096 bits para identificar el servidor. 
2. Utiliza la clave anterior para generar un CSR, considerando que deseas acceder al servidor tanto con el FQDN (`tunombre.iesgn.org`) como con el nombre de host (implica el uso de las extensiones `Alt Name`).
3. Envía la solicitud de firma a la entidad certificadora (su compañero).
4. Recibe como respuesta un certificado X.509 para el servidor firmado y el certificado de la autoridad certificadora.
5. Configura tu servidor web con https en el puerto 443, haciendo que las peticiones http se redireccionen a https (forzar https).
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

### Certificados digital con CAcert

El lema de **CAcert** es *Free digital certificates for everyone* y es que la utilización de certificados emitidos por CA comerciales no es posible para todos los sitios de Internet debido a su coste, lo que los limita su uso a transacciones económicas o sitios con datos relevantes. **CAcert** es una organización sin ánimo de lucro que mantiene una infraestructura equivalente a una CA comercial aunque con ciertas limitaciones.

Los pasos que hay que dar para utilizar un certificado X.509 emitido por CAcert son los siguientes:

1. Darse de alta como usuario en el sitio web.
2. Dar de alta el dominio para el que queremos obtener el certificado. (opción Domains -> Add)
3. CAcert verifica que podemos hacer uso legítimo del dominio enviando un mensaje de correo electrónico.
4. Dar de alta el certificado de un servidor mediante una solicitud de firma certificado (CSR).
5. Configurar el servidor web con el certificado X.509 emitido por la CA.
6. Al acceder a la página debemos evitar el mensaje de error de "Conexión segura fallida".

{% capture notice-text %}
Escribe una documentación donde expliques el proceso y muestra al profesor su funcionamiento.
{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>