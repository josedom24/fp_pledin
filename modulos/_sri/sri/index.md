---
title: "Servicios de Red e Internet + HLC (2023-2024)"
---

<!--
## Unidad 9: Clúster de alta disponibilidad

* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/clusterHA.pdf)
* [Escenarios de HA con pacemaker y corosync](https://github.com/josedom24/escenarios-HA)
    * [Escenario 1: Balanceo de carga por DNS](https://github.com/josedom24/escenarios-HA/tree/master/01-Balanceo-DNS)
    * [Escenario 2: Balanceo de carga por DNS con nombre virtuales](https://github.com/josedom24/escenarios-HA/tree/master/02-Balanceo-DNS-Delegado)
    * [Escenario 3: Balanceo de carga con HAProxy](https://github.com/josedom24/escenarios-HA/tree/master/03-Balanceo-HAProxy)
    * [Escenario 4: HA con pacemaker y corosync. IP Failover](https://github.com/josedom24/escenarios-HA/tree/master/04-HA-IPFailover)
    * [Escenario 5: HA con pacemaker y corosync. IP Failover + Apache2](https://github.com/josedom24/escenarios-HA/tree/master/05-HA-IPFailover-Apache2)
    * [Escenario 6: HA con pacemaker y corosync. IP Failover + Apache2 + DRBD](https://github.com/josedom24/escenarios-HA/tree/master/06-HA-IPFailover-Apache2%2BDRBD)
    * [Escenario 7: HA con pacemaker y corosync. IP Failover + Apache2 + RDBD + GFS2 (Activo-Activo)](https://github.com/josedom24/escenarios-HA/tree/master/07-HA-IPFailover-Apache2%2BDRBD%2BGFS2)
* [Introducción a los cluster de HA con Galera MariaDB](https://www.josedomingo.org/pledin/2022/02/galera-mariadb/)
* [Práctica: Clúster de Alta Disponibilidad](9_clusterha/practica.html)


## Unidad 8: Kubernetes

* [Teoría](https://github.com/josedom24/presentaciones/raw/main/servicios/kubernetes.pdf)
* [Curso Kubernetes](https://github.com/josedom24/curso_kubernetes_ies)
	* [Ejercicio 1: Instalación y configuración de minikube y kubectl](8_k8s/ejercicio1.html)
	* [Ejercicio 2: Trabajando con un Pod multicontenedor (**VOLUNTARIO**)](8_k8s/ejercicio2.html)
	* [Taller 1: Trabajando con Pods](8_k8s/t1.html)
	* [Taller 2: Trabajando con ReplicaSet](8_k8s/t2.html)
	* [Taller 3: Trabajando con Deployments](8_k8s/t3.html)
	* [Taller 4: Trabajando con Services](8_k8s/t4.html)
	* [Taller 5: Despliegues parametrizados](8_k8s/t5.html)
	* [Taller 6: Almacenamiento en Kubernetes](8_k8s/t6.html)
	* [Taller 7: Instalación de un CMS con Helm](8_k8s/t7.html)
* [Práctica: Kubernetes](8_k8s/practica.html)

## Unidad 7: Almacenamiento

* [Teoría](https://github.com/josedom24/presentaciones/raw/main/servicios/almacenamiento.pdf)
* [Introducción al sistema de ficheros btrfs](7_almacenamiento/btrfs.html)
* [Introducción a iSCSI](7_almacenamiento/iscsi.html)
* [Introducción a DRBD](7_almacenamiento/drbd.html)
* [Introducción a GlusterFS](https://github.com/josedom24/taller_glusterfs)
	* [Taller 1: Gestión de pool de almacenamiento lógico en KVM/libvirt](7_almacenamiento/t1.html)
	* [Taller 2: Introducción a iSCSI](7_almacenamiento/t2.html)
	* [Taller 3: Creación de un cluster DRBD + OCFS2](7_almacenamiento/t3.html)


## Unidad 6: Servidor de correo electrónico

* [Teoría](https://github.com/josedom24/presentaciones/raw/main/servicios/correo.pdf)
* [Curso Correo Electrónico](https://github.com/josedom24/curso_correo_electronico_ies)
	* [Taller 1: Servidor de correo en los servidores de clase](6_correo/t1.html)
* [Práctica: Instalación y configuración de un servidor de correos en el VPS](6_correo/practica.html)

## Unidad 5: Protocolo DNS

* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/dns.pdf)
* [Servidor DNS bind9](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/bind9.pdf)
	* [Ejercicio 1: Consultas DNS con dig](5_dns/ejercicio1.html)
	* [Ejercicio 2: DNSmasq como DNS cache/forward en una red local](5_dns/ejercicio2.html)
	* [Taller 1: Instalación y configuración del servidor bind9 en nuestra red local](5_dns/t1.html)
	* [Taller 2: Instalación y configuración de un servidor DNS esclavo](5_dns/t2.html)
	* [Taller 3: Delegación de subdominios con bind9](5_dns/t3.html)
* [Práctica: Servidores Web, Base de Datos y DNS en nuestros escenario de OpenStack](5_dns/practica.html)

## Unidad 4: Cloud Computing IaaS. OpenStack 

* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/hlc/cloudcomputing.pdf)
* [Curso OpenStack](https://github.com/josedom24/curso_openstack_ies)
	* [Ejercicio 1: Creación de instancias desde Horizon](4_iaas/ejercicio1.html)
	* [Ejercicio 2: Creación de instancias desde OSC](4_iaas/ejercicio2.html)
	* [Ejercicio 3: Gestión de almacenamiento](4_iaas/ejercicio3.html)
	* [Taller 1: Configuración del cliente VPN](4_iaas/t1.html)
	* [Taller 2: Gestión de redes en OpenStack](4_iaas/t2.html)
* [Práctica: Escenario en OpenStack](4_iaas/practica.html)

## Unidad 3: Protocolo HTTP

* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/http.pdf)
	* [Taller 1: Peticiones HTTP](3_http/t1.html)
	* [Taller 2: Configuración del servidor web Apache2](3_http/t2.html)
	* [Taller 3: Instalación de phpmyadmin](3_http/t3.html)
	* [Taller 4: apache2 como proxy inverso](3_http/t4.html)
* [Práctica: Instalación de nginx con PHP](3_http/practica.html)


-->
## Unidad 3: Infraestructura como código
	
* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/iac.pdf)
	* [Taller 1: Ansible - Playbook sencillo](3_iac/taller1.html)
	* [Taller 2: Ansible - Playbook con roles](3_iac/taller2.html)
	* [Taller 3: Vagrant - Creación de una máquina virtual](3_iac/taller3.html)

<!--

	* [Taller 4: Vagrant - Creación de escenarios](3_iac/t4.html)
	* [Taller 5: Vagrant + Ansible](3_iac/t5.html)
* [Práctica: Creación y configuración de un escenario router-nat](3_iac/practica.html)




-->
## Unidad 2: Protocolo DHCP

* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/servicios/dhcp.pdf)
	* [Taller 0: Configuración del cliente VPN](2_dhcp/taller0.html)
	* [Taller 1: Instalación y configuración del servidor DHCP](2_dhcp/taller1.html)
	* [Taller 2: Funcionamiento del servidor DHCP](2_dhcp/taller2.html)
* [Práctica: Virtualización en Linux y servidor DHCP (Parte 2)](2_dhcp/practica.html)

## Unidad 1: Virtualización en Linux (HLC)

* [Teoría](https://raw.githubusercontent.com/josedom24/presentaciones/main/hlc/virtualizacion.pdf)
* [Curso: Virtualización en Linux](https://github.com/josedom24/curso_virtualizacion_linux)
	* [Ejercicio 1: Instalación de QEMU/libvirt. Conexión local y remota](1_virtualizacion/ejercicio1.html)
    * [Ejercicio 2: Creación de máquinas virtuales desde la línea de comandos](1_virtualizacion/ejercicio2.html)
	* [Ejercicio 3: Creación de máquinas virtuales con virt-manager](1_virtualizacion/ejercicio3.html)
    * [Taller 1: Gestión del almacenamiento en QEMU/KVM + libvirt](1_virtualizacion/taller1.html)
	* [Taller 2: Gestión de pool de almacenamiento lógico en KVM/libvirt](1_virtualizacion/taller2.html)
    * [Taller 3: Clonación e instantáneas de maquinas virtuales](1_virtualizacion/taller3.html)
	* [Taller 4: Gestión de redes en QEMU/KVM + libvirt](1_virtualizacion/taller4.html)
    * [Taller 5: Trabajando con contenedores LXC](1_virtualizacion/taller5.html)
* [Práctica: Virtualización en Linux y servidor DHCP (Parte 1)](1_virtualizacion/practica.html)
