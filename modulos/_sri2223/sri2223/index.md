---
title: "Servicios de Red e Internet (2022-2023)"
---

* Infraestructura como código (12 h)
	* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/iac.pdf)
	* [Taller 1: Ansible - Playbook sencillo](1_iac/t1.md)
	* [Taller 2: Ansible - Playbook con roles](1_iac/t2.md)
	* [Taller 3: Vagrant - Creación de una máquina virtual](1_iac/t3.md)
	* [Taller 4: Vagrant - Creación de escenarios](1_iac/t4.md)
	* [Práctica 1: Creación y configuración de un escenario router-nat](1_iac/p1.md) 
	* Prueba final
* Protocolo DHCP (12 h)
	* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/dhcp.pdf)	
	* [Taller 1: Instalación y configuración del servidor DHCP](2_dhcp/t1.md)
	* [Taller 2: Funcionamiento del servidor DHCP](2_dhcp/t2.md)
	* Práctica 1: Configuración de un servidor DHCP
* Protocolo HTTP (18 h)
	* Teoría
	* [Taller 1: Peticiones HTTP](3_http/t1.md)
	* [Taller 2: VirtualHosting con apache2](3_http/t2.md)
	* Taller 3: Configuración del servidor web apache2
	* [Taller 4: apache2 como proxy inverso](3_http/t4.md)
	* [Taller 5: Contratación y configuración de un VPS](3_http/t5.md)
	* Práctica 1: Instalación de un servidor LEMP en nuestra VPS
* Protocolo DNS (24 h)
	* Teoría
	* Taller 1: Ficheros importantes en la resolución de nombres 
	* [Taller 2: Consultas DNS con dig](4_dns/t1.md)
	* [Taller 3: Instalación y configuración del servidor bind9 en nuestra red local](4_dns/t2.md)
	* [Taller 4: Instalación y configuración de un servidor DNS esclavo](4_dns/t3.md)
	* [Taller 5: Delegación de subdominios con bind9](4_dns/t4.md)
	* Taller 6: Servidor DNS dinámico (OPTATIVO???)
	* Práctica 1: DNS en nuestro escenario de trabajo

## 2º Evaluación (10 semanas)

* Protocolo HTTPS (6 horas)
	* Teoría
	* Taller 1: Configuración de HTTPS en apache2
	* Práctica 1: Configuración de HTTPS en el VPS (nginx)
* Protocolo HTTP (2ª Parte)
	* Teoría
	* Taller 1: Balanceador de carga con HAProxy
	* Taller 2: Configuración de memcached
	* Taller 3: Proxy inverso caché con Varnish
	* Taller 4: Haciendo pruebas de rendimiento con ab
	* Taller 5: Comparativa de servidores web sirviendo páginas estáticas
	* Práctica 1: Aumento de rendimiento en servidores web
* Protocolos de correo electrónico
	* Teoría
	* Taller 1: Gestión del correo desde el servidor 
	* Taller 2: Gestión del correo desde un cliente remoto 
	* Pŕactica: Configuración del servidor de correos en el VPS
* Clúster de alta disponibilidad
	* Teoría
	* Taller 1: Balanceo de carga por DNS
	* Taller 2: HA con pacemaker y corosync. IP Failover
	* Taller 3: HA con pacemaker y corosync. IP Failover + Apache2
	* Taller 4: HA con pacemaker y corosync. IP Failover + Apache2 + DRBD
	* Práctica 1: HA con pacemaker y corosync. IP Failover + Apache2 + RDBD + GFS2 (Activo-Activo) 
