---
title: "Clase 1: Introducción al protocolo DHCP"
---

## ¿Qué vas a aprender en esta clase?

* DHCP: definición y propósito (Dynamic Host Configuration Protocol).
* Funcionamiento básico del protocolo DHCP.
* Estados del protocolo DHCP.
* Temporizadores y tiempos importantes.
* Ámbito del servidor DHCP (scope)
* Rango de direcciones que el servidor puede asignar
* Reserva de direcciones IP (asignaciones fijas por MAC)
* Parámetros que puede asignar DHCP a los clientes

## Teoría

* [Teoría: Protocolo DHCP](kea.html)

## Ejercicio

Responde estas preguntas:

1. Explica brevemente las fases del proceso DHCP (DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, DHCPACK).
2. ¿Qué ocurre si el cliente no recibe ninguna oferta de dirección IP?
3. ¿Qué diferencia hay entre una **concesión dinámica** y una **reserva** de dirección IP?
4. ¿Qué parámetros, además de la dirección IP, puede proporcionar un servidor DHCP a un cliente?
5. ¿Qué significa el **tiempo de concesión (lease time)** y qué sucede cuando expira?
6. Describe los estados principales del cliente DHCP: INIT, SELECTING, BOUND, RENEWING y REBINDING.
7. ¿Qué ocurre en la fase de **RENEWING** y qué mensaje se envía?
8. ¿Qué diferencia hay entre los temporizadores **T1** y **T2**?
9. ¿Qué mensaje envía un cliente si detecta que la dirección IP ofrecida ya está en uso?
10. ¿Qué función tiene el parámetro “scope” (ámbito) en la configuración de un servidor DHCP?
11. Si configuras un servidor DHCP en una red, ¿qué rango de direcciones IP conviene excluir del ámbito?
12. ¿Cómo podrías garantizar que una impresora de red siempre reciba la misma dirección IP?
13. ¿Qué sucedería si hay dos servidores DHCP en la misma red local?
14. ¿Por qué cuando encendemos un ordenador suele tener la misma dirección IP que anteriormente?
