import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """Génère un mot de passe sécurisé."""
    characters = string.ascii_letters  # Lettres majuscules et minuscules
    
    if use_digits:
        characters += string.digits  # Ajouter les chiffres
    if use_special_chars:
        characters += string.punctuation  # Ajouter les caractères spéciaux
    
    if length < 4:
        raise ValueError("La longueur du mot de passe doit être d'au moins 4 caractères.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()
        password = generate_password(length, use_digits, use_special_chars)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une longueur valide (minimum 4).")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Succès", "Mot de passe copié dans le presse-papiers !")

def reset_fields():
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "12")
    password_entry.delete(0, tk.END)
    digits_var.set(True)
    special_chars_var.set(True)

# Interface graphique
root = tk.Tk()
root.title("Générateur de mots de passe")
root.state('zoomed')  # Ouvrir en plein écran

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centrer les widgets

tk.Label(frame, text="Longueur du mot de passe :", font=("Arial", 14)).grid(row=0, column=0, pady=10)
length_entry = tk.Entry(frame, font=("Arial", 14))
length_entry.grid(row=0, column=1, pady=10)
length_entry.insert(0, "12")

digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)

tk.Checkbutton(frame, text="Inclure des chiffres", variable=digits_var, font=("Arial", 14)).grid(row=1, column=0, columnspan=2, pady=5)
tk.Checkbutton(frame, text="Inclure des caractères spéciaux", variable=special_chars_var, font=("Arial", 14)).grid(row=2, column=0, columnspan=2, pady=5)

tk.Button(frame, text="Générer", command=generate_and_display, font=("Arial", 14)).grid(row=3, column=0, columnspan=2, pady=10)

tk.Button(frame, text="Copier", command=copy_to_clipboard, font=("Arial", 14)).grid(row=4, column=0, pady=10)
tk.Button(frame, text="Réinitialiser", command=reset_fields, font=("Arial", 14)).grid(row=4, column=1, pady=10)

password_entry = tk.Entry(frame, width=30, font=("Arial", 14))
password_entry.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
