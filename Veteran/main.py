import preValidation, loadCsv
from datetime import datetime
import logging
import os, sys
import Config
from Config import dbConfig, fileConfig

def main():
    for x in os.listdir(fileConfig['filepath']):
        if x.endswith(".DAT"):
            logtime = datetime.now()
            logfile = 'csvProcess_'+logtime.strftime('%Y%m%d%H%M%S')+'.log'
            logging.basicConfig(filename=logfile, level=logging.INFO,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.info('csv file found: ' + x)
            Config.FileCount = Config.FileCount + 1
            # Prints only text file present in My Folder

            if preValidation.validation(x):
                logging.info('file: ' + x + ' validation completed successfully.')
            else:
                logging.info('file: ' + x + ' validation failed.')
            if loadCsv.fileload(x):
                logging.info('file: ' + x + ' process completed successfully.')
            else:
                logging.info('file: ' + x + ' process failed.')
            #logging.disable(level=logging.INFO)
    #logging.info('--- file(s) process completed successfully ---')



if __name__ == '__main__':
    main()

