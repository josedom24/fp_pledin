---
title: "Ejercicio 1: Corrector ortográfico de documentos markdown (test)"
---

Imaginemos que estamos escribiendo documentos markdown y lo guardamos en un repositorio de github. Queremos que cada vez que hagamos una modificación (commit - push) queremos probar (test) si tienes alguna falta de ortografía. Ese proceso lo vamos a hacer de forma automática y continua con Github Actions. Cada vez que hagamos un push, Github Actions va a crear una máquina (entorno de pruebas), va a clonar nuestro repositorio y va a realizar la prueba (test) que indiquemos en un fichero yaml en el directorio `.github/workflows`. Cuando termine la prueba nos va mandar un correo informándonos si la prueba ha tenido éxito o no. En nuestro caso vamos a crear el fichero `.github/workflows\ic.yaml` con el contenido:

```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1
    - name: apt
      run: sudo apt-get install aspell-es 
    - name: spell
      run: OUTPUT=`cat doc/*.md | aspell list -d es -p ./.aspell.es.pws`; if [ -n "$OUTPUT" ]; then echo $OUTPUT; exit 1; fi
```

Por lo tanto realiza los siguientes pasos:

* Realiza un fork del repositorio de GitHub: [https://github.com/josedom24/ic-diccionario](https://github.com/josedom24/ic-diccionario).
* Comprueba la prueba que vamos a realizar estudiando el fichero `.github/workflows/ic.yaml`.
* Realiza cambios en los ficheros que están en el directorio `doc` y comprueba en Github Actions como se van ejecutando las pruebas.

