---
title: "Ejercicio 2: DNSmasq como DNS cache/forward en una red local"
permalink: /serviciosgs/u04/ejercicio2.html
---

## Escenario

1. En nuestra red local tenemos un **servidor Web** que sirve dos páginas web: `www.iesgn.org`, `departamentos.iesgn.org`. 
2. Vamos a instalar en nuestra red local un servidor DNS (lo puedes instalar en el mismo equipo que tiene el servidor web)
3. El nombre del servidor DNS va a ser ``tunombre.iesgn.org``.

## Servidor DNSmasq

1. Antes de hacer la instalación, configura de forma adecuada el FQDN de tu servidor DNS: `tunombre.iesgn.org`.
2. Instala el servidor dns **dnsmasq** en ``tunombre.iesgn.org`` y configúralo para que los clientes puedan conocer los nombres necesarios.
3. Modifica los clientes para que utilicen el nuevo servidor dns.

{% capture notice-text %}
**Entrega**

* Una consulta a `www.iesgn.org`, y a `www.josedomingo.org`. 
* Realiza una prueba de funcionamiento para comprobar que el servidor dnsmasq funciona como cache dns. 
* Una consulta preguntando por el nombre del servidor DNS. ¿Se puede realizar resolución inversa?. 
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
