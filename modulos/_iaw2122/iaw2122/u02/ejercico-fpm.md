---
title: "Ejercicio 3: Ejecución de PHP con PHP-FPM"
---

En el escenario donde has realizado la práctica vamos a configurar apache2 + PHP-FPM. Para ello realiza los siguientes pasos:

1. Desinstala el módulo de apache2 que permite la ejecución de PHP.
2. Instala PHP-FPM.
3. Configura apache2 para que utilice PHP-FPM para ejecutar PHP, lo puedes hacer para todos los virtualhost o en cada uno de los virtualhost.
4. Comprueba accediendo a un fichero `info.php`, que los script PHP se estan ejecutando con PHP-FPM. Comprueba que los CMS instalados siguen funcionando.
5. Cambia la configuración de PHP-FPM para que escuche en el puerto tcp/9000. Cambia la configuración de apache2 para que se comunique con PHP-FPM utilizando ese puerto.
6. Comprueba que las aplicaciones siguen funcionando.
7. Cambia la memoria máxima de uso de un script PHP (parámetro `memory_limit`) a 256Mb.

{% capture notice-text %}
## Entrega...

* Pantallazo donde se compruebe que tienes corriendo en tu servidor procesos PHP-FPM. 
* Configuración que has hecho en apache2 para trabajar con PHP-FPM.
* Pantallazo donde se vea la salida del fichero `info.php` donde se ve que la ejecución de PHP se hace con PHP-FPM.
* Pantallazos de los CMS funcionando.
* Configuración de PHP-FPM y apache2 para que funcione el punto 5.
* Indica el fichero que has modificado (con el path completo) para modificar el límite de memoria. Muestra un pantallazo de la salida del fichero `info.php` donde se vea el cambio.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
