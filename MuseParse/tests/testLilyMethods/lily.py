import unittest, os, sys

from MuseParse.classes.Output import LilypondOutput


class Lily(unittest.TestCase):
    def setUp(self):
        self.compile = False
        self.wrappers = []


    def testValue(self):
        if hasattr(self, "lilystring"):
            if hasattr(self, "item"):
                self.assertEqual(self.lilystring, self.item.toLily())

    def testCompilation(self):
        if hasattr(self, "compile"):
            if self.compile and hasattr(self, "item"):
                if os.path.exists("/Users/charlottegodley/testlily.pdf"):
                    os.remove("/Users/charlottegodley/testlily.pdf")
                filepath = ""
                script = ''
                if sys.platform == 'darwin':
                    filepath += '~/'
                    script = '~/bin/lilypond'
                filepath += self.name +".xml"
                ly = LilypondOutput.LilypondRenderer(self.item, filepath, script)
                if hasattr(self, "wrappers"):
                    ly.run(wrappers=self.wrappers)
                else:
                    ly.run()
                self.assertTrue(os.path.exists("/Users/charlottegodley/"+self.name+".pdf"))

