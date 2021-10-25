# -*- coding: utf-8 -*-
 
import cmd
import sys
import time
import random

#Spielerwantworten Definition
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A, B, or C\n") 


# Spielbeginn Einleitung
# TO DOS:
# Story nach update erneuern
# TEXT in verschiedenen Farben(Erzählerfarbe/Spieleingabefarbe/Dialoge),
# BILDER einfügen, 
# MINISPIELE einfügen

def intro():
  Spielername = input() 
  print ("###################################\n WELCOME TO PROTOTYPE TEXTADVENTURE\n###################################")
  time.sleep(1)
  print ("Are you ready?")
  print ("I will be your guide in this realm, and you can command me using (A/B/C or yes/no).")
  print ("Which path shall you take today?")
  time.sleep(1)
  print ("""  A. NEW GAME
  B. INFO
  C. EXIT GAME""")
  choice = input(">>> ") #Erste Auswahl
  if choice in answer_A:
    option_NewGame()
  elif choice in answer_B:
    print ("\nThis is an interactive Textadventure created by Virtual Village GmbH.\nYou can unlock various style minigames by progressing in the story.\nJust type (A/B/C or yes/no) to interact. We wish you a lot of fun! :)"
    "\n")
  elif choice in answer_C:
    Exit_GAME()
  else:
    print (required)
    intro()
    
def option_NewGame(): 
  Spielername = input() 
  print ("\n I wish you luck and hope you will find enjoyment in this adventure game. What is your name?")
  time.sleep(1)
  input() == print ("Hallo");(Spielername) ("What will you do?")
  print ("""  A. Run
  B. Throw another rocka
  C. Run towards a nearby cave""")


def Exit_GAME():
  print ("###################################\n GAME OVER. YOU LOSE!\n###################################")
sys.exit
intro()