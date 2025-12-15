---
title: "Instalación de Jenkins"
---

Tenemos muchos métodos para realizar la instalación de Jenkins: [Installing Jenkins](https://www.jenkins.io/doc/book/installing/).

Vamos a hacer la instalación con apt, para ello ejecutamos los siguientes comandos:

```
apt update
apt install fontconfig-config libfontconfig1 openjdk-21-jre-headless
wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
apt-get update
apt-get install jenkins
```

Accedemos a jenkins, nos pide la clave de administración y la obtenemos ejecutando:

```
cat /var/lib/jenkins/secrets/initialAdminPassword
```

Para terminar instalamos los plugins que nos recomiendan y creamos un usuario administrador.

Una vez que accedamos al programa, vamos a instalar el plugin **Pipeline: Stage View**, que nos va a permitir ver visualmente la ejecución del Pipeline.

Además entraremos en **Administrar Jenkins** -> **Nodes** -> Y comprobar que el nodo **principal** esté activo. Si le falta memoria swap o espacio del directorio temporal podría no estar activo y tendremos que configurar la máquina de la siguiente manera:

* Las instancias de OpenStack no suelen tener swap configuradas, para crear memoria swap ejecutamos como `root`:

    ```
    fallocate -l 2G /swapfile
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    ```

* A continuación configuramos el nodo para que no compruebe el espacio temporal, para ello **Configuración del nodo** -> **Disk Space Monitoring Thresholds** -> **Free Temp Space Threshold** = 0

* Finalmente reiniciamos Jenkins: `systemctl restart jenkins`