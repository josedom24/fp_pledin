---
title: "Clase 5: Tarea - Configuración de un router (SNAT y DNAT)
---

## ¿Qué vas a aprender en esta clase?

* Realiza la configuración de un router Linux
* Activar el reenvío de paquetes.
* Configurar reglas SNAT y DNAT.

## Teoría

* **¿Para qué se usa un router Linux?**

* Para **conectar dos o más redes** y permitir el **enrutamiento de paquetes** entre ellas.
* Útil en redes domésticas, laboratorios o firewalls personalizados.
* Puede realizar funciones como:
  * NAT (traducción de direcciones).
  * Filtrado de paquetes.
  * Redirección de puertos.
  * Compartir conexión a Internet.

* **Habilitar el reenvío de IPs (IP Forwarding)**: Permite que el kernel reenvíe paquetes entre interfaces de red.
    * Comando temporal: `echo 1 > /proc/sys/net/ipv4/ip_forward`
    * Para hacerlo **persistente**:  Editar el archivo `/etc/sysctl.conf` y añadir o descomentar `net.ipv4.ip_forward = 1`. Y ejecutar: `sysctl -p`.
* **SNAT (Source NAT)**: Se usa para **salir a Internet** desde una red local con IPs privadas. Cambia la **IP de origen** de los paquetes por la IP pública del router.

    * Con `iptables`:

    ```bash
    iptables -t nat -A POSTROUTING -o eth0 -s 192.168.0.0/24 -j SNAT --to-source 192.0.2.1
    ```

    * `eth0`: interfaz de salida (por ejemplo, hacia Internet).
    * `-s`: Se indica la red desde la que queremos tener acceso a internet.
    * `192.0.2.1`: IP pública del router.

    * Alternativa más sencilla (masquerade) si se usa IP dinámica:

    ```bash
    iptables -t nat -A POSTROUTING -o eth0 -s 192.168.0.0/24 -j MASQUERADE
    ```
* **DNAT (Destination NAT)**: Se usa para **redirigir tráfico entrante** desde el exterior a una máquina interna. Cambia la **IP de destino** de los paquetes.
    * Con `iptables`:

      ```bash
      iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.1.100:80
      ```

    * Redirige el puerto 80 entrante a una máquina interna con IP 192.168.1.100.


* **Hacer reglas `iptables` persistentes**: Las reglas de `iptables` no sobreviven a un reinicio, se deben guardar. Lo más sencillo para hacerla persistente es usar el paquete `iptables-persistent` (Debian/Ubuntu):
    * Guarda las reglas actuales:

    ```bash
    iptables-save > /etc/iptables/rules.v4
    ```
    * Se restauran automáticamente al iniciar el sistema.

# Recursos

* El [Ejemplo 3: Configuración de un router/NAT](https://github.com/josedom24/curso_kvm_ow/blob/main/curso1/contenidos/unidad06/clase7.md) del curso de virtualización.

## Ejercicio

