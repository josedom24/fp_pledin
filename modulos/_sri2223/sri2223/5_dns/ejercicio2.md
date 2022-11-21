---
title: "Ejercicio 2: DNSmasq como DNS cache/forward en una red local"
---

**Dnsmasq** es un servicio que nos proporciona un servidor DHCP y un servidor DNS. El servidor DNS que nos proporciona es del tipo forward/caché, es decir, sus características son las siguientes:

* Este servidor no hará preguntas recursivas para averiguar la información que le hemos pedido.
* Este servidor preguntará al servidor DNS que tenga configurado el servidor donde está instalado.
* Este servidor guardará en caché las resoluciones que descubra, por lo que acelerará las resoluciones en nuestra red local.
* Este servidor resolverá los nombres que tengamos configurados en el archivo `/etc/hosts` del servidor donde este indtalado (resolución directa e inversa).
* Podemos hacer configuraciones más avanzadas: [Configurando un servidor DNS con dnsmasq](https://www.josedomingo.org/pledin/2020/12/servidor-dns-dnsmasq/).

Realiza los siguientes pasos:

1. Instala en una máquina el servidor `dnsmasq`. Si tienes un cortafuego recuerda que el servicio DNS usa el puerto `53/udp`.
2. Configura el servicio, modifica el fichero `/etc/dnsmasq.conf`:

	* `strict-order`: Podemos descomentar está línea para que las consultas que haga el servidor DNS a los servidores definidos en `/etc/resolv.conf` la haga en el orden que están definidos en ese fichero. El comportamiento por defecto de dnsmasq es hacer preguntas a los servidor DNS definidos en el sistema de una forma aleatoria.
	* `interface`: Otro parámetro que nos puede interesar determinar es la interfaz de red por la que vamos a permitir consultas a nuestros servidor DNS. En mi caso, puedo configurar este parámetro de esta manera: `interface=eth0`.

3. Reinicia el servicio.
4. Configura una máquina cliente modificando su fichero `/etc/resolv.conf` para que use tu servidor dnsmasq como servidor DNS primario.
5. Realiza una consulta con el comando `dig`. ¿Cuánto tiempo ha tardado en resolver? Realiza de nuevo la misma consulta. ¿Cuánto ha tardado ahora? ¿Por qué?
6. Todas las resoluciones que pongamos en el fichero `/etc/hosts` del servidor dnsmasq, podrán ser consultada por el cliente. 
7. Añade algunos nombres con sus direcciones IP en el fichero `/etc/hosts` del servidor dnsmasq (algunas de las páginas web que has realizado en otras prácticas, nombre inventados,...). Reincia el servicio. Asegúrate que esos nombres no están en la resolución estática del cliente. Comprueba que puedes hacer resolución directa e inversa de los nombres que has guardado en el servidor dnsmasq.


