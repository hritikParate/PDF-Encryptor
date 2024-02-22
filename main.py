import tkinter as tk
from tkinter import ttk, filedialog
import pikepdf

def encrypt_pdf():
    file_path = file_path_var.get()
    owner = owner_var.get()
    password = password_var.get()
    save_path = save_path_var.get()

    try:
        old_pdf = pikepdf.Pdf.open(file_path)
        no_extr = pikepdf.Permissions(extract=False)
        old_pdf.save(save_path,
                     encryption=pikepdf.Encryption(
                         user=password,
                         owner=owner,
                         allow=no_extr
                     ))
        result_label.config(text="PDF encrypted successfully!", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    file_path_var.set(file_path)

def browse_save_path():
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    save_path_var.set(save_path)

# Create GUI
root = tk.Tk()
root.title("PDF Encryption Tool")

file_path_var = tk.StringVar()
owner_var = tk.StringVar()
password_var = tk.StringVar()
save_path_var = tk.StringVar()

# Style
style = ttk.Style()
style.configure("TButton", padding=6)
style.configure("TEntry", padding=6, relief="solid")

# Adding some padding and margin for a cleaner look
frame = ttk.Frame(root, padding=(20, 10))
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# File Path
tk.Label(frame, text="PDF File Path:").grid(row=0, column=0, pady=5, sticky=tk.W)
tk.Entry(frame, textvariable=file_path_var, width=40).grid(row=0, column=1, pady=5, padx=5)
tk.Button(frame, text="Browse", command=browse_file).grid(row=0, column=2, pady=5, padx=5)

# Owner
tk.Label(frame, text="Owner:").grid(row=1, column=0, pady=5, sticky=tk.W)
tk.Entry(frame, textvariable=owner_var, width=40).grid(row=1, column=1, pady=5, padx=5)

# Password
tk.Label(frame, text="Password:").grid(row=2, column=0, pady=5, sticky=tk.W)
tk.Entry(frame, textvariable=password_var, show="*", width=40).grid(row=2, column=1, pady=5, padx=5)

# Save Path
tk.Label(frame, text="Save As:").grid(row=3, column=0, pady=5, sticky=tk.W)
tk.Entry(frame, textvariable=save_path_var, width=40).grid(row=3, column=1, pady=5, padx=5)
tk.Button(frame, text="Browse", command=browse_save_path).grid(row=3, column=2, pady=5, padx=5)

# Encrypt Button
encrypt_button = ttk.Button(frame, text="Encrypt PDF", command=encrypt_pdf)
encrypt_button.grid(row=4, column=1, pady=10)

# Result Label
result_label = tk.Label(frame, text="", fg="black")
result_label.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
