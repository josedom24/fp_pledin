---
title: "Práctica: Integridad, firmas y autenticación"
permalink: /seguridadgs/u02/firma.html
---


## Tarea 1: Firmas electrónicas

En este primer apartado vamos a trabajar con las firmas electrónicas, para ello te pueden ayudar los siguientes enlaces:

* [Intercambiar claves](https://www.gnupg.org/gph/es/manual/x75.html)
* [Firmado de claves (Debian)](https://www.debian.org/events/keysigning.es.html)
* [Manual de creación y mantenimiento de clave GPG](https://www.infotics.es/articulo/manual-de-creaci%C3%B3n-y-mantenimiento-de-clave-gpg/)

{% capture notice-text %}

1. Manda un documento y la firma electrónica del mismo a un compañero. Verifica la firma que tu has recibido.
2. ¿Qué significa el mensaje que aparece en el momento de verificar la firma?

        gpg: Firma correcta de "Pepe D <josedom24@gmail.com>" [desconocido]
        gpg: ATENCIÓN: ¡Esta clave no está certificada por una firma de confianza!
        gpg:          No hay indicios de que la firma pertenezca al propietario.
        Huellas dactilares de la clave primaria: E8DD 5DA9 3B88 F08A DA1D  26BF 5141 3DDB 0C99 55FC

3. Vamos a crear un anillo de confianza entre los miembros de nuestra clase, para ello.

    * Tu clave pública debe estar en un servidor de claves
    * Escribe tu fingerprint en un papel y dárselo a tu compañero, para que puede descargarse tu clave pública.
    * Te debes bajar al menos tres claves públicas de compañeros. Firma estas claves.
    * Tu te debes asegurar que tu clave pública es firmada por al menos tres compañeros de la clase.
    * Puedes seguir el esquema que se nos presenta en la siguiente página de Debian:  
    * Una vez que firmes una clave se la tendrás que devolver a su dueño, para que otra persona se la firme.
    * Cuando tengas las tres firmas sube la clave al servidor de claves y rellena tus datos en la tabla [Claves públicas PGP 2019-2020](https://dit.gonzalonazareno.org/redmine/projects/asir2/wiki/Claves_p%C3%BAblicas_PGP_2019-2020)
    * Asegurate que te vuelves a bajar las claves públicas de tus compañeros que tengan las tres firmas.

4. Muestra las firmas que tiene tu clave pública.
5. Comprueba que ya puedes verificar sin "problemas" una firma recibida por una persona en la que confías.
6. Comprueba que puedes verificar sin "problemas" una firma recibida por una tercera problema en la que confía una persona en la que tu confías.
        
    {% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Correo seguro con evolution/thunderbird (2 puntos)

Ahora vamos a configurar nuestro cliente de correo electrónico para poder mandar correos cifrados, para ello:

{% capture notice-text %}
1. Configura el cliente de correo evolution con tu cuenta de correo habitual
2. Añade a la cuenta las opciones de seguridad para poder enviar correos firmados con tu clave privada o cifrar los mensajes para otros destinatarios
3. Envía y recibe varios mensajes con tus compañeros y comprueba el funcionamiento adecuado de GPG
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Integridad

Vamos a descargarnos la ISO de debian, y posteriormente vamos a comprobar su integridad.

Puedes encontrar la ISO en la dirección: [https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/).

{% capture notice-text %}
1. Para validar el contenido de la imagen CD, solo asegúrese de usar la herramienta apropiada para sumas de verificación. Para cada versión publicada existen archivos de suma de comprobación con algoritmos fuertes (SHA256 y SHA512); debería usar las herramientas `sha256sum` o `sha512sum` para trabajar con ellos. 
2. Verifica que el contenido del hash que has utilizado no ha sido manipulado, usando la firma digital que encontrarás en el repositorio. Puedes encontrar una guía para realizarlo en este artículo: [How to verify an authenticity of downloaded Debian ISO images ](https://linuxconfig.org/how-to-verify-an-authenticity-of-downloaded-debian-iso-images)
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


## Integridad y autenticidad (apt secure)

Cuando nos instalamos un paquete en nuestra distribución linux tenemos que asegurarno que ese paquete es legítimo. Para conseguir este objetivo se utiliza criptografía asimétrica, y en el caso de Debian a este sistema se llama **apt secure**. Esto lo debemos tener en cuenta al utilizar los repositorios oficiales. Cuando añadamos nuevos repositorios tendremos que añadir las firmas necesarias para confiar en que los paquetes son legítimos y no han sido modificados.

{% capture notice-text %}
Busca información sobre **apt secure** y responde las siguientes preguntas:

1. ¿Qué software utiliza **apt secure** para realizar la criptografía asimétrica?
2. ¿Para que sirve el comando `apt-key`? ¿Qué muestra el comando `apt-key list`?
3. En que fichero se guarda el anillo de claves que guarda la herramienta `apt-key`?
4. ¿Qué contiene el archivo `Release` de un repositorio de paquetes?. ¿Y el archivo `Release.gpg`?. Puedes ver estos archivos en el repositorio `http://ftp.debian.org/debian/dists/Debian10.1/`. Estos archivos se descargan cuando hacemos un `apt update`.
5. Explica el proceso por el cual el sistema nos asegura que los ficheros que estamos descargando son legítimos.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

# Autenticación ssh

Estudio del protocolo ssh
https://www.hostinger.es/tutoriales/que-es-ssh
http://es.tldp.org/Tutoriales/doc-ssh-intro/introduccion_ssh-0.2.pdf