---
title: "Ejercicio 7: Playbook de ansible para la instalación y configuración de apache2"
---

Utilizando como base la receta ansible que utilizaste para el [ejercicio 6](doc/ejercicio_proxy/ejercicio_proxy.zip), modifícala para añadir las siguientes funcionalidades:

* Instalación de un servidor apache2, que sea capaz de ejecutar PHP.
* La receta debe deshabilitar el virtual host default.
* La receta debe poder desactivar los virtualhost que tengas definido en una lista.
* La receta debe poder desactivar los módulos que tengas definido en una lista.

Configura una máquina con la receta que cree dos virtualhost (`www1.tunombre.org` y `www2.tunombre.org`) cada virtual host debe tener un fichero `index.html` y otro `info.php`.

{% capture notice-text %}
1. Entrega la URL del repositorio donde has realizado la receta.
2. Entrega una captura de pantalla del acceso a `www1.tunombre.org`.
3. Entrega una captura de pantalla del acceso a `www2.tunombre.org/info.php`.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>


