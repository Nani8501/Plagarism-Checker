import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import difflib
from tqdm import tqdm
from time import sleep

class PlagiarismChecker:
    def __init__(self, master):
        self.master = master
        self.master.title("Plagiarism Checker")
        self.master.geometry("500x250")
        self.master.resizable(False, False)

        self.file1_path = ""
        self.file2_path = ""

        self.file1_button = tk.Button(self.master, text="Select File 1", command=self.select_file1)
        self.file1_button.place(relx=0.25, rely=0.2, anchor="center")

        self.file2_button = tk.Button(self.master, text="Select File 2", command=self.select_file2)
        self.file2_button.place(relx=0.75, rely=0.2, anchor="center")

        self.check_button = tk.Button(self.master, text="Check Plagiarism", command=self.check_plagiarism)
        self.check_button.place(relx=0.5, rely=0.5, anchor="center")

        self.progress_bar = tk.ttk.Progressbar(self.master, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.place(relx=0.5, rely=0.7, anchor="center")

    def select_file1(self):
        self.file1_path = filedialog.askopenfilename()
        self.file1_button.config(text="File 1 Selected")

    def select_file2(self):
        self.file2_path = filedialog.askopenfilename()
        self.file2_button.config(text="File 2 Selected")

    def check_plagiarism(self):
        if not self.file1_path or not self.file2_path:
            tk.messagebox.showerror("Error", "Please select two files.")
            return

        file1_text = open(self.file1_path).read()
        file2_text = open(self.file2_path).read()

        matcher = difflib.SequenceMatcher(None, file1_text, file2_text)

        for i in range(101):
            self.progress_bar.step(1)
            self.progress_bar.update()
            sleep(0.01)

        similarity = matcher.ratio() * 100
        tk.messagebox.showinfo("Result", f"The two files are {similarity:.2f}% similar.")

    

root = tk.Tk()
app = PlagiarismChecker(root)
root.mainloop()
