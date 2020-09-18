---
title: "Práctica 3: Integridad de ficheros" 
permalink: /seguridadgs/u01/practica_integridad.html
---

En caso de que algún tipo de malware reemplace o falsifique archivos del sistema operativo, ocultándose para realizar tareas no autorizadas, la búsqueda y detección del mismo se complica ya que los análisis antimalware y de los procesos sospechosos por parte de administradores de sistemas, no dudarán de la veracidad de dichos archivos y procesos. A este tipo de malware se le denomina rootkit, programa que sustituye los ejecutables binarios del sistema para ocultarse mejor, pudiendo servir de puertas trasera o backdoor para la ejecución malware remota.

{% capture notice-text %}
* **Tarea 1:** Crea un manual lo más completo posible de las herramientas SFC y DISM para comprobar la integridad de ficheros en Windows. Indica para qué sirven las opciones más usadas del programa y entrega capturas de pantallas para comprobar que has realizado la práctica.
* **Tarea 2:** Del mismo modo, crea un manual de la herramienta `Rootkit Hunter` (rkhunter) en Linux. Indica las opciones mñas usadas del programa y entrega capturas de pantallas para comprobar que has realizado la práctica.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>