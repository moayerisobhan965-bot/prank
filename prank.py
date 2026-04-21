import time
import os
import sounddevice as sd
import numpy as np

def ton_spielen(frequenz, dauer):
    sample_rate = 44100
    t = np.linspace(0, dauer, int(sample_rate * dauer), False)
    ton = np.sin(2 * np.pi * frequenz * t) * 0.5
    sd.play(ton, sample_rate)
    sd.wait()

for x in range(4):
    ton_spielen(100, 0.3)
    time.sleep(0.1)
    ton_spielen(999, 0.1)
    time.sleep(0.05)

print("Bist du idiot? (Antworte mit (yes) (No))")
user = input()
time.sleep(0.2)
print("......LOADING......")

if user == "yes":
    print("Richtige Antwort")
    print("close prank.py")
if user == "No":
    print("DOCH BIST DU")

    print("......LOADING_VIRUS......")
    time.sleep(0.3)
    print("⚠️  VIRUS DETECTED - DELETING FILES...")
    time.sleep(0.5)
    print("Deleting: C:\\Windows\\System32\\kernel32.dll", end="", flush=True)
    time.sleep(0.3)
    print(" ✓")
    time.sleep(0.2)
    print("Deleting: C:\\Users\\User\\Documents\\fotos.zip", end="", flush=True)
    time.sleep(0.3)
    print(" ✓")
    time.sleep(0.1)
    print("Deleting: C:\\Program Files\\Chrome\\chrome.exe", end="", flush=True)
    time.sleep(0.3)
    print(" ✓")
    time.sleep(0.3)
    print("Deleting: C:\\Windows\\explorer.exe", end="", flush=True)
    time.sleep(0.3)
    print(" ✓")
    time.sleep(0.4)
    print("Deleting: C:\\Users\\User\\Desktop\\wichtig.docx", end="", flush=True)
    time.sleep(0.3)
    print(" ✓")
    print()
    print("❌ 1337 FILES DELETED. SYSTEM CORRUPTED.")
    time.sleep(1)


    os.system("clear")
    print("\033[44m\033[97m", end="")
    print("\n" * 5)
    print("""
            :(

                Dein PC ist auf ein Problem gestoßen und
                muss neu gestartet werden.

                Fehlercode: VIRUS_DETECTED_0x000000FF

                https://totally-not-a-virus.com

                Drücke eine Taste zum Fortfahren... 
         """)
    print("\n" * 10)
    input()
    os.system("clear")
    print("\033[0m", end="")
    print("JUST A PRANK BRO! 😄")
    print()
    print("warte bist du stupit oder was du bist doch dummmmm")
    print()
    print("Spaß!?!?!_.")
    time.sleep(0.3)
    print("SYSTEM CRACHT IT:9978098F898RKUI78:")
    print()
    time.sleep(0.1)
    print("BiS sCH!?uLe B89Y3E")
    print()
    time.sleep(0.2)
    print("897812ujhnc3b7e3")
    time.sleep(0.1)
    print()
    print("CReAtO9R : s0B3HAN")
