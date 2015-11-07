import os


class GWV_filelist:
    def __init__(self):
        self.filelist = os.listdir(os.getcwd())


    def get_txt_files(self):
        return sorted(filter(lambda x: x[-4:] == ".txt", self.filelist))
