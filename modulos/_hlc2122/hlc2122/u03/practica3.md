---
title: DRBD y OCFS2
---

Configura un escenario con dos máquinas. Cada una tiene que tener dos discos adicionales (tamaño 1Gb para que la sincronización sea rápida).

* Crea dos recursos RDBD: `wwwdata` y `dbdata`. Cada uno utilizaran uno de los discos de cada máquina.
* Configura en modo Single-primary el recurso `wwwdata`. 
    * Una vez creado y sincronizado el recurso, formatéalo con XFS.
    * Monta el recurso en el nodo primario y crea un fichero. ¿Se puede montar en el secundario?
    * Desmonta el recurso.
    * Cambia los roles, pon primario el que era secundario, y secundario el primario. 
    * Monta el recurso en el que ahora es primario y comprueba que existe el fichero creado anteriormente.
* Configura en modo Dual-primary el recurso `dbdata`.
    * Una vez creado y sincronizado el recurso, configúralo en modo Dual-primary.
    * Crea un cluster OCFS2.
    * Crea un volumen OCFS2 en el recurso (`mkfs.ocfs2`).
    * Monta en los nodos el recurso, y prueba a escribir en los dos al mismo tiempo.
    
