---
title: Introducción a HAProxy
---

Un **Balanceador de carga** es un dispositivo de hardware o software que se pone al frente de un conjunto de servidores que atienden una aplicación y, tal como su nombre lo indica, asigna o balancea las solicitudes que llegan de los clientes a los servidores usando algún algoritmo.

Al acceder a un nombre de dominio, se accede al balanceador de carga, que decidirá a que servidor backend manda la petición: round robin, menos conexiones, menor tiempo de respuesta, . . .

Ejemplos: apache2, nginx, haproxy, . . .

## Introducción a haproxy

