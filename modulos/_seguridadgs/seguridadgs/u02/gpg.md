---
title: "Cifrado simétrico con gpg"
permalink: /seguridadgs/u02/gpg.html
---

GnuPG (la versión libre de PGP o mejor dicho Pretty Good Privacy), nos permite cifrar cualquier tipo de archivo que podremos mandar "libremente" con cierta seguridad de que nadie lo podrá leer. 

Como ya sabéis el cifrado simétrico es el tipo de cifrado más sencillo que hay, es más rápido de procesar y por desgracia menos seguro que el cifrado asimétrico.

Para empezar la prueba tenemos que tener un archivo de cualquier tipo e introducir en la terminal de Linux el comando `gpg` con el parámetro `-c` para cifrar y `-d` para descifrar.

Por ejemplo para cifrar el fichero `fichero.txt`:

    gpg -c fichero.txt

Nos pide la clave de encriptación y nos genera el fichero `fichero.txt.gpg`.

Para desencriptar el fichero simplemente ejecutamos:

    gpg -d fichero.txt.gpg

Nos pide la clave y nos muestra el contenido del fichero original (**Nota: si estaís usando gnome al introducir la clave para realizar la encriptación se guarda en una cache, por lo que no os va a pedir la clave a la hora de desencriptar**)

Si queremos recuperar el fichero original:

    gpg -d fichero.txt.gpg > fichero2.txt

{% capture notice-text %}
## Ejercicios

1. Crea un documento de texto con cualquier editor o utiliza uno del que dispongas.
2. Cifra este documento con alguna contraseña acordada con el compañero de al lado.
3. Haz llegar por algún medio al compañero de al lado el documento que acabas de cifrar.
4. Descifra el documento que te ha hecho llegar tu compañero de al lado.
5. Instala gpg en windows ([Gpg4win](https://gnupg.org/download/)), repite el ejercicio en Windows. Puedes encriptar un mensaje en linux y desencriptarlo en windows y al contrario.
6. `openssl` es otra herramienta que nos permite cifrar mensajes de forma simetríca, investiga como se realiza este ejercicio utilizando esta herramienta.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
