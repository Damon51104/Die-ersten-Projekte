# -*- coding: utf-8 -*-
 
import cmd
from os import pipe
import sys
import time
import random
import re
from typing import Text, TextIO
import webbrowser

#Spielerwantworten Definition
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A, B, C, or D\n") 

#Reguliert die Textfarben
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\014[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Spielbeginn Einleitung
# TO DOS:
# Story nach Update erneuern
# TEXT in verschiedenen Farben(Erzählerfarbe/Spieleingabefarbe/Dialoge),
# BILDER einfügen, 
# MINISPIELE einfügen

# Spielt Music ab
url = 'https://youtu.be/A8qMyBWZNw0'
webbrowser.open(url)

def intro():
  
  


  print(f"""{bcolors. GREEN}
##########################################################
.  .   .  ..--. .--. .   .--.    .--. .   ..---..-.---.
 \  \ /  /:    :|   )|   |   :  :    :|   ||   (   )|  
  \  \  / |    ||--' |   |   |  |    ||   ||--- `-. |  
   \/ \/  :    ;|  \ |   |   ;  :  ( ;:   ;|   (   )|  
    ' '    `--' '   `'---'--'    `--`- `-' '---'`-' '  
                      .:'
                  _.::'
        .-;;-.   (_.'
       / ;;;' 
      |.  `:   | 
       \:   `;/
        '-..-'

              - created by Virtual Village GmbH (2021)
##########################################################

    """)

  time.sleep(1)
  text = (f"{bcolors. RED}Welcome to WORLD QUEST. Type (A/B/C or D) on your keyboard to play this game.\nWhich path will you take today?\n")
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)
  time.sleep(1)
  print ("""
  A. START A NEW ADVENTURE
  B. ABOUT US
  C. PLAY MINIGAMES
  D. EXIT """)
  choice = input(">>> ") #ERSTE AUSWAHL
  if choice in answer_A:
    option_NewGame()
  elif choice in answer_B:
    
    text = ("""
 This is an interactive retro textadventure game created by Virtual Village GmbH in 2021.
 You can unlock various style minigames by progressing in the story.
 Just type (A/B/C/ or D) on your keyboard to play and win.

      Loading graphics....
      
                          ,d88b.d88b,
                          88888888888
                          `Y8888888Y'
                            `Y888Y'    
                              `Y'
     
     Our development team wishes you a lot of fun! =)

    """)
    for char in text:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.01)
    time.sleep(2)



    print ("""

    A. BACK TO TITLE SCREEN
    B. EXIT """)
    choice = input(">>> ")
    if choice in answer_A:
      intro()
    elif choice in answer_B:
      Exit_GAME2()
    else:
      print (required)
      intro()

  elif choice in answer_C:
    Auswahl_MiniGame()
  elif choice in answer_D:
    Exit_GAME2()
  else:
    print (required)
    intro()
    
def option_NewGame(): 
  text = ("Please enter your name:\n")
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  time.sleep(1)
  Spielername = input (">>> ")
  print = ("Hello ", Spielername , " may your journey be safe & successful!")

  text = ("""
Prolog:
You are an experienced world traveller on a mission to find THE SACRED CORE,
a core which has the power to save the people on your planet from an imminent environmental disaster.""")
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  time.sleep(1)
  erster_decision_tree()


def erster_decision_tree():  # ERSTER DECISION TREEE STORY
  text = ("""

You say goodbye to your loved ones and friends and set off to your journey by stepping through a magical portal.
Which portal do you go through?
    """)
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  time.sleep(1)
  print ("""  


           .-;+$XHHHHHHX$+;-.     		   -;+$XHHHHHHX$+;-.                            
        ,;X@@X%/;=----=:/%X@@X/, 	        ,;X@@X%/;=----=:/%X@@X			   .
      =$@@%=.              .=+H@X:             =$@@%=.              .=+H@X:		 .
    -XMX:                      =XMX=          XMX:                      =XMX=
   /@@:                          =H@+       /@@:                          =H@+
  %@X,                            .$@$      %@X,                            .$@$
 +@X.                               $@%    +@X.                               $@%
-@@,                                .@@=-  @@,                                .@@=
%@%                                  +@$%  @%                                  +@$
H@:                                  :@H   H@:                                  :@H
H@:         :HHHHHHHHHHHHHHHHHHX,    =@H   H@:         :HHHHHHHHHHHHHHHHHHX,    =@H
%@%         ;@M@@@@@@@@@@@@@@@@@H-   +@$   %@%         ;@M@@@@@@@@@@@@@@@@@H-   +@$
=@@,        :@@@@@@@@@@@@@@@@@@@@@= .@@:   =@@,        :@@@@@@@@@@@@@@@@@@@@@= .@@:
 +@X        :@@@@@@@@@@@@@@@M@@@@@@:%@%    +@X        :@@@@@@@@@@@@@@@M@@@@@@:%@%
  $@$,      ;@@@@@@@@@@@@@@@@@M@@@@@@$.     $@$,      ;@@@@@@@@@@@@@@@@@M@@@@@@$.
   +@@HHHHHHH@@@@@@@@@@@@@@@@@@@@@@@+       +@@HHHHHHH@@@@@@@@@@@@@@@@@@@@@@@+
    =X@@@@@@@@@@@@@@@@@@@@@@@@@@@@X=           =X@@@@@@@@@@@@@@@@@@@@@@@@@@@@X=
      :$@@@@@@@@@@@@@@@@@@@M@@@@$:               :$@@@@@@@@@@@@@@@@@@@M@@@@$:
        ,;$@@@@@@@@@@@@@@@@@@X/-                   ,;$@@@@@@@@@@@@@@@@@@X/-
          
  A. Take the portal to your left
  B. Take the portal to your right
  C. Never leave your homeworld and stay """)
  choice = input(">>> ")
  
  if choice in answer_A:
    option_left_portal()

  elif choice in answer_B:
      option_right_portal()

  elif choice in answer_C:
    stay_homeplanet()

  else:
    print (required)
    erster_decision_tree()

def option_left_portal():
  text = ("""
You step through the left portal and discover yourself in a new world:""")
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  print (""" 

        _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /\'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \\
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._ """)
  time.sleep(2)
  text = ("""This world seems beautiful! You think.
During your search for the core, you see different landscapes — snow-clad mountains, meadows of flowers,
animals of various shapes and sizes and the colourful life inside water bodies """)
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  time.sleep(0.3)
  text = ("""

You became curious about the artist who has made this delightful chaos. 
Who is the magical painter who has created this incredible earth? You ask yourself.
And you realize, it is more complicated than you think and not easy to find the core....

""")
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  
  print ("""
  
                      .     :     .
           _           '. _.:._ .'
          (_)       '-. .'     '. .-'
          _;_     ' - ./         \. - ' 
         / | \    - - |           | - -
    ---- \ |  \ ------------------------------
.---.--.   .--..---.   .--..--. .   .---.--.--.   ..   ..---..--. 
  |:    :  |   )      :   :    :|\  | |    |  |\  ||   ||    |   :
  ||    |  |--:|---   |   |    || \ | |    |  | \ ||   ||--- |   |
  |:    ;  |   )      :   :    ;|  \| |    |  |  \|:   ;|    |   ;
  ' `--'   '--''---'   `--'`--' '   ' '  --'--'   ' `-' '---''--' 

""")
  time.sleep (2)
  print ("""
  #######################################################################                            

.---.   .   .    .   .   .-.   .---. .--. .--.   .--..       .  .   .--.--.   . .--..
  | |   |  / \   |\  |  (   )  |    :    :|   )  |   )      / \  \ /   |  |\  |:    |
  | |---| /___\  | \ |-' `-.   |--- |    ||--'   |--'|     /___\  :    |  | \ || --.|
  | |   |/     \ |  \|  (   )  |    :    ;|  \   |   |    /     \ |    |  |  \|:   |'
  ' '   '       `'   '   `-'   '     `--' '   `  '   '---'       `'  --'--'   ' `--'o
                               ( )_____( )
                                / O   O \\
                               |   (@)   |
                               \    ~    /  
                                \ <}*{> /   
                              ___/  ___  \___
                            ()___ /   \ ___()
                                ( \___/ )
                                /_ /   \ _\\
                              (__)     (__)                                                                                        
                                                                                     
                                        
######################################################################

  """)




def option_right_portal():
  text = ("""

  Planet X
    """)
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)


def stay_homeplanet():
  text = ("""
  You change your mind at the last moment. 
  At first, you are ashamed to return so soon after saying goodbye,
  but your loved ones are happy that you are staying with them and welcome you back with open arms...
  """)
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  

  text = ("""
      O      O
     <|\     /|\\
      |   ~o/ | \o    ~o/    _o
      |\  /|  |\ |\   /|      |\\
     / |  / \ |// >   / \    / >
    
    Ten years later…""")
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  time.sleep (3)

  text = ("""
    You are about to eat soemethin when suddenly you hear a loud scream in the distance....
    You go out to look at the night and stare at the sky in horror… The air is burning, the sun has disappeared, and it is raining blood? 
   """)
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)  
  print ("""

               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  """)
  text = ("""
  The earth suddenly trembles, people scream around you. 
  You are about to turn around to look for your family, when a crack opens up under your feet… 
  Before you can react, the earth swallows you up.


         /     \   / \\
         ) ,-==-> /\/ \\
          )__\\/ // \  |
         /  /' \//   | |
        /  (  /|/    | /
       /     //|    /,'
      // /  (( )    '
     //     // \    |
    //     (#) |
   /        )\/ \   '       ____
  /        /#/   )         /,.__\__,,--=_,
 /         \#\  /)      __/ + \____,--==<
 //gnv_____/#/_/'      (\_\__+/_,   ---<^
                                '==--=='

   """)
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  
  text = ("You were the chosen one” were the last whimpering words you heard until your voice died of pain, and you only saw eternal darkness…")
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  time.sleep (3)
  Exit_GAME()




def Auswahl_MiniGame(): # Auswahlmenü für Minigames
  text = ("""
Which minigame do you want to play?
""")
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  time.sleep(1)
  print ("""  
  A. PIRATES NUMBER GAME
  B. HANGMAN
  C. UNO CARDGAME
  D. BACK TO MAINMENU
  """)
  choice = input(">>> ")


  if choice in answer_A:
    Pirate_MiniGame()

  elif choice in answer_B:
      Hangman_MiniGame()

  elif choice in answer_C:
    Uno_MiniGame()

  elif choice in answer_D:
    intro()
  else:
    print (required)
    Auswahl_MiniGame()



def Pirate_MiniGame(): # Code für Zahlenratenminispiel
  Counter = 0
  GesuchteZahl = random.randint(1,100)
  print ("""
                   _____                                             
              .-" .-. "-.                                          
            _/ '=(0.0)=' \_                                        
          /`   .='|m|'=.   `\                                      
          \________________ /                                      
      .--.__///`'-,__~\\\\~`    WELCOME TO THE PIRATE NUMBER GUESSING GAME!        
     / /6|__\// a (__)-\\\\      
     \ \/--`((   ._\   ,)))                                        
     /  \\  ))\  -==-  (O)(                                        
    /    )\((((\   .  /)))))                                       
   /  _.' /  __(`~~~~`)__                                          
  //"\\,-'-"`   `~~~~\\~~`"-.                                      
 //  /`"              `      `\                                    
//
  """)

  time.sleep (2)
  text = ("""
Start guessing a number between 1 and 100 by typing a number on your keyboard.
You have up to 5 failing attemps.
    """)
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
  time.sleep(1)


  while Counter < 6:
    Spielerantwort = int(input("Which number do you guess? , Arrrr!\n"))

    
    Counter = Counter + 1
    print ("Failed attempts: ",Counter)

    if Spielerantwort == GesuchteZahl:
        print("""
                                                                                   
.---.   .                             .                             .      .              .
  |     |                            _|_                            |     / \             |
  |.-.  |.-. .-.   .  ..-..  . .--.   | .--.-. .-.  .--..  . .--.-. |    /___\  .--.--.--.|
  (   ) |-.'(.-'   |  (   )  | |      | | (.-'(   ) `--.|  | | (.-' '   /     \ |  |  |   '
  '`-'`-'  `-`--'  `--|`-'`--`-'      `-'  `--'`-'`-`--'`--`-'  `--'o  '       `'  '  '   o
                      ;                                                                    
                   `-'                                                                          
                              __________
                            /\____;;___\
                          | /         /
                          `. ())oo() .
                            |\(%()*^^()^\
                           %| |-%-------|+
                          % \ | %  ))   |
                          %  \|%________|
            
            """)
        time.sleep (3)
        print("""Back to GAME MENU?
          
          A. Yes
          B. No
          C. Exit
          D. Play again
          """)
        choice = input(">>> ")
          
        if choice in answer_A:
         intro()

        elif choice in answer_B:
         Exit_GAME2()

        elif choice in answer_C:
          Exit_GAME2()

        elif choice in answer_D:
          Pirate_MiniGame()
          
        else:
          print (required)
          Pirate_MiniGame()

    if Spielerantwort < GesuchteZahl:
        print ("Too low, you landlubber!\n")

    if Spielerantwort > GesuchteZahl:
        print ("Too high! Guess again!\n")

  
  print ("""
################################################        
 .--.   .    .    .---.   .--..       .---..--. 
:      / \   |\  /|      :    :\     /|    |   )
| --. /___\  | \/ |---   |    | \   / |--- |--' 
:   |/     \ |    |      :    ;  \ /  |    |  \ 
 `--'       `'    '---'   `--'    '   '---''   `

    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                                               
.---.--.   .      .    .--.   .    --.--.   .  .
  | |   ) /      / \  :      / \     |  |\  |  |
  | |--' :      /___\ | --. /___\    |  | \ |  |
  | |  \ |     /     \:   |/     \   |  |  \|  '
  ' '   `'    '       ``--'       `--'--'   '  o
  
################################################ """)
  time.sleep (2)
  print("""Back to GAME MENU?

      A. Yes
      B. No
      C. Exit
      D. Play again
      """)
  choice = input(">>> ")
      
  if choice in answer_A:
    intro()

  elif choice in answer_B:
    Exit_GAME2() 

  elif choice in answer_C:
    Exit_GAME2()

  elif choice in answer_D:
    Pirate_MiniGame()
      
  else:
    print (required)
    Pirate_MiniGame()





def Hangman_MiniGame():  # Code für Hangmanminispiel
   import random
   import time
   
   print("""

    Welcome to:
     _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___                                   
.   .   .    .   . .--..    .   .    .   .
|   |  / \   |\  |:    |\  /|  / \   |\  |
|---| /___\  | \ || --.| \/ | /___\  | \ |
|   |/     \ |  \|:   ||    |/     \ |  \|
'   '       `'   ' `--''    '       `'   '                                    
   """)
   time.sleep (2)
   text = ("""
  
   Start guessing the letters or word to save this poor fellow above frome hanging.
   Just type the letters you guess on your keyboard.
   You have up to 5 failing attemps.
    """)
   for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
   time.sleep(1)


   list = ["joblinge", "python", "coding", "minigame", "azubidigital", "virtualvillage"]

   strichWort = []

   for wort in list:
    wrongLetter = 0
    strichWort = []
    for i in wort:
        strichWort.append("_")
    print()
    print("Word to be guessed:")
    for w in strichWort:
        print(w, end=" ")
    print()

    while True:
        if wrongLetter > 5:
            print("Game over!")
            Exit_GAME()
            time.sleep (3)
            print("""Back to GAME MENU?
            
            A. Yes
            B. No
            C. Exit
            """)
            choice = input(">>> ")
            
            if choice in answer_A:
               intro()

            elif choice in answer_B:
               break

            elif choice in answer_C:
               break
               Exit_GAME2()
               
            else:
              print (required)
              Auswahl_MiniGame()


        print("Failed attempts: " + str(wrongLetter))

        isSolved = False
        for j in strichWort:
            if j != "_":
                isSolved = True
            if j == "_":
                isSolved = False
                break
        if isSolved:
            print("""
                                                                               
                                                                                
 .--..--. .   . .--..--.     .  .---.   ..       .  .---.--.-- .--. .   ..-.   .
:   :    :|\  |:    |   )   / \   | |   ||      / \   |    |  :    :|\  (   )  |
|   |    || \ || --.|--'   /___\  | |   ||     /___\  |    |  |    || \ |`-.   |
:   :    ;|  \|:   ||  \  /     \ | :   ;|    /     \ |    |  :    ;|  \(   )  '
 `--'`--' '   ' `--''   `'       `'  `-' '---'       `'  --'-- `--' '   '`-'   o                                               
                                You saved him!!!
                                        
                                       \_Q_/
                                         I
                                        /T\   
                                        \|/    
                                    ____=0=____
            
            """)
            time.sleep (3)
            print("""Back to GAME MENU?
            
            A. Yes
            B. No
            C. Exit
            """)
            choice = input(">>> ")
            
            if choice in answer_A:
               intro()

            elif choice in answer_B:
               break

            elif choice in answer_C:
               Exit_GAME2()
               break
            else:
              print (required)
              Auswahl_MiniGame()
            

        letter = input("Which letter do you guess?: ")
        num = 0
        isSolved = False
        for i in wort:
            if i == letter:
                strichWort[num] = letter
                isSolved = True

            num = num + 1
        if not isSolved:
            wrongLetter = wrongLetter + 1

        for w in strichWort:
            print(w, end=" ")
        print()


          
def Uno_MiniGame(): # Code für Uno Kartenspiel
 print ("Uno!")


def Tobeconintinued():
  print = ("""
#######################################################################                            
.---.--.   .--..---.   .--..--. .   .---.--.--.   ..   ..---..--. 
  |:    :  |   )      :   :    :|\  | |    |  |\  ||   ||    |   :
  ||    |  |--:|---   |   |    || \ | |    |  | \ ||   ||--- |   |
  |:    ;  |   )      :   :    ;|  \| |    |  |  \|:   ;|    |   ;
  ' `--'   '--''---'   `--'`--' '   ' '  --'--'   ' `-' '---''--' 
.---.   .   .    .   .   .-.   .---. .--. .--.   .--..       .  .   .--.--.   . .--..
  | |   |  / \   |\  |  (   )  |    :    :|   )  |   )      / \  \ /   |  |\  |:    |
  | |---| /___\  | \ |-' `-.   |--- |    ||--'   |--'|     /___\  :    |  | \ || --.|
  | |   |/     \ |  \|  (   )  |    :    ;|  \   |   |    /     \ |    |  |  \|:   |'
  ' '   '       `'   '   `-'   '     `--' '   `  '   '---'       `'  --'--'   ' `--'o
                               ( )_____( )
                                / O   O \\
                               |   (@)   |
                               \    ~    /  
                                \ <}*{> /   
                              ___/  ___  \___
                            ()___ /   \ ___()
                                ( \___/ )
                                /_ /   \ _\\
                              (__)     (__)                                                                                        
                                                                                     
                                        
######################################################################    
  """)

  sys.exit


def Exit_GAME():
  print ("""
################################################        
 .--.   .    .    .---.   .--..       .---..--. 
:      / \   |\  /|      :    :\     /|    |   )
| --. /___\  | \/ |---   |    | \   / |--- |--' 
:   |/     \ |    |      :    ;  \ /  |    |  \ 
 `--'       `'    '---'   `--'    '   '---''   `

    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                                               
.---.--.   .      .    .--.   .    --.--.   .  .
  | |   ) /      / \  :      / \     |  |\  |  |
  | |--' :      /___\ | --. /___\    |  | \ |  |
  | |  \ |     /     \:   |/     \   |  |  \|  '
  ' '   `'    '       ``--'       `--'--'   '  o
  
################################################ """)
  time.sleep (3)
  print("""Back to GAME MENU?

      A. Yes
      B. No
      C. Exit
      D. Play again
      """)
  choice = input(">>> ")
      
  if choice in answer_A:
    intro()

  elif choice in answer_B:
    Exit_GAME2() 

  elif choice in answer_C:
    Exit_GAME2()

  elif choice in answer_D:
    intro()
      
  else:
    print (required)
    intro()


def Exit_GAME2():
  print ("""
#######################################################################     
.---.              .           .-.            .                        
  | |              |           |              |            o           
  | |--. .-.  .--. |.-. .--.  -|-.-..--.  .,-.| .-.  .  .  .  .--. .-..
  | |  |(   ) |  | |-.' `--.   |(   )     |   )(   ) |  |  |  |  |(   |
  ' '  `-`-'`-'  `-'  `-`--'   ' `-''     |`-'`-`-'`-`--|-' `-'  `-`-`|
                                          |             ;          ._.'
                      ( )_____( )
                       / O   O \\
                      |   (@)   |
                      \    ~    /  
                       \ <}*{> /   
                    ___/  ___  \___
                   ()___ /   \ ___()
                       ( \___/ )
                      /_ /   \ _\\
                     (__)     (__)                 
######################################################################## """)
sys.exit


intro()
