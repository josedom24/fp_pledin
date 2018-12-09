---
title: "Directivas de seguridad en Windows"
permalink: /seguridadgm/u06/directivas.html
---
En esta práctica vamos a configurar las directivas de seguridad local de Windows. Las directivas de seguridad local de Windows se utiliza para configurar una variedad de requisitos de seguridad para los ordenadores que no forman parte de un dominio de Active Directory. Modificará las
solicitudes de contraseña, permitirá la auditoría, configurará algunos derechos de usuario, y establecerá algunas opciones de seguridad. Luego, utilizará el Administrador de eventos para ver la información registrada.

## Politíca de seguridad

Debemos configurar las directivas de seguridad de Windows para conseguir la siguiente política de seguridad:

* Las contraseñas deben tener al menos 8 caracteres.
* Las contraseñas deben cambiar cada 90 días.
* Un usuario puede modificar la contraseña una vez al día.
* Un usuario debe utilizar una contraseña única al menos en 8 cambios de contraseña.
* Una contraseña debe constar de tres de los siguientes cuatro elementos:
    * Al menos un carácter alfabético en minúsculas.
    * Al menos un carácter numérico.
    * Al menos un carácter alfabético en mayúsculas.
    * Al menos un carácter de símbolo.
* Los usuarios son bloqueados después de 5 intentos fallando la contraseña. Un usuario debe esperar 5 minutos para que el contador se restablezca.
* Cada configuración de seguridad para la Directiva de Auditoría debe estar habilitada.
* Después de 30 minutos de inactividad, la cuenta del usuario se cerrará automáticamente.
* En iniciar sesión, a los usuarios se les presentarán los siguientes títulos y textos:
    * Título: Precaución
    * Texto: Se controla su actividad. Este ordenador es solamente para uso comercial.
* Los usuarios recibirán un recordatorio para cambiar la contraseña 7 días antes de que expire.

## Acceder a la directivas de seguridad local en Windows

* **Inicio > Herramientas administrativas > Directiva de seguridad local**
* **Buscar > secpol.msc**

En esta práctica nos vamos a centrar en las **Directivas de cuenta** y las **Directivas locales**.

## Ejercicio

1. Explique con capturas de pantalla la configuración de las directivas de seguridad para ir consiguiendo cada uno de los puntos expuestos en la política de seguridad que hemos presentado.
2. Demuestre con pruebas de funcionamiento que se han cumplido cada uno de los puntos de la política de seguridad.
3. Indique al menos tres directivas que no hayamos tocado, pero crea que puede ser interesante para la seguridad del sistema.
