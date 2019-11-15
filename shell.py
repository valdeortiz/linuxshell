#!/usr/python
'''#!/usr/bin/python3 #para Lfs'''


from cmd import Cmd
import os
import shutil 
import logging

class Comandos(Cmd):
    """lista de comandos 
        copiar -> x
        cambiar directorio -> x
        cambiar los permisos -> Cambiar de permisos de un archivo o directorio.
        cambiar los propietarios -> Cambiar los propietarios de un archivo o directorio.
        cambiar la contrasenha -> 
        agregar usuario -> 
        registro de inicio y fin de sesion -> 
        transferencia ftp.
    """
    intro = "***  Shell  *** \n=> introduzca help para visualizar los comandos habilitados." #Interprete de comandos FiOS.
    prompt = "Introduza un comando: "
    misc_header="Documentacion de los metodos"
    doc_header = "Ayuda de comandos documentados. Presione help <comando>"
    undoc_header="Los siguientes comandos no estan documentados:"
    ruler = "*" # caracter separador al ejecutar help=menu de ayuda

    #fichero_log = "/usr/log/Lfs_Shell_log"
    # logging.basicConfig(level=logging.DEBUG,
    #                 format='%(asctime)s %(message)s', 
    #                 datefmt='%m/%d/%Y %I:%M:%S %p',
    #                 filename=fichero_log,
    #                 filemode='w')

    # En el archivo debe ir el registro de inicio y cierre de sesion.
    # Los mensajes de error son guardados en un archivo independiente llamado Shell_error_log que debe ir dentro del archivo log
    # Descripcion de la libreria logging al final del script.
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)s %(levelname)s %(message)s', # name es el user, asctime es hora y fecha, levelname: severidad, message: mensaje del error.
                        filename="Shell_Error.log")

    def do_diractual(self, args):
        """Muestra en pantalla el directorio actual.
        -> No posee parametros.
        Manera de ejecucion: diractual
        """
        print("Directorio actual:", os.getcwd())

    def do_renombrar(self, args):
        """Renombrar un archivo o directorio
        Recibe dos parametros-> <nombre_actual> <nombre_cambiado>
        Manera de ejecutar: renombrar <nombre_actual> <nombre_a_cambiar>
        """
        args = args.split(" ")

        if self.confirmarLongitud(len(args), 2, "renombrar"):
            try:
                os.rename(args[0],args[1])
                print("<",args[0],">", "fue renombrado a ","<",args[1],">")
            except Exception as e:
                print(f" Error: {e} -> al ejecutar <renombrar>")
                logging.error(f" codigo del error: {e} -> al ejecutar <renombrar>")
        else:
            pass        
        
    def do_listar(self, arg):
        """ Lista todos los archivos del directorio actual o de una ruta especifica.
        Parametros -> Si se ejecuta sin parametro se lista el directorio actual.
                      si se pasa la ruta como parametro se lista el directorio solicitado.
        Manera de ejecucion: listar el directorio actual: < listar >
                             Listar una ruta especifica: listar <ruta>
        """
         
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
             
        except Exception as e:
            print(f"Error {e} -> Ejecute help <listar> para mas informacion")
            logging.error(f" codigo del error: {e} -> Al ejecutar <listar>")

    def do_mover(self, args):
        """
        Mover o renombrar un archivo o directorio. 
        Recibe dos parametros-> <directorio_actual> <directorio_cambiado>
                              o para renombrar un archivo: <nombre_actual> <nombre_cambiado>
        Manera de ejecutar:-> mover <directorio_actual> <directorio_a_cambiar>
                        -> renombrar: mover <nombre_actual> <nombre_a_cambiar>
        """
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 2, "mover"):
            try:
                shutil.move(args[0],args[1])
                print("<",args[0],">", "fue movido a ","<",args[1],">")
            except Exception as e:
                print(f"Error {e}-> Ejecute help <mover> para mas informacion")
                logging.error(f" codigo del error: {e} -> Al ejecutar mover")
        else:
            pass

    #si ponemos car1/car2 .. si car1 existe se crear car2.. pero si no lanza un error
    def do_creardir(self, args):
        """
        Crea un nuevo directorio en la ruta actual. 
        Recibe dos parametros-> <nombre del directorio a crear> 
        Manera de ejecutar:-> creardir <nombre_del_directorio>
        """
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 1, "creardir"):
            #para crear varias carpeta usar os.makedirs(car1/car2/car3)
            try:
                os.mkdir(args[0])
                print("<",args[0],">", "fue creado")
            except Exception as e:
                print(f"Error {e} -> Ejecute help <creardir> para mas informacion")
                logging.error(f"Error {e} -> al ejecutar <creardir>")
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
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 2, "cambiarpermisos"):
            try:
                os.chmod(args[0],int(args[1],8)) #EL segundo parametro que recibe chmod debe ser entero y en octal
                print("<",args[0],">", "permisos cambiado")
            except Exception as e:
                print(f"Error {e}-> Ejecute help <permisos> para mas informacion")
                logging.error(f"codigo del error: {e} -> al ejecutar <permisos> ")
        else:
            pass

    def do_cambiarpropietario(self, args):
        """
        Cambiar  propietario de un archivo o directorio. 
        Recibe dos parametros-> <ruta> <id_propietario> <id_grupo> 
        Manera de ejecutar:-> cambiarpropietario <ruta> <propietario> <grupo>
        """
        args = args.split(" ")
        if self.confirmarLongitud(len(args), 3,"cambiarpropietario"):
            try:
                print("propietario_id del archivo:", os.stat(args[0]).st_uid) 
                print("Grupo_id del archivo:", os.stat(args[0]).st_gid)
                #os.chown(args[0],args[1],args[2]) #EL segundo parametro que recibe chmod debe ser entero y en octal
                print("<",args[0],">", "propietarios cambiados")
                print("propietario_id del archivo:", os.stat(args[0]).st_uid) 
                print("Grupo_id del archivo:", os.stat(args[0]).st_gid)
            except Exception as e:
                print(f"Error {e}-> Ejecute help <propietario> para mas informacion")
                logging.error(f" Codigo de error: {e} -> al ejecutar <propietario>")

        else:
            pass


    def do_limpiar(self, args):
        os.system("clear")

    def do_ejecutar(self, args):
        """ Ejecuta un comando del sistema"""
        os.system(args)
        #llama a las funciones de la shell host.        

######################################################################
    
    def do_comandoejemplo(self, args):
        """Ayuda del comando3: ejecuta comando1 y comando2"""
        self.onecmd("comando1")
        self.onecmd("comando2")

    # precmd se ejecuta antes de cada comando, no recomiendo porque puede causar errores en agunos comandos.
    # def precmd(self, args):
    #     args = args.lower()
    #     return(args)

    def confirmarLongitud(self,longArg,longOficial,comando):
        if longArg == longOficial:
            return True
        else:
            print(f"Error-> La cantidad de parametros es incorrecta. Ejecute help <{comando}>") 
            logging.error(f"La cantidad de parametros es incorrecta. Al ejecutar <{comando}>")
            return False

    def emptyline(self):
        """No realiza ninguna accion"""
        print("Ningun comando ejecutado.")
        logging.warning("Ningun comando ejecutado")
        pass

    def do_salir(self, args):
        logging.info("Finalizacion de sesion")
        print("Hasta pronto!")
        return True 


    def default(self, args):
        logging.error(f"Ejecuto {args}. No existe el comando ")
        print("Error. ",args, " No existe el comando -> Presione help para visualizar los comandos posibles")
    
    # Forma de documentar metodos,
    # def help_confirmarLongitud(self):
    #     print("Verifica la cantidad de parametros enviados al comando.")



#Funcion main .. Verificamos que al ejecutar el script no sea un modulo importado.
# Al ejecutar este script importando desde otro script no se ejecuta estas lineas.
if __name__ == '__main__':
    logging.info("Inicio de sesion")
    Comandos().cmdloop()


    """ Funciones de logging segun el nivel de severidad:
    Debug: informacion de alguna solucion.
    info: todo funciona correctamente. 
    warning: Informacion sobre un posible error.
    error: error que no permite la ejecucion del metodo.
    critical:error critico la app ha dejado de funciona.

    Paramatros del basiconfig:
    format: formato previo al error.
        %(clientip)s = imprime el client ip
        %(name)s = imprime el usuario en que se ejecuta.
    level: nivel de severidad inicial.
    datefmt: cambiar el formato de la fecha, va de la mano con format.

    obs: El nivel predeterminado es el warning. Si ejecutamos un info depues de un warning, no imprimira nada debido a que warning es mas severo.
    por ello comenzamos colocando el level de debug.
    """