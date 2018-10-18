---
title: "Ejercicio 4: Instalación y configuración de un servidor DNS esclavo"
permalink: /serviciosgs/u04/ejercicio4.html
---

```eval_rst
.. note::

	Suponemos que tenemos instalado el servidor DNS del `ejercicio anterior <ejercicio3.html>`_.
```

Actualmente tenemos instalado un servidor DNS que tiene autoridad sobre la zona ``iesgn.org`` y sobre la zona de resolución inversa correspondiente. Este servidor va a funcionar como **DNS maestro**. Vamos a instalar un nuevo servidor DNS que va a estar configurado como **DNS esclavo** del anterior, donde se van a ir copiando periódicamente las zonas del DNS maestro. Suponemos que el nombre del servidor DNS esclavo se va llamar ``nombredelesclavo.iesgn.org``.

Modifica la configuración del servidor DNS actual para que funcione como maestro de las zonas que tiene definida. Instala y configura un nuevo servidor DNS para que funcione como DNS esclavo del anterior. Y realiza las siguientes comprobaciones:

```eval_rst
.. warning::

	1. Entrega la configuración de las zonas del maestro y del esclavo.
	2. Comprueba si las zonas definidas en el maestro tienen algún error con el comando adecuado.
	3. Comprueba si la configuración de named.conf tiene algún error con el comando adecuado.
	4. Reinicia los servidores y comprueba en los logs si hay algún error. **No olvides incrementar el número de serie en el registro SOA si has modificado la zona en el maestro**.
	5. Muestra la salida del log donde se demuestra que se ha realizado la transferencia de zona.
	6. Realiza una consulta con dig tanto al maestro como al esclavo para comprobar que las respuestas son autorizadas. ¿En qué te tienes que fijar?
	7. Configura un cliente para que utilice los dos servidores como servidores DNS.
	8. Solicita una copia completa de la zona desde el cliente ¿qué tiene que ocurrir?. Solicita una copia completa desde el esclavo ¿qué tiene que ocurrir?
	9. Realiza una consulta desde el cliente y comprueba que servidor está respondiendo.
	10. Posteriormente apaga el servidor maestro y vuelve a realizar una consulta desde el cliente ¿quién responde?
```