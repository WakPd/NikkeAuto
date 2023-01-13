from tkinter import *
import os
import sys
import tkinter
import subprocess
from detection import *

devices = open("config.txt", "r").read()

adb = r"scrcpy/scrcpy-win64-v1.25/adb.exe"

nikkegui = Tk()
nikkegui.resizable(False, False)
nikkegui.title("NikkeGui")
nikkegui.geometry("400x500")



NikkeFrame = LabelFrame(nikkegui, text="Options")
NikkeFrame.grid(column=0, row=0, padx=100, pady=100,)

#RunEmulation
RM = tkinter.IntVar()
RunMirroring = Checkbutton(NikkeFrame, text="Run Screen Mirroring", variable=RM)
RunMirroring.pack()

#RunGame
RG = tkinter.IntVar()
RunGame = Checkbutton(NikkeFrame, text="Run Nikke", variable=RG)
RunGame.pack()

#Send and Request Friend Point
SAR = tkinter.IntVar()
SendAndRequest = Checkbutton(NikkeFrame, text="SendAndRequest", variable=SAR)
SendAndRequest.pack()

#Claim Outpost
CLAIM = tkinter.IntVar()
Claim = Checkbutton(NikkeFrame, text="Claim Outpost", variable=CLAIM)
Claim.pack()

#Buy Shop Sale
SALE = tkinter.IntVar()
Sale = Checkbutton(NikkeFrame, text="Buy Sale Items", variable=SALE)
Sale.pack()

#Dispatch Nikke
DIS = tkinter.IntVar()
Dispatch = Checkbutton(NikkeFrame, text="Dispatch",variable=DIS)
Dispatch.pack()
 
#Arena
ARENA = tkinter.IntVar()
Arena = Checkbutton(NikkeFrame, text="Do Arena", variable=ARENA)
Arena.pack()

#Special Arena
SPEA = tkinter.IntVar()
Spea = Checkbutton(NikkeFrame, text="Do Special Arena", variable=SPEA)
Spea.pack()

def runmirroring():
    if RM.get() :
        process = subprocess.Popen(r"scrcpy\scrcpy-win64-v1.25\scrcpy.exe")
    else:
        print("")

def rungame():
    if RG.get() :
        subprocess.run([adb, "-s", devices, "shell", "am","start", "-n", "com.proximabeta.nikke/com.shiftup.nk.MainActivity"])
        os.system("python ./modules/run.py")
    else:
        print("")

def sendandrequest():
    if SAR.get() :
            os.system("python ./modules/sandr.py")
    else:
        print("")

def dispatch():
    if DIS.get() :
        os.system("python ./modules/dispatch.py")
    else:
        print("")
def claim():
    if CLAIM.get() :
        os.system("python ./modules/claim.py")
    else:
        print("")
def sale():
    if SALE.get() :
        os.system("python ./modules/shop.py")
    else:
        print("")
def spea():
    if SPEA.get() :
        os.system("python ./modules/spearena.py")
    else:
        print("")
def arena():
    if ARENA.get() :
        os.system("python ./modules/arena.py")
    else:
        print("")


ButtonFrame = LabelFrame(nikkegui, text="Buttons")
NikkeFrame.grid(column=0, row=0, padx=50, pady=20)
Quit = Button(NikkeFrame, text="Quitter", command=nikkegui.quit)
Quit.pack()

Run = Button(NikkeFrame, text="Run", command=lambda: [runmirroring(), rungame(), sendandrequest(), dispatch(),claim(),sale(),spea(),arena()])
Run.pack()



nikkegui.mainloop()