---
title: "Esquema iptables/nftables"
permalink: /seguridadgs/u03/esquema.html
---

## El cliente incia la comunicación (la conexión). El cliente hace la petición a mi máquina:

### ENTRADA (INPUT). La petición del cliente.

* Direcciones: -s / saddr
* Interface: -i / iifname 
* Puerto: --dport /dport
* State: NEW,ESTABLISHED

### SALIDA (OUTPUT). La respuesta de mi máquina.

* Direcciones: -d / daddr
* Interface: -o / oifname 
* Puerto: --sport / dport
* State: ESTABLISHED

## Mi máquina inicia la comunicación (la conexión). Mi máquina hace una petición a un servidor:

### SALIDA (OUTPUT). La petición de mi máquina.

* Direcciones: -d / daddr
* Interface: -o / oifname
* Puerto: --dport / dport
* State: NEW,ESTABLISHED

### ENTRADA (INPUT). La respuesta del servidor.

* Direcciones: -s / saddr
* Interface: -i / iifname
* Puerto: --dport / dport
* State: ESTABLISHED


