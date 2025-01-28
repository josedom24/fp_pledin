---
title: "teller 4: Construcción de imágenes configurables con variables de entorno"
---

en este taller vamos a hacer un ejercicio similar al mostrado en el apartado [Ejemplo 4: Construcción de imágenes configurables con variables de entorno](https://github.com/josedom24/curso_docker_ies/blob/main/modulo5/ejemplo4.md) del curso de Docker.

En este taller queremos "dockerizar" una aplicación escrita en PHP8 que gestiona los libros de una biblioteca. Para ello necesitamos una base de datos con una tabla `libros` donde guardaremos la información de los libros. Para ello usaremos el fichero `libros.sql`:

```
drop table if exists `libros`;
CREATE TABLE IF NOT EXISTS libros (
    codigo INT AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    disponible TINYINT NOT NULL,
    PRIMARY KEY (codigo)
)  ENGINE=INNODB;
INSERT INTO libros VALUES (1,'La Guerra y la Paz', 'León Tolstoi', TRUE);
INSERT INTO libros VALUES (2,'Las Aventuras de Huckleberry Finn', 'Mark Twain', FALSE);
INSERT INTO libros VALUES (3,'Hamlet', 'William Shakespeare', TRUE);
INSERT INTO libros VALUES (4,'En busca del tiempo perdido', 'Marcel Proust', FALSE);
INSERT INTO libros VALUES (5,'Don Quijote de la Mancha', 'Miguel de Cervantes', TRUE);
```

La aplicación que queremos desplegar estaría guardada en el fichero `index.php`:

```<?php
// Variables
$hostDB = getenv('DB_HOST');
$nombreDB = getenv('DB_NAME');
$usuarioDB = getenv('DB_USER');
$contrasenyaDB = getenv('DB_PASS');
// Conecta con base de datos
$hostPDO = "mysql:host=$hostDB;dbname=$nombreDB;";
$miPDO = new PDO($hostPDO, $usuarioDB, $contrasenyaDB);
// Prepara SELECT
$miConsulta = $miPDO->prepare('SELECT * FROM libros;');
// Ejecuta consulta
$miConsulta->execute();

?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Leer - CRUD PHP</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        table td {
            border: 1px solid orange;
            text-align: center;
            padding: 1.3rem;
        }
        .button {
            border-radius: .5rem;
            color: white;
            background-color: orange;
            padding: 1rem;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <p><a class="button" href="nuevo.php">Crear</a></p>
    <table>
        <tr>
            <th>Código</th>
            <th>Título</th>
            <th>Autor</th>
            <th>¿Disponible?</th>
            <td></td>
            <td></td>
        </tr>
    <?php foreach ($miConsulta as $clave => $valor): ?> 
        <tr>
           <td><?= $valor['codigo']; ?></td>
           <td><?= $valor['titulo']; ?></td>
           <td><?= $valor['autor']; ?></td>
           <td><?= $valor['disponible'] ? 'Si' : 'No'; ?></td>
           <!-- Se utilizará más adelante para indicar si se quiere modificar o eliminar el registro -->
           <td><a class="button" href="modificar.php?codigo=<?= $valor['codigo'] ?>">Modificar</a></td>
           <td><a class="button" href="borrar.php?codigo=<?= $valor['codigo'] ?>">Borrar</a></td>
        </tr>
    <?php endforeach; ?>
    </table>
</body>
</html>
```
Algunas consideraciones:

* Recuerda que la aplicación es compatible con PHP8.
* Esta aplicación conecta a la base de datos usando la librería PDO, por lo que debes instalar y activar las librerías `pdo` y `pdo_mysql`.
* Al igual que en el curso, debes crear un script que se ejecute al iniciar el contenedor y sea responsable de cargar los datos en la base de datos.
* Fíjate en las variables de entorno que necesita la aplicación para funcionar. Debes crear valores por defecto para esta aplicación en la imagen, aunque posteriormente se puedan modificar en la creación del contenedor.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Contenido del fichero `docker-compose.yaml`.
2. Instrucción para ver los contenedores con Compose.
4. Pantallazos accediendo a la aplicación.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
