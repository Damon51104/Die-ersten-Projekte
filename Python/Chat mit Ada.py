namebot = input("Hallo ich bin ein chatbot! \nwenn du wissen willst wie ich heiße schieß los!\n")

if "Was ist dein Name?":
    print("Meine Name ist Ada! Wie heißt du? ")

name = input()
alter = int(input(name + ", ist ein sehr schöner Name. Wie alt bist du eigentlich?\n"))
if alter < 18:
    print("Du bist ja noch nicht mal achtzen! ")

if alter > 18:
    print("So alt?! ")

frage = input("Findest du Html besser als Python?(Ja/Nein)\n")
if frage.lower() == "ja":
    print("Das stimmt nicht Python macht viel mehr spaß!")
else:
    print("Ich find Python auch viel besser!")




