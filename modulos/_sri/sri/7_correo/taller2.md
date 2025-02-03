---
title: "Taller 2: Servidores satélites, alias y redirecciones"
---

Este taller lo puedes hacer cuando tengas el taller 1 terminado y puedas enviar correo desde tu servidor de correos.

En la mayoría de las ocasiones cuando trabajamos con servidores, es necesario que estos servidores nos manden correos de notificación. Además nuestras aplicaciones web también pueden enviar correos. En este taller vamos a configurar determinados servicios y aplicaciones web para que nos envíen correo en nuestro escenario de OpenStack.

## Simulación de cortafuegos

En las infraestructuras locales, normalmente sólo se permite enviar correos desde el servidor de correos "oficial". Para simular este comportamiento añade al cortafuegos de `luffy` estas reglas:

```
# Permitir SMTP solo desde 192.168.0.3 (tráfico que pasa por el router)
iptables -A FORWARD -p tcp --dport 25 -s 192.168.0.3 -j ACCEPT
# Bloquear SMTP para todas las demás máquinas
iptables -A FORWARD -p tcp --dport 25 -j DROP

# Bloquear intentos de conexión al puerto 25 desde el propio router
iptables -A OUTPUT -p tcp --dport 25 -j DROP
```

Esto evita que cualquier máquina a excepción de nuestro servidor de correos pueda mandar correos.

## Instalación de un servidor SMTP en nuestro servidores

Muchos de los servicios que podemos instalar en un servidor manda correos a usuarios del servidor, normalmente al `root`. Para que esto ocurra necesitamos instalar un servidor SMTP en nuestro servidor. En nuestro caso vamos a instalar `postfix`. en la instalación de `postfix` tendrás que tener en cuenta los siguientes aspectos:

* Este servidor de correo va a utilizar como relay a nuestro servidor de correo "oficial" `sanji.tudominio.gonzalonazareno.org` que es el único servidor que puede mandar correos.
* Este servidor no va a recibir correos desde el exterior.
* Durante la instalación puedes escoger estas opciones:
    * **Internet with smarthost**: Este servidor no envía directamente correo, siempre utiliza un relay. Este servidor puede recibir correo.
    * **Satellite system**: Igual que el anterior, pero no puede recibir correo del exterior.
* Cuando se indica el nombre del sistema de correo en este tipo de servidor se suele poner **el nombre del equipo**. Por un lado porque así diferenciamos correos que vienen de otro servidor SMTP, y además como normalmente no recibe correos no es necesario hacer ninguna configuración adicional para que los correos lleguen a este servidor.
* Durante la configuración os preguntará el servidor relay, para rellenar el parámetro `relay_host`, en nuestro caso, `sanji.tudominio.gonzalonazareno.org`.
* Para que podamos usar nuestro servidor de correo `samji` desde otros servidores tenemos que darle permiso. Para ello añade en el parámetro `mynetworks` las redes desde las que podemos mandar correos.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. La configuración del cortafuegos en `luffy` donde se vea que sólo puede mandar correos nuestro servidor de correos "oficial".
2. Desde otra máquina, por ejemplo `luffy`, con la utilidad `mail` manda un correo al exterior.
3. Muestra las cabeceras del correo recibido mostrando las cabeceras donde vemos los servidores por los que ha pasado el correo para comprobar que ha pasado por `sanji`. ¿Por cuántos servidores ha pasado?
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>	

## Envío de correos de notificación

En el servidor de correos con el que estamos trabajando y has instalado el nuevo servidor de correos vamos a instalar un servicio que comprueba las actualizaciones y nos manda un correo avisando de los paquetes que tenemos que actualizar. Este servicio se llama `apticron`. Veamos algunas cosas:

* Instala el servicio `apticron`.
* Este programa por defecto manda correos al usuario `root`.
* Este correo crea una tarea cron definida en `/etc/cron.d/apticron`. Todos los días a una determinada hora te manda un correo con las actualizaciones de paquetes que tienes que hacer.
* Si no quieres esperar a que se ejecuta la tarea del cron, puedes ejecutar el servicio manualmente `sudo apticron`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Ejecuta el servicio manualmente y comprueba que el usuario `root`ha recibido el correo.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>	

## Redirecciones

Hasta ahora todo funciona muy bien, sin embargo el administrador del servidor debe entrar en el servidor y comprobar manualmente si tiene correo el usuario `root`. Estaría muy bien que ese correo lo recibieramos en una dirección de correo externa. Para ello vamos a usar las **redirecciones**.

Una **redirección** se utiliza para enviar el correo que llegue a un usuario a una cuenta de correo exterior. Para usuarios reales las redirecciones se definen en el fichero `~/.forward` y el formato de este fichero es simplemente un listado de cuentas de correo a las que se quiere redirigir el correo.

Crea un fichero `.forward` en el home del usuario `root` con tu dirección de correo electrónico y comprueba que ahora los correos que recibe el usuario `root` te llegan a tu correo.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Ejecuta de nuevo el servicio `apticron` y comprueba que has recibido el correo en la dirección que has indicado.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>	

## Alias

Imaginemos ahora que hay dos administradores del servidor distintos, que usan usuarios sin privilegios para acceder al servidor. Es lo normal, es decir, no se suele usar el usuario `root`para acceder al servidor. Aunque estos usuarios pueden loguearse como `root` estaría muy bien que los correos que recibe el `root`se envíen a los usuarios de los dos administradores.

Para ello vamos a usar un **alias**. Cuando se define un alias para un determinado usuario se redirige el correo que llegue a otro usuario de la misma máquina. Los alias de correo se utilizan principalmente para gestionar el correo de las "cuentas de administración" y se definen en el fichero `/etc/aliases`. Realiza los siguientes pasos:

1. Elimina el fichero `.forward` que creaste en el ejercicio anterior.
2. Crea dos usuarios sin privilegios para simular los dos administradores.
3. Crea un nuevo alias en el fichero `/etc/aliases`, de la siguiente forma: `root: usuario1,usuario2`.
4. Cada vez que se modifica el fichero `/etc/aliases` hay que ejecutar la instrucción `newaliases` para que los cambios tengan efecto.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Ejecuta de nuevo el servicio `apticron` y comprueba que el correo lo reciben los dos nuevos usuarios.
2. Crea un fichero `.forward` en el home de alguno de ellos y comprueba la redirección.

{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>	

## Envío de corros desde una aplicación

Los CMS que instalamos normalmente envían correos. Por ejemplo nuestro WordPress puede enviar correos, por ejemplo si has olvidado la contraseña. Para que nuestro WordPress envíe correos podemos hacer dos cosas:

1. Instala un servidor postfix **Satellite system** en `zoro`, como hemos hecho anteriormente, y configurar WordPress para que use como servidor de correos `localhost`.
2. Configurar WordPress para que use como correo `sanji.tudominio.gonzalonazareno.org`.

{% capture notice-text %}
## ¿Qué tienes que entregar?

1. Investiga como configurar el servidor de correos SMTP en WordPress, elige una de las dos opciones para enviar correos.
2. Entrega una captura de pantalla donde se demuestre que has recibido un correo electrónico desde tu WordPress.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>	

