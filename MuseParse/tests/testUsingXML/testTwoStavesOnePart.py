import unittest
import os

from MuseParse.tests.testUsingXML.xmlSet import parsePiece
from MuseParse.classes.ObjectHierarchy.TreeClasses.StaffNode import StaffNode


partname = "two_staves_one_part.xml"
from MuseParse.SampleMusicXML import testcases
directory = testcases.__path__._path[0]
piece = parsePiece(os.path.join(directory, partname))


class testTwoStavesInOnePart(unittest.TestCase):

    def testItemsIds(self):
        self.assertIsInstance(piece.getPart("P1").getStaff(1), StaffNode)
        self.assertTrue(piece.getPart("P1").getStaff(2), StaffNode)
