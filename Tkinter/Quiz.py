print("IT test von Ergün \n")

print("Welches betriebsystem erstellte Microsoft?")
answer1 = input("Antwort: ")
if answer1 == "Microsoft Windows":
    print("Correct +1 pkt(e) \n")
elif answer1 == "Windows":
    print("Falsch! ITler müssen genau sein! \n"
          "Richtige antwort: Microsoft Windows\n")
else:
    print("Falsch Sorry! \n"
          "Richtige antwort: Microsoft Windows\n")


print("Für was steht BIOS? \n")
answer2 = input("Antwort: ")
if answer2 == "Basic Input Output System":
    print("Correct! +1 pkt(e)\n")
else:
    print("Leider Falsch! \n"
          "Richtige antwort: Basic Input Output System\n")


print("Nenn mir eine IP version!")
answer3 = input("Antwort: ")
if answer3 == "IPv6" or "IPv4":
    print("Richtig Klasse! +1 pkt(e)\n")
else:
    print("Leider Falsch\n"
          "Richtige antwort: IPv6 oder IPv4\n")


print("Wie viel Bit hat eine IPv4-Adresse?")
answer4 = input("Antwort: ")
if answer4 == "32 Bits":
    print("Correct! +1 ptk(e)\n")
elif answer4 == 32:
    print("Nope genau Arbeiten!!!\n"
          "Richtige Antwort: 32 Bits\n")
else:
    print("Leider Nope\n"
          "Richtige Antwort: 32 Bits\n")

print("Nenne mir 4 oder mehr Programmiersprachen!")
answer5 = input("Antwort: ")
liste = answer5.split()
anzahl = len(liste)
if anzahl >= 4:
    print("Schön gemacht! +4 pkt(5)\n")
elif anzahl < 4:
    print("Leider nicht genug \n"
          "Hier sind ein paar: Python, PHP, JavaScript, C#")