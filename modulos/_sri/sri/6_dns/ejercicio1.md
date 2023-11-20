---
title: "Ejercicio 1: Consultas DNS con dig"
---

## ¿Qué vas a aprender en este ejercicio?

* Usar el comando `dig` para realizar consultas DNS.
* Aprender a hacer consultas DNS para preguntar información del servidor DNS.
* Vamos a consultar la información de diferentes registros: NS, A, CNAME, MX, PTR.

## ¿Qué tienes que hacer?

`dig` es una herramienta que permite hacer consultas a un servidor DNS desde la línea de comandos. La sintaxis es:

	dig [tipo de registro] [@servidor DNS] Consulta DNS

El tipo de registro por defecto es A y el servidor DNS por defecto el definido en `/etc/resolv.conf`.

Nota: si no funciona el comando `dig`, instala el paquete `dnsutils` que lo incluye.

Utilizando el comando `dig` realiza las siguientes consultas al servidor DNS (recuerda que la respuesta estará en la sección `ANSWER SECTION`):

1. La dirección IP de los siguientes dominios:

		www.gonzalonazareno.org
		www.debian.org

2. Los servidores con autoridad de los dominios:

		Dominio raíz
		es
		gonzalonazareno.org

3. Los servidores de correo de los dominios:

		gonzalonazareno.org
		us.es

4. ¿Qué tipo de registro es el que resuelve los siguientes dominios?:

		www.josedomingo.org
		informatica.gonzalonazareno.org

5. Comprueba la dirección ip y el servidor DNS asociado a `dit.gonzalonazareno.org`, desde dentro de la intranet del ciclo formativo y desde fuera (para ello haz una consulta al servidor `1.1.1.1`). ¿Cuáles son las diferencias? ¿A qué es debido?

6. Pregunta sobre resolución inversa: En clase, ¿a qué nombre corresponde la dirección ip `172.22.0.1`?

