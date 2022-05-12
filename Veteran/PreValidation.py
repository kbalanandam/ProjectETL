import pandas as pd
import csv
import os
import sys
import Config
import shutil
import json
from datetime import datetime
from Config import dbConfig, fileConfig


for x in os.listdir(fileConfig['filepath']):
    if x.endswith(".DAT"):
        Config.FileCount = Config.FileCount + 1
        # Prints only text file present in My Folder
        print(str(datetime.now())+": Reading file -> ",fileConfig['filepath']+x)

        if x:
            with open(fileConfig['validpath']+x,'w+') as nf:
                with open(fileConfig['errorpath']+x+'.error', 'w+') as ef:
                    with open(fileConfig['filepath']+x,'r') as f:
                        try:
                            reader = csv.reader(f,delimiter=',')
                            for row in reader:
                                if len(row) < Config.FieldCount:
                                    ef.write('error: Not enough fields are provided: '+ str(reader.line_num)+'\n')
                                elif len(row) > Config.FieldCount:
                                    ef.write('error: More fields are provided: '+ str(reader.line_num)+'\n')
                                elif row[0] == '':
                                    ef.write('error: Plate state is NULL at line: '+ str(reader.line_num)+'\n')
                                elif row[1] == '':
                                    ef.write('error: Tag is NULL at line: '+ str(reader.line_num)+'\n')
                                elif row[2] == '':
                                    ef.write('error: Start Date is NULL at line: '+ str(reader.line_num)+'\n')
                                elif row[3] == '':
                                    ef.write('error: End Date is NULL at line: '+ str(reader.line_num)+'\n')
                                else:
                                    nf.write(row[0]+','+row[1]+','+row[2]+','+row[3]+'\n')
                        except csv.Error as e:
                            sys.exit('file {}, line {}: {}'.format(f, reader.line_num, e))
        print(str(datetime.now())+": Archiving file -> ", fileConfig['archivepath'] + x)
        shutil.move(fileConfig['filepath']+x,fileConfig['archivepath']+x)
if Config.FileCount > 0:
    print(str(datetime.now())+": "+str(Config.FileCount)+" file(s) are processed")
else:
    print("no file to process")




