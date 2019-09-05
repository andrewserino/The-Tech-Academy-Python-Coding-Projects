from tkinter import *
import tkinter as tk
import sqlite3
import os
import shutil

import check_files_func

class ParentWindow(Frame):
    
    def __init__(self, master, *args, ** kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.protocol("WM_DELETE_WINDOW", lambda: check_files_func.ask_quit(self)) 
        arg = self.master

        self.master = master
        self.master.minsize(450,170)
        self.master.maxsize(450,170)

        self.outputDir = StringVar()
        self.outputDir2 = StringVar()

        self.master.title("Check files...")
        self.master.configure(bg="#F0F0F0")

        arg = self.master
    
        self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...', command = lambda: check_files_func.get_directory(self))
        self.btn_browse1.grid(row=0, column=0, rowspan=1, columnspan=2, padx=(20,0), pady=(20,0), sticky=N+W)
        self.txt_browse1 = tk.Entry(self.master, width=48, textvariable = self.outputDir)
        self.txt_browse1.grid(row=0, column=4, rowspan=1, columnspan=2, padx=(20,0), pady=(20,0), sticky=N+W)

        self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...', command = lambda: check_files_func.get_directory2(self))
        self.btn_browse2.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(20,0), pady=(20,0), sticky=N+W)
        self.txt_browse2 = tk.Entry(self.master, width=48, textvariable = self.outputDir2)
        self.txt_browse2.grid(row=1, column=4, rowspan=1, columnspan=2, padx=(20,0), pady=(20,0), sticky=N+W)
     
        self.btn_check = tk.Button(self.master, width=12, height=2, text='Check for files...', command = lambda: check_files_func.check_for_files(self))
        self.btn_check.grid(row=3, column=0, rowspan=2, columnspan=2, padx=(20,0), pady=(20,0), sticky=N+W)
        
        self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program', command = lambda: check_files_func.ask_quit)
        self.btn_close.grid(row=3, column=5, rowspan=2, columnspan=2, padx=(65,0), pady=(20,0), sticky=N+W)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
