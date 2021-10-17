import os
import tkinter
from tkinter import filedialog
from tkinter import *
# from main_command_line import output_dict

root = tkinter.Tk()
root.withdraw()
# path = filedialog.askdirectory()

folder_path_var = StringVar()


def select_files():
    root.withdraw()

    files = filedialog.askopenfilenames()
    for f in files:
        print(f)


def select_folder():
    global folder_path
    # Open and return file path
    folder_path = filedialog.askdirectory()
    folder_path_var.set(folder_path) #setting the variable to the value from file path
    #Now the file_path can be acessed from inside the function and outside
    folder_path_var.get() # will return the value stored in file_path_var
    # l1 = Label(root, text="File path: " + folder_path).pack()


def save_logs():
    root.withdraw()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".log")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    # text2save = str(otpt_log.get(1.0, END))  # starts from `1.0`, not `0.0`
    f.write()
    f.close()


# def write_file():
#     file = open('output.log', 'a+')
#     file.write(output.get() + '\n')
#     file.close()
#
#
# def list_folder():
#     # can use 'os.scandir(path)' - it's faster, but add DirEntry at the beginning
#     folder_content = os.listdir(path)
#     print('{0} Contain: '.format(path))
#     for item in folder_content:
#         print('     {0}'.format(item))
#
#
# def scan_dir():
#     for (root, dirs, files) in os.walk(path, topdown=True):
#         if '.xml' in files:
#             print(os.path.abspath(files))


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
