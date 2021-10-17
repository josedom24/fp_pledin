---
title: Gestión de imágenes con OpenStack client (OSC)
---

Podemos encontrar imágenes oficiales para OpenStack en la página: [Get Images](https://docs.openstack.org/image-guide/obtain-images.html). También tenemos una guía para crear nuestras propias imágenes: [OpenStack Virtual Machine Image Guide](https://docs.openstack.org/image-guide/).

## Crear una nueva imagen

Un usuario que no es administrador, no puede subir imágenes públicas. La imagen sólo sería visible para el usuario:

	openstack image create --container-format=bare --disk-format=qcow2 \
	 --file  --file freebsd-13.0-zfs.qcow2 "freeBSD 13.0"

## Listar las imágenes disponibles

	openstack image list

## Ver detalles de la imagen

	openstack image show 1fa049be-667f-4de1-bf7d-50066424a0b0

## Borrar la imagen

	openstack image delete 1fa049be-667f-4de1-bf7d-50066424a0b0

## Documentación

* [OpenStackClient image](http://docs.openstack.org/developer/python-openstackclient/command-objects/image.html)