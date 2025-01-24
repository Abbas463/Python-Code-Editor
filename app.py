from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

win = Tk()
win.title("Python Code Editor")
win.geometry("1280x720")
win.configure(bg="#323846")

# Global variable for file path
file_path = ""

def open_file():
    global file_path
    file_path = askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:  # Ensure the user has selected a file
        try:
            with open(file_path, "r") as file:
                code = file.read()
                code_input.delete('1.0', END)
                code_input.insert('1.0', code)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    global file_path
    if not file_path:  # If no file is currently open, ask the user where to save
        file_path = asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if file_path:  # Ensure a file path was selected
        try:
            with open(file_path, "w") as file:
                code = code_input.get('1.0', END)
                file.write(code)
                messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def run_file():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "Please save or open a file before running.")
        return
    try:
        # Run the Python file and display the output in the output text widget
        command = f"python \"{file_path}\""
        process = subprocess.run(command, capture_output=True, text=True, shell=True)
        code_output.delete('1.0', END)
        code_output.insert('1.0', process.stdout)
        code_output.insert('1.0', process.stderr)  # Show errors first
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run file: {e}")

# Set up icons and layout
image_icon = PhotoImage(file="C:/Users/SHC/Desktop/Project/Python_IDE/logo.png")
win.iconphoto(False, image_icon)

code_input = Text(win, font="consolas 18", bg="#1e1e1e", fg="white", insertbackground="white")
code_input.place(x=180, y=0, width=680, height=720)

code_output = Text(win, font="consolas 15", bg="#323846", fg="lightgreen")
code_output.place(x=860, y=0, width=420, height=720)

open_icon = PhotoImage(file="C:/Users/SHC/Desktop/Project/Python_IDE/open.png")
save_icon = PhotoImage(file="C:/Users/SHC/Desktop/Project/Python_IDE/save.png")
run_icon = PhotoImage(file="C:/Users/SHC/Desktop/Project/Python_IDE/run.png")

Button(win, image=open_icon, bg="#323846", bd=0, command=open_file).place(x=30, y=30)
Button(win, image=save_icon, bg="#323846", bd=0, command=save_file).place(x=30, y=145)
Button(win, image=run_icon, bg="#323846", bd=0, command=run_file).place(x=30, y=260)

win.mainloop()
