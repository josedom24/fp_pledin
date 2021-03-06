---
permalink: /lmgs/2020-2021/html5/formularios.html
layout: single3
---

# Formularios

Los formularios son un elemento presente en muchas páginas web que nos permiten introducir información que se envía al servidor para su procesamiento.

El procesamiento de la información en el servidor necesita que nuestra página web este programada con un **lenguaje de programación web: PHP, Java, Python,** .... Ya que como hemos dicho **HTML5 no es un lenguaje de programación**.


## Estructura del formulario

Todos los elementos que nos vamos a encontrar en un formulario están dentro de la etiquete **<form>**. Esta etiqueta puede tener varios atributos de entre los que destacamos:

* **method** que indica cómo se va a pasar la información al destino. Puede ser por GET (se ve la información en la barra del navegador) y por POST ( no se ve y es la opción por defecto).
* **action** que indica el destino de nuestros datos. Normalmente será una URL que indica el programa que va a procesar dicha información. 

A continuación vamos a ver algunos de los elementos más frecuentes y a describir su estructura y funcionamiento.

### Labels e Input

Normalmente para la recogida de información los formularios usando etiquetas **<input>**. Pero, para poder saber qué campos estamos rellenando una buena práctica (se puede de otras maneras menos elegantes) es poner una etiqueta **<label>** (etiqueta) delante de cada input para dar nombre y asociar ambas.

Un ejemplo sería:

```html
<label for="nombre">Nombre:</label>
<input type="text" id="nombre" name="..." />
```

Aquí estamos asociando la etiqueta al campo usando los atributos **_for_** e **_id_**.

El campo que hemos usado para la recogida de información es un input. Existen muchos tipos que veremos con más detalle en el próximo apartado.

#### Tipos de Input en los formularios

La lista de tipos (type) de Inputs que podemos tener es muy larga. La podemos ver en la siguiente imagen:

![tipos inputs](img/input.png)

El que más usado el **text** que nos proporciona la manera más secilla de introducir texto.

Veamos algunos otros:

* **Radio Group**

Es una agrupación de inputs que presenta opciones que queremos que sean excluyentes:

Un ejemplo sería:

```html
<label for="genero">Sexo</label>
<input type="radio" name="genero" value="masculino" />Hombre<br />
<input type="radio" name="genero" value="fememino" checked />Mujer<br />
```

Para que sean excluyentes deben de tener el mismo valor para el atributo **_name_** y el **_type="radio"_**

* **CheckBoxes**

Es una agrupación de opciones que presenta opciones de las cuáles podemos elegir una o varias.

Un ejemplo sería:

```html
    <label for="dispositivos">Dispositivos electrónicos</label><br />
    <input type="checkbox" name="dispositivos" value="pc" />PC<br />
    <input type="checkbox" name="dispositivos" value="table" />Tableta<br />
    <input type="checkbox" name="dispositivos" value="movil" />Móvil
```

Fijaros que para agruparlos deben de tener el mismo valor para **name** y el **_type="checkbox"_**


* **Data Lista**

Es una nueva forma en HTML5 de hacer una lista de valores posibles para un input.

Un ejemplo sería:

```html
    <input list="editor">

    <datalist id="editor">
        <option value="Atom">
        <option value="NotePad++">
        <option value="VsCode">
        <option value="Sublime">
        <option value="Brackets">
    </datalist>
```

Con el atributo **list** indicamos la lista de opciones que vamos a tener y en la etiqueta **<datalist>** metemos las **<option>** que queramos.

Es importante destacar que podríamos meter otras opciones en el Input pero al usar esta estructura se nos ayuda a rellenarlo y a elegir la opción correcta.

### Listas desplegables

Son elementos que también hemos visto muchas veces. Al hacer click sobre ellos nos muestran varias opciones de las que podremos escoger una o varias.

Para crear listas desplegables usaremos las etiquetas **select** como etiqueta padre y una etiqueta **option** para cada una de las opciones que tengamos en la lista desplegable. Si queremos agrupar esas opciones las meteremos a su vez dentro de una etiqueta **optgroup**.

Un ejemplo sería:

```html

<select name="provincia">
    <optgroup label="Aragon">
        <option value="Z">Zaragoza</option>
        <option>Huesca</option>
        <option selected>Teruel</option>
    </optgroup>

</select>

```

### Áreas de Texto

Son campos de formulario para meter texto largos. Tienen dos atributos interesantes.

- **rows:** para indicar el número de filas que tiene el campo.
- **cols:** para indicar el número de columnas que tiene el campo.

Un ejemplo sería:

```html
<textarea cols="10" rows="10">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque voluptate corrupti ut earum, aliquam sint amet repellendus, vitae placeat repellat quis, ipsa qui. Velit placeat reiciendis tempore autem nostrum eaque?
</textarea>
```

### Botones

La etiqueta **button** no creo que se necesario explicar para que sirve...Haz click!!!

El atributo más importante que tienen es type que puede tomar tres valores:

- **button:** se comporta como un botón que puede estar presionado o no. Nada especial.
- **reset:** al hacer click borra todos los datos introducidos previamente en el formulario y pone los valores por defecto.
- **submit:** al hacer click envía los datos introducidos al destino que hemos puesto en el action del formulario.

### Agrupando atributos

Hay situaciones en las que los campos de los formularios por significado, por importancia o por cualquier razón, queremos que se muestren agrupados. Para estos casos tenemos la etiqueta **fieldset**, que tendrá anidada la etiqueta **legend** (una etiqueta que contiene el nombre del grupo y que se mostrará en la parte de arriba) y los controles que queremos agrupar. 

Un ejemplo sería:

```html
<fieldset>
    <legend>Datos Personales</legend>
    <p>
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" placeholder="Inserta Nombre" required />
    </p>
    <p>
        <label for="apellidos">Apellidos:</label>
        <input type="text" name="apellidos" value="Pérez" readonly />
    </p>

    <p>
        <label for="provincia">Provincia</label>
        <select name="provincia">
            <optgroup label="Aragon">
                <option value="Z">Zaragoza</option>
                <option>Huesca</option>
                <option selected>Teruel</option>
            </optgroup>

        </select>
    </p>

    <p>
        <input type="submit" value="Enviar" />
    </p>
</fieldset>
```

### Atributos interesantes de los elementos de los formularios

Además existen una serie de atributos interesantes que podemos añadir a los controles o elementos de los formularios:

- **required** que indica que un control es obligatorio de rellenar.
- **disabled** que mostrará el elemento como deshabilitado.
- **readonly** que nos dice que el campo es de sólo lectura.
- **placeholder** que muestra un mensaje en los input dando pistas de lo que debemos poner. Al empezar a rellenarlo desaparece.
- **selected** indica la opción seleccionada.
- **value** el valor que tiene el elemento..
- **tabindex** para asegurarnos que podemos navegar por los elementos usando el tabulador podemos establecer un orden para cada uno.
- **multiple** para seleccionar varias opciones en una lista desplegable.
- Y muchos más...



## Envío de información al servidor usando formularios

Cada componete de un formulario HTML posee un nombre (etiqueta **name** al cual se le asigna un valor (etiqueta **value** que no siempre se pone), el cual se corresponde con lo que el usuario introduce en el componente.

Cuando se envían los datos del formulario (normalmente a través de un botón), se envían todos los nombres y valores de los controles del formulario. En el caso típico, un servicio de Internet recoge esta información y hace algo con ella.

![html5](img/envio.png)

Veamos un ejemplo de formulario:

```html
<form action="servicio.php">
    <label for="nombre">Escriba su nombre</label><br>
    <input type="text" id="nombre" name="nombre"><br>
    <label for="apellidos">Escriba sus apellidos</label><br>
    <input type="text" id="apellidos" name="apellidos"><br>
    <label for="sexo">Escriba su sexo: </label><br>
    <input type="radio" id="hombre" name="sexo" value="hombre">
    <label for="hombre">Hombre</label>
    <input type="radio" id="mujer" name="sexo" value="mujer">
    <label for="mujer">Mujer</label><br><br>
    <input type="submit" value="Enviar"/>
</form>
```


### Envío de datos usando el método GET

Una petición HTTP usando el método GET, nos permite solicitar la respuesta de una URL determinada. En este método los datos se pasan en la propia URL. Para enviar el formulario usando el método GET, la etiqueta **form** sería:

```html
<form action="servicio.php" method="get">
```

Al enviar el formulario usando el método GET cada par de nombre y valor de cada componente del formulario se envía usando la URL, por ejemplo con el formulario de ejemplo, la URL sería:

    http://nombredominio/servicio.php??nombre=Jose&apellidos=Perez&sexo=hombre&...

### Envío de datos usando el método POST

En muchas ocasiones es preferible mandar la información usando el método POST, para ello:

```html
<form action="servicio.php" method="post">
```

Al enviar la información del formulario usando el método POST, la información que envíamos (nombre y valor de cada componente) se manda en el cuerpo de la petición HTTP por lo tanto no es visible en la URL.
