---
title: "Orquestación con OpenTofu en OpenStack"
---


En este apartado vamos a usar OpenTofu como software de orquestación de escenarios en OpenStack. 
Para ello necesitamos usar el provider de OpenStack.

Cada ejemplo tiene los siguientes ficheros:

* **provider.tf:** define el proveedor de OpenStack.
* **variables.tf:** declara las variables usadas en la infraestructura.
* **terraform.tfvars:** asigna valores concretos a las variables.
* **main.tf:** declara y construye todos los recursos.
* **outputs.tf:** muestra los valores resultantes tras el despliegue.

Lo primero que debes hacer es modificar el valor de la variables en el fichero `terraform.tfvars`. A continucación carga las credenciales para empezar a trabajar:

```
source Proyecto\ de\ josedom-openrc.sh
tofu init
tofu apply
```

Seguimos trabajando con el repositorio [opentack_ic](https://github.com/josedom24/openstack_ic).

## Ejemplo 1: Instancia con IP flotante

{% capture notice-text %}
## Ejercicio

1. Crea el escenario con OpenTofu.
2. Comprueba los recursos que se han creado.
3. Visualiza la información de salida de la pila para encontrar la dirección IP de la instancia.
4. Accede a la instancia, para comprobar que funciona.
5. Elimina el escenario y comprueba que todos los recursos se han eliminado.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>


## Ejemplo 2: Instancia ejecuta sobre volumen, con un disco extra

{% capture notice-text %}

## Ejercicio

1. Crea el escenario del ejemplo con OpenTofu.
2. Comprueba los recursos que se han creado.
3. Visualiza la información de salida de la pila para encontrar la dirección IP de la instancia.
4. Accede a la instancia, para comprobar que tiene un disco adicional.
5. Elimina el escenario y comprueba que todos los recursos se han eliminado.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Ejemplo 3: Dos instancias (una con IP flotante) conectada a una nueva red y un nuevo router
{% capture notice-text %}

## Ejercicio

1. Crea el escenario del ejemplo con OpenTofu.
2. Comprueba los recursos que se han creado.
3. Visualiza la información de salida de la pila para encontrar la dirección IP de la instancia.
4. Accede a la instancia con IP flotante y haz otro ssh para acceder la segunda instancia.
5. Elimina el escenario y comprueba que todos los recursos se han eliminado.
6. **Modifica el escenario para que podamos escoger la imagen para crear la segunda instancia**.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>
