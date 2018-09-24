---
title: Cuestionario DHCP
permalink: /serviciosgs/u02/cuestionario.html
---

1. ¿Qué es un servidor DHCP?
2. ¿Cómo hay que configurar un cliente DHCP?
3. Ventajas de usar un servidor DHCP
4. Enumera los distintos parámetros que un servidor DHCP puede conceder a un cliente
5. Definición de:
  
    * Ámbito servidor DHCP
    * Rango servidor DHCP
    * Concesión o alquiler de direcciones
    * Reserva de direcciones IP
    * Exclusión de direcciones IP
  
6. ¿Qué es APIPA?
7. ¿Por qué el mensaje DHCPDISCOVER es del tipo broadcast?
8. Desde el estado INIT al estado BOUND. ¿Qué mensajes se transmiten desde el cliente al servidor?
9. ¿Qué significa el mensaje DHCPDECLINE por parte del cliente?
10. Una vez que se ha aceptado una asignación (DHCPACK), explica los siguientes tiempos:
  
    * T1: tiempo de renovación de alquiler
    * T2: tiempo de reenganche
    * T3: tiempo de concesión del alquiler

11. ¿Qué es la renovación (RENEWING) de alquiler?
12. ¿Qué es el estado de reenganche (REBINDING)? 
13. ¿Qué ocurre cuando termina el tiempo de concesión del alquiler (T3)?
14. ¿Qué ocurre cuando un cliente manda un DHCPRELEASE?
15. ¿Qué ocurre cuando un cliente que ya tiene asignación se reinicia?
16. Los clientes toman una configuración, y a continuación apagamos el servidor dhcp. ¿qué ocurre con el cliente windows? ¿Y con el cliente linux?
17. Los clientes toman una configuración, y a continuación cambiamos la configuración del servidor dhcp (por ejemplo el rango). ¿qué ocurriría con un cliente windows? ¿Y con el cliente linux?
18. ¿Qué instrucciones en Windows y en Linux nos permiten?:
  
    * Para renovar una dirección IP y una nueva configuración de red
    * Para liberar la dirección IP
19. ¿Qué es la lista de concesiones? ¿En qué fichero se guarda en Linux?
20. En el servidor isc-dhcp en linux. ¿Qué indican los siguientes parámetros?:
  
    * max-lease-time
    * default-lease-time
21. En el cliente, ¿qué se guarda en los ficheros `dhclient-???.lease`?
