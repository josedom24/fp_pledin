---
title: "Práctica 2: Instalación/migración de aplicaciones web PHP eb tu VPS"
---

## Tarea 1

Realizar la migración de la primera aplicación que tienes instalada en la práctica anterior a nuestro entorno de producción, para ello ten en cuenta lo siguiente:

1. La aplicación se tendrá que migrar a un nuevo virtualhost al que se accederá con el nombre `portal.tudominio.algo`.
2. Vamos a nombrar el servicio de base de datos que tenemos en producción. Como es un servicio interno no la vamos a nombrar en la zona DNS, la vamos a nombrar usando resolución estática. El nombre del servicio de base de datos se debe llamar: `bd.tudominio.algo`.
3. Realiza la migración de la aplicación.
4. La aplicación debe estar disponible en la URL: `portal.tudominio.algo` (Sin ningún directorio).


## Tarea 2

Instalación / migración de la aplicación Nextcloud:

1. Instala la aplicación web Nextcloud en tu entorno de desarrollo.
2. Realiza la migración al servidor en producción, para que la aplicación sea accesible en la URL: `www.tudominio.algo/cloud`
3. Instala en un ordenador el cliente de nextcloud y realiza la configuración adecuada para acceder a "tu nube".

{% capture notice-text %}
Documenta de la forma más precisa posible cada uno de los pasos que has dado, y entrega pruebas de funcionamiento para comprobar el proceso que has realizado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

