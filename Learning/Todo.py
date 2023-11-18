import customtkinter as ctk

window = ctk.CTk()
window.geometry("800x600")
window.title("To Do Liste")
ctk.set_appearance_mode("dark")


def update_listbox():
        # Clear the listbox
    self.listbox.delete(0, ctk.END)

def button():
    todo = entry.get()
    label = ctk.CTkLabel(scroll, text=todo)
    label.pack()

Label = ctk.CTkLabel(window, text="To Do Liste", font=ctk.CTkFont(size=20, weight="bold"), text_color="blue")
Label.pack(pady="20px")

scroll = ctk.CTkScrollableFrame(window, width=500, height=300)
scroll.pack(pady="20px")

entry = ctk.CTkEntry(scroll, placeholder_text="To Do")
entry.pack()

add_button = ctk.CTkButton(window, text="Add", text_color="black", width=600, fg_color="white", command=button)
add_button.pack()

delete_button = ctk.CTkButton(window, text="Delete", text_color="white", width=600, hover_color="red", fg_color="black")
delete_button.pack(pady="10px")


window.mainloop()