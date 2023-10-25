---
title: "Taller 4: Contratación y configuración de un VPS"
---

## ¿Qué vas a aprender en este taller?

* Realizar una búsqueda de distintos proveedores que nos ofrezcan el alquiler de VPS.
* A contratar una VPS.

## ¿Qué tienes que hacer?

Para la realización de distintas prácticas que haremos en distintos módulos, vamos a contratar un VPS (Virtual Personal Server). Los VPS suelen ser instancias de algún cloud (sobre todo de OpenStack) que algunos proveedores de internet comercializan. Tenemos muchas opciones:

* [IONOS VPS](https://www.ionos.es/servidores/vps#packs)
* [OVH cloud](https://www.ovhcloud.com/es-es/vps/)
* [clouding.io](https://clouding.io/)
* [arsys](https://www.arsys.es/servidores/vps)
* [Digital Ocean](https://www.digitalocean.com/pricing/)
* [Piensa Solutions](https://www.piensasolutions.com/vps)
* ...

La máquina que alquiléis debe tener al menos estas características:

* 1 vCPU
* 512 Mb RAM
* 10 Gb HD

Además vamos a contratar un nombre de dominio. Hay mucho proveedores para alquilar un nombre de dominio: puedes hacer una simple [búsqueda](https://duckduckgo.com/?q=dominios&va=b&t=hc&ia=places).  Los dominios se alquilan normalmente por un año. 

Una vez que tengas la máquina debes configurarla de la siguiente manera:

1. Nombra la máquina: Tu máquina tendrá un nombre en tu dominio, por ejemplo: `sauron.mordor.com`. Configura de forma adecuada el FQDN de tu máquina, que podrás obtener ejecutando `hostname -f`.
	Para configurar de forma adecuada el FQDN crea una línea en el fichero `/etc/hosts` donde identificas el nombre completo y el nombre corto. Por ejemplo:

	```
	127.0.1.1	sauron.mordor.com sauron
	```

2. Para evitar ataques configura una contraseña robusta para un usuario sin privilegio, configura el servidor ssh para que no se pueda acceder con root. Configura tu clave pública para que puedas acceder con un usuario sin privilegios.
3. Debes dar de alta en tu DNS un registro de tipo A con el nombre de la máquina, para que al acceder al nombre de la máquina estemos accediendo a la IP pública.
4. Crea un usuario `profesor` al que se pueda acceder los profesores por ssh, para ello sube a este usuario las [claves públicas de los profesores](https://dit.gonzalonazareno.org/redmine/projects/asir2/wiki/Claves_p%C3%BAblicas_de_los_profesores). Este usuario puede utilizar `sudo` sin contraseña.


{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Nombre completo de tu máquina, para que pueda acceder a él con el usuario `profesor`.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
