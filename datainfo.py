import os 
from rich import print 



def Steghide():
    print("[green] Datei Angeben: ........")
    Datei = input()
    steghide_scan1 = os.system(f"steghide extract -sf {Datei}")

#############

    
def zsteg():
    print("[green] Datei Angeben: ........")
    Datei = input()
    zsteg_scan1 = os.system(f"zsteg -a {Datei}")
    
#############

def stegcracker():
    print("[green] Datei Angeben: ........")
    Datei = input()
    Liste = "PUT/HERE/YOUR/WORDLIST......../Hacking/rockyou.txt"
    stegcracker_brute = os.system(f"stegcracker {Datei} {Liste}")
    
#############

def exiftool():
    print("[green] Datei Angeben: ........")
    Datei = input()
    exiftool_scan1 = os.systme(f"exiftool {Datei}")
    
    
def BinWalk():
    print("[green] Datei Angeben: ........")
    Datei = input()
    binwalk_scan1 = os.system(f"binwalk {Datei}")
    
    

def Menu_Anzeigen():
    print("\nMenü:")
    print("1. Steghide ")
    print("2. Zsteg")
    print("3. Stegcracker")
    print("4. Exiftool")
    print("5. BinWalk")
    print("exit/EXIT. Programm beenden")

# Hauptprogramm
while True:
    Menu_Anzeigen()

    try:
        choice = int(input("Bitte wählen Sie eine Option: "))

        if choice == 1:
            Steghide()
        elif choice == 2:
            zsteg()
        elif choice == 3:
            stegcracker()
        elif choice == 4:
            exiftool()
        elif choice == 5:
            BinWalk()
        else:
            print("Ungültige Option. Bitte erneut versuchen.")

    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")