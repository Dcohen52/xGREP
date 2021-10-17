import os
import tkinter
from tkinter import filedialog
from tkinter import *

root = tkinter.Tk()
root.withdraw()

folder_path_var = StringVar()

def select_files():
    root.withdraw()

    files = filedialog.askopenfilenames()
    for f in files:
        print(f)


def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    folder_path_var.set(folder_path)
    folder_path_var.get()

def save_logs():
    root.withdraw()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".log")
    if f is None:
        return
    f.write()
    f.close()


def file_changer(filename, data):
    data_to_put = ''
    with open(filename, 'r+') as fasta_file:
        for line in fasta_file.readlines():
            line = line.rstrip()
            if '[' in line:
                line = line.split('[')[-1]
                data_to_put += '>' + str(line[:-1]) + "\n"
            else:
                data_to_put += str(line) + "\n"
        fasta_file.write(data_to_put)
        fasta_file.close()


def replace_word():
#   take all the files
    pass

#
# if __name__ == '__main__':
#     pass
