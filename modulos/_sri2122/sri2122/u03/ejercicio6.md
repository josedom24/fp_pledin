---
title: "Ejercicio 6: Apache2 como proxy inverso"
---

Descarga el siguiente [fichero](doc/ejercicio_proxy/ejercicio_proxy.zip) donde encontrarás un escenario vagrant y una receta ansible para configurar el siguiente escenario:

* Una máquina "proxy" conectada al exterior y a una red interna.
* Una máquina "servidorweb" conectada a la red interna.

En la máquina "servidorweb" tenemos instalado un apache2 con dos virtualhost. Suponemos que no podemos acceder a ella por la red de mantenimiento, por lo tanto lo que tienes que hacer es lo siguiente:

1. Crea el escenario vagrant y pasa el ansible para configurar la máquina "servidorweb".
2. Instala un servidor web apache2 en la máquina proxy.
3. Configura el proxy para acceder a las páginas del "servidorweb":
    * Opción 1: Para que se acceda a la primera página con la URL www.app1.org y a la segunda página con la URL www.app2.org.
    * Opción 2: Para que se acceda a la primera página con la URL www.servidor.org\app1 y a la segunda página con la URL www.servidor.org\app2.

{% capture notice-text %}
1. Entrega la configuración realizada para la opción 1.
2. Entrega la resolución estática configurado en tu ordenador para acceder a las páginas de la opción 1.
3. Capturas de pantalla para ver el acceso a las páginas como se indica en la opción 1.
4. Entrega la configuración realizada para la opción 2.
5. Entrega la resolución estática configurado en tu ordenador para acceder a las páginas de la opción 2.
6. Capturas de pantalla para ver el acceso a las páginas como se indica en la opción 2.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


