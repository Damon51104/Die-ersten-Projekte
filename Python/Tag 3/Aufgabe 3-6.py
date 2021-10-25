import webbrowser
import time

Pause = 0

print("Der Arbeitstag geht los nach 90 minuten gibts Pause!")

while Pause < 5: #Hier kannst du einstellen wie oft du Pause machst! (5 * 90min) oder auch sowas wie (10 * 45min)
    time.sleep(5400) #Hier kannst du die Lernzeit in sekunden ändern! (90min * 60sek) oder auch sowas wie (45min * 60sek)
    
    print("Gönn dir deine Pause!")
    
    webbrowser.open("https://www.youtube.com/watch?v=MxgsrPFsWzg&ab_channel=scroll忍")
    time.sleep(92)

    webbrowser.open("https://www.youtube.com/watch?v=5o2TeJ211Zc&list=RDMM&start_radio=1&rv=WJrXKhbE3Hg&ab_channel=NightLovell")
    time.sleep(140)

    webbrowser.open("https://www.youtube.com/watch?v=0xJe-6bH724&list=RDMM&index=14&ab_channel=scroll忍")
    time.sleep(137)

    Pause += 1
    time.sleep(2)
    print()
    print("Ran an die Arbeit die " + str(Pause) + " Pause ist schon vorbei!")

    time.sleep(2)
    Game = input ("Oder möchtest du noch eine runde Zahlenraten spielen? (Ja/Nein)\n")
    if Game.lower() == "ja":
        time.sleep(2)
        def main():
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
                    print ("Warm-up ist vorbei jetzt aber ran an die Arbeit!")
                    break
        main()

    if Game.lower() == "nein":
        print("Okay aber dan schnell wieder an die Arbeit!\n")

print("Arbeitstag ist vorbei ab in das Meeting!")

#zum testen hier die musik copy and pasten!