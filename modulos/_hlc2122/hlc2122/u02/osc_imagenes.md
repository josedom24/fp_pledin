---
title: Gestión de imágenes con OpenStack client (OSC)
---

Podemos encontrar imágenes oficiales para OpenStack en la página: [Get Images](https://docs.openstack.org/image-guide/obtain-images.html). También tenemos una guía para crear nuestras propias imágenes: [OpenStack Virtual Machine Image Guide](https://docs.openstack.org/image-guide/).

## Crear una nueva imagen

Un usuario que no es administrador, no puede subir imágenes públicas. La imagen sólo sería visible para el usuario. tenemos varias [niveles de visibilidad](https://wiki.openstack.org/wiki/Glance-v2-community-image-visibility-design)-

Para subir la imagen:

	openstack image create --container-format=bare --disk-format=qcow2 \
	 --file --disk-format=qcow2  --file cirros-0.5.1-x86_64-disk.img "Cirros 0.5.1"

Para que sea visible por todos:

    openstack image set --community "Cirros 0.5.1"

## Listar las imágenes disponibles

	openstack image list

## Ver detalles de la imagen

	openstack image show "Cirros 0.5.1"

## Borrar la imagen

	openstack image delete "Cirros 0.5.1"

## Documentación

* [OpenStackClient image](https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/image-v2.html)