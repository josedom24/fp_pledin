# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.define :proxy do |proxy|
      proxy.vm.box = "debian/bullseye64"
      proxy.vm.hostname = "proxy"
      proxy.vm.synced_folder ".", "/vagrant", disabled: true
      proxy.vm.network :private_network,
          :libvirt__network_name => "red_privada1",
          :libvirt__dhcp_enabled => false,
          :ip => "10.0.0.10",
          :libvirt__forward_mode => "veryisolated"
      proxy.vm.provision "shell", run: "always", inline: <<-SHELL
        apt-get update && apt upgrade -y
        sysctl -w net.ipv4.ip_forward=1
        iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -j MASQUERADE
        echo "10.0.0.6 interno.example1.org interno.example2.org" >> /etc/hosts
      SHELL
    end
    config.vm.define :servidorweb do |servidorweb|
      servidorweb.vm.box = "debian/bullseye64"
      servidorweb.vm.hostname = "servidorweb"
      servidorweb.vm.synced_folder ".", "/vagrant", disabled: true
      servidorweb.vm.network :private_network,
          :libvirt__network_name => "red_privada1",
          :libvirt__dhcp_enabled => false,
          :ip => "10.0.0.6",
          :libvirt__forward_mode => "veryisolated"
      servidorweb.vm.provision "shell", run: "always", inline: <<-SHELL
          ip r del default
          ip r add default via 10.0.0.10
      SHELL
    end
    
  end
  