import os

from tests.testUsingXML.setup import xmlSet, parsePiece
from classes.ObjectHierarchy.ItemClasses import Mark
from classes.ObjectHierarchy.TreeClasses.MeasureNode import MeasureNode
from classes.ObjectHierarchy.TreeClasses.BaseTree import Search
from classes.ObjectHierarchy.TreeClasses.NoteNode import NoteNode
from classes.ObjectHierarchy.TreeClasses.PartNode import PartNode


partname = "breathMarks.xml"
folder = "/Users/charlottegodley/PycharmProjects/FYP/implementation/primaries/SampleMusicXML/testcases"
piece = parsePiece(os.path.join(folder, partname))

class testFile(xmlSet):
    def setUp(self):
        xmlSet.setUp(self)
        self.m_num = 32
        self.p_id = "P1"
        self.p_name = "Flute"

    def testParts(self):
        global piece
        self.assertIsInstance(piece.getPart(self.p_id), PartNode)
        self.assertEqual(self.p_name, piece.getPart(self.p_id).GetItem().name)

    def testMeasures(self):
        self.assertIsInstance(piece.getPart(self.p_id).getMeasure(measure=self.m_num,staff=1), MeasureNode)

class testBreath(xmlSet):
    def setUp(self):
        xmlSet.setUp(self)
        if hasattr(self, "measure_id"):
            self.measure = piece.getPart("P1").getMeasure(measure=self.measure_id,staff=1)
        if hasattr(self, "item_id"):
            self.item = Search(NoteNode, self.measure, self.item_id+1).GetItem()
        if hasattr(self, "n_id"):
            self.notation = self.item.wrap_notation[self.n_id]



    def testInstance(self):
        if hasattr(self, "notation"):
            self.assertIsInstance(self.notation, self.instance)

class testMeasure1Note1(testBreath):
    def setUp(self):
        self.measure_id = 1
        self.item_id = 0
        self.n_id = 0
        self.instance = Mark.BreathMark
        testBreath.setUp(self)

class testMeasure1Note2(testBreath):
    def setUp(self):
        self.measure_id = 1
        self.item_id = 1
        self.n_id = 0
        self.instance = Mark.BreathMark
        testBreath.setUp(self)

class testMeasure1Note3(testBreath):
    def setUp(self):
        self.measure_id = 1
        self.item_id = 3
        self.n_id = 0
        self.instance = Mark.Caesura
        testBreath.setUp(self)

class testMeasure2Note3(testBreath):
    def setUp(self):
        self.measure_id = 1
        self.item_id = 3
        self.n_id = 0
        self.instance = Mark.Caesura
        testBreath.setUp(self)