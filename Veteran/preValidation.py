import csv
import sys
import Config
import shutil
from Config import fileConfig
import logging
name = __name__


def validation(filename):
    try:
        with open(fileConfig['validpath'] + filename, 'w+') as nf:
            with open(fileConfig['errorpath'] + filename + '.error', 'w+') as ef:
                with open(fileConfig['filepath'] + filename, 'r') as f:
                    logging.info('Reading file -> ' + fileConfig['filepath'] + filename)

                    reader = csv.reader(f, delimiter=',')
                    for row in reader:
                        if len(row) < Config.FieldCount:
                            ef.write('error: Not enough fields are provided: ' + str(reader.line_num) + '\n')
                        elif len(row) > Config.FieldCount:
                            ef.write('error: More fields are provided: ' + str(reader.line_num) + '\n')
                        elif row[0] == '':
                            ef.write('error: Plate state is NULL at line: ' + str(reader.line_num) + '\n')
                        elif row[1] == '':
                            ef.write('error: Tag is NULL at line: ' + str(reader.line_num) + '\n')
                        elif row[2] == '':
                            ef.write('error: Start Date is NULL at line: ' + str(reader.line_num) + '\n')
                        elif row[3] == '':
                            ef.write('error: End Date is NULL at line: ' + str(reader.line_num) + '\n')
                        else:
                            nf.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + '\n')
        #        print(str(datetime.now())+": Archiving file -> ", fileConfig['archivepath'] + x)
        #        shutil.move(fileConfig['filepath']+x,fileConfig['archivepath']+x)

        # logging.info('file: '+filename+'  validated successfully.')
        # logging.disable(level=logging.INFO)
        return True
    except csv.Error as e:
        logging.error('Program: '+name+',   file: {}, line {}: {}'.format(filename, reader.line_num, e))
        return False


