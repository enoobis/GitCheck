import requests
import tkinter as tk
from tkinter import ttk

def check_github_username(username):
    url = f'https://github.com/{username}'
    response = requests.get(url)
    if response.status_code == 404:
        return f'The username "{username}" is available on GitHub!'
    else:
        return f'The username "{username}" is already taken on GitHub.'

def check_username():
    username = username_entry.get()
    result = check_github_username(username)
    result_label.config(text=result)

# Set up the main window
root = tk.Tk()
root.title("Check GitHub Username Availability")
root.geometry("820x820")
root.configure(bg="#0D1117")

# Set up the username entry and label
username_label = ttk.Label(root, text="Enter a GitHub username:", foreground="#C9D1D9", background="#0D1117", font=("Arial", 14))
username_label.pack(pady=(20, 5))
username_entry = ttk.Entry(root, font=("Arial", 14))
username_entry.pack(pady=5)

# Set up the check button
check_button = ttk.Button(root, text="Check", command=check_username)
check_button.pack(pady=(5, 20))

# Set up the result label
result_label = ttk.Label(root, foreground="#C9D1D9", background="#0D1117", font=("Arial", 14))
result_label.pack()

# Run the main event loop
root.mainloop()