#Programme affichage horloge
#Création d'une fenêtre


# L'importation de l’ensemble des éléments du paquet tkinter
import tkinter as tk
# Création d'une fenêtre avec la classe Tk :
fenetre = tk.Tk()
#Titre
fenetre.title("Horloge")
#taille fenetre
fenetre.geometry("576x400")
# Définir un icone :
fenetre.iconbitmap("icone.ico")
#faire image
temp_img = tk.PhotoImage(file="imzge.png")

background_img = temp_img.zoom(1, 1)

can = tk.Canvas(fenetre, width=576, height=309)
can.pack()

can.create_image(200, 150, image=background_img)
# Personnaliser la couleur de l'arrière-plan de la fenêtre principale :
fenetre.config(bg = "#51CAEB")
# Affichage d'un texte
textefenetre= tk.Label(fenetre, text='Bonjour tout le monde !', fg='red')
textefenetre.pack()
#affichage heure
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)
#bouton de fermeture
bouton = tk.Button(fenetre, text='Quitter', command = fenetre.destroy)
bouton.pack()
app=App()

# Affichage de la fenêtre créée :
fenetre.mainloop()
