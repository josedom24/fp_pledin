---
title: "Implementación de un cortafuegos perimetral"
permalink: /seguridadgs/u03/perimetral_iptables.html
---

{% capture notice-text %}
## Ejercicios

1. Permite poder hacer conexiones ssh al exterior desde el la máquina cortafuegos.
2. Permite hacer consultas DNS desde la máquina cortafuegos sólo al servidor `192.168.202.2`. Comprueba que no puedes hacer un `dig @1.1.1.1`.
3. Permite que la máquina cortafuegos pueda navegar por internet.
4. Permite realizar conexiones ssh desde los equipos de la LAN
5. Instala un servidor de correos en la máquina de la LAN. Permite el acceso desde el exterior y desde el cortafuego al servidor de correos. Para probarlo puedes ejecutar un `telnet` al puerto 25 tcp.
6. Permite poder hacer conexiones ssh desde exterior a la LAN
7. Modifica la regla anterior, para que al acceder desde el exterior por ssh tengamos que conectar al puerto 2222, aunque el servidor ssh este configurado para acceder por el puerto 22.
8. Permite hacer consultas DNS sólo al servidor `192.168.202.2`. Comprueba que no puedes hacer un `dig @1.1.1.1`.
9. ¿Tendría resolución de nombres y navegación web el cortafuego? ¿Sería necesario? ¿Tendrían que estar esas de reglas de forma constante en el cortafuego?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
