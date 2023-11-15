import customtkinter as ctk
import random

def genre():
    combobox1 = combobox.get()
    Action = ["MEG2", "Matrix", "Fluch der Karibik", "End Game", "Rush hour", "MIB", "Ghost Rider", "The flash", "Lucy"]

    action_set = set(Action)

    action = list(action_set)

    action_number = len(action) - 1

    action_r = random.randint(0, action_number)

    action_label = ctk.CTkLabel(root, text=action[action_r])
    action_label.pack()

root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.geometry("800x600")
root.title("Auto decision")



title_label = ctk.CTkLabel(root, text="Film Generator", text_color="green", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=50, pady=15)

combobox = ctk.CTkComboBox(root, values=["Action", "Horror", "Romance", "Comedy", "Scifi", "Thriller", "Doku"])
combobox.pack()


generate_button = ctk.CTkButton(root, text="Generate", font=ctk.CTkFont(size= 15, weight="bold"), text_color="green", fg_color="white", hover_color="black", command=genre())
generate_button.pack(pady=25, fill="x")



root.mainloop()