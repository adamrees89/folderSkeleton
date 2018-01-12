#import required modules
import os
import sys
import time
import logging
import tkinter
import tkinter.messagebox as mbox
from tkinter import filedialog
now = time.strftime("%c")
logging.basicConfig(filename='Deletinglogfile.txt',level=logging.DEBUG)
logging.info(f'''\n-------------------------------\nDate and Time:\n
{now}\n-------------------------------\n''')

#Define functions

def recursive_scanning(foldername):
    folders=[]
    files=[]
    for root, dirnames, filenames in os.walk(foldername):
        for filename in filenames:
            files.append(os.path.join(root,filename))
        for dirname in dirnames:
            folders.append(os.path.join(root,dirname))
    return[folders,files]


'''Start calling functions and piecing everything together'''

file_path = filedialog.askdirectory()

try:
    folders,files=recursive_scanning(file_path)
except:
    sys.exit(103)

DelNum = len(files)

try:
    for i in files:
        os.remove(i)
except:
    sys.exit(105)
    
window = tkinter.Tk()
window.wm_withdraw()
mbox.showinfo('Success',
f'Deleted {DelNum} files from the parent directory')
logging.info(f'Deleted {DelNum} files')

sys.exit(0)
