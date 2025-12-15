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