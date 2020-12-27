---
permalink: /lmgs/2020-2021/html5/etiquetas_basicas.html
layout: single3
---

## Etiquetas básicas HTML5

**HTML** nos permite estructurar la información. El diseño y el formato lo defineremos con las **hojas de estilo**.

El stándard de HTML5 se aprobó el 28 de octubre de 2014. Podéis encontrar la [documentación oficial de todas las etiquetas] en la página W3C (El Consorcio World Wide Web (W3C) es una comunidad internacional donde las organizaciones Miembros, personal a tiempo completo y el público en general trabajan conjuntamente para desarrollar estándares Web). 

## Etiquetas de línea y etiquetas de bloque

* Una **etiqueta de línea** es aquella que ocupa el espacio mínimo necesario en horizontal, y permite que otro elemento se coloque a su lado. 
* En cambio una **etiqueta de bloque**, ocupa todo el ancho disponible y no permite que otro elemento se coloque a su lado (aunque aparentemente tenga lugar suficiente).

Etiquetas de línea (las más usadas):

`<a>, <span>, <strong>, <img>, <input>, <code>`

Etiquetas de bloque (las más usadas):

`<h1>, <h2>, <h3>, <p>, <ul>, <li>, <div>, <header>, <nav>, <section>, <article>, <footer>, <form>, <table>`


## Comentarios

Además de todas estas etiquetas nuestra página web podrá llevar comentarios que son, normalmente, texto descriptivos que no se van a mostrar en nuestra web.

Los comentarios van encerrados en esta estructura y un ejemplo sería:

`<!-- Esto es un comentario en HTML -->`

## Ejercicio

A continuación se te presenta un documento web con algunos errores de sintaxis y a nivel de estructura del documento web. Señala los errores:

```html
<DOCTYPE html>
<html>
    <head>
        </meta charset="utf-8">
        <meta name="description" content="Ejercicio HTML - Corrige los errores">
    <body>
    </head>
        <title>Corrige los errores que encuenres en el documento</title>
        
    <h1>Aprender HTML es muy divertido</h1>
    
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestiae quam optio nesciunt atque iure  animi dicta velit
   
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestiae quam optio nesciunt atque iure  animi dicta velit</p>
      
   
    </body>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestiae quam optio nesciunt atque iure  animi dicta velit</p>
<html>
```

[Compruebe la solución](doc/solucion1.txt)