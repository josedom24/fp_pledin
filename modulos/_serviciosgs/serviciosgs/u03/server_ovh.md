# Configuración inicial del servidor OVH

1. Comprueba en el panel de control de OVH que tienes los 4 recursos a tu disposición: VPS, DNS, zona DNS y buzón DNS. Si no es así ponte en contacto con José Domingo para solucionar el problema.

2. Ponte en contacto con José Domingo para pedirle la contraseña para acceder a la máquina.

3. Accede a la máquina (usuario debian) y configura tu ip pública (y la de los profesores que encontrarás en la wiki de redmine). Desde ese momento accederemos siempre con nuestra clave privada.

4. Nombra la máquina de forma correcta. Tu máquina tendrá un nombre de host totalmente cualificado (`nombre.iesgnXX.es`). Modifica los ficheros correspondientes para que al ejecutar `hostname -f` obtenga el FQHN.

5. Desde el panel de control de OVH crea un registro de tipo A en la zona DNS de tu dominio, para asignar el nombre elegido a tu dirección IP publica. Desde este momento el acceso a la máquina por ssh será utilizando ese nombre.

6. Responde este mensaje y pon el nombre elegido. Los profesores probaremos a acceder a la máquina.