## This script hides sensitive data from a xlsx data_files

class SensitiveData():

    def __init__(self):
        self.dir_name = '../../data/'
        files = self._get_files()
        if len(files) == 0:
            print "\n ### WARNING: NO DATA FOUND, CHECK ../../data/[0-9]*.xlsx ### \n"
        for file in files:
            self._hide_sensitive_information(file)

    # It returns a list with the data xlsx files
    def _get_files(self):
        import glob
        return glob.glob(self.dir_name + "/[0-9]*.xlsx")

    def _hide_sensitive_information(self, file_name):
        from xlrd import open_workbook
        from xlutils.copy import copy
        import os

        wb = open_workbook(file_name)
        wb_copy = copy(wb)
        wb_copy.get_sheet(0).write(138, 1, '**********')
        head, tail = os.path.split(file_name)
        print head + '/_' + tail
        wb_copy.save('/tmp/data-students/' + tail)

SensitiveData()
