from os import system
from colorama import Fore
import string
import random

system("title " + "Discord Token Gen,   Made By Thraxx#1402,   Discord: https://discord.gg/49YAGUEcMf")

print(Fore.LIGHTCYAN_EX + """
    ______ _                       _   _____     _                _____            
    |  _  (_)                     | | |_   _|   | |              |  __ \           
    | | | |_ ___  ___ ___  _ __ __| |   | | ___ | | _____ _ __   | |  \/ ___ _ __  
    | | | | / __|/ __/ _ \| '__/ _` |   | |/ _ \| |/ / _ \ '_ \  | | __ / _ \ '_ \ 
    ----------------------------Made by Thraxx#1402-------------------------------- 
    |___/ |_|___/\___\___/|_|  \__,_|   \_/\___/|_|\_\___|_| |_|  \____/\___|_| |_|
---------------------------------------------------------------------------------------
""")

def main():
    o = input(Fore.LIGHTBLUE_EX + "Enter 1 to only save to a file, Enter 2 to only display on screen, Enter 3 for both: ")
    a = int(input("How many token's do you want generated: "))
    oi = int(o)

    dig = str(random.randint(1,9))


    def token_id(size = 46, chr = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_' + '-'):
        return "".join(random.choice(chr) for _ in range(size))

    def token_1(size = 20, chr = string.ascii_lowercase + string.ascii_uppercase):
        return  "".join(random.choice(chr) for _ in range(size))

    def enough_token(size = 5, chr = string.ascii_lowercase + string.ascii_uppercase + '_' + '-'):
        return  "".join(random.choice(chr) for _ in range(size))  

    def op1():
        print(Fore.MAGENTA + "-----------------------------------------------------------------------------------")
        t = 1
        for i in range(a):
            with open("Tokens.txt", "a") as f:
                f.write("[" + str(t) + "] OTk" + token_1() +  ".G" + enough_token() + "." + token_id() + "\n")
                f.close()
            t += 1
        with open("Tokens.txt", "a") as f:
            f.write("-----------------------------------------------------------------------------------" + "\n")
            f.close()
        print(Fore.GREEN + "Successfully sent [" + str(a) + "] tokens to the tokens txt in the folder!")
        print(Fore.MAGENTA + "-----------------------------------------------------------------------------------")
        

            
        
    def op2():
        print(Fore.MAGENTA + "-----------------------------------------------------------------------------------")
        t = 1
        for i in range(a):
            print(Fore.MAGENTA + ("[" + str(t) + "] OTk" + token_1() +  ".G" + enough_token() + "." + token_id()))
            print(Fore.MAGENTA + "-----------------------------------------------------------------------------------")
            t += 1

    def op3():
        print(Fore.MAGENTA + "-----------------------------------------------------------------------------------")
        t = 1
        for i in range(a):
            with open("Tokens.txt", "a") as f:
                f.write("[" + str(t) + "] OTk" + token_1() +  ".G" + enough_token() + "." + token_id() + "\n")
                f.close()
            print(Fore.MAGENTA + ("[" + str(t) + "] OTk" + token_1() +  ".G" + enough_token() + "." + token_id()))
            print(Fore.MAGENTA + "-----------------------------------------------------------------------------------")
            t += 1
        with open("Tokens.txt", "a") as f:
            f.write("-----------------------------------------------------------------------------------" + "\n")
            f.close()

    if oi == 1:
        op1()
    elif oi == 2:
        op2()
    elif oi == 3:
        op3()

    End()

def End():
    ed = input(Fore.GREEN + "Do you want to use this again y/n!: ")

    if ed == "y":
        main()
    elif ed == "n":
        exit()         

main()    
