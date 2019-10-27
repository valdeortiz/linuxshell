#!/usr/python
'''#!/usr/bin/python3 #para Lfs'''
# -*- coding: utf-8 -*-
from cmd import Cmd

class Comandos(Cmd):
    """Interprete de comandos"""
    intro = "*** Bienvenido al interprete de comandos ***" #Interprete de comandos FiOS.
    prompt = "Introduza un comando: "
    doc_header = "Ayuda de comandos documentados. Presione help <comando>"
    
    def do_comando1(self, args):
        """Ayuda del comando1"""
        print("comando1 se ha ejecutado")

    def do_comando2(self, args):
        """Ayuda del comando2"""
        print("comando2 se ha ejecutado")

    def do_comando3(self, args):
        """Ayuda del comando3: ejecuta comando1 y comando2"""
        self.onecmd("comando1")
        self.onecmd("comando2")

    def precmd(self, args):
        args = args.lower()
        return(args)

    # def postcmd(self, stop, args):                
    #     if args == "salir":            
    #         stop = True        
    #     else:
    #         print("Para finalizar introducir 'salir'")            
    #         stop = False
    #     return(stop)

    def emptyline(self):
        """No realiza ninguna accion"""
        print("No escribio un comando")
        pass

    def do_salir(self, args):
        """Cerrar el interprete de comandos"""
        print("Hasta pronto!")
        return(True)


    def default(self, args):
        print("Error. ", args, " No existe el comando -> Presione help para visualizar los comandos posibles")



if __name__ == '__main__':
    Comandos().cmdloop()