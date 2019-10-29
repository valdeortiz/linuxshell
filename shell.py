#!/usr/python
'''#!/usr/bin/python3 #para Lfs'''
# -*- coding: utf-8 -*-
from cmd import Cmd
import os


class Comandos(Cmd):
    """lista de comandos 
        diractual -> Imprime en pantalla la ruta del directorio actual.
        renombrar ->  Renombra un archivo.
        listar -> lista todos los archivos del directorio actual,
        comando1 -> 
        comando1 -> 
    """
    intro = "***  Shell  *** \n=> introduzca help para visualizar los comandos habilitados." #Interprete de comandos FiOS.
    prompt = "Introduza un comando: "
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
        try:
            os.rename(args[0],args[1])
            print("<",args[0],">", "fue renombrado a ","<",args[1],">")
        except:
            print("Error-> Ejecute help <renombrar> para mas informacion")
        
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
                print(arg)
                dir = os.listdir(path= arg)
                for dirs in dir:
                    print(dirs, end="  ")
                print("\n")
                print("listado del directorio solicitado")
             
        except:
            print("Error-> Ejecute help <listar> para mas informacion")




######################################################################
    def do_comandoejemplo(self, args):
        """Ayuda del comando3: ejecuta comando1 y comando2"""
        self.onecmd("comando1")
        self.onecmd("comando2")

    def precmd(self, args):
        args = args.lower()
        return(args)

    def emptyline(self):
        """No realiza ninguna accion"""
        print("No escribio un comando")
        pass

    def do_salir(self, args):
        
        print("Hasta pronto!")
        return(True)


    def default(self, args):
        print("Error. ",args, " No existe el comando -> Presione help para visualizar los comandos posibles")

    
        

if __name__ == '__main__':
    Comandos().cmdloop()