---
title: "Ejercicio 5: Contratación y configuración de un VPS"
---

Para la realización de distintas prácticas que haremos en distintos módulos, vamos a contratar un VPS (Virtual Personal Server). Los VPS suelen ser instancias de algún cloud (sobre todo de OpenStack) que algunos proveedores de internet comercializan. Tenemos muchas opciones:

* [IONOS VPS](https://www.ionos.es/servidores/vps#packs)
* [OVH cloud](https://www.ovhcloud.com/es-es/vps/)
* [clouding.io](https://clouding.io/)
* [arsys](https://www.arsys.es/servidores/vps)
* [Digital Ocean](https://www.digitalocean.com/pricing/)
* ...

La máquina que alquiléis debe tener al menos estas características:

* 1 vCPU
* 512 Mb RAM
* 10 Gb HD

Además vamos a contratar un nombre de dominio. Hay mucho provedores para alquilar un nombre de dominio: puedes hacer una simple [búsqueda](https://duckduckgo.com/?q=dominios&va=b&t=hc&ia=places).  Los dominios se alquilan normalmente por un año. También puedes mirar algunos nombres de dominio que se ofrecen de forma gratuita como los [tk](http://www.dot.tk/es/index.html).

Una vez que tengas ela máquina debes configurarla de la siguiente manera:

* Nombra la máquina: Tu máquina tendrá un nombre en tu dominio, por ejemplo: `sauron.mordor.com`. Configura de forma adecuada el FQDN de tu máquina, que podrás obtener ejecutando `hostname -f`.
* Para evitar ataques configura una contraseña robusta para un usuario sin privilegio, configura el servidor ssh para que no se pueda acceder con root.
* Debes dar de alta en tu DNS un registro de tipo A con el nombre de la máquina, para que al acceder al nombre de la máquina estemos accediendo a la IP pública.
* Crea un usuario profesor al que se pueda acceder los profesores por ssh, para ello sube a este usuario las [claves públicas de los profesores](https://dit.gonzalonazareno.org/redmine/projects/asir2/wiki/Claves_p%C3%BAblicas_de_los_profesores). Este usuario puede utilizar sudo sin contraseña.

{% capture notice-text %}
**Entrega**

1. Nombre completo de tu máquina, para que pueda acceder a él con el usuario `profesor`.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


