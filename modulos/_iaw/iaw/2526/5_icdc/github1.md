---
tittle: "Introducción a GitHub Actions"
---

**GitHub Actions** es una herramienta integrada en **GitHub** que permite **automatizar tareas** dentro de un repositorio. Estas tareas pueden ejecutarse automáticamente cuando ocurre un evento, como subir código o crear una rama.

Se utiliza principalmente para implementar **CI/CD** (*Integración Continua / Despliegue Continuo*), aunque también es muy útil para ejecutar scripts, comprobaciones o tareas de mantenimiento.

### ¿Cuándo se ejecuta una acción?

Un *workflow* puede ejecutarse, por ejemplo, cuando:

* Se hace un `push` al repositorio
* Se abre un `pull request`
* Se ejecuta manualmente
* Se programa en un horario concreto


### Conceptos básicos

* **Workflow**: Proceso automático completo. Se define en un archivo YAML dentro de `.github/workflows/`.
* **Job**: Conjunto de tareas que se ejecutan en una máquina.
* **Step**: Cada acción individual dentro de un job.
* **Runner**: La máquina virtual donde se ejecuta el workflow (Linux, Windows o macOS).

## Ejemplo sencillo de GitHub Actions

El siguiente ejemplo muestra un *workflow* muy básico que se ejecuta cada vez que se hace un `push` al repositorio y muestra un mensaje por pantalla.

```yaml
name: Ejemplo básico

on:
  push:

jobs:
  saludo:
    runs-on: ubuntu-latest
    steps:
      - name: Mostrar mensaje
        run: echo "Hola desde GitHub Actions"
```


## Explicación breve de la sintaxis

* **`name`**: Nombre del workflow (solo informativo).
* **`on`**: Indica el evento que dispara el workflow. En este caso, `push` significa “cada vez que se sube código”.
* **`jobs`**: Define los trabajos que se van a ejecutar.
* **`saludo`**:  Nombre del *job* (lo elegimos nosotros).
* **`runs-on`**: Sistema operativo del *runner*. Aquí se usa una máquina Linux (`ubuntu-latest`).
* **`steps`**: Lista de pasos que se ejecutan en orden.
* **`run`**: Comando que se ejecuta en la terminal del runner.

Este tipo de workflow es la base para automatizaciones más avanzadas, como ejecutar scripts, comprobar configuraciones o lanzar procesos automáticamente al trabajar con repositorios.
