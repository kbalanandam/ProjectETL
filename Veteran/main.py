import preValidation
import loadCsv
from datetime import datetime
import logging
import os
import Config
from Config import fileConfig


def main():
    for x in os.listdir(fileConfig['filepath']):
        if x.endswith(".DAT"):
            localtime = datetime.now()
            logfile = 'csvProcess_'+localtime.strftime('%Y%m%d%H%M%S')+'.log'
            logging.basicConfig(filename=logfile, level=logging.INFO,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.info('csv file found: ' + x)
            Config.FileCount = Config.FileCount + 1

            if preValidation.validation(x):
                logging.info('file: ' + x + ' validation completed successfully.')
            else:
                logging.info('file: ' + x + ' validation failed.')
            if loadCsv.fileload(x):
                logging.info('file: ' + x + ' process completed successfully.')
            else:
                logging.info('file: ' + x + ' process failed.')


if __name__ == '__main__':
    main()

