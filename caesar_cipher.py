import customtkinter as ctk

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def perform_encryption():
    message = message_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = encrypt(message, shift)
    result_var.set(encrypted_message)

def perform_decryption():
    message = message_entry.get()
    shift = int(shift_entry.get())
    decrypted_message = decrypt(message, shift)
    result_var.set(decrypted_message)

# Initialize the CustomTkinter application
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()  # Use CTk() instead of Tk()
root.title("Caesar Cipher")

ctk.CTkLabel(root, text="Message:").grid(row=0, column=0)
message_entry = ctk.CTkEntry(root)
message_entry.grid(row=0, column=1)

ctk.CTkLabel(root, text="Shift:").grid(row=1, column=0)
shift_entry = ctk.CTkEntry(root)
shift_entry.grid(row=1, column=1)

encrypt_button = ctk.CTkButton(root, text="Encrypt", command=perform_encryption)
encrypt_button.grid(row=2, column=0)

decrypt_button = ctk.CTkButton(root, text="Decrypt", command=perform_decryption)
decrypt_button.grid(row=2, column=1)

result_var = ctk.StringVar()
ctk.CTkLabel(root, text="Result:").grid(row=3, column=0)
result_label = ctk.CTkLabel(root, textvariable=result_var)
result_label.grid(row=3, column=1)

root.mainloop()
