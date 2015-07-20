import os

from tests.testUsingXML.setup import xmlSet, parsePiece
from classes.ObjectHierarchy.ItemClasses import Note
from classes.ObjectHierarchy.TreeClasses.PartNode import PartNode
from classes.ObjectHierarchy.TreeClasses.MeasureNode import MeasureNode
from classes.ObjectHierarchy.TreeClasses.NoteNode import NoteNode
from classes.ObjectHierarchy.TreeClasses.BaseTree import Search


partname = "GraceNotes.xml"
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
        self.assertIsInstance(piece.getPart(self.p_id).getMeasure(self.m_num, 1), MeasureNode)

class GraceNotes(xmlSet):
    def setUp(self):
        xmlSet.setUp(self)
        self.p_id = "P1"
        if hasattr(self, "measure_id"):
            part = piece.getPart(self.p_id)
            self.measure = part.getMeasure(self.measure_id, 1)

    def testGrace(self):
        if hasattr(self, "nid") and hasattr(self, "grace"):
            note = Search(NoteNode, self.measure, self.nid+1).GetItem()
            self.assertEqual(self.grace, note.Search(Note.GraceNote) is not None)

    def testGraceVal(self):
        if hasattr(self, "nid") and hasattr(self, "grace"):
            if self.grace:
                note = Search(NoteNode, self.measure, self.nid+1).GetItem()
                self.assertIsInstance(note.Search(Note.GraceNote), Note.GraceNote)

    def testGraceSlash(self):
        if hasattr(self, "nid") and hasattr(self, "grace") and hasattr(self, "graceSlash"):
            if self.grace:
                note = Search(NoteNode, self.measure, self.nid+1).GetItem()
                self.assertEqual(self.graceSlash, note.Search(Note.GraceNote).slash)

class testNote1Measure1(GraceNotes):
    def setUp(self):
        self.measure_id= 1
        self.nid = 0
        self.grace = True
        self.graceSlash = True
        GraceNotes.setUp(self)

class testNote2Measure1(GraceNotes):
    def setUp(self):
        self.measure_id= 1
        self.nid = 1
        self.grace = True
        self.graceSlash = False
        GraceNotes.setUp(self)

class testNote3Measure1(GraceNotes):
    def setUp(self):
        self.measure_id= 1
        self.nid = 2
        self.grace = True
        self.graceSlash = False
        GraceNotes.setUp(self)

class testNote4Measure1(GraceNotes):
    def setUp(self):
        self.measure_id= 1
        self.nid = 3
        self.grace = False
        self.graceSlash = False
        GraceNotes.setUp(self)

class testNote5Measure1(GraceNotes):
    def setUp(self):
        self.measure_id= 1
        self.nid = 4
        self.grace = True
        self.graceSlash = False
        GraceNotes.setUp(self)

class testNote6Measure1(GraceNotes):
    def setUp(self):
        self.measure_id= 1
        self.nid = 5
        self.grace = False
        self.graceSlash = False
        GraceNotes.setUp(self)

class testNote7Measure1(GraceNotes):
    def setUp(self):
        self.measure_id= 1
        self.nid = 6
        self.grace = True
        self.graceSlash = False
        GraceNotes.setUp(self)

class testNote8Measure1(GraceNotes):
    def setUp(self):
        self.measure_id= 1
        self.nid = 7
        self.grace = False
        self.graceSlash = False
        GraceNotes.setUp(self)

