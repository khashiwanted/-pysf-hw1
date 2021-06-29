print ("Hello Snappfood")
print ("my name is Khashayar Saemian")
from colorama import Back,Fore,Style
print(Back.MAGENTA + "                      This is Homework 1                    ")
def Sky1():
    i = int(1)
    for i in range(1,4):
        print(Back.BLUE +" "*60)
        i = i+1
def Roof1():
    a = int(29)
    b = int(1)
    c = int(27)
    i = int(1)
    for i in range(1,8):
        print(Back.BLUE +" "*a + Back.RED + "  "*b + Back.RED + "  "*b + Back.BLUE +" "*c)
        a = a-2
        b = b+1
        c = c-2
        i = i+1

def Body1():
    i = int(1)
    for i in range(1,4):
        print(Back.BLUE +" "*17 + Back.GREEN + "    "*7 + Back.BLUE +" "*15)
        i = i+1
    
def Wind1():
    i = int(1)
    for i in range(1,4):
        print(Back.BLUE +" "*17 + Back.GREEN + "    "*4 + Back.WHITE +" "*7 + Back.GREEN +" "*5 + Back.BLUE +" "*15)
        i = i+1

def Door1():
    i=int(1)
    for i in range(1,8):
        print(Back.BLUE +" "*17 + Back.GREEN + "    "*2 + Back.YELLOW +" "*7 + Back.GREEN +" "*13 + Back.BLUE +" "*15)
        i = i+1
        

Sky1()
Roof1()
Body1()
Wind1()
Body1()
Door1()
Sky1()


