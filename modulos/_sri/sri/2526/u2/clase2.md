# Introducción a Kea DHCP

**Kea** es un servidor DHCP (proyecto de ISC, sucesor moderno de `isc-dhcp-server`) diseñado para ofrecer asignación de direcciones IP dinámica y configuración automática de red a clientes.

El protocolo **DHCP (Dynamic Host Configuration Protocol)** permite a los dispositivos obtener información de red automáticamente, como la IP, puerta de enlace, servidores DNS, etc.

# Análisis del fichero de configuración `kea-dhcp4.conf`

A continuación se describen los parámetros principales del siguiente fragmento de configuración:

```json
{
  "Dhcp4": {
    ...
  }
}
```


## 1. interfaces-config

```json
"interfaces-config": {
  "interfaces": [ "ens18" ]
}
```

* Define en qué interfaz de red escucha el servidor DHCP.
* `"ens18"` debe coincidir con el nombre de la interfaz real del sistema.
* Solo los paquetes DHCP recibidos por esta interfaz serán procesados.


## 2. lease-database

```json
"lease-database": {
  "type": "memfile",
  "persist": true,
  "name": "/var/lib/kea/kea-leases4.csv"
}
```

* Indica dónde y cómo se almacenan los arrendamientos (leases) de IP:

  * `"type": "memfile"`: las concesiones se almacenan en memoria y también se escriben en disco.
  * `"persist": true`: los arrendamientos sobreviven a un reinicio del servicio.
  * `"name"`: ruta del fichero donde se guardan las concesiones activas.


## 3. Tiempos de validez de concesiones

```json
"valid-lifetime": 86400,
"max-valid-lifetime": 86400,
```

* `"valid-lifetime"`: duración de una concesión en segundos.

  * 86400 = 24 horas.
  * Después de este tiempo, el cliente debe renovar la IP.

* `"max-valid-lifetime"`: valor máximo permitido para una concesión. Si el cliente solicita más tiempo, este es el máximo que se concede.

### Ampliación teórica: tiempos T1, T2 y T3

En DHCP, los tiempos clave son:

| Tiempo | Descripción                                                                                                                                                    |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **T1** | Momento en que el cliente intenta **renovar** la concesión (por defecto, a la mitad de `valid-lifetime`, es decir, 43200s en este caso).                       |
| **T2** | Momento en que el cliente intenta **renovar con otro servidor** si no obtiene respuesta del primero (por defecto, al 87.5% del tiempo, es decir, 75600s aquí). |
| **T3** | Final del tiempo de concesión (`valid-lifetime`), el cliente debe dejar de usar la IP si no la ha renovado.                                                    |

> Nota: Kea no configura explícitamente T1 y T2; los clientes los calculan según el `valid-lifetime`.


## 4. subnet4

```json
"subnet4": [
  {
    "subnet": "172.22.0.0/16",
    ...
  }
]
```

* Define una **subred IPv4** desde la cual se asignarán direcciones IP.
* `"172.22.0.0/16"`: rango de red sobre el que operará el servidor DHCP.

---

## 5. pools

```json
"pools": [
  { "pool": "172.22.0.5 - 172.22.17.254" }
]
```

* Define el rango de IPs disponibles para los clientes.
* En este caso, se asignan IPs entre `172.22.0.5` y `172.22.17.254`.

---

## 6. option-data

```json
"option-data": [
  { "name": "routers", "data": "172.22.0.1" },
  { "name": "domain-name", "data": "gonzalonazareno.org" },
  { "name": "domain-search", "data": "gonzalonazareno.org,41011038.41.andared.ced.junta-andalucia.es" },
  { "name": "domain-name-servers", "data": "172.22.0.1,192.168.0.1" },
  { "name": "broadcast-address", "data": "172.22.255.255" }
]
```

Cada opción especifica un parámetro de red que se entrega a los clientes:

* **routers**: puerta de enlace predeterminada.
* **domain-name**: nombre de dominio que usarán los clientes.
* **domain-search**: dominios de búsqueda DNS.
* **domain-name-servers**: servidores DNS a utilizar.
* **broadcast-address**: dirección de difusión de la red.


