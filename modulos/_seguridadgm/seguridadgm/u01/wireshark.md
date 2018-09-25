---
title: "Uso del analizador de protocolos Wireshark"
permalink: /seguridadgm/u01/wireshark.html
---

1. Antes de nada deberás recordar (y documentar adecuadamente) los protocolos ICMP, ARP, DNS y HTTP.
2. Realiza la instalación de Wireshark en tu ordenador (en linux o en windows).
3. Familiarízate con la herramienta:

    * Opciones de captura.
    * Generación de tráfico.
    * Filtrado de paquetes. Indicar el significado de cada columna (No, Time, source, Destination, Protocol...)

4. **Protocolo ICMP**: captura paquetes relacionados con este protocolo al ejecutar distintos ping desde la consola y analiza el contenido de los mismos. Utiliza filtros para identificar los paquetes.

    Prueba los siguientes parámetros de ping y observa de nuevo el contenido de los paquetes.

    ```bash
    ping -n [cuenta]
    ping -l [tamaño]
    ```
5. **Protocolo HTTP**. Abre un navegador y sigue los siguientes pasos:

    * Activa la captura de paquetes
    * Accede a esta página: [http://elforocofrade.es/index.php](http://elforocofrade.es/index.php).
    * Detén la captura de paquetes
    * Examina el contenido de lo capturado
    * Establece filtros para identificar nuestros paquetes.
        * Localiza uno de los primeros paquetes HTTP donde esté el comando "GET".
        * Sigue el flujo del protocolo TCP: Pulsando con el botón derecho sobre el paquete, selecciona el comando "Follow TCP Stream".
    * Por último, introduce un usuario y password de un Usuario de correo electrónico ficticio, y trata de obtener la clave, capturando los paquetes transmitidos al pulsar el botón Entrar.

6. **Protocolo ARP**: Realiza capturas de este protocolo haciendo ping a diferentes equipos de la clase. Localiza el contenido de los diferentes campos en las capturas realizadas y obtén la dirección MAC de tus compañeros. Utiliza filtros para identificar los paquetes.

7. **Protocolo DNS**: Haz lo mismo con este protocolo. Para ello realiza ping a diferentes máquinas remotas, que aunque no contesten, obliga a nuestro equipo a resolver su dirección física. Localiza en las capturas realizadas el contenido de los diferentes campos del protocolo. Utiliza filtros para identificar los paquetes.
