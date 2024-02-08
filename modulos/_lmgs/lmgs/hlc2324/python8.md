---
permalink: /python/python8.html
layout: single3
---

# Boletín de ejercicios


{% capture notice-text %}

## ¿Qué tienes que entregar?

Entrega un documento pdf, con el código de los programas y capturas de pantalla de que están funcionando. Del ejercicio 1 entrega capturas de pantalla de las operaciones y sus resultados.

### Ejercicio 1

Escribe el siguiente programa, arreglando los errores que tiene para que se pueda ejecutar:

```python
 Este programa verifica si un número es par o impar y luego muestra los primeros cinco números primos.

# Solicitar al usuario que ingrese un número
numero = intinput("Ingrese un número: "

# Determinar si el número es par o impar
if numero % 2 = 0
    print(numero "es un número par.")
else
    print(numero, "es un número impar.")

# Encontrar los primeros cinco números primos
primos = []
for i in range(2, 20)
    es_primo = True
    for j in range(2, i):
        if i % j = 0:
            es_primo = False
            break
    if es_primo=True
        primos.append(i)

# Mostrar los primeros cinco números primos
print("Los primeros cinco números primos son:" primos[:5])
```

### Ejercicio 2

Escribe un programa que vaya pidiendo números. Nos ira informando si el número es par o impar. el programa termina al introducir un 0.

![ ](../lmgs/hlc2324/img/img4_p7.png)

### Ejercicio 3

Realizar un programa que vaya pidiendo números, hasta que se introduzca el 0 (dicho de otra manera mientras el número introducido sea distinto de 0 sigo pidiendo números). Al finalizar me dirá cuántos números he introducido y la suma de todos. Nota: Si el primer número que meto es 0, me dirá que he metido 0 números.

![ ](../lmgs/hlc2324/img/img5_p7.png)

![ ](../lmgs/hlc2324/img/img6_p7.png)

### Ejercicio 4

Realiza un programa que pida cadena de caracteres hasta que se introduzca la cadena "*". Por cada cadena introducida me saldrá la longitud. Al finalizar me mostrará la cantidad de cadenas con más de 5 caracteres, la cantidad de cadenas con menos o igual de 5 caracteres.

![ ](../lmgs/hlc2324/img/img7_p7.png)

### Ejercicio 5

Hacer un programa de login. El programa pedirá un nombre de usuario y una contraseña. Si el usuario es **pepe** y la contraseña **asdasd** el programa terminará dando un mensaje de bienvenida. Mientras no aciertes el usuario o la contraseña, el programa dará un error y volverá a pedir el usuario y la contraseña. Al finalizar el programa el programa nos dirá el número de intentos que has realizado.

![ ](../lmgs/hlc2324/img/img8_p7.png)

### Ejercicio 6

Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades sean positivas.

![ ](../lmgs/hlc2324/img/img9_p7.png)

![ ](../lmgs/hlc2324/img/img10_p7.png)

![ ](../lmgs/hlc2324/img/img11_p7.png)


### Ejercicio 7

Realiza un programa que vaya pidiendo las notas de los alumnos de una asignatura, cada vez que introducimos una nota nos pregunta "¿Quieres introducir otra nota (S/N)?". Si podemos "S" nos pedirá otra nota. Cuando pongamos "N" nos dirá el número de alumnos de la clase y la nota media obtenida.

![ ](../lmgs/hlc2324/img/img12_p7.png)

### Ejercicio 8

Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
Recuerda que 2 elevado a 3 es 2 * 2 * 2.

### Ejercicio 9

Realizar un programa que genere un número aleatorio del 1 al 100. El objetivo es acertar ese número, por lo tanto me irá pidiendo números hasta que lo acierte. Al final me dirá en cuantos intentos lo he acertado.

![ ](../lmgs/hlc2324/img/img13_p7.png)

### Ejercicio 10

Vamos a mejorar el ejercicio anterior, para que cuando introduzca un número me diga si el que el ha generado es mayor o menor, de esta forma me ayudará a acertar el número más fácilmente.

![ ](../lmgs/hlc2324/img/img14_p7.png)

El método `count` de las cadenas de caracteres en python devuelve el número de ves que aparece una cadena dentro de otra.

Por ejemplo, si queremos saber cuantas "a" tiene la palabra "Abracadabra", podríamos ejecutar:

```python
cadena = "Abracadabra"
cantidad = cadena.count("a")
print(cantidad)
```

Escribe un programa en Python que solicite al usuario que ingrese cadenas de caracteres una tras otra. El programa continuará pidiendo cadenas hasta que el usuario introduzca un asterisco *. Por cada cadena, el programa mostrará la cadena y el número de caracteres que tiene. Al final el programa mostrará.
    * La cantidad de cadenas que has introducido.
    * La cantidad de espacios que has introducido.
    * La cantidad de palabras que tienen una "a".

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>

