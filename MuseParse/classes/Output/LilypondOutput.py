import os, subprocess, sys
from MuseParse.classes import Exceptions

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

    def setup(self):
        defaults = ["/Applications/Lilypond.app/Contents/Resources/bin/lilypond", "C:/Program Files (x86)/LilyPond/usr/bin"]
        if sys.platform == "darwin":
            if self.lily_script is None:
                mac_path = defaults[0]
            else:
                mac_path = self.lily_script
            if os.path.exists(mac_path):
                fob = open(os.path.join("lilypond_mac.sh"), 'r')
                lines = fob.readlines()
                new_lines = [lines[0], "LILYPOND="+mac_path+"\n", lines[1]]
                fob.close()
                fob = open(os.path.join("lilypond"), 'w')
                fob.writelines(new_lines)
                fob.close()
                os.system("chmod u+x "+os.path.join("lilypond"))
                line = "export PATH=$PATH:"+os.getcwd()
                os.system(line)
            else:
                raise Exceptions.LilypondNotInstalledException('ERROR! Mac edition of Lilypond not in expected folder')

        if sys.platform == "win32":
            fob = open(self.lily_script, "r")
            lines = fob.readlines()
            new_lines = ["SET PATH="+defaults[1]+";%PATH%;", lines[0]]
            fob.close()
            fob = open("lilypond", "w")
            fob.writelines(new_lines)
            fob.close()

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
