import pyautogui
import time
import subprocess
import os


def lobby():
    #Lobby Button Detection
    lobby = pyautogui.locateCenterOnScreen(r"utils\img\lobby.png" or r"utils\img\lobby2.png", confidence=.8)
    print("Searching for lobby button.")
    while lobby == None:
        lobby = pyautogui.locateCenterOnScreen(r"utils\img\lobby.png", confidence=.8)
        print("Searching for lobby button.")
        time.sleep(2)
    print("Lobby button find at", lobby)
    pyautogui.moveTo(lobby)
    time.sleep(2)
    pyautogui.click(lobby)

def home():
    #Home Button Detection
    home = pyautogui.locateCenterOnScreen(r"utils\img\home.png", confidence=.8)
    print("Searching for home button.")
    while home == None:
        home = pyautogui.locateCenterOnScreen(r"utils\img\home.png", confidence=.8)
        print("Searching for home button.")
        time.sleep(2)
    print("Homme button find at", home)
    pyautogui.moveTo(home)
    time.sleep(2)
    pyautogui.click(home)

def ark():
    #Ark Button
    ark = pyautogui.locateCenterOnScreen(r"utils\img\ark.png", confidence=.8)
    print("Searching for ark button.")
    while ark == None:
        ark = pyautogui.locateCenterOnScreen(r"utils\img\ark.png", confidence=.8)
        print("Searching for ark button.")
        time.sleep(2)
    print("Ark button find at", ark)
    pyautogui.moveTo(ark)
    time.sleep(2)
    pyautogui.click(ark)

def arena():
    arenaark = pyautogui.locateOnScreen(r"utils\img\arena.png", confidence=.8)
    print(arenaark)
    while arenaark == None:
        arenaark = pyautogui.locateOnScreen(r"utils\img\arena.png", confidence=.8)
        print(arenaark)
    print(arenaark)
    pyautogui.moveTo(arenaark)
    time.sleep(2)
    pyautogui.click()
    pyautogui.click()

def rung():
    #Enter Game Button
    print("Running Nikke to Lobby")
    entr = pyautogui.locateCenterOnScreen(r"utils\img\entr.png", confidence=.8)
    print("Searching for enter button.")
    while entr == None:
        entr = pyautogui.locateCenterOnScreen(r"utils\img\entr.png", confidence=.8)
        print("Searching for enter button.")
        time.sleep(2)
    print("Enter button find at", entr)
    pyautogui.moveTo(entr)
    time.sleep(2)
    pyautogui.click(entr)
    lobby()

def arkarena():
    #ArkArena Button
    ark()
    arena()
    normal = pyautogui.locateOnScreen(r"utils\img\normal.png", confidence=.8)
    print(normal)
    while normal == None:
        normal = pyautogui.locateOnScreen(r"utils\img\normal.png", confidence=.8)
        print(normal)
    print(normal)
    pyautogui.moveTo(normal)
    pyautogui.click()
    pyautogui.click()
    rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
    print(rka)
    while rka == None:
        rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
        print(rka)
    print(rka)
    pyautogui.moveTo(1105, 522)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(954, 784)
    pyautogui.click()
    pyautogui.click()
    rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
    print(rwd)
    while rwd == None:
        rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
        print(rwd)
        time.sleep(5)
    print(rwd)
    pyautogui.moveTo(1105, 522)
    time.sleep(2)
    pyautogui.click()
    pyautogui.click()
    rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
    print(rka)
    while rka == None:
        rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
        print(rka)
    print(rka)
    pyautogui.moveTo(1105, 522)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(954, 784)
    pyautogui.click()
    pyautogui.click()
    rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
    print(rwd)
    while rwd == None:
        rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
        print(rwd)
        time.sleep(5)
    print(rwd)
    pyautogui.moveTo(1105, 522)
    time.sleep(2)
    pyautogui.click()
    pyautogui.click()
    rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
    print(rka)
    while rka == None:
        rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
        print(rka)
    print(rka)
    pyautogui.moveTo(1105, 522)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(954, 784)
    pyautogui.click()
    pyautogui.click()
    rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
    print(rwd)
    while rwd == None:
        rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
        print(rwd)
        time.sleep(5)
    print(rwd)
    pyautogui.moveTo(1105, 522)
    time.sleep(2)
    pyautogui.click()
    pyautogui.click()
    rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
    print(rka)
    while rka == None:
        rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
        print(rka)
    print(rka)
    pyautogui.moveTo(1105, 522)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(954, 784)
    pyautogui.click()
    pyautogui.click()
    rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
    print(rwd)
    while rwd == None:
        rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
        print(rwd)
        time.sleep(5)
    print(rwd)
    pyautogui.moveTo(1105, 522)
    time.sleep(2)
    pyautogui.click()
    pyautogui.click()
    rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
    print(rka)
    while rka == None:
        rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
        print(rka)
    print(rka)
    pyautogui.moveTo(1105, 522)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(954, 784)
    pyautogui.click()
    pyautogui.click()
    rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
    print(rwd)
    while rwd == None:
        rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
        print(rwd)
        time.sleep(5)
    print(rwd)
    pyautogui.moveTo(1105, 522)
    time.sleep(2)
    pyautogui.click()
    pyautogui.click()
    rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
    print(rka)
    while rka == None:
        rka = pyautogui.locateOnScreen(r"utils\img\rookiea.png", confidence=.8)
        print(rka)
    print(rka)
    home()

def arkspecialarena():
    ark()
    arena()
    spea = pyautogui.locateOnScreen(r"utils\img\special.png", confidence=.8)
    print(spea)
    while spea == None:
        spea = pyautogui.locateOnScreen(r"utils\img\special.png", confidence=.8)
        print(spea)
    print(spea)
    pyautogui.moveTo(spea)
    pyautogui.click()
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1104, 601)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(970, 774)
    pyautogui.click()
    pyautogui.click()
    rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
    print(rwd)
    while rwd == None:
        rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
        print(rwd)
    print(rwd)
    pyautogui.moveTo(rwd)
    pyautogui.click()
    pyautogui.click()
    spa = pyautogui.locateOnScreen(r"utils\img\spa.png", confidence=.8)
    print(spa)
    while spa == None:
        spa = pyautogui.locateOnScreen(r"utils\img\spa.png", confidence=.8)
        print(spa)
    print(spa)
    pyautogui.moveTo(1104, 601)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(970, 774)
    pyautogui.click()
    pyautogui.click()
    rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
    print(rwd)
    while rwd == None:
        rwd = pyautogui.locateOnScreen(r"utils\img\rwd.png", confidence=.8)
        print(rwd)
    print(rwd)
    pyautogui.moveTo(rwd)
    pyautogui.click()
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(1104, 601)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(970, 774)
    pyautogui.click()
    pyautogui.click()
    home()

def outpost():
    #Outpost and claim Button
    out = pyautogui.locateCenterOnScreen(r"utils\img\out.png", confidence=.8)
    print("Searching for outpost button.")
    while out == None:
        out = pyautogui.locateCenterOnScreen(r"utils\img\out.png", confidence=.8)
        print("Searching for outpost button.")
        time.sleep(2)
    print("Outpost button find at", out)
    pyautogui.moveTo(out)
    time.sleep(2)
    pyautogui.click(out)
    claim = pyautogui.locateCenterOnScreen(r"utils\img\claim.png", confidence=.8)
    print("Searching for claim button.")
    while claim == None:
        claim = pyautogui.locateCenterOnScreen(r"utils\img\claim.png", confidence=.8)
        print("Searching for claim button.")
        time.sleep(2)
    print("Claim button find at", claim)
    pyautogui.moveTo(claim)
    time.sleep(2)
    pyautogui.click(claim)
    time.sleep(2)
    pyautogui.click(claim)
    lobby()

def dispatch():
    #Dispatch Button
    outpst = pyautogui.locateCenterOnScreen(r"utils\img\outpst.png", confidence=.8)
    print("Searching for outpost button.")
    while outpst == None:
        outpst = pyautogui.locateCenterOnScreen(r"utils\img\outpst.png", confidence=.8)
        print("Searching for outpost button.")
        time.sleep(2)
    print("Outpost button find at", outpst)
    pyautogui.moveTo(outpst)
    time.sleep(2)
    pyautogui.click(outpst)
    bulb = pyautogui.locateCenterOnScreen(r"utils\img\bulb.png", confidence=.8)
    print("Searching for Bulletin Board button.")
    while bulb == None:
        bulb = pyautogui.locateCenterOnScreen(r"utils\img\bulb.png", confidence=.8)
        print("Searching for Bulletin Board button.")
        time.sleep(2)
    print("Bulletin Board button find at", bulb)
    pyautogui.moveTo(bulb)
    time.sleep(2)
    pyautogui.click(bulb)
    dispa = pyautogui.locateCenterOnScreen(r"utils\img\dispa.png", confidence=.8)
    while dispa == None:
        dispa = pyautogui.locateCenterOnScreen(r"utils\img\dispa.png", confidence=.8)
        print(dispa) 
        time.sleep(2)
    print(dispa)
    pyautogui.moveTo(dispa)
    pyautogui.click()
    disp = pyautogui.locateCenterOnScreen(r"utils\img\disp.png", confidence=.8)
    while disp == None:
        disp = pyautogui.locateCenterOnScreen(r"utils\img\disp.png", confidence=.8)
        print(disp) 
        time.sleep(2)
    print(disp)
    pyautogui.moveTo(disp)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    close = pyautogui.locateCenterOnScreen(r"utils\img\close.png", confidence=.8)
    while close == None:
        close = pyautogui.locateCenterOnScreen(r"utils\img\close.png", confidence=.8)
        print(close) 
        time.sleep(2)
    print(close)
    pyautogui.moveTo(close)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    home()

def shop_sale():
    #Shop and sale Button
    shop = pyautogui.locateCenterOnScreen(r"utils\img\shop.png", confidence=.8)
    print("Searching for shop button.")
    while shop == None:
        shop = pyautogui.locateCenterOnScreen(r"utils\img\shop.png", confidence=.8)
        print("Searching for shop button.")
        time.sleep(2)
    print("Shop button find at", shop)
    pyautogui.moveTo(shop)
    time.sleep(2)
    pyautogui.click(shop)
    sale = pyautogui.locateCenterOnScreen(r"utils\img\sale.png", confidence=.8)
    print("Searching for sale button.")
    while sale == None:
        sale = pyautogui.locateCenterOnScreen(r"utils\img\sale.png", confidence=.8)
        print("Searching for sale button.")
        time.sleep(2)
    print("Sale button find at", sale)
    pyautogui.moveTo(sale)
    time.sleep(2)
    pyautogui.click(sale)
    time.sleep(2)
    pyautogui.click()
    buy = pyautogui.locateCenterOnScreen(r"utils\img\buy.png", confidence=.8)
    print("Searching for sale button.")
    while buy == None:
        buy = pyautogui.locateCenterOnScreen(r"utils\img\buy.png", confidence=.8)
        print("Searching for sale button.")
        time.sleep(2)
    print("Buy button find at", buy)
    pyautogui.moveTo(buy)
    time.sleep(2)
    pyautogui.click(buy)
    time.sleep(2)
    pyautogui.click()
    home()

def sandr():
    #Friend Button
    friend = pyautogui.locateCenterOnScreen(r"utils\img\friend.png", confidence=.8)
    print("Searching for friend button.")
    while friend == None:
        friend = pyautogui.locateCenterOnScreen(r"utils\img\friend.png", confidence=.8)
        print("Searching for friend button.")
        time.sleep(2)
    print("Friend button find at", friend)
    pyautogui.moveTo(friend)
    time.sleep(2)
    pyautogui.click(friend)
    SendandRequest = pyautogui.locateCenterOnScreen(r"utils\img\sandr.png", confidence=.8)
    print("Searching for Send and Request button.")
    while SendandRequest == None:
        SendandRequest = pyautogui.locateCenterOnScreen(r"utils\img\sandr.png", confidence=.8)
        print("Searching for Send and Request button.")
        time.sleep(2)
    print("Send and Request button find at", SendandRequest)
    pyautogui.moveTo(SendandRequest)
    time.sleep(2)
    pyautogui.click(SendandRequest)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    lobby()