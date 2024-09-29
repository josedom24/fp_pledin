---
title: "Práctica (1 / 2): Despliegue de página web estática"
---

## Descripción

### Generadores de páginas estáticas

En los últimos años se han desarrollado programas de ordenador que nos permiten de forma sencilla generar sitios web estáticos.

* Están programados en distintos lenguajes.
* Incluyen un motor de plantillas para facilitar la generación del código html.
* Por lo tanto es fácil encontrar distintos temas (ficheros de hojas de estilos) para cambiar el aspecto de las páginas generadas.
* El usuario final sólo se debe preocupar del contenido.
* Normalmente el contenido se escribe en un lenguaje de marcas sencillo como es Markdown. 
* Una vez generado el sitio estático sólo tenemos que desplegar el sitio en nuestro servidor en producción.
* Tenemos muchos generadores de páginas estáticas: Jekyll, Hugo, Pelican, ...  

¿Qué tienes que hacer?

1. Elige entre alguno de los programas generadores de páginas web estáticas: lo más usados, son **Jekyll** y **Hugo**. Pero puedes elegir cualquier otro.
2. Lee en la documentación e instala el programa en tu ordenador (en tu host o en alguna máquina virtual).
3. Añade una página de contenido a tu página web escrita en Markdown y genera la página estática. ¿En qué directorio guarda el contenido generado tu generador?
4. Configura el generador para cambiar el nombre de tu página, el tema o estilo de la página,...
5. Genera un sitio web estático con al menos 3 páginas. Deben estar escritas en Markdown y deben tener los siguientes elementos HTML: títulos, listas, párrafos, enlaces e imágenes.
6. El proyecto que has generado para ru sitio web (configuración del generador, páginas en markdown,...) debe estar en un repositorio Git (no es necesario que el código generado se guarde en el repositorio, evítalo usando el fichero `.gitignore`).


{% capture notice-text %}
## Entrega

1. Entrega una captura de pantalla, donde se vea la página web funcionando en local, con las modificaciones realizadas.
2. Entrega la URL del repositorio donde has guardado tu proyecto.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>



 
