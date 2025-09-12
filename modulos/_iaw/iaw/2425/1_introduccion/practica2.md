---
title: "Práctica (2 / 2): Despliegue de página web estática"
---

## Despliegue de nuestro sitio web

Una vez generada nuestra página podemos desplegarla en nuestro servidor en producción. Podemos tener un servidor web propio (que administramos nosotros), o utilizar servicios de hosting para implantar nuestras páginas.

* Vamos a usar un hosting externo para desplegar nuestra página.
* Los servicios modernos para alojar páginas estáticas pueden proporcionar métodos de despliegues automáticos o semiautomáticos, y suelen usar repositorios git (el uso de servidores FTP está desapareciendo).
* Hosting que podemos usar: Netlify, Surge, GitHub Pages, GitLab Pages, render, Firebase, Vercel, Neocities, quantcdn, ...
* Algunos de estos servicios te permiten de forma automática generar en ellos la página estática (Integración Continúa). En nuestra práctica no vamos a usar esa característica. **La página se genera en nuestro ordenador y posteriormente se despliega al hosting externo**.
* Si nos permite varias formas de subir la página al hosting **siempre elegiremos el uso de repositorio Git**.

## ¿Qué tienes que hacer?

1. Elige un servicio de hosting de páginas web estáticas que te permita el despliegue de tu sitio web generado usando un repositorio Git.
2. Recuerda que los ficheros que vamos a desplegar son los generados por el generado de páginas web estática, por lo tanto necesitas **otro repositorio git** donde se guarde el contenido generado que vamos a desplegar (**el que no guardamos en el repositorio anterior**).
3. Despliega manualmente la página que has desarrollado en el hosting elegido.
4. Realiza un script bash que te permita automatizar la generación de la página (integración continua) y el despliegue automático de la página en el entorno de producción, después de realizar un cambio de la página en el entorno de desarrollo. 

{% capture notice-text %}
## Entrega

1. Indica el hosting externo que vas a utilizar.
2. Entrega la URL del repositorio Git que has creado en esta parte de la práctica.
3. Entrega el script que has creado, y **muestra al profesor su funcionamiento**.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
