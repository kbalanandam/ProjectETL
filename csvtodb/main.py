import preValidation
import loadCsv
from datetime import datetime
import logging
import os
import Config
from Config import fileConfig


def main():
    for x in os.listdir(fileConfig['filepath']):
        if x.endswith(fileConfig['extension']):
            localtime = datetime.now()
            logfile = 'csvProcess_'+localtime.strftime('%Y%m%d%H%M%S')+'.log'
            logging.basicConfig(filename=logfile, level=logging.INFO,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.info('csv file found: ' + x)
            Config.FileCount = Config.FileCount + 1

            if preValidation.validation(x):
                logging.info('file: ' + x + ' validation completed successfully.')
                if loadCsv.fileload(x):
                    logging.info('file: ' + x + ' process completed successfully.')
                else:
                    logging.info('file: ' + x + ' process failed.')
            else:
                logging.info('file: ' + x + ' validation failed.')

    logging.info(str(Config.FileCount) + ' file(s) are processed.')


if __name__ == '__main__':
    main()

