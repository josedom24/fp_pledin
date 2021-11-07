---
title: "Ejercicio 2: Instalación y configuración de un servidor DNS esclavo"
---

El servidor DNS actual funciona como **DNS maestro**. Vamos a instalar un nuevo servidor DNS que va a estar configurado como **DNS esclavo** del anterior, donde se van a ir copiando periódicamente las zonas del DNS maestro. Suponemos que el nombre del servidor DNS esclavo se va llamar ``tusapellidos.iesgn.org``.

1. Realiza la instalación del servidor DNS esclavo.
2. Comprueba si las zonas definidas en el maestro tienen algún error con el comando adecuado.
3. Comprueba si la configuración de ``named.conf`` tiene algún error con el comando adecuado.
4. Reinicia los servidores y comprueba en los logs si hay algún error. **No olvides incrementar el número de serie en el registro SOA si has modificado la zona en el maestro**.
5. Configura un cliente para que utilice los dos servidores como servidores DNS.

{% capture notice-text %}
* Entrega la configuración de las zonas del maestro y del esclavo.
* Entrega la comprobación para determinar si las zonas definidas en el maestro tienen algún error con el comando adecuado.
* Entrega la comprobación para determinar si la configuración de ``named.conf`` tiene algún error con el comando adecuado.
* Muestra la salida del log donde se demuestra que se ha realizado la transferencia de zona.
* Entrega la configuración dDNS de los clientes.
* Realiza una consulta con ``dig`` tanto al maestro como al esclavo para comprobar que las respuestas son autorizadas. ¿En qué te tienes que fijar?
* Solicita una copia completa de la zona desde el cliente ¿qué tiene que ocurrir?. Solicita una copia completa desde el esclavo ¿qué tiene que ocurrir?
* Realiza una consulta desde el cliente y comprueba que servidor está respondiendo.
* Posteriormente apaga el servidor maestro y vuelve a realizar una consulta desde el cliente ¿quién responde?
**Enseña al profesor el funcionamiento del servidor esclavo.**
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>