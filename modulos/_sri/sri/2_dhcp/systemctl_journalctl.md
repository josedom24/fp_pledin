---
title: "Gestión del ciclo de vida y monitorización de servicios"
---

## systemctl

En este manual, veremos cómo gestionar los servicios en sistemas basados en Linux utilizando `systemctl`, una herramienta que forma parte de systemd. Esta herramienta es fundamental para administrar servicios, controlar el estado de los mismos, y gestionar su ciclo de vida.

### ¿Qué es systemd y systemctl?

systemd es un sistema de inicialización y un gestor de servicios que gestiona los procesos y recursos del sistema. `systemctl` es la utilidad principal que se utiliza para interactuar con systemd.

### Comandos Básicos de systemctl

Estos son algunos de los comandos más usados para administrar los servicios:

1. Iniciar un Servicio
    
    Para iniciar un servicio de manera manual, utiliza el siguiente comando:
    ``````bash
    sudo systemctl start <nombre_servicio>
    ```
2. Detener un Servicio
    Si quieres detener un servicio que está corriendo, utiliza:

    ``````bash
    sudo systemctl stop <nombre_servicio>
    ```

3. Reiniciar un Servicio
    Reiniciar un servicio es útil cuando quieres que se apliquen cambios de configuración.

    ``````bash
    sudo systemctl restart <nombre_servicio>
    ```
4. Recargar la Configuración de un Servicio
    Para recargar la configuración de un servicio sin interrumpir su funcionamiento:

    ``````bash
    sudo systemctl reload <nombre_servicio>
    ```

5. Habilitar un Servicio
    Para que un servicio se inicie automáticamente al arrancar el sistema, puedes habilitarlo con:

    ``````bash
    sudo systemctl enable <nombre_servicio>
    ```

6. Deshabilitar un Servicio
    Si no quieres que el servicio se inicie automáticamente en el arranque:

    ``````bash
    sudo systemctl disable <nombre_servicio>
    ```

7. Comprobar el Estado de un Servicio
    Para verificar si un servicio está activo, detenido, o fallando, utiliza:

    ``````bash
    sudo systemctl status <nombre_servicio>
    ```

### Ciclo de Vida de un Servicio

El ciclo de vida de un servicio bajo systemd se puede dividir en varios estados clave:

* **Inactivo (Dead)**: El servicio está completamente detenido.
* **Activo (Active)**: El servicio está funcionando correctamente.
* **Activado (Enabled)**: El servicio está configurado para iniciarse automáticamente al arrancar el sistema.
* **Deshabilitado (Disabled)**: El servicio no se iniciará automáticamente.
* **Fallando (Failed)**: El servicio intentó iniciarse pero no lo consiguió. Puedes usar systemctl status para obtener más detalles.

## journalctl

Ahora explicaremos cómo utilizar `journalctl`, la herramienta de systemd para visualizar y gestionar los logs del sistema. Veremos cómo se relaciona con syslog, la ubicación de los archivos de logs y cómo algunos servicios pueden tener sus propios registros.

### ¿Qué es journalctl?

`journalctl` es una utilidad incluida en systemd que permite consultar los logs centralizados del sistema. A diferencia de los sistemas tradicionales de logs, que utilizan archivos de texto como `/var/log/syslog`, `journalctl` almacena los logs en un formato binario, lo que permite búsquedas más rápidas y avanzadas opciones de filtrado.

### Relación con syslog y /var/log/syslog

Antes de systemd, la mayoría de los sistemas usaban `syslog` o variantes como `rsyslog` para la gestión de logs. Los mensajes del sistema se escribían en archivos de texto plano ubicados en `/var/log`, siendo `/var/log/syslog` uno de los más importantes.

* `/var/log/syslog`: Este archivo sigue existiendo en muchos sistemas actuales, especialmente si se ejecuta un servicio de syslog como `rsyslog` junto a systemd. En este caso, `rsyslog` captura mensajes del sistema, incluyendo mensajes que también están registrados por `journalctl`.
* `journalctl vs syslog`: `journalctl` centraliza la gestión de los logs de todos los servicios controlados por systemd. Sin embargo, en algunos casos, los servicios específicos pueden continuar escribiendo en sus propios archivos de logs en /var/log, y algunos administradores optan por mantener ambos sistemas en paralelo.

### Logs Específicos de Servicios

Algunos servicios tienen archivos de logs propios que no están gestionados por systemd. Por ejemplo, el servidor web Apache escribe sus logs en `/var/log/apache2/` (o similar), mientras que systemd solo gestiona los logs relacionados con el estado del servicio. Esto significa que si bien `journalctl` proporciona una visión global de todos los eventos del sistema, no siempre captura los detalles específicos de aplicaciones que mantienen sus propios archivos de logs.

### Opciones Más Usadas de journalctl

Aquí están las opciones más comunes que puedes utilizar para gestionar y visualizar los logs con `journalctl`:

1. Ver todos los logs del sistema
    Muestra todos los logs del sistema de manera cronológica:

    ``````bash
    sudo journalctl
    ```

2. Filtrar por servicio
    Para ver los logs de un servicio específico, por ejemplo, nginx:

    ``````bash
    sudo journalctl -u nginx
    ```

3. Mostrar solo los logs recientes
    Puedes limitar la salida a los logs recientes con la opción -b, que muestra solo los mensajes desde el último arranque:
    ``````bash
    sudo journalctl -b
    ```

4. Ver logs en tiempo real
    Al igual que `tail -f`, puedes seguir los logs en tiempo real:

    ``````bash
    sudo journalctl -f
    ```

5. Filtrar por fecha y hora
    Puedes buscar logs dentro de un rango de tiempo específico. Por ejemplo, para ver los logs desde una fecha específica:
    ``````bash
    sudo journalctl --since "2024-10-07 10:00:00"
    ```
    También puedes especificar un rango hasta una fecha y hora concreta:
    ``````bash
    sudo journalctl --since "2024-10-07 10:00:00" --until "2024-10-07 12:00:00"
    ```

6. Filtrar por prioridad
    journalctl permite filtrar los logs por su nivel de prioridad. Las prioridades están numeradas del 0 (emergencia) al 7 (depuración). Para mostrar solo los mensajes de error, puedes usar. Sepuede poner un rango de prioridades con `-p err1..err2`:

    ``````bash
    sudo journalctl -p err
    ```

7. Mostrar mensajes del kernel
    Para ver solo los mensajes del kernel (`dmesg`):
    ``````bash
    sudo journalctl -k
    ```

8. Borrar los logs de journalctl
    En ocasiones, es necesario liberar espacio eliminando logs antiguos.  Para saber cuanto espacio ocupan tus logs:

    ``````bash
    sudo journalctl --disk-usage
    ```

    Puedes eliminar todos los logs o especificar un tamaño máximo permitido:
    ``````bash
    sudo journalctl --vacuum-size=500M
    ```
    
    Esto eliminará los logs más antiguos hasta que los archivos ocupen menos de 500 MB.
    También podemos decir que queremos borrar todos los logs más antiguos de una fecha. En este caso, se aceptan unidades como «s» para segundo, «m» para minutos, «h» para horas, «w» para semanas o «M» para meses.

    ``````bash
    sudo journalctl --vacuum-time=1M
    ```

    Esto borraría los logs más antiguos de un mes.

### Ejemplo Práctico

Imagina que estás administrando un servidor y necesitas investigar por qué un servicio de nginx falló recientemente. Aquí hay un flujo típico usando `journalctl`:

* Ver los logs recientes del servicio nginx:

    ``````bash
    sudo journalctl -u nginx --since "1 hour ago"
    ```

* Seguir los logs en tiempo real para ver si el servicio se recupera:

    ``````bash
    sudo journalctl -u nginx -f
    ```

* Consultar solo los mensajes de error:

    ``````bash
    sudo journalctl -u nginx -p 0..4
    ```

* Investigar los mensajes del kernel si sospechas de un problema de hardware:

    ``````bash
    sudo journalctl -k --since "1 hour ago"
    ```