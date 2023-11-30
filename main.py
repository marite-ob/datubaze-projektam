import sqlite3 as db 
import tkinter as tk
from tkinter import messagebox

with db.connect("lietotajs.db") as con:
    cur = con.cursor()


def izveidot_lietotaju(nikneims, parole):
    cur.execute('INSERT INTO Lietotajs (nikneims, parole) VALUES (?, ?)', (nikneims, parole))
    con.commit()
    con.close()

def parbaudit_lietotaju(nikneims, parole):
    cur.execute('SELECT * FROM Lietotajs WHERE nikneims=? AND parole=?', (nikneims, parole))
    result = cur.fetchone()
    con.close()
    return result is not None

def registracijas_loga_poga():
    nikneims = nikneims_entry.get()
    parole = parole_entry.get()

    if nikneims and parole:
        izveidot_lietotaju(nikneims, parole)
        messagebox.showinfo("Reģistrācija", "Reģistrācija veiksmīga!")
    else:
        messagebox.showwarning("Kļūda", "Lūdzu, aizpildiet visus laukus.")

def pieteikuma_loga_poga():
    nikneims = login_nikneims_entry.get()
    parole = login_parole_entry.get()

    if nikneims and parole:
        if parbaudit_lietotaju(nikneims, parole):
            messagebox.showinfo("Pieteikšanās", "Pieteikšanās veiksmīga! Varat sākt spēli.")
        else:
            messagebox.showwarning("Kļūda", "Nepareizs nikneims vai parole.")
    else:
        messagebox.showwarning("Kļūda", "Lūdzu, aizpildiet visus laukus.")


# Izveidojam galveno logu
logs = tk.Tk()
logs.title("Spēles Logins")

# Reģistrācijas loga izveide
registracijas_loga = tk.Frame(logs)
registracijas_loga.pack(padx=50, pady=10)

tk.Label(registracijas_loga, text="Reģistrācija", font=("Helvetica", 16)).grid(row=0, column=1, pady=10)

tk.Label(registracijas_loga, text="Nikneims:").grid(row=1, column=0, pady=5)
nikneims_entry = tk.Entry(registracijas_loga)
nikneims_entry.grid(row=1, column=1, pady=5)

tk.Label(registracijas_loga, text="Parole:").grid(row=2, column=0, pady=5)
parole_entry = tk.Entry(registracijas_loga, show="*")
parole_entry.grid(row=2, column=1, pady=5)

registracijas_poga = tk.Button(registracijas_loga, text="Reģistrēties", command=registracijas_loga_poga)
registracijas_poga.grid(row=3, column=1, pady=10)

# Pieteikuma loga izveide
pieteikuma_loga = tk.Frame(logs)
pieteikuma_loga.pack(padx=10, pady=10)

tk.Label(pieteikuma_loga, text="Pieteikšanās", font=("Helvetica", 16)).grid(row=0, column=1, pady=10)

tk.Label(pieteikuma_loga, text="Nikneims:").grid(row=1, column=0, pady=5)
login_nikneims_entry = tk.Entry(pieteikuma_loga)
login_nikneims_entry.grid(row=1, column=1, pady=5)

tk.Label(pieteikuma_loga, text="Parole:").grid(row=2, column=0, pady=5)
login_parole_entry = tk.Entry(pieteikuma_loga, show="*")
login_parole_entry.grid(row=2, column=1, pady=5)

pieteikuma_poga = tk.Button(pieteikuma_loga, text="Pieteikties", command=pieteikuma_loga_poga)
pieteikuma_poga.grid(row=3, column=1, pady=10)

# Palaižam logu
logs.mainloop()
  