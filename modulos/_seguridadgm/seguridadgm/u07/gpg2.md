---
title: "Cifrado asimétrico con gpg"
permalink: /seguridadgm/u07/gpg2.html
---

En esta práctica vamos a cifrar ficheros utilizando cifrado asimétrico utilizando el programa gpg. Puedes encontrar el resumen de comando en esta [cluleta](https://elbauldelprogramador.com/chuleta-de-comandos-para-gpg/) o buscar información en internet.

## Generación de claves

Los algoritmos de cifrado asimétrico utilizan dos claves para el cifrado y descifrado de mensajes. Cada persona involucrada (receptor y emisor) debe disponer, por tanto, de una pareja de claves pública y privada.
Para generar nuestra pareja de claves con gpg utilizamos la opción `--gen-key`:

Para esta práctica no es necesario que indiquemos frase de paso en la generación de las claves (al menos para la clave pública).

{% capture notice-text %}
1. Genera un par de claves (pública y privada). ¿En que directorio se guarda las claves de un usuario?
2. Lista las claves públicas que tienes en tu almacén de claves. Explica los distintos datos que nos muestra. ¿Cómo deberías haber generado las claves para indicar, por ejemplo, que tenga un 1 mes de validez?
3. Lista las claves privadas de tu almacén de claves.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Importar / exportar clave pública

Para enviar archivos cifrados a otras personas, necesitamos disponer de sus claves públicas. De la misma manera, si queremos que cierta persona pueda enviarnos datos cifrados, ésta necesita conocer nuestra clave pública. Para ello, podemos hacérsela llegar por email por ejemplo. Cuando recibamos una clave pública de otra persona, ésta deberemos incluirla en nuestro keyring o anillo de claves, que es el lugar donde se almacenan todas las claves públicas de las que disponemos. 

{% capture notice-text %}
1. Exporta tu clave	pública	en formato ASCII y guardalo en un archivo `nombre_apellido.asc` y envíalo al compañero con el que vas a hacer esta práctica.
2. Importa las claves públicas recibidas de vuestro compañero.
3. Comprueba que las claves se han incluido correctamente en vuestro keyring.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Cifrado asimétrico con claves públicas

Tras realizar el ejercicio anterior, podemos enviar ya documentos cifrados utilizando la clave pública de los destinatarios del mensaje. (**Nota: No es necesario indicar el emisor con la opción `-u`)

{% capture notice-text %}
1. Cifraremos un archivo cualquiera y lo remitiremos por email a uno de nuestros compañeros que nos proporcionó su clave pública.
2. Nuestro compañero, a su vez, nos remitirá un archivo cifrado para que nosotros lo descifremos.
3. Tanto  nosotros  como  nuestro  compañero  comprobaremos  que  hemos  podido descifrar los mensajes recibidos respectivamente.
4. Por último, enviaremos el documento cifrado a alguien que no estaba en la lista de destinatarios y comprobaremos que este usuario no podrá descifrar este archivo.
5. Para terminar, indica los comando necesarios para borrar las claves públicas y privadas que posees.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
