---
title: "Clase 4: Configuración de red y DNS en sistemas Linux"
---

## ¿Qué vas a aprender en esta clase?

* Los distintos mecanismos de configuración de red en sistemas Linux.
* Configurar los sistemas Linux según el mecanismo de configuración de red que tengan instalado.
* Los distintos mecanismos de resolución de nombres en sistemas Linux.
* Configurar los servidores DNS según el mecanismo de resolución de nombres que estemos usando.

## Teoría

### Configuración de red

Actualmente según la distribución que utilicemos y la configuración del sistema que estemos utilizando, tendremos a nuestra disposición algunos de estos métodos:

* **ifupdown**: Es una herramienta tradicional para configurar redes en Linux basada en los archivos que encontramos en el directorio `/etc/network`. En sistemas modernos con `systemd`, su funcionamiento está vinculado a la unidad `networking.service`, que activa las configuraciones definidas en estos archivos durante el inicio del sistema o cuando se reinicia el servicio. Aunque es más antigua, sigue siendo usada en sistemas donde se prefieren configuraciones más simples o específicas.
* **NetworkManager**: Es una solución moderna y flexible diseñada para entornos de escritorio y servidores. Ofrece una interfaz gráfica (como `nm-applet`) y herramientas de línea de comandos (`nmcli` y `nmtui`). Está orientada a la gestión dinámica de redes y se integra bien con configuraciones más complejas, como Wi-Fi, VPNs y conexiones móviles.
* **systemd-networkd**: Es una alternativa más reciente que forma parte de `systemd`. Se utiliza principalmente en servidores y entornos que buscan configuraciones administradas de manera declarativa a través de archivos de configuración en `/etc/systemd/network/`. Es particularmente eficiente en sistemas modernos que ya utilizan `systemd` para otros servicios.
* **netplan**: Herramienta de configuración de red introducida en Ubuntu, que permite gestionar la red de forma declarativa utilizando archivos YAML. Esta herramienta se encarga de traducir la configuración declarada en sus archivos en configuraciones aplicables por `NetworkManager` o `systemd-networkd`, dependiendo del backend elegido.

### DNS

* **DNS (Domain Name System):** sistema jerárquico que traduce nombres de dominio (como `www.google.com`) en direcciones IP.
* **Servidor DNS:** máquina que responde a estas consultas. Se configura en el archivo `/etc/resolv.conf`.
* **Resolución estática:** asignaciones fijas de nombres a IPs definidas manualmente en `/etc/hosts`.

**Orden de resolución: NSS y nsswitch.conf**

* Linux usa una biblioteca llamada **NSS (Name Service Switch)** para definir **el orden en que se consultan las fuentes de información**, como por ejemplo el mecanismo de resolución de nombre.
* Este orden se configura en el archivo `/etc/nsswitch.conf`, en la línea que comienza con `hosts:`.
  * Ejemplo:

    ```plaintext
    hosts: files dns
    ```
    * Primero consulta `/etc/hosts` (resolución estática).
    * Si no encuentra el nombre, consulta los servidores DNS.

**El archivo `/etc/resolv.conf`**

* Contiene los servidores DNS que se usan para resolver nombres.
* Parámetros comunes:

  * `nameserver`: dirección del servidor DNS (pueden indicarse varios).
  * `search` / `domain`: dominios que se añaden al nombre buscado si no está completo.
  * `options`: opciones como tiempo de espera o número de intentos.
* **¡Ojo!**: A menudo este archivo **se genera automáticamente** (por ejemplo, por `resolvconf` o `systemd-resolved`). No se debe editar directamente si hay un sistema que lo gestiona.

**Herramientas para consultar nombres**

* **Herramientas como `dig`, `host` y `nslookup`:**

  * Consultan directamente al servidor DNS.
  * **No usan** el orden definido en `/etc/nsswitch.conf`.
* **`getent ahosts`:**

  * Usa el orden definido por NSS.
  * Consulta primero `/etc/hosts` y después DNS (si está configurado así).

**systemd-resolved (nuevo método de resolución)**

* Es un servicio moderno de Linux para gestionar la resolución de nombres.
* Es mucho más complejo, pero simplificando ofrece un servidor DNs forward local en `127.0.0.53` que ofrece:

  * Consulta los **servidores DNS** que tiene configurado para resolver nombres.
  * **Caché local de DNS** (mejora el rendimiento).
  * **Integración con NSS** (`resolve`, `myhostname` (resuelve el nombre del host local), `mymachines` (resuelve nombres de contenedores gestionados por `systemd`)).
  * El orden se ajusta en `/etc/nsswitch.conf`, por ejemplo:

    ```plaintext
    hosts: mymachines resolve myhostname
    ```
  * Herramienta propia: `resolvectl`: Comando para interactuar con `systemd-resolved`.
    * Ver configuración: `resolvectl status`
    * Consultar DNS: `resolvectl query nombre`
    * Ver servidores DNS: `resolvectl dns`
    * Borrar caché: `resolvectl flush-caches`

## Recursos

* [Configuración de red en sistemas Linux - ifupdown](https://www.josedomingo.org/pledin/2025/01/configuracion-red-linux-ifupdown/)
* [Configuración de red en sistemas Linux - NetworkManager](https://www.josedomingo.org/pledin/2025/01/configuracion-red-linux-networkmanager/)
* [Configuración de red en sistemas Linux - systemd-networkd](https://www.josedomingo.org/pledin/2025/03/configuracion-red-linux-systemd-networkd/)
* [Configuración de red en sistemas Linux - Netplan](https://www.josedomingo.org/pledin/2025/04/configuracion-red-linux-netplan/)
* [Resolución de nombres de dominios en sistemas Linux](https://www.josedomingo.org/pledin/2024/02/resolucion-nombres-linux/)

## Ejercicio

1. Necesitamos una máquina Linux con el sistema operativo Debian conecta a una red de tipo NAT. En este caso estamos usando el mecanismo **ifupdown**. 
  * Comprueba la configuración actual y visualiza la configuración de red actual.
  * Visualiza las rutas de enrutamiento definidas en el sistema.
  * ¿Cómo se añade una nueva ruta? ¿Cómo se configura una ruta de manera permanente?
  * Cambia a una configuración estática indicando la dirección IP que había tomado de forma dinámica.
2. Para trabajar con **NetworkManager** tenemos varias alternativas:
  * Trabajar con Debian con entorno gráfico gnome.
  * Instalando NetworkManager en nuestro Debian sin entorno gráfico.
  * Usando una distribución Linux que lo use por defecto, por ejemplo Fedora.
3. Prepara una máquina que utilice NetworkManager y realiza los siguientes pasos desde la línea de comandos:
  * Visualiza la configuración de red actual.
  * Cambia a una configuración estática indicando la dirección IP que había tomado de forma dinámica.
  * Si tienes entorno gráfico, utiliza `nm-applet` para gestionar la configuración de red.
4. Normalmente no se trabaja directamente con **networkd-systemd**. Los sistemas que usan este mecanismo de gestión de red suelen tener instalado **netplan**. Es el caso de Ubuntu. Instala una máquina Ubuntu, y realiza los siguientes ejercicios:
  * Comprueba el backend con el que está trabajando netplan.
  * Visualiza la configuración actual del fichero de configuración de netplan.
  * Visualiza la configuración de red actual.
  * Cambia a una configuración estática indicando la dirección IP que había tomado de forma dinámica.

5. En el sistema Debian:
  * Comprueba el orden de mecanismos de resolución de nombres que tienes configurado.
  * Comprueba los servidores DNS que tienes configurado.
  * Añade una resolución estática con el nombre `www.example.com` y una dirección IP privada.
  * Realiza una consulta con `dig` para averiguar la dirección IP de `www.example.com` y otra con `getent ahosts`. ¿Por qué salen resultados distintos?

6. En el sistema Ubuntu:
  * Comprueba el orden de mecanismos de resolución de nombres que tienes configurado.
  * ¿Usa `systemd-resolved`? ¿Por qué?
  * Comprueba los servidores DNS que tienes configurado con `resolvectl`.
  * Realiza una consulta con `resolvectl` para averiguar la dirección IP de `www.example.com`. Quita la resolución estática y vuelve a hacer la consulta.
  * ¿Qué modo uso está utilizando `systemd-resolved`?¿Cómo lo compruebas? 
