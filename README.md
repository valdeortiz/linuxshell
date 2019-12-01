# Shell para linux 🚀

[![Python versions](https://img.shields.io/badge/Python-%3Ev3.6-blue)](https://python.org/) [![version](https://img.shields.io/badge/Version-v1.0-blue)](https://gitlab.com/valdeortiz/linuxshell)

Una Shell de Unix o también shell, es el término usado en informática para referirse a un intérprete de comandos, el cual consiste en la interfaz de usuario tradicional de los sistemas operativos basados en Unix y similares, como GNU/Linux.
Mediante las instrucciones que aporta el intérprete, el usuario puede comunicarse con el núcleo y por extensión, ejecutar dichas órdenes, así como herramientas que le permiten controlar el funcionamiento de la computadora. 
[mas informacion](https://es.wikipedia.org/wiki/Shell_de_Unix)

*** 
## Descarga de Repositorio :arrow_backward:

Ejecutar:``` git clone https://gitlab.com/valdeortiz/linuxshell.git ```



o decargar en el repositorio. En la seccion de clone, click en "Descargar en zip"



![Descarga](https://i.imgur.com/3JZUE96.png)

***
## Pre-requisitos 📋.
Se necesita tener instalado python 3.6 en adelante, que viene instalado en la mayoria de distribuciones GNU/Linux. Para asegurarse cual version se encuentra instalado en tu maquina. Ejecuta:

     python --version

Seguir las intruciones del enunciado anterior para la Descarga del repositorio.


### Ejecucion 🔩
Desde nuestro interprete de comandos(host, ejemplo bash o zsh). Ingresamos a la carpeta donde se encuentra el repositorio previamente descargado o clonado. Ejecutamos:

    python shell.py

***

## Construido con 🛠️

- [Python version 3.6.X](https://www.python.org/ "Pagina oficial del lenguaje de programacion Python")


## Comandos ⌨️

1. Copiar: Copiar un archivo o directorio de una ruta a otra.
2. Mover: Mueve un archivo o directorio de una ruta a otra.
3. Renombrar: Renonbra un archivo o directorio.
4. Listar: Lista el contenido del directorio actual.
5. Creardir: Crea un directorio.
6. Cdir: Cambiar de directorio.
7. Cpermisos: Cambiar de permisos.
8. Cpropietarios: Cambiar de propietarios.
9. Ccontra: Cambiar contrasena.
10. Nuevousuario: Crear un usuario.
11. Deminios: Levanta o apaga demonios.
12. Ejecutar: Ejecuta cualquier comando de del Interprete de comando Host.


> ***PARA LISTAR LOS COMANDOS. EJECUTAR***

    help

---

## Modo de ejecucion de cada comando.
    copiar <diractual> <dirnuevo>    
    mover <diractual> <dirnuevo>
    renombrar <nom_antes> <nom_actual>
    listar 
    creadir <nombre>
    cdir <dir_pasado> <dir_nuevo>
    cpermisos <archivo> <permisos>
    cpropietarios <archivo> <id-propietarios>
    ccontra
    nuevousuario
    demonios
    ejecutar <comando>

> ***PARA LEER LA DOCUMENTACION EJECUTA***

    help <comando>

---

## Observacion 📢 

> ***El codigo funciona solo para python3.***

> ***Si al ejecutar `python --version`, da como resultado una version 2.X. Reemplaza python por python3(ASEGURAR QUE SEA PYTHON 3.6 O MAS ACTUAL), quedaria asi: `python3 --version` y debe devolver una version de 3.6 o mas actual. Para la ejecucion quedaria asi: `python3 shell.py`***


## Documentacion oficial 📄
[libreria cmd](https://docs.python.org/3/library/cmd.html "Construccion de un interprete de comandos")

[Libreria os](https://docs.python.org/3/library/os.html "Operaciones del s.o.")

[Libreria shutil](https://docs.python.org/3/library/shutil.html "Operaciones con archivos")

[Libreria logging](https://docs.python.org/3/library/logging.html#module-logging "Registros/Log")



***

## Recomendaciones 📦

- Aegurarse que la version de python sea 3.6 en adelante.
- Tener conocimientos basicos en linux.
- Asegurarse de tener todo lo necesario instalado en su dispositivo, recomendamos la lectura de pre-requisitos.

## Autores ✒️

* **Valdemar Ortiz** - [valdeortiz](https://github.com/valdeortiz)
* **Se Joon Oh** -  [Sjoh](https://gitlab.com/SJO)