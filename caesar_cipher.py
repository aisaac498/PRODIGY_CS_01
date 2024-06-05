import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, Text
from PIL import Image, ImageTk

# Function to toggle between light and dark mode
def toggle_mode(event=None):
    global is_dark_mode
    if is_dark_mode:
        ctk.set_appearance_mode("Light")
        icon_label.config(image=sun_img)
        set_theme_colors(light_mode=True)
    else:
        ctk.set_appearance_mode("Dark")
        icon_label.config(image=moon_img)
        set_theme_colors(light_mode=False)
    is_dark_mode = not is_dark_mode

# Function to set the theme colors
def set_theme_colors(light_mode):
    bg_color = "#ffffff" if light_mode else "#2A2D2E"
    fg_color = "#000000" if light_mode else "#ffffff"
    result_text.config(bg=bg_color, fg=fg_color)

# Function to encrypt text using Caesar Cipher
def encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Function to decrypt text using Caesar Cipher (by shifting in the opposite direction)
def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)

# Function to handle encryption button click
def perform_encryption() -> None:
    try:
        message = message_entry.get()
        shift = int(shift_entry.get())
        encrypted_message = encrypt(message, shift)
        result_text.config(state='normal')
        result_text.delete(1.0, 'end')
        result_text.insert('end', encrypted_message)
        result_text.config(state='disabled')
    except ValueError:
        messagebox.showerror("Input Error", "Please insert a shift value")

# Function to handle decryption button click
def perform_decryption() -> None:
    try:
        message = message_entry.get()
        shift = int(shift_entry.get())
        decrypted_message = decrypt(message, shift)
        result_text.config(state='normal')
        result_text.delete(1.0, 'end')
        result_text.insert('end', decrypted_message)
        result_text.config(state='disabled')
    except ValueError:
        messagebox.showerror("Input Error", "Please insert a shift value")

# Function to copy the result to the clipboard
def copy_result() -> None:
    root.clipboard_clear()
    root.clipboard_append(result_text.get(1.0, 'end').strip())
    messagebox.showinfo("Copied", "Result copied to clipboard")

# Function to paste text from the clipboard into the message entry widget
def paste_message() -> None:
    try:
        clipboard_content = root.clipboard_get()
        message_entry.delete(0, 'end')
        message_entry.insert(0, clipboard_content)
    except:
        messagebox.showerror("Clipboard Error", "No text in clipboard to paste")

# Function to set up the GUI
def setup_gui():
    # Set appearance and theme of the CustomTkinter application
    ctk.set_appearance_mode("System")  # Set appearance mode (System, Dark, Light)
    ctk.set_default_color_theme("blue")  # Set the color theme

    global root
    root = ctk.CTk()  # Initialize the main window
    root.title("Caesar Cipher")
    root.geometry("500x600")  # Set the window size

    # Create a main frame to hold all widgets
    main_frame = ctk.CTkFrame(root, width=480, height=580)
    main_frame.place(relx=0.5, rely=0.5, anchor='center')
    main_frame.pack_propagate(False)  # Prevent frame from resizing to fit its content

    # Manually set a matching background color for the Text widget
    bg_color = "#2A2D2E"  # Example dark color to match a typical CustomTkinter theme

    # Light/Dark mode toggle image inside main_frame
    global icon_label, is_dark_mode, moon_img, sun_img
    moon_img = ImageTk.PhotoImage(Image.open("images/moon.png"))
    sun_img = ImageTk.PhotoImage(Image.open("images/sun.png"))
    is_dark_mode = True
    icon_label = tk.Label(main_frame, image=moon_img, cursor="hand2")
    icon_label.pack(pady=10, anchor='ne')
    icon_label.bind("<Button-1>", toggle_mode)  # Bind left mouse click to toggle_mode function

    # Message input
    ctk.CTkLabel(main_frame, text="Message:").pack(pady=5)
    global message_entry
    message_entry = ctk.CTkEntry(main_frame)
    message_entry.pack(pady=5)

    # Paste button to paste from clipboard
    paste_button = ctk.CTkButton(main_frame, text="Paste", command=paste_message, width=100)
    paste_button.pack(pady=5)

    # Shift input
    ctk.CTkLabel(main_frame, text="Shift:").pack(pady=5)
    global shift_entry
    shift_entry = ctk.CTkEntry(main_frame)
    shift_entry.pack(pady=5)

    # Frame to hold Encrypt and Decrypt buttons
    button_frame = ctk.CTkFrame(main_frame)
    button_frame.pack(pady=10)

    # Encrypt button
    encrypt_button = ctk.CTkButton(button_frame, text="Encrypt", command=perform_encryption, width=100)
    encrypt_button.pack(side='left', padx=5, pady=5)

    # Decrypt button
    decrypt_button = ctk.CTkButton(button_frame, text="Decrypt", command=perform_decryption, width=100)
    decrypt_button.pack(side='left', padx=5, pady=5)

    # Result display area
    ctk.CTkLabel(main_frame, text="Result:").pack(pady=5)
    global result_text
    result_text = Text(main_frame, wrap='word', height=5, width=45, bg=bg_color, fg="white", bd=0)
    result_text.pack(pady=5, padx=5)
    result_text.config(state='disabled')  # Make the Text widget read-only
    
    # Copy button to copy the result to clipboard
    copy_button = ctk.CTkButton(main_frame, text="Copy", command=copy_result, width=100)
    copy_button.pack(pady=10)

    root.mainloop()  # Start the GUI event loop

# Run the GUI setup
if __name__ == "__main__":
    setup_gui()
