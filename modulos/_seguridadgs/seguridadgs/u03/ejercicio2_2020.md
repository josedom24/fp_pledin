---
title: "Implementación de un cortafuegos perimetral"
permalink: /seguridadgs/u03/ejercicio2_cortafuegos.html
---

## Ejercicios

Configura un cortafuegos perimetral en una máquina con dos interfaces de red (externa e interna). Debes controlar el tráfico a la máquina cortafuego y el trafico a los equipos de la LAN.

Realiza la configuración necesaria para que el cortafuegos sea consistente.

{% capture notice-text %}

1. Permite poder hacer conexiones ssh al exterior desde la máquina cortafuegos.
2. Permite hacer consultas DNS desde la máquina cortafuegos sólo al servidor `192.168.202.2`. Comprueba que no puedes hacer un `dig @1.1.1.1`.
3. Permite que la máquina cortafuegos pueda navegar por internet.
4. Los equipos de la red local deben poder tener conexión al exterior.
5. Permitimos el ssh desde el cortafuego a la LAN
6. Permitimos hacer ping desde la LAN a la máquina cortafuegos.
7. Permite realizar conexiones ssh desde los equipos de la LAN
8. Instala un servidor de correos en la máquina de la LAN. Permite el acceso desde el exterior y desde el cortafuego al servidor de correos. Para probarlo puedes ejecutar un `telnet` al puerto 25 tcp.
9. Permite poder hacer conexiones ssh desde exterior a la LAN
10. Modifica la regla anterior, para que al acceder desde el exterior por ssh tengamos que conectar al puerto 2222, aunque el servidor ssh este configurado para acceder por el puerto 22.
11. Permite hacer consultas DNS desde la LAN sólo al servidor `192.168.202.2`. Comprueba que no puedes hacer un `dig @1.1.1.1`.
12. Permite que los equipos de la LAN puedan navegar por internet

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
