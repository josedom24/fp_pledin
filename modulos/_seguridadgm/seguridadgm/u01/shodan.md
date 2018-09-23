---
title: "Shodan, el buscador terrorífico"
permalink: /seguridadgm/u01/shodan.html
---

Shodan detecta servidores, cámaras web, routers, impresoras, es decir, todos aquellos dispositivos capaces de conectarse a internet. Google sólo detecta páginas web. Se pide instalar la versión gratuita de Shodan y bichear por la direcciones IP de los dispositivos mas extraños y raros, téngase en cuenta que según la propaganda Shodan detecta 500 millones de dispositivos mensualmente. Será esto cierto. Qué tipo de información proporciona Shodan. ¿Las medidas de seguridad informática están implantadas en todas estas conexiones?.

## Recursos de interés

* [VÍDEO: Para que se utiliza el navegador Shodan](https://www.youtube.com/watch?time_continue=3&v=0phCROiqNV4)

## Ejercicios

1. Busca una webcam e intenta acceder a ella usando el nombre de usuario y la contraseña por defecto. Te puede ser útil este [artículo](https://hackpuntes.com/hacking-camaras-ip-montandome-propio-gran-hermano/). Entrega una captura de pantalla donde se vea la localización de la cámara, el país, el proveedor de internet, los puertos abiertos,...

2. Intenta acceder a un router con el nombre de usuario y la contraseña por defecto. **No hagas ninguna modificación**. Razona tu respuesta: ¿crees que es legal hacer una modificación a la configuración de un router al que puedas acceder?

3. Comprueba si hay algún sistema con "Windows XP" conectado a internet, ¿en qué país?, ¿qué puerto está exponiendo?. Razona tu respuesta: ¿qué problemas de seguridad puede tener?,¿por qué?

4. Lee el artículo [Este es el estado de la seguridad informática de España, según Shodan](https://www.redeszone.net/2018/04/09/estado-seguridad-espana-shodan/), accede a la URL que nos muestra, indica la siguiente información:

    * ¿Cuántos puertos abiertos hay en España?, ¿cuál es el más usado?, ¿a qué servicio corresponde?
    * ¿Cuántas webcam están abiertas en la actualidad en España?
    * ¿Cuántos sistemas de control industriales están conectados a internet?
    * ¿Cuántas páginas web utilizan el protocolo obsoleto SSLv2 en el protocolo https?
    * ¿Qué porcentaje de servidores SAMBA no tienen habilitados un sistema de autentificación?
    * ¿Cuántas bases de datos están comprometidas?
    * ¿Cuál es la vulnerabilidad más detectada? A qué fallo corresponde.
