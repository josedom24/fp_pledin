---
title: "Ejercicio 1: Instalación y configuración del servidor bind9 en nuestra red local"
---

## Escenario

1. En nuestra red local tenemos un **servidor Web** que sirve dos páginas web: `www.iesgn.org`, `departamentos.iesgn.org`. 
2. Vamos a instalar en nuestra red local un servidor DNS (lo puedes instalar en el mismo equipo que tiene el servidor web)
3. El nombre del servidor DNS va a ser ``tunombre.iesgn.org``.

## Servidor bind9

Instala un servidor dns **bind9**.  Las características del servidor DNS que queremos instalar son las siguientes:

* El servidor DNS se llama ``tunombre.iesgn.org`` y por supuesto, va a ser el servidor con autoridad para la zona ``iesgn.org``.
* Vamos a suponer que tenemos un servidor para recibir los correos que se llame ``correo.iesgn.org`` y que está en la dirección x.x.x.200 (esto es ficticio).
* Vamos a suponer que tenemos un servidor ftp que se llame ``ftp.iesgn.org`` y que está en x.x.x.201 (esto es ficticio)
* Además queremos nombrar a los clientes.
* También hay que nombrar a los virtual hosts de apache: ``www.iesgn.org`` y ``departamentos.iesgn.org``
* Se tienen que configurar la zona de resolución inversa.

{% capture notice-text %}
* Entrega las zonas que has definido.
* Realiza las consultas dig/nslookup desde los clientes preguntando por los siguientes:
	* Dirección de ``pandora.iesgn.org``, ``www.iesgn.org``, ``ftp.iesgn.org``
	* El servidor DNS con autoridad sobre la zona del dominio ``iesgn.org``
	* El servidor de correo configurado para ``iesgn.org``
	* La dirección IP de ``www.josedomingo.org``
	* Una resolución inversa
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>