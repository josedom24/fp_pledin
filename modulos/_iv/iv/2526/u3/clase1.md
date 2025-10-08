---
title: Primeros pasos con OpenStack
---

## ¿Qué vas a aprender en esta clase?

* Configurar el componente horizon para usar OpenStack
* Gestionar nuestras par de claves en OpenStack
* Gestionar el grupo de seguridad de OpenStack.
* Crear instancias en OpenStack.
* Acceder a las instancias utilizando las IP flotantes.

## Recursos

* [Curso OpenStack](https://github.com/josedom24/curso_openstack_ies)

En concreto, los apartados:

* [Acceso a Horizon y primeros pasos](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo1/horizon.md)
* [Conceptos previos](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/conceptos_previos.md)
* [Creación de instancias a partir de una imagen](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/instancias.md)
* [Operaciones sobre la instancia](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/operaciones.md)

## Ejercicio

1. Siguiendo la documentación de [Acceso a Horizon y primeros pasos](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo1/horizon.md):
    * Accede a **horizon**.
    * Sube tu clave privada a OpenStack, esta clave privada se inyectará en las instancia que creemos.
    * Abre el puerto 22 de tu cortafuegos (**Grupo de Seguridad**).
2. Repasa los [Conceptos previos](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/conceptos_previos.md) sobre instancias.
3. Siguiendo la documentación de [Creación de instancias a partir de una imagen](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/instancias.md):
    * Crea una instancia desde una imagen. No uses volúmenes.
    * Utiliza un sabor que comience con el nombre **m1**.
    * Conecta la instancia a tu red.
    * Elige tu clave pública para que se inyecte en la instancia.
    * Asigna una **Ip flotante** para acceder desde el exterior.
4. Accede a la instancia desde tu ordenador. Recuerda que si eliges la imagen debian el usuario se llama **debian**. El usuario se llama **ubuntu** en el caso de ese sistema operativo.
5. Repasa las distintas [Operaciones sobre la instancia](https://github.com/josedom24/curso_openstack_ies/blob/main/modulo3/operaciones.md).