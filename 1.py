import tkinter as tk
from tkinter import messagebox
import mysql.connector

def insert_data():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    wiek = entry_wiek.get()

    if imie and nazwisko and wiek:
        try:
            wiek = int(wiek)
            conn = mysql.connector.connect(
                host='172.26.178.39',
                user='adam',
                password='adam',
                database='ZZ'
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO osoby (imie, nazwisko, wiek) VALUES (%s, %s, %s)", (imie, nazwisko, wiek))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sukces", "Dane zostały wprowadzone pomyślnie.")
            entry_imie.delete(0, tk.END)
            entry_nazwisko.delete(0, tk.END)
            entry_wiek.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Błąd", "Wiek musi być liczbą całkowitą.")
        except mysql.connector.Error as err:
            messagebox.showerror("Błąd", f"Błąd połączenia z bazą danych: {err}")
    else:
        messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione.")

root = tk.Tk()
root.title("Wprowadzanie danych")

tk.Label(root, text="Imię:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Nazwisko:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Wiek:").grid(row=2, column=0, padx=10, pady=5)

entry_imie = tk.Entry(root)
entry_imie.grid(row=0, column=1, padx=10, pady=5)
entry_nazwisko = tk.Entry(root)
entry_nazwisko.grid(row=1, column=1, padx=10, pady=5)
entry_wiek = tk.Entry(root)
entry_wiek.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Wprowadź", command=insert_data).grid(row=3, columnspan=2, pady=10)

root.mainloop()
