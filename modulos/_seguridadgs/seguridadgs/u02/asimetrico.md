---
title: "Práctica: Cifrado asimétrico con gpg y openssl"
permalink: /seguridadgs/u02/asimetrico.html
---

# Cifrado asimétrico con gpg

En esta práctica vamos a cifrar ficheros utilizando cifrado asimétrico utilizando el programa gpg. Puedes encontrar el resumen de comando en esta [chuleta](https://elbauldelprogramador.com/chuleta-de-comandos-para-gpg/) o buscar información en internet.

## Tarea 1: Generación de claves (1 punto)

Los algoritmos de cifrado asimétrico utilizan dos claves para el cifrado y descifrado de mensajes. Cada persona involucrada (receptor y emisor) debe disponer, por tanto, de una pareja de claves pública y privada.
Para generar nuestra pareja de claves con gpg utilizamos la opción `--gen-key`:

Para esta práctica no es necesario que indiquemos frase de paso en la generación de las claves (al menos para la clave pública).

{% capture notice-text %}
1. Genera un par de claves (pública y privada). ¿En que directorio se guarda las claves de un usuario?
2. Lista las claves públicas que tienes en tu almacén de claves. Explica los distintos datos que nos muestra. ¿Cómo deberías haber generado las claves para indicar, por ejemplo, que tenga un 1 mes de validez?
3. Lista las claves privadas de tu almacén de claves.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 2: Importar / exportar clave pública (1 punto)

Para enviar archivos cifrados a otras personas, necesitamos disponer de sus claves públicas. De la misma manera, si queremos que cierta persona pueda enviarnos datos cifrados, ésta necesita conocer nuestra clave pública. Para ello, podemos hacérsela llegar por email por ejemplo. Cuando recibamos una clave pública de otra persona, ésta deberemos incluirla en nuestro keyring o anillo de claves, que es el lugar donde se almacenan todas las claves públicas de las que disponemos. 

{% capture notice-text %}
1. Exporta tu clave	pública	en formato ASCII y guardalo en un archivo `nombre_apellido.asc` y envíalo al compañero con el que vas a hacer esta práctica.
2. Importa las claves públicas recibidas de vuestro compañero.
3. Comprueba que las claves se han incluido correctamente en vuestro keyring.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 3: Cifrado asimétrico con claves públicas (2 puntos)

Tras realizar el ejercicio anterior, podemos enviar ya documentos cifrados utilizando la clave pública de los destinatarios del mensaje. 

{% capture notice-text %}
1. Cifraremos un archivo cualquiera y lo remitiremos por email a uno de nuestros compañeros que nos proporcionó su clave pública.
2. Nuestro compañero, a su vez, nos remitirá un archivo cifrado para que nosotros lo descifremos.
3. Tanto  nosotros  como  nuestro  compañero  comprobaremos  que  hemos  podido descifrar los mensajes recibidos respectivamente.
4. Por último, enviaremos el documento cifrado a alguien que no estaba en la lista de destinatarios y comprobaremos que este usuario no podrá descifrar este archivo.
5. Para terminar, indica los comandos necesarios para borrar las claves públicas y privadas que posees.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 4: Exportar clave a un servidor público de claves PGP (2 puntos)

Para distribuir las claves públicas es mucho más habitual utilizar un servidor específico para distribuirlas, que permite a los clientes añadir las claves públicas a sus anillos de forma mucho más sencilla.

{% capture notice-text %}
1. Genera la clave de revocación de tu clave pública para utilizarla en caso de que haya problemas.
2. Exporta tu clave pública al servidor pgp.rediris.es
3. Borra la clave pública de alguno de tus compañeros de clase e impórtala ahora del servidor público de rediris.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Tarea 5: Correo seguro con evolution/thunderbird (2 puntos)

Ahora vamos a configurar nuestro cliente de correo electrónico para poder mandar correos cifrados, para ello:

{% capture notice-text %}
1. Configura el cliente de correo evolution con tu cuenta de correo habitual
2. Añade a la cuenta las opciones de seguridad para poder enviar correos firmados con tu clave privada o cifrar los mensajes para otros destinatarios
3. Envía y recibe varios mensajes con tus compañeros y comprueba el funcionamiento adecuado de GPG
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

# Tarea 6: Cifrado asimétrico con openssl (2 puntos)

En esta ocasión vamos a cifrar nuestros ficheros de forma asimétrica utilizando la herramienta openssl.

{% capture notice-text %}
1. Genera un par de claves (pública y privada). 
2. Envía tu clave pública a un compañero.
3. Utilizando la clave pública cifra un fichero de texto y envíalo a tu compañero.
4. Tu compañero te ha mandado un fichero cifrado, muestra el proceso para el descifrado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
