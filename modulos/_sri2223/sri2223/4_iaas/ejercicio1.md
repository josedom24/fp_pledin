---
title: "Creación de instancia desde Horizon"
---

Realiza los siguientes pasos:

1. Subimos nuestra clave pública a openstack.
2. Abrimos en el grupo de seguridad (cortafuegos) default el puerto 22/TCP y todo el protocolo ICMP.
3. Creamos una instancia:
	* Desde la imagen Debian 11
	* No creamos un volumen en la creación
	* Usando un sabor m1
4. Asignamos una IP flotante a la instancia y accedemos por ssh usando el usuario debian.
5. Crea un volumen de 1Gb y asócialo a la instancia.
6. Ejecuta `lsblk` en la instancia para comprobar que has añadido un nuevo dispositivo de bloque.
