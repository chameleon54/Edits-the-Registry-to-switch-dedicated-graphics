import tkinter as tk
from tkinter import filedialog, messagebox
import winreg
import os 

REG_PATH = r"Software\Microsoft\DirectX\UserGpuPreferences"

def force_high_gpu(exe_path):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        winreg.SetValueEx(key, exe_path, 0, winreg.REG_SZ, "GpuPreference=2;")
        winreg.CloseKey(key)
        messagebox.showinfo("Success", f"Successfully set high-performance GPU for {exe_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to set GPU preference: {e}")
    
def remove_gpu_rule(exe_path):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, exe_path)
        winreg.CloseKey(key)
        messagebox.showinfo("Success", f"Successfully removed GPU preference for {exe_path}")
    except FileNotFoundError:
        messagebox.showwarning("Warning", f"No GPU preference found for {exe_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to remove GPU preference: {e}")
    
def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select Game EXE",
        filetypes=[("Executable Files", "*.exe")]
    )
    if file_path:
        exe_path_var.set(file_path)

def apply_remove():
    path = exe_path_var.get()
    if not os.path.isfile(path):
        messagebox.showerror("Error", "Please enter a valid executable path.")
        return
    remove_gpu_rule(path) 

def apply_force():
    path = exe_path_var.get()
    if not os.path.isfile(path):
        messagebox.showerror("Error", "Please enter a valid executable path.")
        return
    force_high_gpu(path)


#gui setup

root = tk.Tk()
root.title("GPU Switcher – Force Dedicated GPU")
root.geometry("500x180")
root.resizable(False, False)

# THIS VARIABLE IS ALWAYS DEFINED
exe_path_var = tk.StringVar()  # <--- This prevents "exe_path is not defined"

tk.Label(root, text="Select Game EXE:", font=("Segoe UI", 10)).pack(pady=5)
tk.Entry(root, textvariable=exe_path_var, width=55).pack()
tk.Button(root, text="Browse", command=browse_file).pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Force Dedicated GPU", width=20, command=apply_force).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Remove GPU Rule", width=20, command=apply_remove).grid(row=0, column=1, padx=10)

root.mainloop()


