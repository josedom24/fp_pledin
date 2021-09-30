---
title: "Ejercicio 3: Configuración de una reserva"
---

Utilizando el servidor del ejercicio anterior, vamos a configurar una reserva. Para ello añade un segundo cliente al que le vamos a configurar la reserva.

**Ejercicios**

1. Crea en el servidor dhcp una sección HOST para conceder al cliente una dirección IP determinada (`192.168.0.105`).
2. Obtén una nueva dirección IP en el cliente y comprueba que es la que has asignado por medio de la sección host.

{% capture notice-text %}
## Entrega

1. La nueva configuración del servidor dhcp.
2. Muestra la salida del comando ` ip address` en el nuevo cliente.
3. ¿Se ha guardado la concesión en el fichero de concesiones en el servidor?
<div class="notice--info">{{ notice-text | markdownify }}</div>
