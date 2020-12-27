---
permalink: /lmgs/2020-2021/html5/etiquetas_listas.html
layout: single3
---

## Listas

Las **listas** nos permiten colocar texto en líneas separadas. Pueden ser listas ordenadas o no ordenadas. Para las primeras usamos las etiquetas:

`<ol></ol>`

mientras que para las segundas:

`<ul></ul>`

Los elementos colocados dentro de la lista, ordenadas o sin ordenar, se sitúan con la etiqueta:

 `<li>Elemento de la lista</li>`

Esta etiqueta debe estar siempre dentro de alguna de las anteriores. Todos las etiquetas usadas para describir listas son **etiquetas de bloques**.

Ejemplo de uso de listas ordenadas y no ordenadas

```html
<!DOCTYPE html>
<html lang="es" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Listas</title>
  </head>
  <body>
    <h2>Lista ordenada. Pasos:</h2>
    <ol>
      <li>Conectarse al servidor</li>
      <li>Solicitar documento</li>
      <li>Esperar respuesta</li>
    </ol>
    <h2>Lista no ordenada. Comprar:</h2>
    <li>Leche</li>
    <li>Café</li>
    <li>Pan</li>
  </body>
</html>
```

Queda renderizado de la siguiente manera:

![html5](img/html-05.png)

