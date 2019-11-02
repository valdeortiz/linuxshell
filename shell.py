#!/usr/python
'''#!/usr/bin/python3 #para Lfs'''
# -*- coding: utf-8 -*-
from cmd import Cmd
import os
import shutil 

class Comandos(Cmd):
    """lista de comandos 
        diractual -> Imprime en pantalla la ruta del directorio actual.
        renombrar ->  Renombra un archivo.
        listar -> lista todos los archivos del directorio actual,
        copiar -> x
        mover -> Mueve - renombra un archivo o directorio.
        crear un directorio -> Crea un directorio en la ruta actual.
        cambiar directorio -> x
        cambiar los permisos -> Cambiar de permisos de un archivo o directorio.
        cambiar los propietarios -> Cambiar los propietarios de un archivo o directorio.
        cambiar la contrasenha -> 
        agregar usuario -> 
        registro de inicio y fin de sesion -> 
        transferencia ftp.
        ejecutar el comando de Bash -> Ejecuta cualquier comando del s.o.

    """
    intro = "***  Shell  *** \n=> introduzca help para visualizar los comandos habilitados." #Interprete de comandos FiOS.
    prompt = "Introduza un comando: "
    misc_header="Documentacion de los metodos de la clase"
    doc_header = "Ayuda de comandos documentados. Presione help <comando>"
    undoc_header="Los siguientes comandos no estan documentados:"
    ruler = "*" # caracter que separa al ejecutar help=menu de ayuda

    def do_diractual(self, args):
        """Muestra en pantalla el directorio actual.
        -> No posee parametros.
        Manera de ejecucion: diractual
        """
        print("directorio actual:", os.getcwd())

    def do_renombrar(self, args):
        """Renombrar un archivo o directorio
        Recibe dos parametros-> <nombre_actual> <nombre_cambiado>
        Manera de ejecutar: renombrar <nombre_actual> <nombre_a_cambiar>
        """
        args = args.split(" ")
        if len(args) == 2:
            try:
                os.rename(args[0],args[1])
                print("<",args[0],">", "fue renombrado a ","<",args[1],">")
            except:
                print("Error-> Ejecute help <renombrar> para mas informacion")
        else:
            print("La cantidad de parametros es incorrecta-> Ejecute help <renombrar> ")
        
        
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
                #arg = arg.split(" ") buscar la forma de evitar el lower
                #print(arg)
                dir = os.listdir(path= arg)
                for dirs in dir:
                    print(dirs, end="  ")
                print("\n")
                print("listado del directorio solicitado")
             
        except:
            print("Error-> Ejecute help <listar> para mas informacion")

    def do_mover(self, args):
        """
        Mover o renombrar un archivo o directorio. 
        Recibe dos parametros-> <directorio_actual> <directorio_cambiado>
                              o para renombrar un archivo: <nombre_actual> <nombre_cambiado>
        Manera de ejecutar:-> mover <directorio_actual> <directorio_a_cambiar>
                        -> renombrar: mover <nombre_actual> <nombre_a_cambiar>
        """
        args = args.split(" ")
        if len(args) == 2:
            try:
                shutil.move(args[0],args[1])
                print("<",args[0],">", "fue movido a ","<",args[1],">")
            except:
                print("Error-> Ejecute help <mover> para mas informacion")
        else:
            print("Error-> La cantidad de parametros es incorrecta. Ejecute help <mover>")

    #si ponemos car1/car2 .. si car1 existe se crear car2.. pero si no lanza un error
    def do_creardir(self, args):
        """
        Crea un nuevo directorio en la ruta actual. 
        Recibe dos parametros-> <nombre del directorio a crear> 
        Manera de ejecutar:-> creardir <nombre_del_directorio>
        """
        args = args.split(" ")
        if len(args) == 1:
            #para crear varias carpeta usar os.makedirs(car1/car2/car3)
            try:
                os.mkdir(args[0])
                print("<",args[0],">", "fue creado")
            except:
                print("Error-> Ejecute help <creardir> para mas informacion")
        else:
            print("Error-> La cantidad de parametros es incorrecta. Ejecute help <creardir>")   
        
    def do_cambiarpermisos(self, args):
        """
        Cambiar los permisos de un archivo o directorio. 
        Recibe dos parametros-> <ruta> <permisos> 
        Manera de ejecutar:-> cambiarpermisos <ruta> <permisos>
        """
        args = args.split(" ")
        if len(args) == 2:
            #para crear varias carpeta usar os.makedirs(car1/car2/car3)
            try:
                os.chmod(args[0],int(args[1],8)) #EL segundo parametro que recibe chmod debe ser entero y en octal
                print("<",args[0],">", "permisos cambiado")
            except:
                print("Error-> Ejecute help <permisos> para mas informacion")
        else:
            print("Error-> La cantidad de parametros es incorrecta. Ejecute help <permisos>") 

    def do_cambiarpropietario(self, args):
        """
        Cambiar  propietario de un archivo o directorio. 
        Recibe dos parametros-> <ruta> <id_propietario> <id_grupo> 
        Manera de ejecutar:-> cambiarpropietario <ruta> <propietario> <grupo>
        """
        args = args.split(" ")
        if len(args) == 3:
            try:
                print("propietario_id del archivo:", os.stat(args[0]).st_uid) 
                print("Grupo_id del archivo:", os.stat(args[0]).st_gid)
                #os.chown(args[0],args[1],args[2]) #EL segundo parametro que recibe chmod debe ser entero y en octal
                print("<",args[0],">", "propietarios cambiados")
                print("propietario_id del archivo:", os.stat(args[0]).st_uid) 
                print("Grupo_id del archivo:", os.stat(args[0]).st_gid)
            except:
                print("Error-> Ejecute help <propietario> para mas informacion")
        else:
            print("Error-> La cantidad de parametros es incorrecta. Ejecute help <propietario>") 


    def do_limpiar(self, args):
        os.system("clear")

    def do_ejecutar(self, args):
        """ Ejecuta un comando del sistema"""
        os.system(args)

    
# verificar que la cantidad de parametros sean los correctos 
######################################################################
    
    def do_comandoejemplo(self, args):
        """Ayuda del comando3: ejecuta comando1 y comando2"""
        self.onecmd("comando1")
        self.onecmd("comando2")

    # def precmd(self, args):
    #     args = args.lower()
    #     return(args)

    def emptyline(self):
        """No realiza ninguna accion"""
        print("No escribio un comando")
        pass

    def do_salir(self, args):
        
        print("Hasta pronto!")
        return(True)


    def default(self, args):
        print("Error. ",args, " No existe el comando -> Presione help para visualizar los comandos posibles")

    
        
#Funcion main .. Verificamos que al ejecutar el script no sea un modulo
if __name__ == '__main__':
    Comandos().cmdloop()