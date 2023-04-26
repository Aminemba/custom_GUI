import customtkinter as cs

cs.set_appearance_mode("dark")
cs.set_default_color_theme("dark-blue")

root = cs.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = cs.CTkFrame(master=root)
frame.pack()

label = cs.CTkLabel(master=frame,text ='Login System' )
label.pack(pady=12,padx=10)

entry1 = cs.CTkEntry(master=frame,placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2 = cs.CTkEntry(master=frame , placeholder_text="Password" , show="*")
entry2.pack(pady=12,padx=10)

button = cs.CTkButton(master=frame,text="Login" , command=login)
button.pack(pady=12 ,padx=10)

checkbox =cs.CTkCheckBox(master=frame ,text="Remember Me")
checkbox.pack(pady=12 ,padx=10)

root.mainloop()
