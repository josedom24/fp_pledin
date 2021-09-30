---
title: "Ejercicio 2: Trabajo con redes en libvirt"
---

Realiza las siguientes tareas con `virsh` conectándote a `qemu:///system`:

1. Crea una máquina virtual conectada a la `red_interna` del ejercicio anterior, utilizando `virt-install`. Está máquina se debe llamar *nodo1_tunombre*. 
2. Crea un clon de la máquina anterior con `virt-clone`, esta máquina se debe llamar *nodo2_tunombre*. Cambia el nombre de la máquina una vez creada (ficheros `/etc/hostname` y `/etc/hosts`) **Nota: Si está máquina no tiene red, comprueba que el nombre de la interfaz coincide con el nombre definido en `/etc/network/interfaces`, si no coincide, cambia el fichero.**
3. Crea una red aislada (very isolated) que nos permita unir el nodo1 y el nodo2, pero que no esté conectada al host. Añade una interfaz a cada máquina (en caliente) y configúralas de forma estática usando el direccionamiento 192.168.10.0/24. Desconecta la segunda máquina de la red `red_interna`.
4. Añade un bridge externo a tu máquina (llámalo `br0`). Conecta a este bridge tu máquina física.
5. Crea una red pública que utilice `br0` y añade una interfaz a la primera máquina que se conecta al bridge `br0`.

{% capture notice-text %}
## Entrega...

1. Cuando termines el punto 2, un pantallazo donde se vea un ping a la segunda máquina desde la primera.
2. Cuando termines el punto 3, un pantallazo donde se vea un ping a la segunda máquina desde la primera.
3. Cuando termines el punto 3, pantallazo con la ejecución de `ip a` en la segunda máquina.
4. Cuando termines pantallazo con la ejecución de `ip a` en la primera máquina.
{% endcapture %}<div class="notice--info">{{ notice-text | markdownify }}</div>
