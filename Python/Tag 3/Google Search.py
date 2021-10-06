import webbrowser

Search = input("Gib 'suche' ein um google zu öffnen.\n")
if Search.lower() == "suche":
    print("Browser wird gestartet!")
    webbrowser.open("https://www.google.de/?hl=de") 

