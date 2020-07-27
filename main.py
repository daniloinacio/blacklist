import sys
from scapy.all import *
import importlib
import socket
from termcolor import colored


def shell():
  exploit = None
  scanner = None
  target = None
  print(colored("# Welcome to Blacklist Framework!!!", "yellow") + colored("""

bbbb  l          a       ccccc k   k  l      i  sssss  ttttttttt
b  b  l         a a     cc     k  k   l      i ss          t
bbbb  l        a   a   c       kkk    l      i  sssss      t
b   b l       aaaaaaa   cc     k  k   l      i      ss     t
bbbb  llllll a       a   ccccc k    k llllll i  sssss      t

""", "blue") + colored("""
##################################################################
########################  ######  ######  ########################
########################  ######  ######  ########################
####################                          ####################
####################  ######################  ####################
##############        ######################       ###############
####################  #######        #######  ####################
####################  #####            #####  ####################
###############       #####   ##   ##   ####       ###############
####################  ######    ##     #####  ####################
####################  #########     ########  ####################
###############       ######### # # ########       ###############
####################  ######################  ####################
####################                          ####################
########################  ######  #######  #######################
########################  ######  #######  #######################
##################################################################

""", "red") + 
colored("Digite o comando help para começar", "yellow"))
  while(1):
    command_str = input(colored("blf > ", "blue"))
    if command_str == "exit" or command_str == "quit":
      break
    elif "set target" in command_str:
      if len(command_str.split()) < 3:
        print("%s: missing operand" %command_str)
      elif len(command_str.split()) > 3:
        print("%s: invalid argument" %command_str)  
      else:
        command_str = command_str.replace("set target ", "")
        try:
          socket.inet_aton(command_str)
          target = command_str
        except socket.error:
          print("%s: invalid IP" %command_str)          
    elif "set exploit" in command_str:
      if len(command_str.split()) < 3:
        print("%s: missing operand" %command_str)
      elif len(command_str.split()) > 3:
        print("%s: invalid argument" %command_str)
      else:
        command_str = command_str.replace("set exploit ", "")
        command_str = command_str.replace('/', '.')
        try:
          exploit_module =  __import__(command_str, fromlist=[''])
          exploit = exploit_module.exploit()
        except:
          command_str = command_str.replace('.', '/')
          print("%s: exploit not found!" %command_str)
    elif "set option" in command_str:
      if len(command_str.split()) < 4:
        print("%s: missing operand" %command_str)
      elif len(command_str.split()) > 4:
        print("%s: invalid argument" %command_str)
      else:
        command_str = command_str.replace("set option ", '')
        if exploit != None:
          exploit.set_options(command_str)
        else:
          print("No exploits selected")
    elif command_str == "show options":
      if exploit != None:
        exploit.show_options()
      else:
        print("No exploits selected")
    elif command_str == "show exploit":
      if exploit != None:
        exploit.show_details()
      else:
          print("No exploits selected")
    elif command_str == "show exploits":
      print("""Name:                                                    Description:           
..........                                               ............
modules/exploits/freertos/CVE-2018-16524
modules/exploits/freertos/CVE-2018-16601
modules/exploits/generics/land
modules/exploits/generics/tcp_syn_floon                                                               
""")
    elif command_str == "show target":
      if target != None:
        print(target)
      else:
        print("No target selected")
    elif command_str == "run":  
      if exploit != None and target != None:
        exploit.run(target)
      elif target == None:
        print("No target selected")
      else:
        print("No exploits selected")      
    elif command_str == "help":
      print("""\nShell commands:
################\n      
set target <target IP>       - configura um target
set exploit <exploit path>   - seleciona um exploit
set option  <option> <value> - configura as opções disponíveis do atual exploit
show target                  - exibe o target
show exploit                 - exibe o exploit selecionado
show exploits                - exibe todos os exploits disponíveis
show options                 - exibe opções do exploit atual 
run                          - executa o exploit
help                         - mostra todos os comandos
exit ou quit                 - sai do console\n""")
    else:
      print("%s: command not found" %command_str)

if __name__ == "__main__":

  shell()
