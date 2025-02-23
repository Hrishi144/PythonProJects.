import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
from cryptography.fernet import Fernet

def generate_key():
   key=Fernet.generate_key()
   with open("key.key","wb") as key_file:
      key_file.write(key)
def load_key():
    return open("key.key","rb").read()
if not os.path.exists("key.key"):
   generate_key()  


def encrypt_password(password):
   key=load_key()
   cipher=Fernet(key)
   encrypted_password=cipher.encrypt(password.encode())
   return encrypted_password
def decrypt_password(encrypted_password):
   key=load_key()
   cipher=Fernet(key)
   decrypted_password=cipher.decrypt(encrypted_password).decode()
   return decrypted_password

def data_base():
   connection=sqlite3.connect("Passwords.db")
   cursor=connection.cursor()
   
   cursor.execute('''CREATE TABLE IF NOT EXISTS Passwords (
                  ID INTEGER PRIMARY KEY,
                  Website TEXT NOT NULL,
                  Username TEXT NOT NULL,
                  Password TEXT NOT NULL
   )''')
   connection.commit()
   connection.close()

data_base()    


root=tk.Tk()
root.title("PASSWORD MANAGER!")
root.geometry("400x400") 

tk.Label(root,text="Website:").grid(row=0,column=0,padx=10,pady=5,sticky="e")
tk.Label(root,text="Username:").grid(row=1,column=0,padx=10,pady=5,sticky="e")
tk.Label(root,text="Password:").grid(row=2,column=0,padx=10,pady=5,sticky="e")

website_entry=tk.Entry(root,width=30)
website_entry.grid(row=0,column=1,padx=10,pady=5)
username_entry=tk.Entry(root,width=30)
username_entry.grid(row=1,column=1,padx=10,pady=5)
password_entry=tk.Entry(root,width=30)
password_entry.grid(row=2,column=1,padx=10,pady=5)

def save_password():
 website=website_entry.get().strip()
 username=username_entry.get().strip()
 password=password_entry.get().strip()

 if website and username and password:
    encrypted_password=encrypt_password(password)
    connection=sqlite3.connect("Passwords.db")
    cursor=connection.cursor()
    cursor.execute("INSERT INTO Passwords(Website, Username, Password) VALUES (?, ?, ?)",
                   (website, username, encrypted_password))
    connection.commit()
    connection.close()

    messagebox.showinfo("success","Password is saved!")
    website_entry.delete(0,tk.END)
    username_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
 else:
    messagebox.showwarning("Error","All fields are required!")  
def get_password():
    website = website_entry.get().strip()
    username = username_entry.get().strip()

    if not website or not username:
        messagebox.showwarning("Error", "Both Website and Username are required!")
        return

    connection = sqlite3.connect("Passwords.db")
    cursor = connection.cursor()
    cursor.execute("SELECT ID, Password FROM Passwords WHERE Website = ? AND Username = ?", (website, username))
    results = cursor.fetchall()
    connection.close()
    if results:
        output = ""
        for record in results:
            record_id, encrypted_password = record
            if isinstance(encrypted_password, str):
                encrypted_password = encrypted_password.encode()
            decrypted_password = decrypt_password(encrypted_password)
            output += f"ID: {record_id}\nPassword: {decrypted_password}\n\n"
        messagebox.showinfo("Retrieved Data", f"Website: {website}\nUsername: {username}\n\n{output}")
    else:
        messagebox.showwarning("Not Found", "No details found for that website and username!")


save_button=tk.Button(root,text="save password",command=save_password)
save_button.grid(row=3,column=1,pady=10)

retrieve_button=tk.Button(root,text="Retrieve password",command=get_password)
retrieve_button.grid(row=4,column=1,pady=5)

root.mainloop()
