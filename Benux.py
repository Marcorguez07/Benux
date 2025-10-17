# Benux High Level OS
# Benux High Level OS, Made by Marco Rodríguez, Spanish Student of Computer Science.

# Library imports, required for certain functions

import os
import time
from datetime import date

# Declaration of Global Variables, called through the entire code

CommandLine = ("")
EmptyLine = ("")
today = date.today()

# Declaration of memory variables, this is really complex stuff, but in short: 8 variables will be dedicated to general storing purpose, 8 variables will be
# dedicated to store information written by the user and another 8 variables will be used to check what variables are stored inside a folder, if the user creates folders. Another
# 8 variables will be dedicated to check if the user is inside the folder, necessary to make a useful explorer
 
memory1 = ("")
memory2 = ("")
memory3 = ("")
memory4 = ("")
memory5 = ("")
memory6 = ("")
memory7 = ("")
memory8 = ("")
writtendata1 = ("")
writtendata2 = ("")
writtendata3 = ("")
writtendata4 = ("")
writtendata5 = ("")
writtendata6 = ("")
writtendata7 = ("")
writtendata8 = ("")
storedinfolder1 = []
storedinfolder2 = []
storedinfolder3 = []
storedinfolder4 = []
storedinfolder5 = []
storedinfolder6 = []
storedinfolder7 = []
storedinfolder8 = []
insidefolder1 = False
insidefolder2 = False
insidefolder3 = False
insidefolder4 = False
insidefolder5 = False
insidefolder6 = False
insidefolder7 = False
insidefolder8 = False
isadoc1 = False
isadoc2 = False
isadoc3 = False
isadoc4 = False
isadoc5 = False
isadoc6 = False
isadoc7 = False
isadoc8 = False
storer = [storedinfolder1, storedinfolder2, storedinfolder3, storedinfolder4, storedinfolder5, storedinfolder6, storedinfolder7, storedinfolder8] 

# app status variables, required to check if a program is currently open

BenuxHelperActive = False
CalculatorActive = False
ExplorerActive = False
NotesWriterActive = False


def InitMessage():
    print("-------------------------------------------------------------------------------------------------")
    print(f"                  Benux 1.1v , Operating System Written in Python, write /h for help\n                             By Marco Rodríguez, Current date: {today}\n-------------------------------------------------------------------------------------------------\n")
    NewCommand()


def ScreenClearing():
    # Not really required, but if you want your program to look good, use it.
    os.system('cls' if os.name == 'nt' else 'clear')

def NewCommand():
    global CommandLine, EmptyLine # required "global" if changing a variable set outside a def function
    CommandLine = ("")
    EmptyLine = ("")
    try:
        while CommandLine == EmptyLine:
            CommandLine = input("> :")
        Executer()
    except:
        NewCommand()

############ Application Specific DEFS ######################

def AdditionCalc(a, b):
    c = a + b
    print(f"The result of your addition is {c}")
    
def SubstractionCalc(a, b):
    c = a - b
    print(f"The result of your substraction is {c}")

def MultplicationCalc(a, b):
    c = a * b
    print(f"The result of your multiplication is {c}")

def DivideCalc(a, b):
    c = a / b
    print(f"The result of your divide is {c}")

def storerinUI1(x):

    global storedinfolder1
    storedinfolder1.append(x)

def storerinUI2(x):
    global storedinfolder2
    storedinfolder2.append(x)

def storerinUI3(x):
    global storedinfolder3
    storedinfolder3.append(x)

def storerinUI4(x):
    global storedinfolder4
    storedinfolder4.append(x)

def storerinUI5(x):
    global storedinfolder5
    storedinfolder5.append(x)

def storerinUI6(x):
    global storedinfolder6
    storedinfolder6.append(x)

def storerinUI7(x):
    global storedinfolder7
    storedinfolder7.append(x)

def storerinUI8(x):
    global storedinfolder8
    storedinfolder8.append(x)

def textsaver1(a,b,c,d,e,f,g,h):
    global writtendata1
    writtendata1 = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")

def textsaver2(a,b,c,d,e,f,g,h):
    global writtendata2
    writtendata2 = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")

def textsaver3(a,b,c,d,e,f,g,h):
    global writtendata3
    writtendata3 = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")

def textsaver4(a,b,c,d,e,f,g,h):
    global writtendata4
    writtendata4 = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")

def textsaver5(a,b,c,d,e,f,g,h):
    global writtendata5
    writtendata5 = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")

def textsaver6(a,b,c,d,e,f,g,h):
    global writtendata6
    writtendata6 = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")

def textsaver7(a,b,c,d,e,f,g,h):
    global writtendata7
    writtendata7 = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")

def textsaver8(a,b,c,d,e,f,g,h):
    global writtendata8
    writtendata8 = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")
    


##############################################################

def Executer():

    # Make programs here, programs should be treated as "windows", they should be able to be closed at any moment.
    
    # the executer should be ALWAYS at the end of the code, since python requires to read the code first to "declare?" stuff, really weird.

    global writtendata1, writtendata2, writtendata3, writtendata4, writtendata5, writtendata6, writtendata7, writtendata8, BenuxHelperActive, CalculatorActive, ExplorerActive, NotesWriterActive, EmptyLine, memory1, memory2, memory3, memory4, memory5, memory6, memory7, memory8, insidefolder1, insidefolder2, insidefolder3, insidefolder4, insidefolder5, insidefolder6, insidefolder7, insidefolder8, storedinfolder1, storedinfolder2, storedinfolder3, storedinfolder4, storedinfolder5, storedinfolder6, storedinfolder7, storedinfolder8, storer, isadoc1, isadoc2, isadoc3, isadoc4, isadoc5, isadoc6, isadoc7, isadoc8 

    if CommandLine == ("/h"):
        BenuxHelperActive = True
        ScreenClearing()
        print("------Benux Helper------\n\nType /helpsys , to get information about the Operating System\nType /helpcommands , to get information about the commands\nType /close , to close the Benux Helper application\n\n")
    else:
        pass

    if CommandLine == ("/helpsys"):
        if BenuxHelperActive == True:
            ScreenClearing()
            print("------Benux Helper------\nBenux is a basic Operating System written in Python, a high level programming language.\nThis program is capable of doing simple tasks, like creating, saving, destroying files\ninside its environment, writing text documents and completing simple arithmetic equations\n\nI built this program to learn the basics of python, you can asbolutely redestribute\nand modify this software in any way you see fit\n\nBenux Version: 1.1, by Marco Rodríguez")
        else:
            pass
    else:
        pass

    if CommandLine == ("/helpcommands"):
        if BenuxHelperActive == True:
            ScreenClearing()
            print("------Benux Helper------\n\n/h -> Shows basic help and starts the Benux Helper Program\n/calc -> Starts the calculator program\n/exp -> Starts the explorer program\n/ntwriter -> Starts the notes writer program\n/close -> Closes all oppened applications and clears the screen\n/changelog -> List of changes introduced with the current version of Benux\n\n")
        else:
            pass
    else:
        pass

    if CommandLine == ("/changelog"):
        if BenuxHelperActive == True:
            ScreenClearing()
            print("------Benux Helper------\n\nList of changes for 1.1v\n\n- You can no longer divide any number by zero\n- Pressing ctrl+c no longer crashes the program\n- Updated /helpexp\n\n")
        else:
            pass
    else:
        pass

    if CommandLine == ("/calc"):
        CalculatorActive = True
        ScreenClearing()
        print("------Benux Calculator------")
        print("")
        print("Calc: Welcome to Benux Calculator, type /helpcalc to get started")
        print("")
    else:
        pass

    if CommandLine == ("/helpcalc"):
        if CalculatorActive == True:
            print("\nBefore making any calculations, you need to state which arithmetic operation you want to perform.\nState the desired operation, then you will be asked to enter the two numbers you want to operate on.\n\n--List of Operations--\n\n/add -> a + b = c\n/substract -> a - b = c\n/multiply -> a x b = c\n/divide -> a / b = c\n\n")
        else:
            pass
    else:
        pass

    if CommandLine == ("/add"):
        if CalculatorActive == True:

            # Declaration of local variables, will be passed to the aritmetic function through def parameters ("")

            a = None
            b = None

            print("\nCalc: Addition Aritmetic Operation has been activated!, a + b = c\n")


            while a == None:
                try:
                    a = int(input("Type the first number of your addition :> "))
                except:
                    a = None
            while b == None:
                try:
                    b = int(input("Type the second number of your addition :> "))
                except:
                    b = None
                    
            print("")
            AdditionCalc(a, b)
            
        else:
            pass
    else:
        pass

    if CommandLine == ("/substract"):
        if CalculatorActive == True:

            # Declaration of local variables, will be passed to the aritmetic function through def parameters ("")

            a = None
            b = None

            print("")
            print("Calc: Substraction Aritmetic Operation has been activated!, a - b = c")
            print("")

            while a == None:
                try:
                    a = int(input("Type the first number of your substraction :> "))
                except:
                    a = None
            while b == None:
                try:
                    b = int(input("Type the second number of your substraction :> "))
                except:
                    b = None
                
            print("")
            SubstractionCalc(a, b)
            
        else:
            pass
    else:
        pass

    if CommandLine == ("/multiply"):
        if CalculatorActive == True:

            # Declaration of local variables, will be passed to the aritmetic function through def parameters ("")

            a = None
            b = None

            print("")
            print("Calc: Multiplication Aritmetic Operation has been activated!, a x b = c")
            print("")

            while a == None:
                try:
                    a = int(input("Type the first number of your multiplication :> "))
                except:
                    a = None
            while b == None:
                try:
                    b = int(input("Type the second number of your multiplication :> "))
                except:
                    b = None
                    
            print("")
            MultplicationCalc(a, b)
            
        else:
            pass
    else:
        pass

    if CommandLine == ("/divide"):
        if CalculatorActive == True:

            # Declaration of local variables, will be passed to the aritmetic function through def parameters ("")

            a = None
            b = None

            print("")
            print("Calc: Divide Aritmetic Operation has been activated!, a x b = c")
            print("")

            while a == None:
                try:
                    a = int(input("Type the first number of your divide :> "))
                except:
                    a = None
            while b == None:
                try:
                    b = int(input("Type the second number of your divide :> "))
                except:
                    b = None

                
            print("")

            if b == 0:
                pass
                print("You cannot divide by zero, try again")
            else:
                DivideCalc(a, b)
            
        else:
            pass
    else:
        pass

    ################ explorer program, things get complex here.

    if CommandLine == ("/exp"):
        ExplorerActive = True
        ScreenClearing()
        print("------Benux Files Explorer------")
        print("")
        print("Exp: Welcome to Benux file explorer, type /helpexp to get started")
        print("")


        # Making sure that if we reset the explorer no folders will be open by default, this way /close doesnt handle it.
        insidefolder1 = False
        insidefolder2 = False
        insidefolder3 = False
        insidefolder4 = False
        insidefolder5 = False
        insidefolder6 = False
        insidefolder7 = False
        insidefolder8 = False
        
    else:
        pass

    if CommandLine == ("/helpexp"):
        if ExplorerActive == True:
            print("")
            print("Benux File Explorer is limited to eight files, you cannot save more than eight files.\nFiles will only be saved in the very same session, if you terminate Benux, files will dissapear.\n\n/fdcreate -> Creates a folder, any name is tolerated.\n/fdremove (name) -> Deletes a folder\n/goto (name) -> Go to a certain folder\n/open (name) -> Opens a file\n/list -> Shows all created files")
            print("")
        else:
            pass
    else:
        pass

    if CommandLine == ("/fdcreate") and insidefolder1 == False and insidefolder2 == False and insidefolder3 == False and insidefolder4 == False and insidefolder5 == False and insidefolder6 == False and insidefolder7 == False and insidefolder8 == False:
        if ExplorerActive == True:
            if memory1 == EmptyLine:
                memory1 = input("Choose a name for your folder >: ") 
            else:
                if memory2 == EmptyLine:
                    memory2 = input("Choose a name for your folder >: ") 
                else:
                    if memory3== EmptyLine:
                        memory3 = input("Choose a name for your folder >: ") 
                    else:
                        if memory4 == EmptyLine:
                            memory4 = input("Choose a name for your folder >: ") 
                        else:
                            if memory5 == EmptyLine:
                                memory5 = input("Choose a name for your folder >: ") 
                            else:
                                if memory6 == EmptyLine:
                                    memory6 = input("Choose a name for your folder >: ") 
                                else:
                                    if memory7 == EmptyLine:
                                        memory7 = input("Choose a name for your folder >: ") 
                                    else:
                                        if memory8 == EmptyLine:
                                            memory8 = input("Choose a name for your folder >: ") 
                                        else:
                                            print("Benux Error 1: No Storage Left, please delete a folder and try again...")
        else:
            pass
    else:
        if ExplorerActive == True:
            if CommandLine == ("/fdcreate"):
                if insidefolder1 == True:
                    if memory1 == EmptyLine:
                        memory1 = input("Choose a name for your folder >: ")
                        x = memory1
                        storerinUI1(x)
                    else:
                        if memory2 == EmptyLine:
                            memory2 = input("Choose a name for your folder >: ")
                            x = memory2
                            storerinUI1(x)
                        else:
                            if memory3== EmptyLine:
                                memory3 = input("Choose a name for your folder >: ")
                                x = memory3
                                storerinUI1(x)
                            else:
                                if memory4 == EmptyLine:
                                    memory4 = input("Choose a name for your folder >: ")
                                    x = memory4
                                    storerinUI1(x)
                                else:
                                    if memory5 == EmptyLine:
                                        memory5 = input("Choose a name for your folder >: ")
                                        x = memory5
                                        storerinUI1(x)
                                    else:
                                        if memory6 == EmptyLine:
                                            memory6 = input("Choose a name for your folder >: ")
                                            x = memory6
                                            storerinUI1(x)
                                        else:
                                            if memory7 == EmptyLine:
                                                memory7 = input("Choose a name for your folder >: ")
                                                x = memory7
                                                storerinUI1(x)
                                            else:
                                                if memory8 == EmptyLine:
                                                    memory8 = input("Choose a name for your folder >: ")
                                                    x = memory8
                                                    storerinUI1(x)
                                                else:
                                                    print("Benux Error 1: No Storage Left, please delete a folder and try again...")
                
                else:
                    if insidefolder2 == True:
                        if memory1 == EmptyLine:
                            memory1 = input("Choose a name for your folder >: ")
                            x = memory1
                            storerinUI2(x)
                        else:
                            if memory2 == EmptyLine:
                                memory2 = input("Choose a name for your folder >: ")
                                x = memory2
                                storerinUI2(x)
                            else:
                                if memory3== EmptyLine:
                                    memory3 = input("Choose a name for your folder >: ")
                                    x = memory3
                                    storerinUI2(x)
                                else:
                                    if memory4 == EmptyLine:
                                        memory4 = input("Choose a name for your folder >: ")
                                        x = memory4
                                        storerinUI2(x)
                                    else:
                                        if memory5 == EmptyLine:
                                            memory5 = input("Choose a name for your folder >: ")
                                            x = memory5
                                            storerinUI2(x)
                                        else:
                                            if memory6 == EmptyLine:
                                                memory6 = input("Choose a name for your folder >: ")
                                                x = memory6
                                                storerinUI2(x)
                                            else:
                                                if memory7 == EmptyLine:
                                                    memory7 = input("Choose a name for your folder >: ")
                                                    x = memory7
                                                    storerinUI2(x)
                                                else:
                                                    if memory8 == EmptyLine:
                                                        memory8 = input("Choose a name for your folder >: ")
                                                        x = memory8
                                                        storerinUI2(x)
                                                    else:
                                                        print("Benux Error 1: No Storage Left, please delete a folder and try again...")

                                
                    else:
                        if insidefolder3 == True:
                            if memory1 == EmptyLine:
                                memory1 = input("Choose a name for your folder >: ")
                                x = memory1
                                storerinUI3(x)
                            else:
                                if memory2 == EmptyLine:
                                    memory2 = input("Choose a name for your folder >: ")
                                    x = memory2
                                    storerinUI3(x)
                                else:
                                    if memory3== EmptyLine:
                                        memory3 = input("Choose a name for your folder >: ")
                                        x = memory3
                                        storerinUI3(x)
                                    else:
                                        if memory4 == EmptyLine:
                                            memory4 = input("Choose a name for your folder >: ")
                                            x = memory4
                                            storerinUI3(x)
                                        else:
                                            if memory5 == EmptyLine:
                                                memory5 = input("Choose a name for your folder >: ")
                                                x = memory5
                                                storerinUI3(x)
                                            else:
                                                if memory6 == EmptyLine:
                                                    memory6 = input("Choose a name for your folder >: ")
                                                    x = memory6
                                                    storerinUI3(x)
                                                else:
                                                    if memory7 == EmptyLine:
                                                        memory7 = input("Choose a name for your folder >: ")
                                                        x = memory7
                                                        storerinUI3(x)
                                                    else:
                                                        if memory8 == EmptyLine:
                                                            memory8 = input("Choose a name for your folder >: ")
                                                            x = memory8
                                                            storerinUI3(x)
                                                        else:
                                                            print("Benux Error 1: No Storage Left, please delete a folder and try again...")
                        else:
                            if insidefolder4 == True:
                                if memory1 == EmptyLine:
                                    memory1 = input("Choose a name for your folder >: ")
                                    x = memory1
                                    storerinUI4(x)
                                else:
                                    if memory2 == EmptyLine:
                                        memory2 = input("Choose a name for your folder >: ")
                                        x = memory2
                                        storerinUI4(x)
                                    else:
                                        if memory3== EmptyLine:
                                            memory3 = input("Choose a name for your folder >: ")
                                            x = memory3
                                            storerinUI4(x)
                                        else:
                                            if memory4 == EmptyLine:
                                                memory4 = input("Choose a name for your folder >: ")
                                                x = memory4
                                                storerinUI4(x)
                                            else:
                                                if memory5 == EmptyLine:
                                                    memory5 = input("Choose a name for your folder >: ")
                                                    x = memory5
                                                    storerinUI4(x)
                                                else:
                                                    if memory6 == EmptyLine:
                                                        memory6 = input("Choose a name for your folder >: ")
                                                        x = memory6
                                                        storerinUI4(x)
                                                    else:
                                                        if memory7 == EmptyLine:
                                                            memory7 = input("Choose a name for your folder >: ")
                                                            x = memory7
                                                            storerinUI4(x)
                                                        else:
                                                            if memory8 == EmptyLine:
                                                                memory8 = input("Choose a name for your folder >: ")
                                                                x = memory8
                                                                storerinUI4(x)
                                                            else:
                                                                print("Benux Error 1: No Storage Left, please delete a folder and try again...")

                            else:
                                if insidefolder5 == True:
                                    if memory1 == EmptyLine:
                                        memory1 = input("Choose a name for your folder >: ")
                                        x = memory1
                                        storerinUI5(x)
                                    else:
                                        if memory2 == EmptyLine:
                                            memory2 = input("Choose a name for your folder >: ")
                                            x = memory2
                                            storerinUI5(x)
                                        else:
                                            if memory3== EmptyLine:
                                                memory3 = input("Choose a name for your folder >: ")
                                                x = memory3
                                                storerinUI5(x)
                                            else:
                                                if memory4 == EmptyLine:
                                                    memory4 = input("Choose a name for your folder >: ")
                                                    x = memory4
                                                    storerinUI5(x)
                                                else:
                                                    if memory5 == EmptyLine:
                                                        memory5 = input("Choose a name for your folder >: ")
                                                        x = memory5
                                                        storerinUI5(x)
                                                    else:
                                                        if memory6 == EmptyLine:
                                                            memory6 = input("Choose a name for your folder >: ")
                                                            x = memory6
                                                            storerinUI5(x)
                                                        else:
                                                            if memory7 == EmptyLine:
                                                                memory7 = input("Choose a name for your folder >: ")
                                                                x = memory7
                                                                storerinUI5(x)
                                                            else:
                                                                if memory8 == EmptyLine:
                                                                    memory8 = input("Choose a name for your folder >: ")
                                                                    x = memory8
                                                                    storerinUI5(x)
                                                                else:
                                                                    print("Benux Error 1: No Storage Left, please delete a folder and try again...")
                                else:
                                    if insidefolder6 == True:
                                        if memory1 == EmptyLine:
                                            memory1 = input("Choose a name for your folder >: ")
                                            x = memory1
                                            storerinUI6(x)
                                        else:
                                            if memory2 == EmptyLine:
                                                memory2 = input("Choose a name for your folder >: ")
                                                x = memory2
                                                storerinUI6(x)
                                            else:
                                                if memory3== EmptyLine:
                                                   memory3 = input("Choose a name for your folder >: ")
                                                   x = memory3
                                                   storerinUI6(x)
                                                else:
                                                    if memory4 == EmptyLine:
                                                        memory4 = input("Choose a name for your folder >: ")
                                                        x = memory4
                                                        storerinUI6(x)
                                                    else:
                                                        if memory5 == EmptyLine:
                                                            memory5 = input("Choose a name for your folder >: ")
                                                            x = memory5
                                                            storerinUI6(x)
                                                        else:
                                                            if memory6 == EmptyLine:
                                                                memory6 = input("Choose a name for your folder >: ")
                                                                x = memory6
                                                                storerinUI6(x)
                                                            else:
                                                                if memory7 == EmptyLine:
                                                                    memory7 = input("Choose a name for your folder >: ")
                                                                    x = memory7
                                                                    storerinUI6(x)
                                                                else:
                                                                    if memory8 == EmptyLine:
                                                                        memory8 = input("Choose a name for your folder >: ")
                                                                        x = memory8
                                                                        storerinUI6(x)
                                                                    else:
                                                                        print("Benux Error 1: No Storage Left, please delete a folder and try again...")
                                    else:
                                        if insidefolder7 == True:
                                            if memory1 == EmptyLine:
                                                memory1 = input("Choose a name for your folder >: ")
                                                x = memory1
                                                storerinUI7(x)
                                            else:
                                                if memory2 == EmptyLine:
                                                    memory2 = input("Choose a name for your folder >: ")
                                                    x = memory2
                                                    storerinUI7(x)
                                                else:
                                                    if memory3== EmptyLine:
                                                        memory3 = input("Choose a name for your folder >: ")
                                                        x = memory3
                                                        storerinUI7(x)
                                                    else:
                                                        if memory4 == EmptyLine:
                                                            memory4 = input("Choose a name for your folder >: ")
                                                            x = memory4
                                                            storerinUI7(x)
                                                        else:
                                                            if memory5 == EmptyLine:
                                                                memory5 = input("Choose a name for your folder >: ")
                                                                x = memory5
                                                                storerinUI7(x)
                                                            else:
                                                                if memory6 == EmptyLine:
                                                                    memory6 = input("Choose a name for your folder >: ")
                                                                    x = memory6
                                                                    storerinUI7(x)
                                                                else:
                                                                    if memory7 == EmptyLine:
                                                                        memory7 = input("Choose a name for your folder >: ")
                                                                        x = memory7
                                                                        storerinUI7(x)
                                                                    else:
                                                                        if memory8 == EmptyLine:
                                                                            memory8 = input("Choose a name for your folder >: ")
                                                                            x = memory8
                                                                            storerinUI7(x)
                                                                        else:
                                                                            print("Benux Error 1: No Storage Left, please delete a folder and try again...")
                                        else:
                                            if insidefolder8 == True:
                                                if memory1 == EmptyLine:
                                                    memory1 = input("Choose a name for your folder >: ")
                                                    x = memory1
                                                    storerinUI8(x)
                                                else:
                                                    if memory2 == EmptyLine:
                                                        memory2 = input("Choose a name for your folder >: ")
                                                        x = memory2
                                                        storerinUI8(x)
                                                    else:
                                                        if memory3== EmptyLine:
                                                           memory3 = input("Choose a name for your folder >: ")
                                                           x = memory3
                                                           storerinUI8(x)
                                                        else:
                                                            if memory4 == EmptyLine:
                                                                memory4 = input("Choose a name for your folder >: ")
                                                                x = memory4
                                                                storerinUI8(x)
                                                            else:
                                                                if memory5 == EmptyLine:
                                                                    memory5 = input("Choose a name for your folder >: ")
                                                                    x = memory5
                                                                    storerinUI8(x)
                                                                else:
                                                                    if memory6 == EmptyLine:
                                                                        memory6 = input("Choose a name for your folder >: ")
                                                                        x = memory6
                                                                        storerinUI8(x)
                                                                    else:
                                                                        if memory7 == EmptyLine:
                                                                            memory7 = input("Choose a name for your folder >: ")
                                                                            x = memory7
                                                                            storerinUI8(x)
                                                                        else:
                                                                            if memory8 == EmptyLine:
                                                                                memory8 = input("Choose a name for your folder >: ")
                                                                                x = memory8
                                                                                storerinUI8(x)
                                                                            else:
                                                                                print("Benux Error 1: No Storage Left, please delete a folder and try again...")

      
        else:
            pass
                    
    

    if CommandLine == (f"/goto {memory1}") or CommandLine == (f"/goto {memory2}") or CommandLine == (f"/goto {memory3}") or CommandLine == (f"/goto {memory4}") or CommandLine == (f"/goto {memory5}") or CommandLine == (f"/goto {memory6}" or CommandLine == (f"/goto {memory7}") or CommandLine == (f"/goto {memory8}")) :
        if ExplorerActive == True:
            # we should save the last command line in a local variable so we know what folder did the user enter to, it is not safe to work with CommandLine variable anymore
            # since the user can override it if he enters a new line. Remember to delete the local variable later.

            if CommandLine == (f"/goto {memory1}"):
                LocalCommandLine = memory1
            else:
                pass
            if CommandLine == (f"/goto {memory2}"):
                LocalCommandLine = memory2
            else:
                pass
            if CommandLine == (f"/goto {memory3}"):
                LocalCommandLine = memory3
            else:
                pass
            if CommandLine == (f"/goto {memory4}"):
                LocalCommandLine = memory4
            else:
                pass
            if CommandLine == (f"/goto {memory5}"):
                LocalCommandLine = memory5
            else:
                pass
            if CommandLine == (f"/goto {memory6}"):
                LocalCommandLine = memory6
            else:
                pass
            if CommandLine == (f"/goto {memory7}"):
                LocalCommandLine = memory7
            else:
                pass
            if CommandLine == (f"/goto {memory8}"):
                LocalCommandLine = memory8
            else:
                pass
            
            ################ Saving variable, also making sure other variables are turned off, we can only be inside one folder at a time.

            if LocalCommandLine == memory1:
                if isadoc1 == True:
                    pass
                else:
                    insidefolder1 = True
                    insidefolder2 = False
                    insidefolder3 = False
                    insidefolder4 = False
                    insidefolder5 = False
                    insidefolder6 = False
                    insidefolder7 = False
                    insidefolder8 = False
                    print(f"You have entered into {LocalCommandLine}")
            else:
                if LocalCommandLine == memory2:
                    if isadoc2 == True:
                        pass
                    else:
                        insidefolder1 = False
                        insidefolder2 = True
                        insidefolder3 = False
                        insidefolder4 = False
                        insidefolder5 = False
                        insidefolder6 = False
                        insidefolder7 = False
                        insidefolder8 = False
                        print(f"You have entered into {LocalCommandLine}")
                else:
                    if LocalCommandLine == memory3:
                        if isadoc3 == True:
                            pass
                        else:
                            insidefolder1 = False
                            insidefolder2 = False
                            insidefolder3 = True
                            insidefolder4 = False
                            insidefolder5 = False
                            insidefolder6 = False
                            insidefolder7 = False
                            insidefolder8 = False
                            print(f"You have entered into {LocalCommandLine}")
                    else:
                        if LocalCommandLine == memory4:
                            if isadoc4 == True:
                                pass
                            else:
                                insidefolder1 = False
                                insidefolder2 = False
                                insidefolder3 = False
                                insidefolder4 = True
                                insidefolder5 = False
                                insidefolder6 = False
                                insidefolder7 = False
                                insidefolder8 = False
                                print(f"You have entered into {LocalCommandLine}")
                        else:
                            if LocalCommandLine == memory5:
                                if isadoc5 == True:
                                    pass
                                else:
                                    insidefolder1 = False
                                    insidefolder2 = False
                                    insidefolder3 = False
                                    insidefolder4 = False
                                    insidefolder5 = True
                                    insidefolder6 = False
                                    insidefolder7 = False
                                    insidefolder8 = False
                                    print(f"You have entered into {LocalCommandLine}")
                            else:
                                if LocalCommandLine == memory6:
                                    if isadoc6 == True:
                                        pass
                                    else:
                                        insidefolder1 = False
                                        insidefolder2 = False
                                        insidefolder3 = False
                                        insidefolder4 = False
                                        insidefolder5 = False
                                        insidefolder6 = True
                                        insidefolder7 = False
                                        insidefolder8 = False
                                        print(f"You have entered into {LocalCommandLine}")
                                else:
                                    if LocalCommandLine == memory7:
                                        if isadoc7 == True:
                                            pass
                                        else:
                                            insidefolder1 = False
                                            insidefolder2 = False
                                            insidefolder3 = False
                                            insidefolder4 = False
                                            insidefolder5 = False
                                            insidefolder6 = False
                                            insidefolder7 = True
                                            insidefolder8 = False
                                            print(f"You have entered into {LocalCommandLine}")
                                    else:
                                        if LocalCommandLine == memory8:
                                            if isadoc8 == True:
                                                pass
                                            else:
                                                insidefolder1 = False
                                                insidefolder2 = False
                                                insidefolder3 = False
                                                insidefolder4 = False
                                                insidefolder5 = False
                                                insidefolder6 = False
                                                insidefolder7 = False
                                                insidefolder8 = True
                                                print(f"You have entered into {LocalCommandLine}")
                                        else:
                                            pass

            

            

            del LocalCommandLine
            
        else:
            pass
            
            
    else:
        pass


    if CommandLine == ("/list"):
        if ExplorerActive == True:
            print("\nList of files stored:\n")
            if insidefolder1 == False and insidefolder2 == False and insidefolder3 == False and insidefolder4 == False and insidefolder5 == False and insidefolder6 == False and insidefolder7 == False and insidefolder8 == False:

        # Be careful with lists, the sublists are a thing, and you have to check in them, as "in" function does only check if the value you want to compare is in the main list
        # and not inside of the sublists, use "for sublist" to direct the attention to storer, syntax only, doesnt make sense but it is what it is.
        
                if memory1 == EmptyLine:
                    pass
                else:
                    if any(memory1 in sublist for sublist in storer):
                        pass
                    else:
                        print(memory1)
                if memory2 == EmptyLine:
                    pass
                else:
                    if any(memory2 in sublist for sublist in storer):
                        pass
                    else:
                        print(memory2)
                if memory3 == EmptyLine:
                    pass
                else:
                    if any(memory3 in sublist for sublist in storer):
                        pass
                    else:
                        print(memory3)
                if memory4 == EmptyLine:
                    pass
                else:
                    if any(memory4 in sublist for sublist in storer):
                        pass
                    else:
                        print(memory4)
                if memory5 == EmptyLine:
                    pass
                else:
                    if any(memory5 in sublist for sublist in storer):
                        pass
                    else:
                        print(memory5)
                if memory6 == EmptyLine:
                    pass
                else:
                    if any(memory6 in sublist for sublist in storer):
                        pass
                    else:
                        print(memory6)
                if memory7 == EmptyLine:
                    pass
                else:
                    if any(memory7 in sublist for sublist in storer):
                        pass
                    else:
                        print(memory7)
                if memory8 == EmptyLine:
                    pass
                else:
                    if any(memory8 in sublist for sublist in storer):
                        pass
                    else:
                        print(memory8)

#############################################################################################3
                        
            else:
                if insidefolder1 == True:
                    if storedinfolder1 == []:
                        print("No files are inside this folder...")
                    else:
                        print(storedinfolder1)
                else:
                    if insidefolder2 == True:
                        if storedinfolder2 == []:
                            print("No files are inside this folder...")
                        else:
                            print(storedinfolder2)
                    else:
                        if insidefolder3 == True:
                            if storedinfolder3 == []:
                                print("No files are inside this folder...")
                            else:
                                print(storedinfolder3)
                        else:
                            if insidefolder4 == True:
                                if storedinfolder4 == []:
                                    print("No files are inside this folder...")
                                else:
                                    print(storedinfolder4)
                            else:
                                if insidefolder5 == True:
                                    if storedinfolder5 == []:
                                        print("No files are inside this folder...")
                                    else:
                                        print(storedinfolder5)
                                else:
                                    if insidefolder6 == True:
                                        if storedinfolder6 == []:
                                            print("No files are inside this folder...")
                                        else:
                                            print(storedinfolder6)
                                    else:
                                        if insidefolder7 == True:
                                            if storedinfolder7 == []:
                                                print("No files are inside this folder...")
                                            else:
                                                print(storedinfolder7)
                                        else:
                                            if insidefolder8 == True:
                                                if storedinfolder8 == []:
                                                    print("No files are inside this folder...")
                                                else:
                                                    print(storedinfolder8)
                                            else:
                                                pass
                    
            if memory1 == EmptyLine and memory2 == EmptyLine and memory3 == EmptyLine and memory4 == EmptyLine and memory5 == EmptyLine and memory6 == EmptyLine and memory7 == EmptyLine and memory8 == EmptyLine:
                print("")
                print("No files have been created...\n")
            else:
                pass
                
        else:
            pass
    else:
        pass

    if CommandLine == (f"/fdremove {memory1}"):
        if ExplorerActive == True:
            if isadoc1 == True:
                memory1 = ("")
                writtendata1 = ("")
                isadoc1 = False
            else:
                for sub in storer:
                    if memory1 in sub:
                        sub.remove(memory1)
                        memory1 = ("")
                        print(memory1)
                        break
                    else:
                        memory1 = ("")
        else:
            pass
    else:
        pass

    
    if CommandLine == (f"/fdremove {memory2}"):
        if ExplorerActive == True:
            if isadoc2 == True:
                memory2 = ("")
                writtendata2 = ("")
                isadoc2 = False
            else:
                for sub in storer:
                    if memory2 in sub:
                        sub.remove(memory2)
                        memory2 = ("")
                        print(memory2)
                        break
                    else:
                        memory2 = ("")
        else:
            pass
    else:
        pass

    if CommandLine == (f"/fdremove {memory3}"):
        if ExplorerActive == True:
            if isadoc3 == True:
                memory3 = ("")
                isadoc3 = False
                writtendata3 = ("")
            else:
                for sub in storer:
                    if memory3 in sub:
                        sub.remove(memory3)
                        memory3 = ("")
                        print(memory3)
                        break
                    else:
                        memory3 = ("")
        else:
            pass
    else:
        pass

    if CommandLine == (f"/fdremove {memory4}"):
        if ExplorerActive == True:
            if isadoc4 == True:
                memory4 = ("")
                isadoc4 = False
                writtendata4 = ("")
            else:
                for sub in storer:
                    if memory4 in sub:
                        sub.remove(memory4)
                        memory4 = ("")
                        print(memory4)
                        break
                    else:
                        memory4 = ("")
        else:
            pass
    else:
        pass

    if CommandLine == (f"/fdremove {memory5}"):
        if ExplorerActive == True:
            if isadoc5 == True:
                memory5 = ("")
                isadoc5 = False
                writtendata5 = ("")
            else:
                for sub in storer:
                    if memory5 in sub:
                        sub.remove(memory5)
                        memory5 = ("")
                        print(memory5)
                        break
                    else:
                        memory5 = ("")
        else:
            pass
    else:
        pass

    if CommandLine == (f"/fdremove {memory6}"):
        if ExplorerActive == True:
            if isadoc6 == True:
                memory6 = ("")
                isadoc6 = False
                writtendata6 = ("")
            else:
                for sub in storer:
                    if memory6 in sub:
                        sub.remove(memory6)
                        memory6 = ("")
                        print(memory6)
                        break
                    else:
                        memory6 = ("")
        else:
            pass
    else:
        pass

    if CommandLine == (f"/fdremove {memory7}"):
        if ExplorerActive == True:
            if isadoc7 == True:
                memory7 = ("")
                isadoc7 = False
                writtendata7 = ("")
            else:
                for sub in storer:
                    if memory7 in sub:
                        sub.remove(memory7)
                        memory7 = ("")
                        print(memory7)
                        break
                    else:
                        memory7 = ("")
        else:
            pass
    else:
        pass

    if CommandLine == (f"/fdremove {memory8}"):
        if ExplorerActive == True:
            if isadoc8 == True:
                memory8 = ("")
                isadoc8 = False
                writtendata8 = ("")
            else:
                for sub in storer:
                    if memory8 in sub:
                        sub.remove(memory8)
                        memory8 = ("")
                        print(memory8)
                        break
                    else:
                        memory8 = ("")
        else:
            pass
    else:
        pass


    if CommandLine == (f"/open {memory1}"):
        if ExplorerActive == True:
            if isadoc1 == True:
                ScreenClearing()
                print(f"----------{memory1}----------\n")
                print(writtendata1)
                print("")
            else:
                print("Benux Error 2: This file is not a FOLDER. Use /goto command to enter inside a folder")
            
        else:
            pass
    else:
        pass


    if CommandLine == (f"/open {memory2}"):
        if ExplorerActive == True:
            if isadoc2 == True:
                ScreenClearing()
                print(f"----------{memory2}----------\n")
                print(writtendata2)
                print("")
            else:
                print("Benux Error 2: This file is not a FOLDER. Use /goto command to enter inside a folder")
            
        else:
            pass
    else:
        pass

    if CommandLine == (f"/open {memory3}"):
        if ExplorerActive == True:
            if isadoc3 == True:
                ScreenClearing()
                print(f"----------{memory3}----------\n")
                print(writtendata3)
                print("")
            else:
                print("Benux Error 2: This file is a FOLDER. Use /goto command to enter inside a folder")
            
        else:
            pass
    else:
        pass

    if CommandLine == (f"/open {memory4}"):
        if ExplorerActive == True:
            if isadoc4 == True:
                ScreenClearing()
                print(f"----------{memory4}----------\n")
                print(writtendata4)
                print("")
            else:
                print("Benux Error 2: This file is a FOLDER. Use /goto command to enter inside a folder")
            
        else:
            pass
    else:
        pass

    if CommandLine == (f"/open {memory5}"):
        if ExplorerActive == True:
            if isadoc5 == True:
                ScreenClearing()
                print(f"----------{memory5}----------\n")
                print(writtendata5)
                print("")
            else:
                print("Benux Error 2: This file is a FOLDER. Use /goto command to enter inside a folder")
            
        else:
            pass
    else:
        pass

    if CommandLine == (f"/open {memory6}"):
        if ExplorerActive == True:
            if isadoc6 == True:
                ScreenClearing()
                print(f"----------{memory6}----------\n")
                print(writtendata6)
                print("")
            else:
                print("Benux Error 2: This file is a FOLDER. Use /goto command to enter inside a folder")
            
        else:
            pass
    else:
        pass

    if CommandLine == (f"/open {memory7}"):
        if ExplorerActive == True:
            if isadoc7 == True:
                ScreenClearing()
                print(f"----------{memory7}----------\n")
                print(writtendata7)
                print("")
            else:
                print("Benux Error 2: This file is a FOLDER. Use /goto command to enter inside a folder")
            
        else:
            pass
    else:
        pass

    if CommandLine == (f"/open {memory8}"):
        if ExplorerActive == True:
            if isadoc8 == True:
                ScreenClearing()
                print(f"----------{memory8}----------\n")
                print(writtendata8)
                print("")
            else:
                print("Benux Error 2: This file is a FOLDER. Use /goto command to enter inside a folder")
            
        else:
            pass
    else:
        pass
    
    #### Writer program

    if CommandLine == ("/ntwriter"):
        NotesWriterActive = True
        ScreenClearing()
        print("------Benux Notes writer------")
        print("")
        print("Ntwriter: In this program you will be able to write and save small documents\nwrite /ntwhelp to get more information about the program")
        print("")
    else:
        pass

    if CommandLine == ("/ntwhelp"):
        if NotesWriterActive == True:
            print("\nYou can write up to eight lines of text in each document. Once you hit Enter, a new\nline will be available to write on.\n\n/ntstart -> Creates a New Document and starts editing text\n")
        else:
            pass
    else:
        pass

    if CommandLine == ("/ntstart"):
        if NotesWriterActive == True:
            ScreenClearing()
            print("------Benux Notes writer------\n##############################\n\nThis is your document! You can write up to eight lines of unlimited number of characters, each time\nyou hit ENTER you will start writing onto a new line. As of Benux 1.0 there's sadly no way of\nreturning to the previous line")
            print("")
            a = input("1: ")
            b = input("2: ")
            c = input("3: ")
            d = input("4: ")
            e = input("5: ")
            f = input("6: ")
            g = input("7: ")
            h = input("8: ")
            print("")
            savingquestion = input("Would you want to save this document?, If you dont want to, just type ENTER.\nIf you actually want to, type : /save (folder), if you dont want to\nsave this document inside a folder, just type /save\n\n >: ")

            # Okay, so now, we need to save the document, the right way to do this is to first ask the user if he wants to save the document, because if he doesnt, then we dont
            # need to do anything, but if he does, then we should check what written memories are empty, those who are, will get overwritten, those who arent, wont be touched.
            # we may need to create an extra boolean to tag what memory slots are actually documents, so /fdremove can also empty

            # variable as pointers
            
            if savingquestion == EmptyLine:
                pass
            elif savingquestion == ("/save"):
                if memory1 == EmptyLine:
                    isadoc1 = True
                    memory1 = input("State the name of your new document: ")
                    textsaver1(a,b,c,d,e,f,g,h)
                elif memory2 == EmptyLine:
                    isadoc2 = True
                    memory2 = input("State the name of your new document: ")
                    textsaver2(a,b,c,d,e,f,g,h)
                elif memory3 == EmptyLine:
                    isadoc3 = True
                    memory3 = input("State the name of your new document: ")
                    textsaver3(a,b,c,d,e,f,g,h)
                elif memory4 == EmptyLine:
                    isadoc4 = True
                    memory4 = input("State the name of your new document: ")
                    textsaver4(a,b,c,d,e,f,g,h)
                elif memory5 == EmptyLine:
                    isadoc5 = True
                    memory5 = input("State the name of your new document: ")
                    textsaver5(a,b,c,d,e,f,g,h)
                elif memory5 == EmptyLine:
                    isadoc5 = True
                    memory5 = input("State the name of your new document: ")
                    textsaver5(a,b,c,d,e,f,g,h)
                elif memory6 == EmptyLine:
                    isadoc6 = True
                    memory6 = input("State the name of your new document: ")
                    textsaver6(a,b,c,d,e,f,g,h)
                elif memory7 == EmptyLine:
                    isadoc7 = True
                    memory7 = input("State the name of your new document: ")
                    textsaver7(a,b,c,d,e,f,g,h)
                elif memory8 == EmptyLine:
                    isadoc8 = True
                    memory8 = input("State the name of your new document: ")
                    textsaver8(a,b,c,d,e,f,g,h)
                else:
                    print("\nBenux Error 3: There is no available memory to save this document, please delete a file and try again...")

            elif savingquestion == (f"/save {memory1}"):
                # FOLDER 1
                if memory1 == EmptyLine:
                    pass
                else:
                    if isadoc1 == False:
                        # now we need to loop for all the seven remaining memory slots to check what should this doc get.
                        if memory2 == EmptyLine:
                            memory2 = input("State the name of your new document: ")
                            x = memory2
                            isadoc2 = True
                            storerinUI1(x)  # remember, still in folder 1
                            textsaver2(a, b, c, d, e, f, g, h)
                        elif memory3 == EmptyLine:
                            memory3 = input("State the name of your new document: ")
                            x = memory3
                            isadoc3 = True
                            storerinUI1(x)
                            textsaver3(a, b, c, d, e, f, g, h)
                        elif memory4 == EmptyLine:
                            memory4 = input("State the name of your new document: ")
                            x = memory4
                            isadoc4 = True
                            storerinUI1(x)
                            textsaver4(a, b, c, d, e, f, g, h)
                        elif memory5 == EmptyLine:
                            memory5 = input("State the name of your new document: ")
                            x = memory5
                            isadoc5 = True
                            storerinUI1(x)
                            textsaver5(a, b, c, d, e, f, g, h)
                        elif memory6 == EmptyLine:
                            memory6 = input("State the name of your new document: ")
                            x = memory
                            isadoc6 = True
                            storerinUI1(x)
                            textsaver6(a, b, c, d, e, f, g, h)
                        elif memory7 == EmptyLine:
                            memory7 = input("State the name of your new document: ")
                            x = memory7
                            isadoc7 = True
                            storerinUI1(x)
                            textsaver7(a, b, c, d, e, f, g, h)
                        elif memory8 == EmptyLine:
                            memory8 = input("State the name of your new document: ")
                            x = memory8
                            isadoc8 = True
                            storerinUI1(x)
                            textsaver8(a, b, c, d, e, f, g, h)
                        else:
                            pass
                    else:
                        pass  # up to the if, perfectly indented

            elif savingquestion == (f"/save {memory2}"):
                # FOLDER 2
                if memory2 == EmptyLine:
                    pass
                else:
                    if isadoc2 == False:
                        if memory1 == EmptyLine:
                            memory1 = input("State the name of your new document: ")
                            x = memory1
                            isadoc1 = True
                            storerinUI2(x)
                            textsaver1(a, b, c, d, e, f, g, h)
                        elif memory3 == EmptyLine:
                            memory3 = input("State the name of your new document: ")
                            x = memory3
                            isadoc3 = True
                            storerinUI2(x)
                            textsaver3(a, b, c, d, e, f, g, h)
                        elif memory4 == EmptyLine:
                            memory4 = input("State the name of your new document: ")
                            x = memory4
                            isadoc4 = True
                            storerinUI2(x)
                            textsaver4(a, b, c, d, e, f, g, h)
                        elif memory5 == EmptyLine:
                            memory5 = input("State the name of your new document: ")
                            x = memory5
                            isadoc5 = True
                            storerinUI2(x)
                            textsaver5(a, b, c, d, e, f, g, h)
                        elif memory6 == EmptyLine:
                            memory6 = input("State the name of your new document: ")
                            x = memory6
                            isadoc6 = True
                            storerinUI2(x)
                            textsaver6(a, b, c, d, e, f, g, h)
                        elif memory7 == EmptyLine:
                            memory7 = input("State the name of your new document: ")
                            x = memory7
                            isadoc7 = True
                            storerinUI2(x)
                            textsaver7(a, b, c, d, e, f, g, h)
                        elif memory8 == EmptyLine:
                            memory8 = input("State the name of your new document: ")
                            x = memory8
                            isadoc8 = True
                            storerinUI2(x)
                            textsaver8(a, b, c, d, e, f, g, h)
                        else:
                            pass
                    else:
                        pass

            elif savingquestion == (f"/save {memory3}"):
                # FOLDER 3
                if memory3 == EmptyLine:
                    pass
                else:
                    if isadoc2 == False:
                        if memory1 == EmptyLine:
                            memory1 = input("State the name of your new document: ")
                            x = memory1
                            isadoc1 = True
                            storerinUI3(x)
                            textsaver1(a, b, c, d, e, f, g, h)
                        elif memory2 == EmptyLine:
                            memory2 = input("State the name of your new document: ")
                            x = memory2
                            isadoc2 = True
                            storerinUI3(x)
                            textsaver2(a, b, c, d, e, f, g, h)
                        elif memory4 == EmptyLine:
                            memory4 = input("State the name of your new document: ")
                            x = memory4
                            isadoc4 = True
                            storerinUI3(x)
                            textsaver4(a, b, c, d, e, f, g, h)
                        elif memory5 == EmptyLine:
                            memory5 = input("State the name of your new document: ")
                            x = memory5
                            isadoc5 = True
                            storerinUI3(x)
                            textsaver5(a, b, c, d, e, f, g, h)
                        elif memory6 == EmptyLine:
                            memory6 = input("State the name of your new document: ")
                            x = memory6
                            isadoc6 = True
                            storerinUI3(x)
                            textsaver6(a, b, c, d, e, f, g, h)
                        elif memory7 == EmptyLine:
                            memory7 = input("State the name of your new document: ")
                            x = memory7
                            isadoc7 = True
                            storerinUI3(x)
                            textsaver7(a, b, c, d, e, f, g, h)
                        elif memory8 == EmptyLine:
                            memory8 = input("State the name of your new document: ")
                            x = memory8
                            isadoc8 = True
                            storerinUI3(x)
                            textsaver8(a, b, c, d, e, f, g, h)
                        else:
                            pass
                    else:
                        pass

            elif savingquestion == (f"/save {memory4}"):
                # FOLDER 4
                if memory4 == EmptyLine:
                    pass
                else:
                    if isadoc4 == False:
                        if memory1 == EmptyLine:
                            memory1 = input("State the name of your new document: ")
                            x = memory1
                            isadoc1 = True
                            storerinUI4(x)
                            textsaver1(a, b, c, d, e, f, g, h)
                        elif memory2 == EmptyLine:
                            memory2 = input("State the name of your new document: ")
                            x = memory2
                            isadoc2 = True
                            storerinUI4(x)
                            textsaver2(a, b, c, d, e, f, g, h)
                        elif memory3 == EmptyLine:
                            memory3 = input("State the name of your new document: ")
                            x = memory3
                            isadoc3 = True
                            storerinUI4(x)
                            textsaver3(a, b, c, d, e, f, g, h)
                        elif memory5 == EmptyLine:
                            memory5 = input("State the name of your new document: ")
                            x = memory5
                            isadoc5 = True
                            storerinUI4(x)
                            textsaver5(a, b, c, d, e, f, g, h)
                        elif memory6 == EmptyLine:
                            memory6 = input("State the name of your new document: ")
                            x = memory6
                            isadoc6 = True
                            storerinUI4(x)
                            textsaver6(a, b, c, d, e, f, g, h)
                        elif memory7 == EmptyLine:
                            memory7 = input("State the name of your new document: ")
                            x = memory7
                            isadoc7 = True
                            storerinUI4(x)
                            textsaver7(a, b, c, d, e, f, g, h)
                        elif memory8 == EmptyLine:
                            memory8 = input("State the name of your new document: ")
                            x = memory8
                            isadoc8 = True
                            storerinUI4(x)
                            textsaver8(a, b, c, d, e, f, g, h)
                        else:
                            pass
                    else:
                        pass

            elif savingquestion == (f"/save {memory5}"):
                # FOLDER 5
                if memory5 == EmptyLine:
                    pass
                else:
                    if isadoc5 == False:
                        if memory1 == EmptyLine:
                            memory1 = input("State the name of your new document: ")
                            x = memory1
                            isadoc1 = True
                            storerinUI5(x)
                            textsaver1(a, b, c, d, e, f, g, h)
                        elif memory2 == EmptyLine:
                            memory2 = input("State the name of your new document: ")
                            x = memory2
                            isadoc2 = True
                            storerinUI5(x)
                            textsaver2(a, b, c, d, e, f, g, h)
                        elif memory3 == EmptyLine:
                            memory3 = input("State the name of your new document: ")
                            x = memory3
                            isadoc3 = True
                            storerinUI5(x)
                            textsaver3(a, b, c, d, e, f, g, h)
                        elif memory4 == EmptyLine:
                            memory4 = input("State the name of your new document: ")
                            x = memory4
                            isadoc4 = True
                            storerinUI5(x)
                            textsaver4(a, b, c, d, e, f, g, h)
                        elif memory6 == EmptyLine:
                            memory6 = input("State the name of your new document: ")
                            x = memory6
                            isadoc6 = True
                            storerinUI5(x)
                            textsaver6(a, b, c, d, e, f, g, h)
                        elif memory7 == EmptyLine:
                            memory7 = input("State the name of your new document: ")
                            x = memory7
                            isadoc7 = True
                            storerinUI5(x)
                            textsaver7(a, b, c, d, e, f, g, h)
                        elif memory8 == EmptyLine:
                            memory8 = input("State the name of your new document: ")
                            x = memory8
                            isadoc8 = True
                            storerinUI5(x)
                            textsaver8(a, b, c, d, e, f, g, h)
                        else:
                            pass
                    else:
                        pass

            elif savingquestion == (f"/save {memory6}"):
                # FOLDER 6
                if memory6 == EmptyLine:
                    pass
                else:
                    if isadoc6 == False:
                        if memory1 == EmptyLine:
                            memory1 = input("State the name of your new document: ")
                            x = memory1
                            isadoc1 = True
                            storerinUI6(x)
                            textsaver1(a, b, c, d, e, f, g, h)
                        elif memory2 == EmptyLine:
                            memory2 = input("State the name of your new document: ")
                            x = memory2
                            isadoc2 = True
                            storerinUI6(x)
                            textsaver2(a, b, c, d, e, f, g, h)
                        elif memory3 == EmptyLine:
                            memory3 = input("State the name of your new document: ")
                            x = memory3
                            isadoc3 = True
                            storerinUI6(x)
                            textsaver3(a, b, c, d, e, f, g, h)
                        elif memory4 == EmptyLine:
                            memory4 = input("State the name of your new document: ")
                            x = memory4
                            isadoc4 = True
                            storerinUI6(x)
                            textsaver4(a, b, c, d, e, f, g, h)
                        elif memory5 == EmptyLine:
                            memory5 = input("State the name of your new document: ")
                            x = memory5
                            isadoc5 = True
                            storerinUI6(x)
                            textsaver5(a, b, c, d, e, f, g, h)
                        elif memory7 == EmptyLine:
                            memory7 = input("State the name of your new document: ")
                            x = memory7
                            isadoc7 = True
                            storerinUI6(x)
                            textsaver7(a, b, c, d, e, f, g, h)
                        elif memory8 == EmptyLine:
                            memory8 = input("State the name of your new document: ")
                            x = memory8
                            isadoc8 = True
                            storerinUI6(x)
                            textsaver8(a, b, c, d, e, f, g, h)
                        else:
                            pass
                    else:
                        pass

            elif savingquestion == (f"/save {memory7}"):
                # FOLDER 7
                if memory7 == EmptyLine:
                    pass
                else:
                    if isadoc7 == False:
                        if memory1 == EmptyLine:
                            memory1 = input("State the name of your new document: ")
                            x = memory1
                            isadoc1 = True
                            storerinUI7(x)
                            textsaver1(a, b, c, d, e, f, g, h)
                        elif memory2 == EmptyLine:
                            memory2 = input("State the name of your new document: ")
                            x = memory2
                            isadoc2 = True
                            storerinUI7(x)
                            textsaver2(a, b, c, d, e, f, g, h)
                        elif memory3 == EmptyLine:
                            memory3 = input("State the name of your new document: ")
                            x = memory3
                            isadoc3 = True
                            storerinUI7(x)
                            textsaver3(a, b, c, d, e, f, g, h)
                        elif memory4 == EmptyLine:
                            memory4 = input("State the name of your new document: ")
                            x = memory4
                            isadoc4 = True
                            storerinUI7(x)
                            textsaver4(a, b, c, d, e, f, g, h)
                        elif memory5 == EmptyLine:
                            memory5 = input("State the name of your new document: ")
                            x = memory5
                            isadoc5 = True
                            storerinUI7(x)
                            textsaver5(a, b, c, d, e, f, g, h)
                        elif memory6 == EmptyLine:
                            memory6 = input("State the name of your new document: ")
                            x = memory6
                            isadoc6 = True
                            storerinUI7(x)
                            textsaver6(a, b, c, d, e, f, g, h)
                        elif memory8 == EmptyLine:
                            memory8 = input("State the name of your new document: ")
                            x = memory8
                            isadoc8 = True
                            storerinUI7(x)
                            textsaver8(a, b, c, d, e, f, g, h)
                        else:
                            pass
                    else:
                        pass

            elif savingquestion == (f"/save {memory8}"):
                # FOLDER 8
                if memory8 == EmptyLine:
                    pass
                else:
                    if isadoc8 == False:
                        if memory1 == EmptyLine:
                            memory1 = input("State the name of your new document: ")
                            x = memory1
                            isadoc1 = True
                            storerinUI8(x)
                            textsaver1(a, b, c, d, e, f, g, h)
                        elif memory2 == EmptyLine:
                            memory2 = input("State the name of your new document: ")
                            x = memory2
                            isadoc2 = True
                            storerinUI8(x)
                            textsaver2(a, b, c, d, e, f, g, h)
                        elif memory3 == EmptyLine:
                            memory3 = input("State the name of your new document: ")
                            x = memory3
                            isadoc3 = True
                            storerinUI8(x)
                            textsaver3(a, b, c, d, e, f, g, h)
                        elif memory4 == EmptyLine:
                            memory4 = input("State the name of your new document: ")
                            x = memory4
                            isadoc4 = True
                            storerinUI8(x)
                            textsaver4(a, b, c, d, e, f, g, h)
                        elif memory5 == EmptyLine:
                            memory5 = input("State the name of your new document: ")
                            x = memory5
                            isadoc5 = True
                            storerinUI8(x)
                            textsaver5(a, b, c, d, e, f, g, h)
                        elif memory6 == EmptyLine:
                            memory6 = input("State the name of your new document: ")
                            x = memory6
                            isadoc6 = True
                            storerinUI8(x)
                            textsaver6(a, b, c, d, e, f, g, h)
                       


                        
                            
                        else:
                            pass
            
            
            
                    else:
                        pass

        

    else:
        pass

    

   
    # this following line is technically not a program, but a direct order to "close" all programs by setting their respective booleans to the false value,
    # clearing the screen and calling InitMessage which in theory should also reset all variables. Basically it should work somehow like a "reset" for the OS.

    if CommandLine == ("/close"):
        BenuxHelperActive = False
        CalculatorActive = False
        ExplorerActive = False
        NotesWriterActive = False
        ScreenClearing()
        InitMessage() 
    else:
        pass

    # We only need to call this once, python works in a really interesting way... it always reads the whole code and wont stop unless we add a "while".
    # Note to my self: teoría de punteros

    NewCommand()

    # garbage

    del x, a, b, c, d, e, f, g, h



# Benux Starter, this "starts" up the program.

InitMessage()
