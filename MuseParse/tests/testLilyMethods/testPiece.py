from MuseParse.classes.ObjectHierarchy.ItemClasses import Meta, Part
from MuseParse.tests.testLilyMethods.setup import Lily
from MuseParse.classes.ObjectHierarchy.TreeClasses.PieceTree import PieceTree


class testPiece(Lily):
    def setUp(self):
        self.item = PieceTree()
        self.lilystring = "\\version \"2.18.2\" \n<<>>"

class testPieceWithPart(Lily):
    def setUp(self):
        self.item = PieceTree()
        self.item.addPart(Part.Part(), "P1")
        self.lilystring = "\\version \"2.18.2\" \n<<>>"

class testPieceWithTitle(Lily):
    def setUp(self):
        self.item = PieceTree()
        self.item.GetItem().meta = Meta.Meta(title="hello world")
        self.lilystring = "\\version \"2.18.2\" \n\n\header {\ntitle = \"hello world\"\n\n}<<>>"

