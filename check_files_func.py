from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
import sqlite3
import shutil


import check_files_gui
import check_files_main


# This is the source code
def get_directory(self):
    dirName = filedialog.askdirectory()
    print(dirName)
    self.outputDir.set(dirName)

# This is the destination code
def get_directory2(self):
    dirName1 = filedialog.askdirectory()
    print(dirName1)
    self.outputDir2.set(dirName1)

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
           
def check_for_files(self):
    fPath = self.outputDir.get()
    dPath = self.outputDir2.get()

    dirs = os.listdir(fPath)

    for file in dirs:
        abPath = os.path.join(fPath, file)
        mTime = os.path.getmtime(abPath)
        if file.endswith(".txt"):
            shutil.move(abPath, dPath)
            print(mTime, abPath)


            conn = sqlite3.connect('drill103.db')

            with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS tbl_filenames ( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_datatype TEXT \
                    )")

                cur.execute('INSERT INTO tbl_filenames(col_datatype) VALUES(?)',(file,))
                        
                conn.commit()
            conn.close()



