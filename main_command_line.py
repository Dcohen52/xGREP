import os
from tkinter import filedialog
from tkinter import *
import colorama
from colorama import Fore, Back, Style
import functions
from functions import select_files, select_folder

colorama.init(autoreset=True)

print(
    """
                                      {0}*** xGREP ***

{1}Search for something (string). xGREP will search for the given string inside all the files in the selected folder/path 
or selected files. Select files/folder & the program will search for the string in them. If nothing's selected - 
defaults apply.

{2}Example:
 -  Valid path example: C:/Users/admin/Desktop.
 -  Valid file type: *file_type* / *.file_type*
 -  (File name: test.txt) - (Line no: 1, Index: 21) - (Full line: test 123)
 
 {3}You can always enter {4}[-e] or [-E]{5} to exit.
 Hope xGREP will serve you well :)

---
""".format(Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX, Fore.MAGENTA, Fore.LIGHTWHITE_EX, Fore.LIGHTMAGENTA_EX,
           Fore.LIGHTWHITE_EX))
search_path = input('{0}[+] [-F]/[-f] for visual file dialog, or input manually: '.format(Fore.LIGHTGREEN_EX))
if search_path == '-f' or search_path == '-F':
    folder_selected = select_folder()
    # folder_selected = folder_selected + "/"
    search_path = functions.folder_path_var.get()
    print('{0}You choose to search in {1}'.format(Fore.CYAN, functions.folder_path_var.get() + '/'))
elif search_path == '-e' or search_path == '-E':
    print('Goodbye!')
    exit(0)

while True:
    file_type = input("{0}[+] File Type: ".format(Fore.LIGHTGREEN_EX))
    if file_type == 'pdf' or file_type == 'doc' or file_type == 'docx':
        print('{0}{1}[!] Unsupported file type - only text-based formats.'.format(Fore.BLACK, Back.RED, ))
        continue
    elif file_type == '-e' or file_type == '-E':
        print('Goodbye!')
        exit(0)
    else:
        break

search_str = input("{0}[+] Enter the search string: ".format(Fore.LIGHTGREEN_EX))
if search_str == '-E' or search_str == '-e':
    print('{0}Goodbye!'.format(Fore.LIGHTYELLOW_EX))
    exit(0)
if not (search_path.endswith("/") or search_path.endswith("\\")):
    search_path = search_path + "/"
if not os.path.exists(search_path):
    search_path = "."
output_list = []
for fname in os.listdir(path=search_path):

    if fname.endswith(file_type):
        fo = open(search_path + fname)
        line = fo.readline()
        line_no = 1
        while line != '':
            index = line.find(search_str)
            if index != -1:
                print(" -  ", "\033[1m" + fname + "\033[0m", "  (", line_no, ",", index, ") ", "\033[1m" + '    ' + line + "\033[0m", sep="")
                output_list.append('File name: {0}, Line number: {1}, Index: {2}, Containing line: {3}'.format(fname,
                                                                                                            line_no,
                                                                                                            index, line))
            line = fo.readline()
            line_no += 1
        fo.close()

# save the output
# save_output = input('{0}[!] Before we continue - Do you want to save the output? [Y/n]: '.format(Fore.LIGHTYELLOW_EX))
#
# if save_output == 'y' or save_output == 'Y':
#     root = Tk()
#     root.withdraw()
#     f = filedialog.asksaveasfile(mode='w+', defaultextension=".txt",
#                                  filetypes=[("Log", "*.log"), ("Text Document", "*.txt"), ("All Files", "*.*")])
#     try:
#         f.write(str(output_list))
#         f.close()
#         print('''
#
#         {0}{1}[!] You successfully saved the logs!{2}
#
#         '''.format(Fore.LIGHTWHITE_EX, Back.LIGHTGREEN_EX, Back.RESET))
#     except AttributeError:
#         print('''
#
#         {0}{1}[!] Operation canceled!{2}
#
#         '''.format(Fore.BLACK, Back.LIGHTYELLOW_EX, Back.RESET))
# elif save_output == 'n' or save_output == 'N':
#     pass

# change the value
change = input('{0}[+] Do you want to replace? [Y/n] [-c] to cancel: '.format(Fore.LIGHTGREEN_EX))

if change == 'Y' or change == 'y':
    word = input('{0}[-] Enter replacement: '.format(Fore.LIGHTGREEN_EX))
    for fname in os.listdir(path=search_path):

        if fname.endswith(file_type):

            fo = open(search_path + fname, 'rt')
            line = fo.readline()
            line_no = 1
            while line != '':
                index = line.find(search_str)
                fw = open(search_path + fname, 'wt')
                replacement = fw.write(line.replace(search_str, word))
                if index != -1:
                    print(" -  ", fname, "  (", line_no, ",", index, ") ", replacement, sep="")
                    print('\n{0}{1}[!] Operation completed successfully!{2} \n'.format(Fore.LIGHTWHITE_EX,
                                                                                       Back.LIGHTGREEN_EX,
                                                                                       Back.RESET))

                line = fo.readline()
                line_no += 1
                fw.close()
            fo.close()

elif change == 'N' or change == 'n':
    print('[!] So there you go, the log saved automatically to save you some time'
          'on looking for it again.')
elif change == '-c' or change == '-C':
    print('''
    
    {0}{1}[!] Operation canceled!{2}
    
    '''.format(Fore.BLACK, Back.LIGHTYELLOW_EX, Back.RESET))
else:
    print('TEST - You choose neither Y or N')
