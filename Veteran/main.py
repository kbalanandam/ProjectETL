import preValidation, loadCsv
from datetime import datetime
import logging

logging.basicConfig(filename='log1.log',level=logging.INFO)
def main():
    preValidation.validation()
    logging.info('csv validation completed')
    loadCsv.fileload()
    logging.info('csv processed')


if __name__ == '__main__':
    main()

