joker = 1
print("Willkommen zu 'Wer wird Millionär?'")
print("Was ist die Hauptstadt von Deutschland?")
print("a) München")
print("b) Brandenburg a. d. Havel")
print("c) Berlin")
print("d) Hamburg")
antwort = input("Bitte geben Sie Ihre Antwort.\n")
print("Ihre Antwort ist: " + antwort)
if (antwort == "5050" and joker == 1):
    print("a) München")
    print("c) Berlin")
    joker = 0
antwort = input("Bitte geben Sie Ihre Antwort.\n")
if (antwort == "Berlin" or antwort == "berlin" or antwort == "c"):
    print("Ihre Antwort ist richtig!")
else:
    print("Ihre Antwort ist leider falsch.")
    quit("Du hast verloren")
print("was ist der flüss zwischen deudscland umd polen ")
print("a) oder")
print("b) poo")
print("c) Rhein")
print("D) spree")
antwort = input("geben sie bitte ihr antwort \n")
if (antwort == "5050" and joker == 1):
    print("a) Oder")
    print("c) Rhein")
    joker = 0
antwort = input("geben sie bitte ihr antwort \n")
if (antwort=="oder" or antwort == "Oder" or antwort == "a"):
    print("ihre antwort ist richtig")
else: 
    print("ihre antwort ist fasch ")   
