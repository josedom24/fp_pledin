---
title: "Orquestación con Heat en OpenStack"
---

##  OpenStack Heat 

**Heat** es el servicio de orquestación de OpenStack, nos permite gestionar recursos en nuestra infrestructura en la nube (instancias, volúmenes, redes,...) de forma automática.
  
## Conceptos
    
* Stack: Es el conjunto de recursos que se van a crear con Heat (Instancias, volúmenes, redes, subredes, puertos, etc.)
* Template: Sirve para definir los recursos del Stack y sus relaciones.
* Parámetros: Es una de las secciones del template, y en ella podemos pedir información al usuario (imagen, par de claves,...)
* Resources: Siguiente sección del template donde definimos los recursos que vamos a añadir o modificar.
* Output: Tercera sección del template, que nos permite indicar la información que tenemos que ofrecer al usuario (ip flotante, ...)
* HOT (Heat Orchestration Template), el formato de los  templates en heat, escrito en YAML. 
 
  
## ¿Cómo funciona Heat?
    
* En el template describimos la la infraestructura que queremos crear. 
* Se describe cada uno de los [recursos](http://docs.openstack.org/developer/heat/template_guide/index.html)  que necesitamos. 
* Heat ofrece un servicio de autoescalado, utilizando la información que nos ofrece el componente *Ceilometer*.
* Se puede especificar también las relaciones que hay entre los recursos (volumen conectado a una instancia).
* Heat maneja el ciclo de vida completo de la infraestructura, cuando necesitas cambiarla, solo hay que modificar el template y realizar la actualización del stack. 
* Heat gestiona infrestructura, pero los templates se pueden integrar con herramientas de automatización para realizar la configuración de los recursos. 

## Ejemplo 1: Instancia con IP flotante


Vamos a trabajar con en el ejemplo 1 del repositorio [opentack_ic](https://github.com/josedom24/openstack_ic). Si quieres puedes hacerte un fork.

### Lanzar un stack Heat desde Horizon

* **Orquestación** → **Pilas** → **Lanzar Pila**.
* Selecciona la plantilla eligiendo el archivo.
* Modifica el fichero `env` y pon tus datos. Elígelo como archivo de entorno.
* Tienes que poner un nombre a la pila y poner tu contraseña.
* Introducir los parámetros: Si no usaste un `.env`, Horizon muestra los parámetros definidos en el template: **image**, **flavor**, **network**, **key_name**, **public_network**.

Una vez que se ha lanzado la pila, puedes comprobar que se han creado los recursos. Además puedes hacer distintas operaciones:

* Ver los recursos: Accede a la pila y ve a la pestaña **Topología**.
* Salidas de la plantilla: Si quieres ver la sección **output** de la plantilla con la información, puedes ir a la pestaña **Visión general**.
* Puedes ver los recursos que se han creado en la pestaña **recursos**.

Operaciones:

* **Suspender pila**: Deja el escenario sin funcionar (por ejemplo detiene las instancias). Una pila se puede **reanudar**.
* **Comprobar pila**: Revisa que todos los recursos creados por Heat sigan existiendo y funcionando correctamente.
* **Suprimir pila**: Elimina la pila y los recursos creados.

{% capture notice-text %}
## Ejercicio

1. Crea la pila desde Horizon.
2. Comprueba los recursos que se han creado.
3. Accede a la instancia, para comprobar que funciona.
4. Elimina la pila y comprueba que todos los recursos se han eliminado.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

### Lanzar una pila con OSC

Para utilizar heat desde la línea de comandos, además del cliente de OpenStack, tenemos que instalar el siguiente paquete:

```
sudo apt install python3-heatclient
```

A continuar cargamos la credenciales: `source Proyecto\ de\ josedom-openrc.sh`.

Veamos distintas operaciones:

* Para crear una pila: `openstack stack create -t template.yaml -e env nombre_pila`.
* Si no indicamos el fichero de parámetros, habrá que indicarlo al crear la pila. En este ejemplo:

  ```
  openstack stack create \
  -t template.yaml \
  -P image="Ubuntu 22.04" \
  -P flavor="m1.small" \
  -P network="red-interna" \
  -P key_name="mi_clave" \
  -P public_network="public" \
  nombre_pila
  ```

* Listar las pilas: `openstack stack list`.
* Ver detalles de una pila: `openstack stack show nombre_pila`.
* Ver recursos creados por la pila: `openstack stack resource list nombre_pila`.
* Actualizar una pila: `openstack stack update -t nuevo_template.yaml -e env nombre_pila`
* Comprobar el estado de una pila: `openstack stack check nombre_pila`
* Ver la información de salida de una pila: `openstack stack output show nombre_pila --all`
* Suspender una pila: `openstack stack suspend nombre_pila`
* Reanudar una pila: `openstack stack resume nombre_pila`
* Eliminar una pila: `openstack stack delete nombre_pila`.

{% capture notice-text %}
## Ejercicio

1. Crea la pila desde la línea de comandos con OSC.
2. Comprueba los recursos que se han creado.
3. Visualiza la información de salida de la pila para encontrar la dirección IP de la instancia.
4. Accede a la instancia, para comprobar que funciona.
5. Elimina la pila y comprueba que todos los recursos se han eliminado.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Ejemplo 2: Instancia ejecuta sobre volumen, con un disco extra

{% capture notice-text %}

## Ejercicio

1. Crea la pila del ejemplo desde la línea de comandos con OSC.
2. Comprueba los recursos que se han creado.
3. Visualiza la información de salida de la pila para encontrar la dirección IP de la instancia.
4. Accede a la instancia, para comprobar que tiene un disco adicional.
5. Elimina la pila y comprueba que todos los recursos se han eliminado.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>

## Ejemplo 3: Dos instancias (una con IP flotante) conectada a una nueva red y un nuevo router
{% capture notice-text %}

## Ejercicio

1. Crea la pila del ejemplo desde la línea de comandos con OSC.
2. Comprueba los recursos que se han creado.
3. Visualiza la información de salida de la pila para encontrar la dirección IP de la instancia.
4. Accede a la instancia con IP flotante y haz otro ssh para acceder la segunda instancia.
5. Elimina la pila y comprueba que todos los recursos se han eliminado.
6. **Modifica la plantilla para que podamos escoger la imagen para crear la segunda instancia**.

{% endcapture %}<div class="notice--warning">{{ notice-text | markdownify }}</div>
