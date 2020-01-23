# Shell para linux 🚀

[![Python versions](https://img.shields.io/badge/Python-%3Ev3.6-blue)](https://python.org/) [![version](https://img.shields.io/badge/Version-v1.0-blue)](https://gitlab.com/valdeortiz/linuxshell)

Una Shell de Unix o también shell, es el término usado en informática para referirse a un intérprete de comandos, el cual consiste en la interfaz de usuario tradicional de los sistemas operativos basados en Unix y similares, como GNU/Linux.
Mediante las instrucciones que aporta el intérprete, el usuario puede comunicarse con el núcleo y por extensión, ejecutar dichas órdenes, así como herramientas que le permiten controlar el funcionamiento de la computadora. 
[mas informacion](https://es.wikipedia.org/wiki/Shell_de_Unix)

*** 
## Descarga de Repositorio :arrow_backward:

Ejecutar: ``` git clone https://gitlab.com/valdeortiz/linuxshell.git ```



o decargar en el repositorio. En la seccion de clone, click en "Descargar en zip"



![Descarga](https://i.imgur.com/3JZUE96.png)

***

## Pre-requisitos 📋.

- Se necesita tener instalado python 3.6 en adelante, que viene instalado en la mayoria de distribuciones GNU/Linux. Para asegurarse cual version se encuentra instalado en tu maquina. Ejecuta: ``` python --version```

- Para instalar las dependencias del proyecto ejecutar: ```pip install requirements.txt``` OBS: Debe tener instalado pip.

- Seguir las intruciones del enunciado anterior para la Descarga del repositorio.


### Ejecucion 🔩
Desde nuestro interprete de comandos(host, ejemplo bash o zsh). Ingresamos a la carpeta donde se encuentra el repositorio previamente descargado o clonado. Ejecutamos:

    python shell.py

***

## Construido con 🛠️

- [Python version 3.6.X](https://www.python.org/ "Pagina oficial del lenguaje de programacion Python")


## Comandos ⌨️

1. Copiar archivos/directorio.

<details>

**Descripcion:**
Copia un archivo o directorio de un lugar a otro 

**Argumentos:**
- Archivo1: El archivo a ser copiado.
- ruta Destino: Ruta destino.

Examples:

```copia archivo1 destino```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

2. Mover

<details>

**Descripcion:**
Mueve un archivo o directorio de una ruta a otra. 

**Argumentos:**
- Archivo1: El archivo a ser movido.
- ruta Destino: Ruta destino.

Examples:

```mover archivo1 destino```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

3. Renombrar

<details>

**Descripcion:**
Renombrar un archivo o directorio.

**Argumentos:**
- Archivo1: El archivo a ser renombrado.
- nombre a colocar: Nmobre deseado.

Examples:

```renombrar archivoActual nombreNuevo```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

4. Listar

<details>

**Descripcion:**
Lista el contenido del directorio actual. OBS: tambien imprime los archivos ocultos.

**Argumentos:**
- sin argumentos lista el directorio altual.
- con el argumento [ruta] : lista el directorio colocado en [ruta]

Examples:

```listar ruta```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

5. Creardir

<details>

**Descripcion:**
Crea un directorio nuevo en el directorio actual.

**Argumentos:**
- nombre : nombre del directorio a ser creado.

Examples:

```creadir nombre```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

6. Cambiar de directorio.
<details>

**Descripcion:**
Cambiar de directorio.

**Argumentos:**
- ruta Destino: Ruta a ser dirigido.

Examples:

``` ir destino```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

7. Cambiar permisos.

<details>

**Descripcion:**
Cambiar de permisos de un archivo.

**Argumentos:**
- Archivo: El archivo a ser cambiado.
- permisos: Los permisos deseados.

Examples:

```cambiarpermisos archivo permisos```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

8. Cambiar propietarios.

<details>

**Descripcion:**
 Cambiar de propietarios de un archivo.

**Argumentos:**
- Archivo1: El archivo a ser copiado.
- id propietario deseado:id del propietario nuevo.
- id del grupo: id del grupo a ser asignado.

Examples:

```cambiarpropietario propietarios archivo1 Idpropietario idGrupo```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

9. Cambiar contrasenha:

<details>

**Descripcion:**
 Cambiar contrasena de un usuario.

**Argumentos:**
- usuario: usuario a ser cambiado su contrasenha

Examples:

```cambiarcontra archivo1 destino```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

10. Nuevo usuario.

<details>

**Descripcion:**
Crear un usuario en el archivo usuarios_log que esta en /var/log/usuarios_log

**Argumentos:**
- nombre: Nombre del usuario a ser ingresado al usuarios_log.
- Horario de entrada: su horario de entrada.
- horario de salida: su horario maximo.
- ip: su lista de posibles conexiones. 

Examples:

```usuario mombre horario_entrada horario_salida ips```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

11. servicios.

<details>

**Descripcion:**
Levanta o apaga demonios.

**Argumentos:**
- demonio: nombre del demonio.
- accion: accion a ejecutar

Examples:

```servicio demonio accion```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

12. Ejecutar comando fuera de la shell.

<details>

**Descripcion:**
Ejecuta cualquier comando de del Interprete de comando Host.

**Argumentos:**
- comando: comando a ser ejecutado.

Examples:

```ejecutar comando```

**Retorno:**
En caso de realizar con exito la copia se imprime un mensaje de exito.
En caso de producirse un error se imprime un mensaje del error producido.

</details>

> ***PARA LISTAR LOS COMANDOS. EJECUTAR***

    help

---


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

[Libreria getpass](https://docs.python.org/3/library/getpass.html "manejo de contrasenhas")

[Libreria datetime](https://docs.python.org/3/library/datetime.html "manejo de fecha/hora")

[Libreria socket](https://docs.python.org/3/library/socket.html "interfaz de red")

[Libreria ftplib](https://docs.python.org/3/library/ftplib.html "protocolo ftp")

### Fuera de la biblioteca standar.

> ***Ejecutar: ```pip install requirements.txt``` para instalar todas las dependencias.***


[Libreria Psutil](https://psutil.readthedocs.io/en/latest/ "procesos/demonios")

***

## Recomendaciones 📦

- Aegurarse que la version de python sea 3.6 en adelante.
- Tener conocimientos basicos en linux.
- Asegurarse de tener todo lo necesario instalado en su dispositivo, recomendamos la lectura de pre-requisitos.

## Autores ✒️

* **Valdemar Ortiz** - [valdeortiz](https://github.com/valdeortiz)
* **Se Joon Oh** -  [Sjoh](https://gitlab.com/SJO)