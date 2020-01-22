#!/usr/python
'''#!/usr/bin/python3 #para Lfs'''


from cmd import Cmd
import os
import shutil 
#import pwd
import logging
import getpass 
import ftplib
from datetime import datetime
import socket
import psutil
from multiprocessing import Process
import subprocess

# global archivo = "/var/log"
global archivo_usuario 
archivo_usuario = "usuarios_log" # /var/log/usuarios_log
global archivo_personalHorarios 
archivo_personalHorarios = "personal_horarios_log" # /var/log/personal_horarios_log

class Comandos(Cmd):
    """lista de comandos 
        copiar -> x ..usamos makefile de shutil podemos hacer con tar, comprimimos despues movemos a donde queremos copiar y lo descomprimimos.
        - Levantar o apagar demonios(Sin llamar a la funcion service).
        -Registrar el inicio de sesión y la salida sesión del usuario. Se puede comparar con los registrosde su horario cada vez que inicia/cierra la sesión y si esta fuera del rango escribir en el archivo de log (personal_horarios_log)un mensaje que aclare que esta fuera del rango y deben agregar el lugar desde donde realizo la conexión que también puede estar fuera de sus IPshabilitado.
        -Ejecutar una transferencia por ftp o scp, se debe registrar en el log Shell_transferencias del usuario.
    """
    intro = "***  Shell  *** \n=> introduzca <help> para visualizar los comandos." #Interprete de comandos FiOS.
    prompt = "Introduza un comando: "
    misc_header="Documentacion de los metodos"
    doc_header = "Ayuda de comandos documentados. Presione help <comando>"
    undoc_header="Los siguientes comandos no estan documentados:"
    ruler = "*" # caracter separador al ejecutar help=menu de ayuda
        
    logging.basicConfig( level=logging.INFO,
                        # formato del horario (YYYY-MM-DD hh:min:sec), 
                        format='%(asctime)s %(name)s %(levelname)s %(message)s', # name es el user, asctime es hora y fecha, levelname: severidad, message: mensaje del error.
                        filename="Shell_FiOs.log")

    log_error = logging.getLogger("")
    fhp = logging.FileHandler("errores_sistema.log")
    fhp.setLevel(logging.ERROR)
    log_error.addHandler(fhp)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhp.setFormatter(formatter)
    log_error.addHandler(fhp)

    def do_diractual(self, args):
        """Muestra en pantalla el directorio actual.
        -> No posee parametros.
        Manera de ejecucion: diractual
        """
        self.log(f"diractual {args} ")
        print("Directorio actual:", os.getcwd())

    def do_renombrar(self, args):
        """Renombrar un archivo o directorio
        Recibe dos parametros-> <nombre_actual> <nombre_cambiado>
        Manera de ejecutar: renombrar <nombre_actual> <nombre_a_cambiar>
        """
        args = args.split(" ")

        if self.confirmarLongitud(len(args), 2, "renombrar"):
            try:
                self.log(f"renombrar {args} ")
                os.rename(args[0],args[1])
                print("<",args[0],">", "fue renombrado a ","<",args[1],">")
            except OSError:
                print("Error -> nombres y rutas de archivos no válidos o inaccesibles.")
                self.log_error.error("nombres y rutas de archivos no válidos o inaccesibles. Al ejecutar <renombrar>")
            except Exception as e:
                print(f" Error: {e} -> al ejecutar <renombrar>")
                self.log_error.error(f" codigo del error: {e} -> al ejecutar <renombrar>")
        else:
            pass 
        
    def do_listar(self, arg):
        """ Lista todos los archivos del directorio actual o de una ruta especifica.
        Parametros -> Si se ejecuta sin parametro se lista el directorio actual.
                      si se pasa la ruta como parametro se lista el directorio solicitado.
        Manera de ejecucion: listar el directorio actual: < listar >
                             Listar una ruta especifica: listar <ruta>
        """
        self.log(f"listar {arg} ")
        try:
            if arg == "":
                dir = os.listdir(path=".")
                for dirs in dir:
                    print(dirs, end="  ")
                print("\n")
            else:
                dir = os.listdir(path= arg)
                for dirs in dir:
                    print(dirs, end="  ")
                print("\n")
                print("listado del directorio solicitado")
        except OSError:
                print("Error -> nombres y rutas de archivos no válidos o inaccesibles.")
                self.log_error.error("nombres y rutas de archivos no válidos o inaccesibles. Al ejecutar <listar>")
        except Exception as e:
            print(f"Error {e} -> Ejecute help <listar> para mas informacion")
            self.log_error.error(f" codigo del error: {e} -> Al ejecutar <listar>")

    def do_mover(self, args):
        """
        Mover o renombrar un archivo o directorio. 
        Recibe dos parametros-> <directorio_actual> <directorio_cambiado>
                              o para renombrar un archivo: <nombre_actual> <nombre_cambiado>
        Manera de ejecutar:-> mover <directorio_actual> <directorio_a_cambiar>
                        -> renombrar: mover <nombre_actual> <nombre_a_cambiar>
        """
        self.log(f"mover {args} ")
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 2, "mover"):
            try:
                shutil.move(args[0],args[1])
                print("<",args[0],">", "fue movido a ","<",args[1],">")
            except OSError:
                print("Error -> nombres y rutas de archivos no válidos o inaccesibles.")
                self.log_error.error("nombres y rutas de archivos no válidos o inaccesibles. Al ejecutar <mover>")
            except Exception as e:
                print(f"Error {e}-> Ejecute help <mover> para mas informacion")
                self.log_error.error(f" codigo del error: {e} -> Al ejecutar mover")
        else:
            pass

    #si ponemos car1/car2 .. si car1 existe se crear car2.. pero si no lanza un error
    def do_creardir(self, args):
        """
        Crea un nuevo directorio en la ruta actual. 
        Recibe dos parametros-> <nombre del directorio a crear> 
        Manera de ejecutar:-> creardir <nombre_del_directorio>
        """
        self.log(f"creardir {args} ")
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 1, "creardir"):
            #para crear varias carpeta usar os.makedirs(car1/car2/car3)
            try:
                os.mkdir(args[0])
                print("<",args[0],">", "fue creado")
            except OSError:
                print("Error -> nombres y rutas de archivos no válidos o inaccesibles.")
                self.log_error.error("nombres y rutas de archivos no válidos o inaccesibles. Al ejecutar <creardir>")
            except Exception as e:
                print(f"Error {e} -> Ejecute help <creardir> para mas informacion")
                self.log_error.error(f"Error {e} -> al ejecutar <creardir>")
        else:
            pass        

        #os.geteuid() para saber el userid
        #os.getgid() para saber el grupid
    def do_cambiarpermisos(self, args):
        """
        Cambiar los permisos de un archivo o directorio. 
        Recibe dos parametros-> <ruta> <permisos> 
        Manera de ejecutar:-> cambiarpermisos <ruta> <permisos>
        """
        self.log(f"cambiarpermisos {args} ")
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 2, "cambiarpermisos"):
            try:
                os.chmod(args[0],int(args[1],8)) #EL segundo parametro que recibe chmod debe ser entero y en octal
                print("<",args[0],">", "permisos cambiado")
            except OSError:
                print("Error -> nombres y rutas de archivos no válidos o inaccesibles.")
                self.log_error.error("nombres y rutas de archivos no válidos o inaccesibles. Al ejecutar <permisos>")
            except Exception as e:
                print(f"Error {e}-> Ejecute help <permisos> para mas informacion")
                self.log_error.error(f"codigo del error: {e} -> al ejecutar <permisos> ")
        else:
            pass

    def do_cambiarpropietario(self, args):
        """
        Cambiar  propietario de un archivo o directorio. 
        Recibe dos parametros-> <ruta> <id_propietario> <id_grupo> 
        Manera de ejecutar:-> cambiarpropietario <ruta> <propietario> <grupo>
        """
        self.log(f"cambiarpropietario {args} ")
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 3,"cambiarpropietario"):
            try:
                print("propietario_id del archivo:", os.stat(args[0]).st_uid) 
                print("Grupo_id del archivo:", os.stat(args[0]).st_gid)
                #os.chown(args[0],args[1],args[2]) #EL segundo parametro que recibe chmod debe ser entero y en octal
                print("<",args[0],">", "propietarios cambiados")
                print("propietario_id del archivo:", os.stat(args[0]).st_uid) 
                print("Grupo_id del archivo:", os.stat(args[0]).st_gid)
            except OSError:
                print("Error -> nombres y rutas de archivos no válidos o inaccesibles.")
                self.log_error.error("nombres y rutas de archivos no válidos o inaccesibles. Al ejecutar <cambiarpropietario>")
            except Exception as e:
                print(f"Error {e}-> Ejecute help <propietario> para mas informacion")
                self.log_error.error(f" Codigo de error: {e} -> al ejecutar <propietario>")
        else:
            pass

    def do_ccontra(self, args):
        """ Cambiar la contrasenha de un usuario 
        parametros:
            -> [usuario]
        Modo de Ejecucion:
            -> ccontra [usuario]
        """
        #os.system(f"passwd {args}")
        # contra_nueva = getpass.getpass("Introduce el nuevo password")
        # print(contra_nueva)
        self.log(f"ccontra {args} ")
        os.system("passwd " + args)

    def do_copia(self, args):
        """Copia el contenido de un archivo a otro
        Parametros: [archivo1]  Archivo cuyo contenido sera copiado en otro archivo.
                    [archivo2]  Archivo destinatario del archivo1.
        Ejecucion: copia [archivo 1] [archivo 2]
        """
        self.log(f"copia {args} ")
        args = args.split()
        try:
            fileCat = open(args[0], "r")
            fileTarget = open(args[1],"w")
            fileTarget.write(fileCat.read())
            print(f"Se copio el contenido de {args[0]} al {args[1]}")
            fileTarget.close()
            fileCat.close()
        except:
            print(f"El archivo {args[0]}, no se pudo abrir o no existe")
    
    #sin llamada al sistema cd
    def do_ir(self, args):
        """ Cambiar de Directorio.
            parametros:[directorio a ser movido.]
            Ejecucion: ir [directorio deseado]
         """
        self.log(f"ir {args} ")
        args = args.split()
        try:
            os.chdir(args[0])  # verificar si realiza una llamada al sistema.
            print(os.getcwd()) 
        except:
            print("No se pudo cambiar de directorio o no existe el directorio seleccionado")
            self.log_error.error("Error en cambio de directorio")
            
##################################################################################
    def do_usuario(self, args):
        """Crea un nuevo usuario en el sistema. Los datos se guardan dentro del archivo /var/log/usuarios_log.
        parametros:
            -> [nombre de usuario] [hora de entrada] [hora de salida] [ip de conexion]
        Ejecucion:
            -> usuario <nombre de usuario> <hora de entrada> <hora de salida> <ip de conexion>
        """
        self.log(f"usuario {args} ")
        if len(args.split(" ")) < 4:
            self.confirmarLongitud(0,1,"usuario")
            pass
        else:
            with open(archivo_usuario, "a") as f:
                f.write(args + "\n")
                print("Usuario Registrado en /var/log/usuarios_log")
          
    def do_ftp(self,args):
        """Ftp brinda la posibilad de conectarse a traves del protocolo FTP.
        Parametros: [urlFtp] -> Url del servidor FTP.
        Ejecucion: ftp [urlFtp]
        """
        self.log(f"ftp {args} ")
        ftp = ftplib.FTP(args)
        usuario = input("Introduce el usuario: ")
        contra = getpass.getpass("Introduce la contrasenha: ")
        ftp.login(usuario, contra)
        ftp.quit()

    def do_limpiar(self, args):
        os.system("clear")

    def do_servicio(self,args):
        """
        Comando Servicio se utiliza para poder matar-para-iniciar demonios. 
        Recibe dos parametros-> <nombre del demonio> <accion a ejecutar>
        Manera de ejecutar:-> servicio <nombre del demonio> <accion a ejecutar>
        """
        # llamar al comando jobs y stdOut agregar a una lista. comparar el proceso enviado atravez de arg com la lista y verificar si existe
        # para lanzar un comando en segundo plano se agrega & al final del comando
        # fg %id es para recuperar un servicio en segundo plano (podemos ver el id ejecutando jobs)
        # bg %id es para que una vez estando en segundo plano(crtl + z) pasar de detenido a en marcha
        # kill %id es para matar el procso
        self.log(f"servicio {args} ")
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 2, "servicio"):
            # systemctl list-unit-files --state=enabled para los  deamons activos
            # guardar la salida del comando y verificar si dentro se encuentra el nombre
            procName = args[0]
            procs = []
            processList = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if procName in p.info['name']]
            #los procesos deamon tienen una d al final
            #como saber si es un servicio(deamon) o un proceso

            for x in processList:
                if psutil.Process(x["pid"]).status().upper() == psutil.STATUS_SLEEPING.upper():
                    procs.append(x)
            
            if len(procs) == 0:
                print("No se encontro su demonio")
                return False

            try:
                print(procs)                
                for proc in procs: 
                    if args[1] == "levantar":
                        psutil.Process(proc["pid"]).resume() #reanuda la ejecucion del proceso
                        print("Demonio levantado con exito")
                    elif args[1] == "bajar":
                        #proc.terminate() # la diferencia con kill, este espera al proceso a que termine sus tareas
                        psutil.Process(proc["pid"]).kill()
                        print("Demonio bajado con exito")
                    break
                    # checamos si el nombre se encuentra en la lista y luego ejecutamos la funcion kill(matar)                
            except Exception as e:
                print(f"Error {e} -> Ejecute help <servicio> para mas informacion")
                self.log_error.error(f"Error {e} -> al ejecutar <servicio>")
        else:
            pass  
        
       
######################################################################

    def log(self, args):
        logging.info(f"Se ejecuto el comando -- {args}")

    def confirmarLongitud(self,longArg,longOficial,comando):
        if longArg == longOficial:
            return True
        else:
            print(f"Error-> La cantidad de parametros es incorrecta. Ejecute help <{comando}>") 
            self.log_error.error(f"La cantidad de parametros es incorrecta. Al ejecutar <{comando}>")
            return False

    def emptyline(self):
        """No realiza ninguna accion"""
        print("Ningun comando ejecutado.")
        logging.warning("Ningun comando ejecutado")
        pass

    def do_salir(self, args):
        print("Hasta pronto!")
        return True 

    def do_ejecutar(self, args):
        """ Ejecuta un comando del sistema
        Parametros: [comando del interprete host]
        Ejecucion: ejecutar <comando>
        """
        self.log(f"ejecutar {args} ")
        os.system(args)
        # subprocess.call("comando")
        #llama a los comandos del interprete de comandos-host. 

    def default(self, args):
        """ Se ejecuta en caso de un comando no valido"""
        logging.warning(f"Ejecuto {args}. No existe el comando ")
        print("Atencion. ",args, " No existe el comando -> Presione help para visualizar los comandos posibles")
    

class UsuarioNoEncontradoError(Exception):
    """Clase base para excepciones en el módulo."""
    pass

def ipVerificacion(ipList, ipDeConexion):
    for ip in ipList:
        if ip == ipDeConexion:
            return ipDeConexion
    else:
        return f"Ip no registrado = {ipDeConexion}"

def inicioDeSesion(user, ip):
    """Funcion para verificar la existencia del usuario, si se encuentra en horario laboral y con alguna ip reconocidad
        Parametros: [user] -> Es el nombre de usuario de la maquina que se conecto.
                    [ip] -> ip de la maquina conectada.
        Funcion:- Hacemos uso de dos archivos, el principal usuarios_log que es donde se encuentra los datos de los usuarios registrados
            y personal_horarios_log donde guardamos las conexiones y si fue en horario o no. Ambos son abierto en modo append(agregar).
            - hacemos uso de los metodos proporcionados por datetime para la manipulacion de fechas.
        Excepciones: Tenemos una excepcion en el caso de que no se encuentre registrado el usuario en el archivo usuarios_log
    """
    usuario = user
    ipDeConexion = ip            
    with open(archivo_usuario,"r+") as archivoUsuario: 
        try:
            for linea in archivoUsuario:
                usuario_info = linea.split() 
                if usuario == usuario_info[0]:
                    hora_entrada = datetime.strptime(usuario_info[1], "%H:%M") 
                    hora_salida = datetime.strptime(usuario_info[2], "%H:%M") 
                    ips = usuario_info[3:]
                    strIp = ipVerificacion(ips, ipDeConexion)
                    #abrir con whith
                    archivoPersonalHorario = open(archivo_personalHorarios, "a+")
                    horario_actual = datetime.now() 
                    if hora_entrada.strftime("%H:%M") <= horario_actual.strftime("%H:%M") <= hora_salida.strftime("%H:%M"):
                        horario_actual = horario_actual.strftime("%m/%d/%Y, %H:%M:%S")
                        archivoPersonalHorario.write(f"{ horario_actual } - {usuario} Se conecto dentro de su horario, IP: {strIp} \n")
                        archivoPersonalHorario.close() 
                        return f"{usuario}: Se conecto dentro de su horario, IP: {strIp} \n"
                    else:
                        horario_actual = horario_actual.strftime("%m/%d/%Y, %H:%M:%S")
                        archivoPersonalHorario.write(f"{horario_actual} - {usuario} Se conecto fuera del horario, IP: {strIp} \n")
                        archivoPersonalHorario.close() 
                        return f"{usuario}: Se conecto fuera del horario, IP: {strIp} \n"
                    break
            else:
                raise UsuarioNoEncontradoError()
        except UsuarioNoEncontradoError:
            print("Atencion: No se encontro su usuario en el registro: Ejecute <nuevoUsuario> para registarse o <help nuevoUsuario> para mas ayuda. \n")

def demonios(args):
    jobs = subprocess.check_output("jobs")
    jobs = jobs.split(" ")


if __name__ == '__main__':
    #pwd.getpwnam(name) retorna una lista con los datos del user name
    user = getpass.getuser()
    nombre_equipo = socket.gethostname()
    ipDeConexion = socket.gethostbyname(nombre_equipo)
    
    logger = logging.getLogger('sesion_Log')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('sesion.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    try:
        logger.info(f"{user} - Inicio sesion")
        result = inicioDeSesion(user, ipDeConexion) # 
        print(result)
        Comandos().cmdloop()
    except KeyboardInterrupt:
        print(f"\nCierre de sesion : {user} - Interrupcion de teclado")
        logger.info(f" {user} Cerro sesion por Interrupcion de teclado")
        exit()
    else:
        logger.info(f"Cierre de sesion : {user}")


"""
-copiar(sin llamada al sistema de la funcion cp)
-mover - mover
-renombrar - renombrar
-listar un directorio(sin ls)
-crear un directorio - creardir
***-cambiar de directorio(sin cd)- ir
-cambiar los permisos sobre un archivo o conjunto de archivos - permisos
-cambiar los propietarios sobre un archivo o conjunto de archivos - propietarios
-cambiar la contraseña - contraseña
- proveer la capacidad de poder ejecutar comandos del sistema

-Agregar usuario, y deben de registrar los datos personales del mismo incluyendo su horario de trabajo 
y posibles lugares de conexion(ejemplo ips o localhost)- usuario
    Solo en usuarios_log?
- Registrar el inicio de sesion y la salida sesion del ususario. 
Se puede comparar con los registros de su horario cada vez que inicia/cierra sesion y si esta fuera de su rango escribir en el archivo
de log ""(personal_horarios_log)"" un mensaje que aclare que esta fuera del rango y deben agregar el lugar donde realizo la conexion
que tambien puede estar fuera de sus ips habilitado.

- El usuario puede levantar o bajar demonios dentro del sistema, utilizando un sitema parecido a service(sin llamar a service)- 
-Ejecutar una transferencia ftp o scp, se debe registrar en el "log Shell_transferencias" del usuario

usuarios.log 
<user> <horario_entrada> <horario_salida> <ip>

#########
los errores deben ir en /var/log con nombre errores_sistema.log

"""


"""
class testdaemon(daemon.Daemon):
    def run(self):
        self.i = 0
        with open('test1.txt', 'w') as f:
            f.write(str(self.i))
        while True:
            self.i += 1
            time.sleep(1)

    def quit(self):
        with open('test2.txt', 'w') as f:
            f.write(str(self.i))

daemon = testdaemon()

if 'start' == sys.argv[1]: 
    daemon.start()
elif 'stop' == sys.argv[1]: 
    daemon.stop()
elif 'restart' == sys.argv[1]: 
    daemon.restart()

"""

# class MyProcessAbstraction(object):
#     def __init__(self, parent_pid, command):
#         """
#         @type parent_pid: int
#         @type command: str
#         """
#         self._child = None
#         self._cmd = command
#         self._parent = psutil.Process(pid=parent_pid)

#     def run_child(self):
#         """
#         Start a child process by running self._cmd. 
#         Wait until the parent process (self._parent) has died, then kill the 
#         child.
#         """
#         print '---- Running command: "%s" ----' % self._cmd
#         self._child = psutil.Popen(self._cmd)
#         try:
#             while self._parent.status == psutil.STATUS_RUNNING:
#                 sleep(1)
#         except psutil.NoSuchProcess:
#             pass
#         finally:
#             print '---- Terminating child PID %s ----' % self._child.pid
#             self._child.terminate()

    
    # def reap_children(self,timeout=3, proceso):
    #     "Tries hard to terminate and ultimately kill all the children of this process."
    #     def on_terminate(proc):
    #         print("process {} terminated with exit code {}".format(proc, proc.returncode))

    #     procs = psutil.Process(proceso).children()
    #     # send SIGTERM
    #     for p in procs:
    #         try:
    #             p.terminate()
    #         except psutil.NoSuchProcess:
    #             pass
    #     gone, alive = psutil.wait_procs(procs, timeout=timeout, callback=on_terminate)
    #     if alive:
    #         # send SIGKILL
    #         for p in alive:
    #             print("process {} survived SIGTERM; trying SIGKILL".format(p))
    #             try:
    #                 p.kill()
    #             except psutil.NoSuchProcess:
    #                 pass
    #         gone, alive = psutil.wait_procs(alive, timeout=timeout, callback=on_terminate)
    #         if alive:
    #             # give up
    #             for p in alive:
    #                 print("process {} survived SIGKILL; giving up".format(p))