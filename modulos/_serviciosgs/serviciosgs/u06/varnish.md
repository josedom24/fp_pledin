---
title: "Introducción a varnish"
permalink: /serviciosgs/u06/varnish.html
---

## ¿Qué es Varnish?

[Varnish](http://varnish-cache.org/) es un **acelerador HTTP** que funciona como un proxy reverso. Se sitúa por delante del servidor web, cacheando la respuesta de dicho servidor web en memoria. La próxima vez que un visitante visite la misma URL, la página será servida desde Varnish en lugar de desde el servidor web, ahorrando recursos en el backend y permitiendo más conexiones simultáneas. También se puede usar como **balanceador de carga**, distribuyendo peticiones a varios servidores o como **control de acceso** a tu servidor, por ejemplo permitiendo conexiones sólo desde la IP o grupo de IPs especificadas.

Las principales características de Varnish son:

* Es estable y muy rápido, capaz de servir varios cientos de miles de peticiones por segundo, según ciertos [benchmarks](https://kly.no/posts/2010_10_23__High_End_Varnish___275_thousand_requests_per_second___.html).
* Dispone de un lenguaje propio de configuración, llamado **VCL** (Varnish Configuration Language), con el que es posible definir las reglas para cachear contenido. Gracias a esto es extremadamente flexible, pudiéndose configurar para solucionar problemas muy diversos.
* Está escrito en **C**, y es posible extender su funcionalidad con módulos llamados **VMODs**, escritos asimismo en C. Puedes ver una [lista de VMODs publicados](http://varnish-cache.org/vmods/) aquí.
* Ofrece soporte para GZIP y ESI ([Edge Side Includes](https://en.wikipedia.org/wiki/Edge_Side_Includes)), y es capaz de recomponer una página usando ESI sin pasar por el back-end. Esto permite cachear fragmentos de la página usando tiempos de expiración diferentes, mostrando siempre contenido fresco sin necesidad de borrar de caché las secciones menos cambiantes de la página.

## ¿Cómo usar Varnish?

Una vez instalado Varnish desde el repositorio de tu sistema operativo, hay que configurarlo para que sea el encargado de recibir todas las peticiones desde el exterior. Vamos a editar el archivo `/etc/default/varnish` y a configurar el demonio para que escuche desde el puerto 80 de la interfaz pública del servidor.

    DAEMON_OPTS="-a :80 
     -T localhost:6082 
     -f /etc/varnish/default.vcl 
     -S /etc/varnish/secret 
     -s malloc,1G"

Lo más interesante de esta sencilla configuración es el parámetro -s. Con él indicaremos dónde queremos guardar la caché (RAM o disco) y cuanto espacio queremos reservar. Obviamente la RAM (malloc) es varios órdenes de magnitud más rápida que el disco por lo que es recomendable usarla para almacenar la caché siempre y cuanto dispongas de suficiente memoria en el servidor. Puedes usar el comando `varnishd --help` puedes ver que significa cada parámetro.

Hay muchas más opciones configurables pero que sólo hará falta cambiarlas en servidores con mucho tráfico (varios millones de visitas). Si estás interesado, este [tutorial](https://kly.no/posts/2009_10_19__High_end_Varnish_tuning__.html) al respecto es muy interesante.

A continuación debemos cambiar la configuración del servidor para que deje de escuchar en el puerto 80 de la IP pública.

## Lenguaje de configuración VLC

Varnish utiliza un lenguaje de configuración llamado apropiadamente VCL (Varnish Configuration Language). Su sintaxis recuerda un poco a C o Perl y es compilado a C por Varnish, que ejecutará las directivas de caché según estén definidas en un archivo de configuración, situado en `/etc/varnish/default.vcl`. En la web de Varnish hay un completo [manual de VCL](http://varnish-cache.org/docs/3.0/reference/vcl.html) que recomiendo seguir para poder dominar VCL en profundidad.

En este fichero tenemos que configurar donde se encuentra el servidor web (backend), si suponemos que hemos configurado el servidor web para que escuche en el puerto 8080:

    backend default {
        .host = "127.0.0.1";
        .port = "8080";
    }

Por último indicar que con el comando `varnishstat` podemos obtener la estadística de uso de varnish.