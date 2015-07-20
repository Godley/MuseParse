import unittest
import os

from MuseParse.tests.testUsingXML.setup import parsePiece
from MuseParse.classes.ObjectHierarchy.TreeClasses.StaffNode import StaffNode


partname = "two_staves_one_part.xml"
folder = "/Users/charlottegodley/PycharmProjects/FYP/implementation/primaries/SampleMusicXML/testcases"
piece = parsePiece(os.path.join(folder, partname))

class testTwoStavesInOnePart(unittest.TestCase):

    def testItemsIds(self):
        self.assertIsInstance(piece.getPart("P1").getStaff(1), StaffNode)
        self.assertTrue(piece.getPart("P1").getStaff(2), StaffNode)