#!/bin/python3
#------------------------------------------------
#
# pro by Ihor Skripnichenko
# ver 1.0 Date 2019/06/06/ Info Initial Version
#
#-----------------------------------------------

import shutil        # For CopyFile
import os            # For getsoze and Check if file exist
import sys           # For CLI Arguments


#purgelog.py mylog.txt 10 5  # параметр запуска
# 10 - размер лог файла
# 5 кол-во файлов


if(len(sys.argv) < 4):
    print("Missing arguments! Usage is name: $script.py logfile.txt 10 5")
    print("10 = file size in kilobyte")
    print("5 = number of copies")
    exit(1)
elif(len(sys.argv) > 4):
    print ("Please enter only two args!")
    exit()

filename = sys.argv[1]
limitsize = int(sys.argv[2])
logsnumber = int(sys.argv[3])



if(os.path.isfile(filename) == True):        # Check if MAIN logfile exist
    log_size = os.stat(filename).st_size     # Get Filesize in BYTES
    log_size = log_size / 1024               # get size in Kbytes
    if(log_size >= limitsize):
        if(logsnumber > 0):
            for i in range(logsnumber, 1, -1):
                scr = filename + "_" + str(i-1)
                dst = filename + "_" + str(i)
                if(os.path.isfile(scr) == True):
                    shutil.copy(scr, dst)

                    print("Copied " + scr + " to " + dst)
            shutil.copyfile(filename, filename + "_1")
        logfile = open(filename, 'w')
        logfile.close()
    else:
        print("File size is less than limit size")
else:
    print("File not exist!")
