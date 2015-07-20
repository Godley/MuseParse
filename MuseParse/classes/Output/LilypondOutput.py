import os, subprocess

class LilypondRenderer(object):

    def __init__(
            self,
            piece_obj,
            fname,
            lyscript="/Users/charlottegodley/bin/lilypond"):
        self.piece_obj = piece_obj
        self.file = fname
        self.lyfile = self.file.split(".")[0] + ".ly"
        self.pdf = self.file.split(".")[0] + ".pdf"
        self.folder = "/".join(self.file.split("/")[:-1])
        self.lily_script = lyscript

    def run(self, wrappers=["", ""]):
        '''
        run the lilypond script on the hierarchy class
        :param wrappers: this is useful for testing: use wrappers to put something around the outputted "lilypond string" from the hierarchy class.
        For example if you're testing a pitch, you might put \relative c {} around the note so that lilypond handles it properly without causing an error
        :return: doesn't return anything, side effect that a PDF should be created.
        '''
        opened_file = open(self.lyfile, 'w')
        lilystring = self.piece_obj.toLily()
        opened_file.writelines(
            wrappers[0] +
            "\\version \"2.18.2\" \n" +
            lilystring +
            wrappers[1])
        opened_file.close()
        # subprocess.Popen(['sudo', self.lily_script," --output=" +
        #     self.folder, self.lyfile])
        os.system(self.lily_script +
             " --output=" +
            self.folder + " " + self.lyfile
             )

    def cleanup(self, pdf=False):
        if os.path.exists(self.lyfile):
            os.remove(self.lyfile)

        if pdf:
            if os.path.exists(self.pdf):
                os.remove(self.pdf)
