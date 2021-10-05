import random
zahl = random.randint(1,100)
durchgang = 0

print("ARRRRRGGHH... Ich bin Kapt'n Hook.\nIch habe mir eine Zahl von 1-100 ausgedacht. Wenn du sie errätst, kriegst du meinen Schatz!\nDu hast nur 6 Versuche sie zu finden!")

while True:
    durchgang = durchgang + 1
    print ()
    print ("Versuch Nummer: " + str(durchgang))

    versuch = int(input("Errate meine Zahl: "))
    if versuch == zahl: 
        print("Du hast meine Zahl erraten! Gut gemacht... der Schatz gehört dir!")
        break

    if versuch < zahl: print("Zu niedrig, du Landratte!")

    if versuch > zahl: print("Zu hoch!")

    if (durchgang == 6):
        print ()
        print ("Game over!")
        print ("Die richtige Zahl war " + str(zahl))
        break