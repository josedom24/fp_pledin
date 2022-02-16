---
title: "Práctica: Cluster de Alta Disponibilidad"
---

El objetivo de este práctica es la instalación de una aplicación php (WordPress) sobe dos cluster de alta disponibilidad:

## Cluster de HA activo-pasivo

1. Utiliza el `Vagrantfile` la receta ansible del escenario 6: [06-HA-IPFailover-Apache2+DRBD+GFS2](https://github.com/josedom24/escenarios-HA/tree/master/06-HA-IPFailover-Apache2+DRBD+GFS2) para crear un cluster de alta disponibilidad activo-pasivo. Nota: La receta instala apache2 + php.
2. Comprueba que los recursos están configurados de manera adecuada, configura tu host para que use el servidor DNS y comprueba que puedes acceder de forma adecuada a la página.
3. Instala en los dos nodos un Galera MariaDB.
4. Instala Wordpress en el cluster.

{% capture notice-text %}
## Entrega

1. Una vez pasada la receta. La salida del comando `pcs status`.
2. Antes de instalar wordpress: una captura de pantalla donde se ve accediendo a `index.php` (se accede a nodo1). Apaga el nodo1 y vuelve a entregar un pantallazo a `index.php`. Muestra que accede a nodo2.
3. Antes de instalar WordPress una demostración de que el cluster de Galera MariaDB tiene dos nodos.
4. Pantallazo donde se ve el wordpress instalado con un post creado.
5. Demuestra al profesor que apagando un nodo el WordPress sigue funcionando.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

## Cluster de HA activo-activo

Siguiendo las instrucciones que encuentras en el escenario 6: [06-HA-IPFailover-Apache2+DRBD+GFS2](https://github.com/josedom24/escenarios-HA/tree/master/06-HA-IPFailover-Apache2+DRBD+GFS2) convierte el cluster en activo-activo. **Es necesario instalar el [fencing](https://github.com/josedom24/escenarios-HA/blob/master/06-HA-IPFailover-Apache2%2BDRBD%2BGFS2/fencing.md) para que el cluster funcione de manera adecuada.**
*Nota: Tienes que tener en cuenta que se va a formatear de nuevo el drbd, por lo que se va a perder el wordpress. Si quieres puedes guardarlo en otro directorio, para luego recuperarlo.*

Una vez que el cluster este configurado como activo-activo y WordPress esté funcionado, configura un método de balanceo de carga:

* Balanceo por DNS: Podríamos quitar el recurso VirtualIP y hacer un balanceo de carga por DNS como vimos en el escenario 1 (**1 punto**) o el escenario 2 (**2 puntos**).
* Añadir un balanceador de carga HAProxy (que balancee la carga entre los dos servidores web) (**2 puntos**). 
* Podrías instalar un HAProxy en los dos nodos y crear un recurso del cluster para que los controle. Para ello habría que crear un recurso con pacemaker para controlar los balanceadores de carga (no esta instalado por defecto, el recurso se llama `ocf.pacemaker.happroxy` y lo puedes encontrar en este [repositorio](https://github.com/thisismitch/cluster-agents/). Este [hilo](https://www.reddit.com/r/linuxadmin/comments/6pzbhe/pacemaker_and_haproxy/) te puede ayudar.), y se podría configurar como activo-pasivo o activo-activo (**3 puntos**).

{% capture notice-text %}
## Entrega

1. Una vez configurado el cluster activo-activo: la salida del comando `pcs status`.
2. Pantallazo donde se ve el wordpress instalado con un post creado.
3. Demuestra al profesor el balanceo de carga que has desarrollado.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

