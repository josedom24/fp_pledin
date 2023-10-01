---
title: "Práctica: Virtualización en Linux y servidor DHCP (Parte 2)"
---

## 3. Instalación del servidor DHCP 

1. Instala un servidor DHCP en el contenedor **servidorDHCP** con las siguientes características:
	* Rango de direcciones: `192.168.200.10` - `192.168.200.200`.
	* Máscara de red: `255.255.255.0`
	* Duración de la concesión: 30 minutos
	* Puerta de enlace: `192.168.200.1`
	* Servidor DNS: `172.22.0.1`

## 5. Instalación del servidor Web

Para ello sigue los siguientes pasos:

1. Instala el servidor `apache2` en el contenedor **servidorWeb**.
2. Crea en tu host un directorio en `/srv/web` con un fichero `index.html`.
3. Monta ese directorio en el directorio `/var/www/html` del contenedor **servidorWeb**.
4. Configura en el **router** una regla de DNAT para que podamos acceder al servidor Web desde el exterior.

{% capture notice-text %}
## Entrega

1. 
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


